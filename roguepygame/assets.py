import os
import pygame
import constants as const


# File names
BUTTON_REGULAR_IMAGE = 'Button.png'
BUTTON_HOVERED_IMAGE = 'ButtonHovered.png'
BUTTON_INACTIVE_IMAGE = 'ButtonInactive.png'
TEXT_BOX_IMAGE = 'TextBox.png'


def load_image(image_name: str, transparent_color: pygame.Color=None, alpha: int=None) -> pygame.Surface:
    """
    Function used to load the image from the disk to the pygame.Surface
    :param image_name: name of the file
    :param transparent_color: transparent color of the image
    :param alpha: alpha value of the image
    :return: image Surface
    """
    image = pygame.image.load(os.path.join(const.IMAGE_FOLDER, image_name))
    if transparent_color is not None:
        image.set_colorkey(transparent_color)
    if alpha is not None:
        image.set_alpha(alpha)
    return image.convert_alpha()


class Assets:
    """
    Class used to work with the images/sounds etc.
    """
    def __init__(self):
        self.images: dict[str, list[pygame.Surface]] = {}

    def load(self) -> None:
        """
        Loads the images from the disk
        :return: None
        """
        self.images["BUTTON"] = [load_image(BUTTON_REGULAR_IMAGE),
                                 load_image(BUTTON_HOVERED_IMAGE),
                                 load_image(BUTTON_INACTIVE_IMAGE)]
        self.images["TEXTBOX"] = [load_image(TEXT_BOX_IMAGE)]

    def get_image(self, name: str) -> pygame.Surface:
        """
        Returns the image
        :param name: name of the image
        :return: image Surface
        """
        return self.images[name][0]

    def get_images(self, name: str) -> list[pygame.Surface]:
        """
        Returns the list of images
        :param name: name of the images
        :return: list of image Surface
        """
        return self.images[name]
