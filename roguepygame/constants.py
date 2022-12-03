from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from game import Game

program: Optional["Game"] = None  # Game class

WIDTH: int = 800
HEIGHT: int = 600
SCREEN_SIZE: tuple[int, int] = (WIDTH, HEIGHT)
FPS: int = 60
