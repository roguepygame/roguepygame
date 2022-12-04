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

    def update(self):
        self.rect.x += 5
        if self.rect.x > const.WIDTH:
            self.destroy_object()
