import os
import sys
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from game import Game

import pygame

program: Optional["Game"] = None  # Game class

WIDTH: int = 800
HEIGHT: int = 600
SCREEN_SIZE: tuple[int, int] = (WIDTH, HEIGHT)
FPS: int = 60

FONT_NAME: str = pygame.font.get_default_font()
FOLDER = os.path.dirname(sys.modules['__main__'].__file__)
IMAGE_FOLDER = os.path.join(FOLDER, 'Assets\\Images')

BUTTON_IMAGE = 'Button.png'