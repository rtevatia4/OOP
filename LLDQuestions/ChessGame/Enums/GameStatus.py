from enum import Enum

class GameStatus(Enum):
    Active = 1
    BlackWin = 2
    WhiteWin = 3
    Forfeit = 4
    Resignation = 5
    Draw = 5