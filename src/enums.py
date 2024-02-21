from enum import Enum

class Code(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Center(Enum):
    PAC = 0
    orbital = 1
    hangar = 2
    bridge = 3
    engineering = 4
    robotics = 5