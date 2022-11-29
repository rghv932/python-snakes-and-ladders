# This is a sample Python script.
from math import ceil

from models.game import Game
from models.player import Player

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # take board size input
    board_size: int = 10
    while True:
        try:
            board_size = int(input("Enter the size of the board(It will become squared of NxN size):"))
            if board_size < 4 or board_size > 100:
                print("Board size must be between 4 and 100 inclusive([4,100])")
                continue
            else:
                break
        except ValueError:
            print("Sorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue

    # take no. of players input
    no_of_players: int = 2
    while True:
        try:
            no_of_players = int(input("Enter the number of players:"))
            if no_of_players < 2 or no_of_players > 100:
                print("No of players must be between 2 and 100 inclusive([2,100])")
                continue
            else:
                break
        except ValueError:
            print("Sorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue

    players: list[Player] = list()
    for i in range(0, no_of_players, 1):
        while True:
            name: str = input(f"Enter player {i+1} name:")
            if len(name) == 0:
                print("Sorry, a name cannot be empty.")
                continue
            else:
                break
        players.append(Player.Builder().set_name(name).build())

    # something

    game = Game(board_size, no_of_players, players)

    satisfied = False
    while not satisfied:
        game.print_board_details()
        satisfied_input = input(
            "Are you satisfied with the current configuration of Movers(Snakes and Ladders)? Yes/yes/y/Y "
            "for *yes* and No/no/n/N for *no*")
        if satisfied_input not in ["Yes", "yes", "y", "Y", "No", "no", "N", "n"]:
            print("Sorry, your response isn't from expected values.Pls retry")
            continue
        else:
            if satisfied_input in ["Yes", "yes", "y", "Y"]:
                satisfied = True
            else:
                config: int = 2
                while True:
                    try:
                        config = int(
                            input("Press :\n1)For configuring Snakes and Ladders yourself 1 by 1(Number of Snakes "
                                  "and Ladders are fixed based on your board input size).\nThe number of Snakes will "
                                  "be 1 greater (if odd board size)than number of Ladders to keep ur game long "
                                  "running, but same in case of even board size.\nFor example: if you input 7 as your "
                                  "board size then number of Snakes will be 4 and number of Ladders will be 3."
                                  "\n2)For randomly generating Snakes and Ladders again."))
                        if config != 1 and config != 2:
                            print("Value must be 1 or 2 to configure")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Sorry, I didn't understand that.")
                        # better try again... Return to the start of the loop
                        continue
                if config == 2:
                    print("configuring")
                    game.configure_snakes_ladders()
                elif config == 1:
                    snakes_ladders: list[tuple[int, int]] = list()
                    print(f"First lets take {ceil(board_size/2)} Snakes:")
                    while len(snakes_ladders) < board_size / 2:
                        while True:
                            try:
                                start, end = map(int, input("enter snake: head and tail").split())
                                list_to_check = [item for tup in snakes_ladders for item in tup]
                                if start in list_to_check or end in list_to_check:
                                    print("One of the given values are already a starting or ending position of "
                                          "either Snake or Ladder.Please try again!")
                                    continue
                                elif start <= end or start not in range(2, board_size*board_size) or end not in range(2, board_size*board_size):
                                    print(f"Snake head position must be greater than its tail position.Also the "
                                          f"values should be more than 1 and less than board size: {board_size}")
                                    continue
                                else:
                                    print("added")
                                    snakes_ladders.append((start, end))
                                    break
                            except ValueError:
                                print("Sorry, I didn't understand that.")
                                # better try again... Return to the start of the loop
                                continue

                    print(f"Lets take {board_size - len(snakes_ladders)} Ladders: ")
                    while len(snakes_ladders) < board_size:
                        while True:
                            try:
                                start, end = map(int, input("enter ladder: start and end").split())
                                list_to_check = [item for tup in snakes_ladders for item in tup]
                                if start in list_to_check or end in list_to_check:
                                    print("One of the given values are already a starting or ending position of "
                                          "either Snake or Ladder.Please try again!")
                                    continue
                                elif end <= start or start not in range(2, board_size*board_size) or end not in range(2, board_size*board_size):
                                    print("Ladder start position must be lesser than its end position.Also the "
                                          f"values should be more than 1 and less than board size: {board_size}")
                                    continue
                                else:
                                    print("added")
                                    snakes_ladders.append((start, end))
                                    break
                            except ValueError:
                                print("Sorry, I didn't understand that.")
                                # better try again... Return to the start of the loop
                                continue
                    game.configure_snakes_ladders(snakes_ladders)

    game.start_game()
    input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
