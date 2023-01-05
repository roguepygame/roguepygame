import pygame
import constants as const
import root
import ui
import objects
import enums


class MainMenu(root.Scene):
    """
    Main menu scene. First scene that gets run after you start the game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ui.Button("New game", (const.WIDTH // 2, const.HEIGHT // 4),
                  self.start_game_button_click)

    def update(self) -> None:
        self.object_manager.object_update()

    def render(self, screen: pygame.Surface) -> None:
        screen.fill("LIGHTGRAY")  # Place for the background
        self.object_manager.object_render(screen)

    def start_game_button_click(self) -> None:
        """
        Method that gets called when the player press the New game button
        :return: None
        """
        self.program.get_manager().go_to(GameScene)


class GameScene(root.Scene):
    """
    Game Scene
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ui.Text('Game', (const.WIDTH // 2, const.HEIGHT // 2), 48)
        self.player = objects.Player(pygame.Vector2(100,100), [enums.Animations.PLAYER_WALK, enums.Animations.PLAYER_WALK]).add_object()

    def update(self):
        self.object_manager.object_update()

    def render(self, screen):
        screen.fill("LIGHTGRAY")  # Place for the background
        self.object_manager.object_render(screen)
