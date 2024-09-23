from time import sleep


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self) -> str:
        return f"{self.title}, {self.duration}, {self.time_now}, {self.adult_mode}"


class UrTube:
    def __init__(self):
        self.current_user: User | None = None
        self.users: dict[str, User] = {}
        self.videos: dict[str, Video] = {}

    def log_in(self, nickname: str, password: str):
        """функция входа в аккаунт

        Args:
            nickname (str): имя пользователя
            password (str): пароль пользователя
        """

        if nickname in self.users.keys():
            if self.users[nickname].password == hash(password):
                self.current_user = self.users[nickname]

    def register(self, nickname, password, age):
        """функция регистрации пользователя

        Args:
            nickname (str): имя пользователя
            password (str): пароль пользователя
            age (int): возраст пользователя
        """

        if nickname in self.users.keys():
            print(f"Пользователь {nickname} уже существует")
            return
        user = User(nickname, password, age)
        self.users[nickname] = user
        self.current_user = user

    def log_out(self):
        """функция выхода из аккаунта"""

        self.current_user = None

    def add(self, *video: Video):
        """функция добавления видео

        Args:
            video (Video): видео
        """

        for clip in video:
            if clip.title.lower() not in map(str.lower, self.videos.keys()):
                self.videos[clip.title] = clip

    def get_videos(self, name: str):
        """функция поиска видео

        Args:
            name (str): название видео
        """

        return [
            clip.title
            for clip in self.videos.values()
            if name.lower() in clip.title.lower()
        ]

    def watch_video(self, title: str):
        """функция просмотра видео
           проверяет возраст пользователя


        Args:
            title (str): название видео
        """

        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if title not in self.videos.keys():
            print("Видео не найдено")
            return
        if self.videos[title].adult_mode and self.current_user.age < 18:
            print(f"Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for sec in range(self.videos[title].duration + 1):
            print(sec)
            sleep(1)


ur = UrTube()
v1 = Video("Лучший язык программирования 2024 года", 200)
v2 = Video("Для чего девушкам парень программист?", 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos("лучший"))
print(ur.get_videos("ПРОГ"))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video("Для чего девушкам парень программист?")
ur.register("vasya_pupkin", "lolkekcheburek", 13)
ur.watch_video("Для чего девушкам парень программист?")
ur.register("urban_pythonist", "iScX4vIJClb9YQavjAgF", 25)
ur.watch_video("Для чего девушкам парень программист?")

# Проверка входа в другой аккаунт
ur.register("vasya_pupkin", "F8098FM8fjm9jmi", 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video("Лучший язык программирования 2024 года!")
