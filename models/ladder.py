from models.mover import Mover


class Ladder(Mover):

    def __init__(self, start: int, end: int):
        # print("ladder end: " + str(end) + "start: " + str(start))
        super().__init__(start, end)
        if end <= start:
            raise ValueError("Ladder start must be lesser than its end.")
