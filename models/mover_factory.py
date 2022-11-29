import random

from models.mover_enum import MoverType
from models.mover import Mover
from models.snake import Snake
from models.ladder import Ladder


class MoverFactory:
    __boardSize: int

    def __init__(self, board_size: int):
        self.__boardSize = board_size

    def create_mover(self, mover_type: MoverType, element=None) -> Mover:
        start: int
        end: int

        if mover_type == MoverType.SNAKE:
            if element is None:
                start_row: int = random.randint(1, self.__boardSize-1)
                end_row: int = random.randint(0, start_row-1)
                start = self.__boardSize * start_row + random.randint(1, self.__boardSize-1)
                end = self.__boardSize * end_row + random.randint(1, self.__boardSize-1)
            else:
                start = element[0]
                end = element[1]
            return Snake(start, end)

        else:
            if element is None:
                end_row: int = random.randint(1, self.__boardSize-1)
                start_row: int = random.randint(0, end_row-1)
                start = self.__boardSize * start_row + random.randint(1, self.__boardSize-1)
                end = self.__boardSize * end_row + random.randint(1, self.__boardSize-1)
            else:
                start = element[0]
                end = element[1]
            return Ladder(start, end)
