from typing import Type

import pygame
import constants as const
import root


class Game:  # TODO Rename this to the game name later
    """
    Main class of the game.
    If you want to run the game you should create the Game object and call run() method.
    """

    def __init__(self, start_scene: Type[root.Scene]):
        """
        Initialise the game

        :param start_scene: Scene used at the start
        """
        const.program = self
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode(const.SCREEN_SIZE)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.manager: root.SceneManager = root.SceneManager()
        self.manager.go_to(start_scene)

    def run(self) -> None:
        """
        Game loop

        :return: None
        """
        while True:
            scene = self.get_scene()
            scene.update_state()
            scene.events(pygame.event.get())
            scene.update()
            scene.render(self.screen)
            pygame.display.flip()
            self.clock.tick(const.FPS)

    def quit(self) -> None:
        """
        Method used to quit the game

        :return: None
        """
        raise SystemExit()

    def get_object_manager(self) -> root.ObjectManager:
        """
        Returns the ObjectManager of the game

        :return: object manager
        """
        return self.manager.object_manager

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
