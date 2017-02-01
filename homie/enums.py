from enum import Enum


class Resolution(Enum):
    FULL_HD = {
        'height': 1920, 
        'width': 1080
    }
    HD = {
        'height': 1280,
        'width': 720
    }
    STANDARD = {
        'height': 1024,
        'width': 768
    }
    
class Rotation(Enum):
    NORMAL = 0
    RIGHT = 90 
    UPSIDE_DOWN = 180
    LEFT = 270
