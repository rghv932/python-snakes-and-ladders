from models.board import Board
from models.mover import Mover
from models.mover_enum import MoverType
from models.mover_factory import MoverFactory


class Builder:
    __size: int
    __movers: dict[int, Mover]
    __mover_factory: MoverFactory
    ar: [bool]

    def __init__(self, size: int):
        self.__size = size
        self.__mover_factory = MoverFactory(self.__size)
        self.__movers = dict()
        self.ar = [False] * (size * size)
        self.ar[0] = self.ar[size*size - 1] = True
        # print(len(self.ar), self.ar)
        # print("mover map size:" + str(len(self.__movers)))
        self.configure_snakes_ladders()
        # print("mover map size:" + str(len(self.__movers)), self.__movers.items(), end="\n")

    def configure_snakes_ladders(self, snakes_ladders: list = None) -> dict[int, Mover]:
        self.ar = [False] * (self.__size * self.__size)
        self.ar[0] = self.ar[self.__size * self.__size - 1] = True
        self.__movers = dict()
        if snakes_ladders is not None:
            while len(self.__movers) < self.__size / 2:
                self.add_mover(self, MoverType.SNAKE, snakes_ladders[len(self.__movers)])
            while len(self.__movers) < self.__size:
                self.add_mover(self, MoverType.LADDER, snakes_ladders[len(self.__movers)])
            return self.__movers
        while len(self.__movers) < self.__size / 2:
            # print("adding snake")
            # print(self.ar)
            self.add_mover(self, MoverType.SNAKE)

        while len(self.__movers) < self.__size:
            self.add_mover(self, MoverType.LADDER)
        # print("mover map size:" + str(len(self.__movers)), self.__movers.items())
        return self.__movers

    @staticmethod
    def add_mover(cls, mover_type: MoverType, element=None):
        mover: Mover = cls.__mover_factory.create_mover(mover_type, element)
        # print(cls.__movers.items())
        if cls.ar[mover.get_start()-1] is False and cls.ar[mover.get_end()-1] is False:
            # print("adding")
            cls.ar[mover.get_start()-1] = cls.ar[mover.get_end()-1] = True
            cls.__movers[mover.get_start()] = mover

    def build(self) -> Board:
        return Board(self.__size, self.__movers)
