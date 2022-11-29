import random


class DiceService:

    @staticmethod
    def roll_dice() -> int:
        return random.randint(1, 6)

    @staticmethod
    def roll_all_dice(num_of_dices) -> int:
        sum_of_dices: int = 0
        for i in range(0, num_of_dices):
            sum_of_dices += DiceService.roll_dice()
        return sum_of_dices
