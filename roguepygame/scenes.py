import pygame
import root


class MainMenu(root.Scene):
    """
    Main menu scene. First scene that gets run after you start the game.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self) -> None:
        """
        Method that updates the MainMenu
        :return: None
        """
        pass

    def render(self, screen: pygame.Surface) -> None:
        """
        Method that renders the MainMenu
        :param screen: game window
        :return: None
        """
        screen.fill("LIGHTGRAY")  # Place for the background
        self.program.get_object_manager().object_render(screen)
