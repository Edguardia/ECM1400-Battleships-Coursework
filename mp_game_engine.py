"""Contains game engine functions for playing against an AI opponent"""

import random
import components
import game_engine

players = {"player": [],
           "ai": []}


def generate_attack(board: list) -> tuple:
    """Generates the coordinates of the computer's attack"""
    x = random.randint(0, len(board) - 1)
    y = random.randint(0, len(board[x]) - 1)
    coordinates = (x, y)

    return coordinates


def board_to_ascii(board: list) -> str:
    """Converts the board to ascii text to be printed"""

    board_ascii = ""
    for column in enumerate(board):
        for row in enumerate(column[1]):
            if board[column[0]][row[0]] is None:
                board_ascii += "O"
            if board[column[0]][row[0]] is not None:
                board_ascii += "X"
        board_ascii += "\n"

    return board_ascii


def ai_opponent_game_loop():
    """Game loop for playing against AI opponent"""
    print("Welcome to Battleships!")
    for user in players:
        players[user] = [
            components.initialise_board(), components.create_battleships()]
    players["ai"][0] = components.place_battleships(
        players["ai"][0], players["ai"][1], algorithm="random")

    players["player"][0] = components.place_battleships(
        players["player"][0], players["player"][1], algorithm="custom")

    print("Your board:")
    print(board_to_ascii(players["player"][0]))

    userhits = 0
    aihits = 0
    needed_hits = sum(players[user][1].values())

    turn_counter = 0
    while userhits < needed_hits and aihits < needed_hits:
        if turn_counter == 0:
            print("USER TURN:")
            target_coordinates = game_engine.cli_coordinates_input(players["player"][0])
            hit_or_miss = game_engine.attack(
                target_coordinates, players["ai"][0], players["ai"][1])
            if hit_or_miss is True:

                userhits += 1
            turn_counter = 1

        elif turn_counter == 1:
            print("AI TURN:")
            target_coordinates = generate_attack(players["player"][0])
            hit_or_miss = game_engine.attack(
                target_coordinates, players["player"][0], players["player"][1])
            if hit_or_miss is True:
                aihits += 1
            print(board_to_ascii(players["player"][0]))
            turn_counter = 0

    if userhits == needed_hits:
        print("You sunk all the AI battleships!")

    elif aihits == needed_hits:
        print("The AI sunk all your battleships!")


if __name__ == "__main__":
    ai_opponent_game_loop()
