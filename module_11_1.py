import json
from bs4 import BeautifulSoup
from yarl import URL
import requests
from os import mkdir, path
from threading import Thread
from queue import Queue
from time import sleep
from PIL import Image, ImageFilter


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

FILE_DIRECTORY = "module_11_1_files"
if not path.exists(FILE_DIRECTORY):
    mkdir(FILE_DIRECTORY)


def get_img_urls(query):
    url = URL("https://yandex.ru/images/search")
    # query = {'text': 'коты воители'}
    query = {"text": query}

    response = requests.get(url=url.with_query(query), params=headers)

    soup = BeautifulSoup(response.content, features="html5lib")
    data_html = soup.find("div", class_="page-layout__content-wrapper b-page__content")
    data_html = data_html.find("div", class_="Root")
    data_json = json.loads(data_html["data-state"])
    img_list = data_json["initialState"]["serpList"]["items"]["entities"]
    img_url_list = []
    for img in img_list:
        img_url_list.append(str(URL(img_list[img]["origUrl"])))

    # Смог обойтись без промежуточной записи в файл
    # with open("example_urls.txt", "w", encoding="utf-8") as f:
    #     for line in img_url_list:
    #         f.write(f"{line}\n")

    return img_url_list


def get_image(queue):
    url = URL(queue.get())
    file_name = url.name
    if not file_name.endswith((".jpg", ".jpeg")):
        file_name += ".jpg"
    file_path = path.join(FILE_DIRECTORY, file_name)

    # для избежания блокировки сервером
    sleep(0.5)

    # скачиваем картинку
    r = requests.get(url)
    if r.status_code == 200:
        with open(file_path, "wb") as f:
            # f.write(r.content)

            # что-то мне подсказывает что это более правильный способ
            for chunk in r.iter_content(1024):
                f.write(chunk)

        # Преобразовываем в контурный рисунок
        try:
            img_to_contur(file_path)
        except ValueError:
            print(f"ОШИБКА! При конвертировании файла {file_name}")
        else:
            print(f"Файл {file_name} записан в папку {path.abspath(FILE_DIRECTORY)}")
    else:
        print(f"ОШИБКА! При скачивании файла {file_name} (статус ответа: {r.status_code})")


def put_queue(queue):
    with open("example_urls.txt", "r", encoding="utf-8") as f:
        # for line in f.readlines():
        for line in f:
            queue.put(line)


def img_to_contur(file_path):
    with Image.open(file_path) as img:
        img.load()

    img = img.convert("L")
    threshold = 65
    img = img.point(lambda x: 255 if x > threshold else 0)
    img = img.filter(ImageFilter.CONTOUR)
    img.save(file_path)


def main():
    urls_list = get_img_urls(input("Введите запрос для получения изображений:\n"))

    # с помощью очереди ограничиваю количество потоков
    queue = Queue(maxsize=10)

    # th_start = Thread(target=put_queue, args=(queue, ))
    # т.к. map это генератор, применил tuple чтобы применить map ко всему списку
    # скорее всего можно как-то лучше выйти из ситуации
    th_put = Thread(target=lambda: tuple(map(queue.put, urls_list)))
    th_put.start()

    # надо помнить, что для чтения файла нужно время
    # после переделки на список, всё равно оставлю задержку!
    sleep(0.01)
    while not queue.empty():
        th = Thread(target=get_image, args=(queue,))
        th.start()

        # и тут тоже надо ждать, чтобы заполнилась очередь!
        sleep(0.01)

    th_put.join()


if __name__ == "__main__":
    main()
