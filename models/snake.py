from models.mover import Mover


class Snake(Mover):

    def __init__(self, head: int, tail: int):
        # print("snake start: " + str(head) + "end: " + str(tail))
        super().__init__(head, tail)
        if head <= tail:
            raise ValueError("Snake start must be greater than its end.")
