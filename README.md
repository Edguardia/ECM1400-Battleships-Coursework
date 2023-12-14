# ECM1400-Battleships-Coursework

## Introduction
This is the repository for the ECM1400 Battleships Coursework. The aim of this project is to create a Battleships game 
in Python. The game will have multiple ways to play, either in a console or with a web interface.
## Prerequisites
* Python 3.11docs

## Installation
* Clone the GitHub repository or run `pip install battleships-pkg-epratt`
* RUN `pip install -r requirements.txt`

## Getting Started
### For Simple Game
* RUN `python game_engine.py -c`

### For Command Line Game against AI
* EDIT `placement.json` to change where your ships will be placed
* Format of {"Ship_Name": ["X_coord", "Y_coord", "direction either v or h"]}
* RUN `python mp_game_engine.py -c`

### For Web Game against AI
* RUN `python main.py`
* Then go to https://127.0.0.1/placement in your browser

## Testing
* RUN `pytest`
## Developer Documentation
### Accessing Logs
* Logs for the games are stored in `battleships.log`
### Sphinx/Autodoc
To access the sphinx autodoc documentation, open `docs/build/html/index.html` in your browser or
visit [https://edguardia.github.io/ECM1400-Battleships-Coursework/](https://edguardia.github.io/ECM1400-Battleships-Coursework/)
####
### Config Documentation
* `config.yaml` contains the configuration for the game. This includes the board size
* To edit the board size, change the `board_size` variable in `config.yaml` to an integer preferably less than 20
* You can also change level of logging here by setting `logging_level` to one of `DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET`
####

* To edit the number or length of battleships add or edit new rows in `battleships.txt` with the format `name_of_ship, length_of_ship`

## Details

### Authors
* Edward Pratt
### Licence
* GPL-3.0
### Source
https://pypi.org/project/battleships-pkg-epratt/1.0.0/
https://github.com/Edguardia/ECM1400-Battleships-Coursework
#### Documentation
https://edguardia.github.io/ECM1400-Battleships-Coursework




# Self Assessment
## Complete Features
* components.py tasks
  * Simple Placement
  * Random Placement 
  * Custom Placement
* game_engine.py tasks
* mp_game_engine.py tasks
* main.py (FLASK) tasks
* Logging tasks
* Code Styling
* Project Delivery
  * https://pypi.org/project/battleships-pkg-epratt/1.0.0/
  * Sphinx Documentation
  * Hosting on GitHub
      * https://github.com/Edguardia/ECM1400-Battleships-Coursework
      * https://edguardia.github.io/ECM1400-Battleships-Coursework
* Input Validation

## Partially Complete Features
* Difficulty Levels
  * AI has been slightly improved to stop it hitting the same squared twice
* Testing
    * Most of the testing has been written
    * Not all custom functions have written tests
* Config Files
  * Config files have been implemented but not for all features user could choose


## Incomplete Features
* Multi-Player Interface
