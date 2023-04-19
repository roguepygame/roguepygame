import pygame
import root
import scenes


class RandomObject(root.DrawableObject):  # TODO: Remove, this is just for testing
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill("GREEN")
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.pos = pygame.Vector2(self.rect.topleft)
        self.velocity = pygame.Vector2(300, 0)  # pixels per second
        self.object_manager.add_object(self)

    def update(self):
        self.pos.x += self.program.dt * self.velocity.x
        self.rect.x = round(self.pos.x)
        walls = self.object_manager.get_group("walls")
        if walls.group_collide(self):
            self.destroy_object()


class Wall(root.DrawableObject):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill("GRAY")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, "DARKGRAY", self.rect, 1)
        self.rect.center = (x, y)
        self.object_manager.add_object(self, group_name="walls")


class ControlObject(root.GameObject):  # TODO Testing object, can be removed in future
    def __init__(self):
        super().__init__()
        self.program.get_event_manager().subscribe(pygame.KEYDOWN, self)
        self.add_object()

    def events(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.program.get_manager().go_to_with_save('GameScene', scenes.PauseScene)


class ControlObjectPause(root.GameObject):
    def __init__(self):
        super().__init__()
        self.program.get_event_manager().subscribe(pygame.KEYDOWN, self)
        self.add_object()

    def events(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.program.get_manager().load_scene('GameScene')
