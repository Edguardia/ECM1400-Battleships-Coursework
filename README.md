# ECM1400-Battleships-Coursework

## Introduction
This is the repository for the ECM1400 Battleships Coursework. The aim of this project is to create a Battleships game 
in Python. The game will have multiple ways to play, either in a console or with a web interface.
## Prerequisites
* Python 3.11

## Installation
* Clone the repository
* RUN `pip install -r requirements.txt`

## Getting Started
### For Simple Game
* RUN `python3 game_engine.py -c`

### For Command Line Game against AI
* RUN `python3 mp_game_engine.py -c`

### For Web Game against AI
* RUN `python3 main.py`
* Then go to [127.0.0.1/placement](https://127.0.0.1/placement) in your browser

## Testing
* RUN `pytest`
## Developer Documentation
### Config Documentation
* `config.yaml` contains the configuration for the game. This includes the board size
* To edit the board size, change the `board_size` variable in `config.yaml` to an integer preferably less than 20
####

* To edit the number or length of battleships add or edit new rows in `battleships.txt` with the format `name_of_ship, length_of_ship`

## Details

### Authors
* Edward Pratt
### Licence
*GPL-3.0
### Source
https://github.com/Edguardia/ECM1400-Battleships-Coursework
