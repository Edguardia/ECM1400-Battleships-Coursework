"""This file contains the game loop and the functions that are used in the game loop."""

import components
from base_logger import logger


def attack(coordinates: tuple, board: list, battleships: dict) -> bool:
    """Checks if the attack is a hit or a miss and changes value in board and battleships"""
    if board[coordinates[0]][coordinates[1]] is not None:
        battleships[board[coordinates[0]][coordinates[1]]] -= 1
        board[coordinates[0]][coordinates[1]] = None
        print("Hit!")

        for ships in battleships.copy():
            if battleships[ships] == 0:
                print("You sunk my " + ships)
                del battleships[ships]
        return True

    print("Miss!")
    return False


def cli_coordinates_input(board: list) -> tuple:
    """Takes the coordinates of the attack from the user"""
    board_size = len(board)
    while True:
        try:
            coordinates = input("Enter the coordinates of your attack: ")
            coordinates = coordinates.split(",")
            coordinates = (int(coordinates[0]), int(coordinates[1]))

            if 0 <= int(coordinates[0]) < board_size and 0 <= int(coordinates[1]) < board_size:
                return coordinates

            print("Invalid coordinates")
            continue

        except (ValueError, IndexError):
            print("Invalid coordinates")


def simple_game_loop():
    """A simple game loop for testing"""

    print("Welcome to Battleships!")
    initial_board = components.initialise_board()
    battleships = components.create_battleships()
    board = components.place_battleships(initial_board, battleships)
    needed_hits = sum(battleships.values())
    hits = 0
    while hits < needed_hits:
        target_coordinates = cli_coordinates_input(board)
        hit_or_miss = attack(target_coordinates, board, battleships)
        if hit_or_miss is True:
            hits += 1
    print("You sunk all the battleships!")


if __name__ == "__main__":
    simple_game_loop()
