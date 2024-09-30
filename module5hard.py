class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.User = User
        self.Video = Video
        self.current_user = current_user

    def __log_in__(self, nickname, password, current_user):
    def __register__(self, nickname, password, age):
    def __log_out__(self):
    def __add__(self, other):
    def __get_videos__(self):
    def __watch_video__(self):