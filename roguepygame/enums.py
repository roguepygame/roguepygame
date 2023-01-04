import enum


class ButtonStates(enum.Enum):
    ACTIVE = 0
    HOVERED = 1
    INACTIVE = 2

class PlayerAnimations(enum.Enum):
    WALK = 0
    RUN = 1
    IDLE = 3