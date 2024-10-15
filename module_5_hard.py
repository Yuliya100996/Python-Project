import time
import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __repr__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.user = []
        self.video = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        for user in self.user:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                return
        return f'Неверный логин или пароль'

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.user):
            print(f'Пользователь {nickname} уже существует.')
        new_user = User(nickname, password, age)
        self.user.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *new_video):
        for new_video in new_video:
            if not any(video.title == new_video.title for video in self.video):
                self.video.append(new_video)

    def get_videos(self, search_word):
        return [video.title for video in self.video if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.video:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for second in range(1, video.duration+1):
                    print(f'{second}')
                    time.sleep(1)
                print('Конец видео')
                return
                print('Видео не найдено')


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