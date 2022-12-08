from typing import Callable

import pygame
import constants as const
import root


class Text(root.DrawableObject):
    """
    Text element class
    """
    def __init__(self, text: str, position: tuple[int, int], size: int = 20,
                 color: pygame.Color = pygame.Color("BLACK"), allign: str = "center",
                 create_object=True):
        super(Text, self).__init__()
        self.text: str = text
        self.position: tuple[int, int] = position
        self.size: int = size
        self.color: pygame.Color = color
        self.allign: str = allign
        self.font: pygame.font.Font = pygame.font.Font(const.FONT_NAME, size)
        self.create_surface()
        if create_object:
            self.create_object()

    def create_surface(self) -> None:
        """
        Creates the Surface object for the text
        :return: None
        """
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(**{self.allign: self.position})

    def update_text(self, new_text: str) -> None:
        """
        Function that changes the text of the Text object
        :param new_text: New text
        :return: None
        """
        if new_text != self.text:
            self.text = new_text
            self.create_surface()


class Button(root.ClickableObject):
    """
    Button class
    """
    def __init__(self, text: str, position: tuple[int, int], do: Callable):
        super(Button, self).__init__()
        self.image = self.program.get_assets().get_image('BUTTON')
        self.rect = self.image.get_rect(**{'center': position})
        self.do: Callable = do
        self.add_child(Text(text, self.rect.center, 24, create_object=False))
        self.create_object()

    def click_function(self) -> None:
        """
        Function that gets called when the button is pressed
        :return: None
        """
        self.do()
