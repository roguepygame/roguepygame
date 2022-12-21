import pygame
import constants as const
import root


class RandomObject(root.DrawableObject):  # TODO: Remove, this is just for testing
    def __init__(self):
        super(RandomObject, self).__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill("GREEN")
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.pos = pygame.Vector2(self.rect.topleft)
        self.speed = 300  # pixels per second

    def update(self):
        self.pos.x += self.program.dt * self.speed
        self.rect.x = round(self.pos.x)
        if self.rect.left > const.WIDTH:
            self.destroy_object()
