import pygame
import constants as const
import root
import ui


class MainMenu(root.Scene):
    """
    Main menu scene. First scene that gets run after you start the game.
    """

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        ui.Button("New game", (const.WIDTH // 2, const.HEIGHT // 4),
                  self.start_game_button_click)

    def update(self) -> None:
        self.program.get_object_manager().object_update()

    def render(self, screen: pygame.Surface) -> None:
        screen.fill("LIGHTGRAY")  # Place for the background
        self.program.get_object_manager().object_render(screen)

    def start_game_button_click(self):
        self.program.get_manager().go_to(GameScene)


class GameScene(root.Scene):
    """
    Game Scene
    """
    def __init__(self, **kwargs):
        super(GameScene, self).__init__(**kwargs)
        ui.Text('Game', (const.WIDTH // 2, const.HEIGHT // 2), 48)

    def update(self):
        self.program.get_object_manager().object_update()

    def render(self, screen):
        screen.fill("LIGHTGRAY")  # Place for the background
        self.program.get_object_manager().object_render(screen)
