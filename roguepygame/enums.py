import enum


class ButtonStates(enum.Enum):
    ACTIVE = 0
    HOVERED = 1
    INACTIVE = 2

class Animations(enum.Enum):
    PLAYER_WALK = 0
    PLAYER_RUN = 1
    PLAYER_IDLE = 3