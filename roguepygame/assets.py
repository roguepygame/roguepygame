import os
import pygame
import constants as const


def load_image(image_name: str, transparent_color: pygame.Color=None, alpha: int=None) -> pygame.Surface:
    """
    Function used to load the image from the disk to the pygame.Surface
    :param image_name: name of the file
    :param transparent_color: transparent color of the image
    :param alpha: alpha value of the image
    :return: image Surface
    """
    image = pygame.image.load(os.path.join(const.IMAGE_FOLDER, image_name))
    if transparent_color:
        image.set_colorkey(transparent_color)
    if alpha:
        image.set_alpha(alpha)
    return image.convert_alpha()


class Assets:
    """
    Class used to work with the images/sounds etc.
    """
    def __init__(self):
        self.images: dict[str, pygame.Surface] = {}
        self.images_list: dict[str, list[pygame.Surface]] = {}

    def load(self) -> None:
        """
        Loads the images from the disk
        :return: None
        """
        self.images_list["BUTTON"] = [load_image(const.BUTTON_IMAGE),
                                      load_image(const.HOVERED_BUTTON_IMAGE),
                                      load_image(const.INACTIVE_BUTTON_IMAGE)]

    def get_image(self, name: str) -> pygame.Surface:
        """
        Returns the image
        :param name: name of the image
        :return: image Surface
        """
        return self.images[name]

    def get_images(self, name: str) -> list[pygame.Surface]:
        """
        Returns the list of images
        :param name: name of the images
        :return: list of image Surface
        """
        return self.images_list[name]