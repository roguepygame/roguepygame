import pygame
import constants as const
import root


class Game:  # Rename this to the game name later
    def __init__(self, start_scene):
        const.program = self
        pygame.init()
        self.screen = pygame.display.set_mode(const.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.manager = root.SceneManager()
        self.manager.go_to(start_scene)

    def run(self):
        while True:
            scene = self.get_scene()
            scene.events(pygame.event.get())
            scene.update()
            scene.render(self.screen)
            pygame.display.flip()
            self.clock.tick(const.FPS)

    def quit(self):
        raise SystemExit()

    def get_object_manager(self):
        return self.manager.object_manager

    def get_scene(self):
        return self.manager.scene

    def get_manager(self):
        return self.manager
