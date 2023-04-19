from typing import Type, Optional

import pygame
import constants as const
import root
import scenes
import assets


class Game:  # TODO Rename this to the game name later
    """
    Main class of the game.
    If you want to run the game you should create the Game object and call run() method.
    """

    def __init__(self, start_scene: Optional[Type[root.Scene]]=scenes.GameScene):
        """
        Initialise the game
        :param start_scene: Scene used at the start
        """
        const.program = self
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode(const.SCREEN_SIZE)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.assets: assets.Assets = assets.Assets()
        self.assets.load()
        self.manager: root.SceneManager = root.SceneManager()
        self.dt: int = 0
        self.manager.start_program(start_scene)

    def run(self) -> None:
        """
        Game loop
        :return: None
        """
        while True:
            scene = self.get_scene()
            pygame.display.set_caption(f"{self.clock.get_fps():.2f} {len(self.manager.object_manager.objects)}")
            scene.update_state()
            scene.events(pygame.event.get())
            scene.update()
            scene.render(self.screen)
            pygame.display.flip()
            self.manager.end_frame()
            self.dt = self.clock.tick(const.FPS) / 1000

    def quit(self) -> None:
        """
        Method used to quit the game
        :return: None
        """
        raise SystemExit

    def get_object_manager(self) -> root.ObjectManager:
        """
        Returns the ObjectManager of the game
        :return: object manager
        """
        return self.manager.object_manager

    def get_event_manager(self) -> root.EventManager:
        """
        Returns the EventManager of the game
        :return: object manager
        """
        return self.manager.object_manager.event_manager

    def get_scene(self) -> root.Scene:
        """
        Returns the currently active Scene
        :return: active Scene
        """
        return self.manager.scene

    def get_manager(self) -> root.SceneManager:
        """
        Returns the SceneManager of the game
        :return: scene manager
        """
        return self.manager

    def get_assets(self) -> assets.Assets:
        """
        Returns the Assets
        :return: assets
        """
        return self.assets
