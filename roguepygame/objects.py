import pygame
import constants as const
import root
import assets
import enums


class RandomObject(root.DrawableObject):  # TODO: Remove, this is just for testing
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill("GREEN")
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.pos = pygame.Vector2(self.rect.topleft)
        self.velocity = pygame.Vector2(300, 0)  # pixels per second

    def update(self):
        self.pos.x += self.program.dt * self.velocity.x
        self.rect.x = round(self.pos.x)
        if self.rect.left > const.WIDTH:
            self.destroy_object()

class Player(root.AnimatedObject):
    def __init__(self, pos, animations):
        super().__init__(animations)
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos.x, self.pos.y)