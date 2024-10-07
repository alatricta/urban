from multiprocessing import Pool
from datetime import datetime


all_data = []

def read_info(file_name):
    global all_data
    with open(file_name, 'r') as f:
        line = f.readline().strip()
        while line != '':
            all_data.append(line)
            line = f.readline().strip()

def main_thread(files):
    start = datetime.now()
    for file in files:
        read_info(file)
    end = datetime.now()
    print('Время выполнения последовательно:', end-start)
    
def main_process(files):
    start = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, files)
    end = datetime.now()
    print('Время выполнения мультипроцессорно:', end-start)
    

if __name__ == '__main__':
    filenames = [f'./module_10_5_files/file {number}.txt' for number in range(1, 5)]
    # main_thread(filenames)
    main_process(filenames)
