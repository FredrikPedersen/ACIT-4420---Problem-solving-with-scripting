import random


def game_loop():
    size: int = int(input("Enter a number n for to get a map on the size n x n : "))
    mines: int = int(input("How many mines do you want? "))

    game_board: list = initialize_game_board(size, mines)
    player_board: list = generate_player_board(size)
    print_board(player_board)

    while True:

        if not check_victory_condition(player_board, game_board):

            x: int = int(input(f"X-value (1 to {size}): ")) - 1
            y: int = int(input(f"Y-value (1 to {size}): ")) - 1

            if game_board[y][x] == "X":
                print("GAME OVER")
                print_board(game_board)
                break

            else:
                player_board[y][x] = game_board[y][x]
                print_board(player_board)

        else:
            print("YOU WON!")
            break


def print_board(board: list):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()


def check_victory_condition(player_board: list, game_board: list) -> bool:
    for row in range(len(player_board)):
        for cell in range(len(player_board[row])):
            if player_board[row][cell] == "-" and game_board[row][cell] != "X":
                return False

    return True


def generate_player_board(size: int) -> list:
    player_map: list = [["-"] * size for i in range(size)]
    return player_map


def initialize_game_board(size: int, bombs: int) -> list:
    game_board: list = [[0] * size for i in range(size)]

    for i in range(bombs):
        x: int = random.randint(0, size - 1)
        y: int = random.randint(0, size - 1)
        game_board[y][x] = "X"

    add_values(game_board, size)

    return game_board


def add_values(game_board: list, size: int):

    for row in range(size):
        for cell in range(size):

            # Skip if there is a bomb in the cell
            if game_board[row][cell] == "X":
                continue

            # Check over current cell
            if row > 0 and game_board[row-1][cell] == "X":
                game_board[row][cell] += 1

            # Check under current cell
            if row < size - 1 and game_board[row + 1][cell] == "X":
                game_board[row][cell] += 1

            # Check left of current cell
            if cell > 0 and game_board[row][cell - 1] == "X":
                game_board[row][cell] += 1

            # Check right of current cell
            if cell < size - 1 and game_board[row][cell + 1] == "X":
                game_board[row][cell] += 1

            # Check top-left of current cell
            if row > 0 and cell > 0 and game_board[row - 1][cell - 1] == "X":
                game_board[row][cell] += 1

            # Check top-right of current cell
            if row > 0 and cell < size - 1 and game_board[row - 1][cell + 1] == "X":
                game_board[row][cell] += 1

            # Check down-left of current cell
            if row < size - 1 and cell > 0 and game_board[row + 1][cell - 1] == "X":
                game_board[row][cell] += 1

            # Check down-right of current cell
            if row < size - 1 and cell < size - 1 and game_board[row + 1][cell + 1] == "X":
                game_board[row][cell] += 1
