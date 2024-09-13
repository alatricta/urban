import time 

class User:
    def __init__(self, nickname, passwd, age = 0):
        self.nickname = nickname
        self.password = hash(passwd)
        self.age = age
        
    def __eq__(self, other_user):
        if isinstance(other_user, User):
            return self.nickname == other_user.nickname and \
                   self.password == other_user.password
        else:
            return self.nickname == other_user
            
    def __str__(self):
        return self.nickname

        
class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        # self.time_now = 0
        
    def __eq__(self, other_video):
        if isinstance(other_video, Video):
            return  self.title == other_video.title and \
                    self.duration == other_video.duration
        else:
            return self.title == other_video
        
        
class UrTube:
    def __init__(self, users=None, videos=None, current_user=None):
        if users is not None:
            self.users = users
        else:
            self.users = []
        if videos is not None:
            self.videos = videos 
        else:
            self.videos = []
        self.current_user = current_user
        
        
    def log_in(self, nickname, password):
        if user := User(nickname, password) in self.users:
            self.current_user = user
        else:
            print('Такого пользователя не найдено, зарегистрируйтесь.')


    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user


    def log_out(self):
        self.current_user = None


    def add(self, *videos: Video):
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)


    def get_videos(self, find: str):
        result_find = []
        for video in self.videos:
            if find.lower() in video.title.lower():
                result_find.append(video)

        if result_find:
            return [v.title for v in result_find]
        else:
            return 'Такого видео не найдено'


    def watch_video(self, title: str):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return False
        elif self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return False
        
        for video in self.videos:
            if title == video.title:
                for n in range(1,video.duration+1):
                    print(n, end=' ')
                    #time.sleep(1)
                print('Конец видео')
                return True
        else:
            print('Такокого видео нет')
            return False


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    
    # Добавление видео
    ur.add(v1, v2)
    
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    
    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    
    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
