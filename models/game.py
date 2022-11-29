from models.board import Board
from models.builder import Builder
from models.mover import Mover
from models.player import Player
from services.dice_service import DiceService as ds


class Game:
    __board_size: int
    __board: Board
    __no_of_players: int
    __players: list[Player]
    __winners: list[Player]

    def __init__(self, board_size, no_of_players, players: list[Player]):
        self.__no_of_players: int
        self.__board_size = board_size
        self.__no_of_players = no_of_players
        self.builder = Builder(self.__board_size)
        self.__board = self.builder.build()
        self.__players = players
        self.__winners = list()

    def configure_snakes_ladders(self, snakes_ladders: list = None):
        # print("print inside game.py configure")
        self.__board.set_movers(self.builder.configure_snakes_ladders(snakes_ladders))

    def print_board_details(self):
        self.__board.print_board_details()

    def __is_player_won(self, player) -> bool:
        if player.get_position() == self.__board_size * self.__board_size:
            return True
        return False

    def __mover_play(self, position: int):
        new_position = 0
        movers: dict[int, Mover] = self.__board.get_movers()
        if movers.get(position) is not None:
            new_position = movers.get(position).get_end()
        return new_position if new_position != 0 else position

    def __move_player_by_dice(self, dice: int, player: Player):
        current_position = player.get_position()
        if current_position + dice <= self.__board_size * self.__board_size:
            position = current_position + dice
            position = self.__mover_play(position)
            player.set_position(position)
            print(f"Player {player.get_name()} moved from {current_position} to {position}")
        else:
            print(f"Unlucky! You need to get to exact {self.__board_size * self.__board_size} position to win!")

    def start_game(self):
        while True:
            for player in self.__players:
                dice_value: int = ds.roll_all_dice(1)
                print("current position: " + str(player.get_position()) + ",current dice value: " + str(dice_value))
                self.__move_player_by_dice(dice_value, player)
                if self.__is_player_won(player):
                    self.__winners.append(self.__players.pop(self.__players.index(player)))

            if len(self.__winners) == self.__no_of_players - 1:
                break
        self.__on_game_end()

    def __on_game_end(self):
        for i, winner in enumerate(self.__winners, 1):
            print(f"Player {winner.get_name()} won at rank: {i}")
        lost_player: Player = list(set(self.__players) - set(self.__winners))[0]
        print(f"Unfortunately! player {lost_player.get_name()} lost! Better luck next time :)")
