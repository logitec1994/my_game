class Character:

    def __init__(self) -> None:
        self.__healt: int = 0

    def create(self) -> None:
        self.__healt = 100

    def status(self) -> int:
        return self.__healt

    def hit(self, damage: int):
        self.__healt -= damage
        return self.__healt

    def get_health(self):
        return self.__healt
