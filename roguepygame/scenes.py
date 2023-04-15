import pygame
import constants as const
import root
import ui
import objects


class MainMenu(root.Scene):
    """
    Main menu scene. First scene that gets run after you start the game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ui.Button("New game", (const.WIDTH // 2, const.HEIGHT // 4),
                  self.start_game_button_click)
        ui.TextBox((const.WIDTH // 2, const.HEIGHT // 2))

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
        objects.ControlObject()
        self.pause_text = ui.Text("PAUSE", (const.WIDTH // 2, const.HEIGHT // 2), 48, create_object=False)
        self.timer = root.Timer(1000, self.spawn_unit).add_object()
        self.counter = ui.Text('', (const.WIDTH // 2, const.HEIGHT // 2 + 50), 48)
        for i in range(5):
            objects.Wall(const.WIDTH - 100, 50 + i * 40)

    def update(self):
        if self.running:
            self.object_manager.object_update()
            self.counter.update_text(f'Objects on screen: {len(self.program.get_object_manager().objects)}')

    def render(self, screen):
        screen.fill("LIGHTGRAY")  # Place for the background
        self.object_manager.object_render(screen)

    def pause(self):
        super().pause()
        if not self.running:
            self.pause_text.add_object()
            self.counter.update_text(f'Objects on screen: {len(self.program.get_object_manager().objects)}')
            for text_object in self.object_manager.get_objects_of_type(ui.Text):
                text_object.update_color(pygame.Color("RED"))
        else:
            self.object_manager.remove_object(self.pause_text)
            for text_object in self.object_manager.get_objects_of_type(ui.Text):
                text_object.update_color(pygame.Color("BLACK"))

    def spawn_unit(self) -> None:
        """
        Method used to spawn game object
        :return: None
        """
        objects.RandomObject()
