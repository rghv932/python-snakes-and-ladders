class Player:
    __name: str
    __position: int

    def __init__(self, name: str, position: int):
        self.__name = name
        self.__position = position

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def set_position(self, position: int):
        self.__position = position

    class Builder:
        __name: str

        @classmethod
        def set_name(cls, name: str) -> 'Builder':
            cls.__name = name
            return cls

        @classmethod
        def build(cls) -> 'Player':
            return Player(cls.__name, 1)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()
