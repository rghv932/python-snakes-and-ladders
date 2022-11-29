from models.mover import Mover


class Board:
    __size: int
    __movers: dict[int, Mover]

    def __init__(self, size: int, movers: dict):
        self.__size = size
        self.__movers = movers

    def get_movers(self):
        return self.__movers

    def set_movers(self, movers: dict[int, Mover]):
        # print("inside board set movers")
        self.__movers = movers

    def print_board_details(self):
        print("Board size: " + str(self.__size * self.__size))
        print("Movers: ")

        for mover in self.__movers.values():
            mover_name = type(mover).__name__
            # print(mover_name)  # might need to change here
            something = "Snake" if mover_name == "Snake" else "Ladder"
            print(something + ": start: " + str(mover.get_start()) + " end " + str(mover.get_end()))
