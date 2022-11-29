from abc import ABC


class Mover(ABC):
    _start: int
    _end: int

    def __init__(self, start: int, end: int):
        if start == end:
            raise ValueError("Start and end positions cannot be same")
        self._start = start
        self._end = end

    def get_start(self) -> int:
        return self._start

    def get_end(self) -> int:
        return self._end
