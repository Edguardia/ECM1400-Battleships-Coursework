"""This module contains the initial functions for the battleships game"""

import random
import json
from base_logger import logger


def initialise_board(size: int = 10) -> list:
    """Initialises the board with the given size"""
    board = []
    # x = columns and y = rows
    for column in range(int(size)):
        board.append([])
        for _ in range(int(size)):
            board[column].append(None)
    logger.info(("Board initialised, Size:", size))
    return board


def create_battleships(file_name: str = "battleships.txt") -> dict:
    """Creates a dictionary of battleships from the given file"""
    ships = {}

    with open(file_name, encoding="utf-8") as file:
        for line in file:
            (key, val) = line.split(",")
            ships[key] = int(val)

    logger.info(("Battleships created", ships))
    return ships


def validate_placement(direction: str, board: list, x: int, y: int, length: int) -> bool:
    """Checks if the placement of the battleships is valid on the board"""
    logger.debug(("Validating placement", direction, board, x, y, length))
    board_size = len(board)
    valid = True
    if direction == "h":
        for i in range(0, length):
            if x + i >= board_size or board[x + i][y] is not None:
                valid = False
                logger.debug("Invalid Placement")
                break

            continue

    elif direction == "v":
        for i in range(0, length):
            if y + i >= board_size or board[x][y + i] is not None:
                valid = False
                logger.debug("Invalid Placement")
                break

            continue
    logger.debug("Valid Placement")
    return valid


def place_battleships(board: list, ships: dict, board_data: list = None, algorithm: str = "simple") -> list:
    """Places the battleships on the initialised board"""
    if algorithm == "simple":
        logger.info("Placing battleships with simple algorithm")
        i = 0
        for ship in ships:
            logger.info(("Placing battleship:", ship))
            for length in range(ships[ship]):
                board[i][length] = ship
            i += 1

    elif algorithm == "random":
        logger.info("Placing battleships with random algorithm")
        for ship in ships:
            logger.info(("Placing battleship:", ship))
            placed = False
            while placed is False:
                x = random.randint(0, len(board) - 1)
                y = random.randint(0, len(board) - 1)
                # v = down, h = right
                options = ["v", "h"]
                choose_direction = random.choice(options)
                if choose_direction == "h":
                    valid = validate_placement("h", board, x, y, ships[ship])
                    if valid is True:
                        for i in range(0, ships[ship]):
                            board[x + i][y] = ship
                        placed = True
                    else:
                        continue

                elif choose_direction == "v":
                    valid = validate_placement("v", board, x, y, ships[ship])
                    if valid is True:
                        for i in range(0, ships[ship]):
                            board[x][y + i] = ship
                        placed = True
                    else:
                        continue

    elif algorithm == "custom":
        logger.info("Placing battleships with custom algorithm")
        with open("placement.json", encoding="utf-8") as file:
            placement = json.load(file)

        if board_data is not None:
            placement = board_data

        logger.info(("Placing with these instructions:", placement))
        for ship in placement:
            logger.info(("Placing battleship:", ship))
            x = int(placement[ship][0])
            y = int(placement[ship][1])
            direction = placement[ship][2]
            placed = False
            while placed is False:

                if direction == "h":
                    valid = validate_placement(
                        "h", board, x, y, ships[ship])
                    if valid is True:
                        for i in range(0, ships[ship]):
                            board[x + i][y] = ship
                        placed = True
                    else:
                        continue

                elif direction == "v":
                    valid = validate_placement(
                        "v", board, x, y, ships[ship])
                    if valid is True:
                        for i in range(0, ships[ship]):
                            board[x][y + i] = ship
                        placed = True
                    else:
                        continue

                else:
                    print("Invalid direction")
                    continue
    else:
        print("Invalid difficulty")
    print(board)
    return board
