from typing import Callable, Literal

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
    BUTTON_STATES = {'ACTIVE': 0, 'HOVERED': 1, 'INACTIVE': 2}
    """
    Button class
    """
    def __init__(self, text: str, position: tuple[int, int], do: Callable, active: bool=True):
        super(Button, self).__init__()
        self.state = 'ACTIVE' if active else 'INACTIVE'
        self.images = self.program.assets.get_images('BUTTON')
        self.image = self.images[Button.BUTTON_STATES[self.state]]
        self.rect = self.image.get_rect(**{'center': position})
        self.do: Callable = do
        if active:
            self.program.get_event_manager().subscribe(pygame.MOUSEMOTION, self)
        self.add_child(Text(text, self.rect.center, 24, create_object=False))
        self.create_object()

    def check_state(self) -> None:
        """
        Check if button is hovered
        :return: None
        """
        if self.state != 'INACTIVE':
            mouse_pos = self.program.get_scene().state['mouse_pos']
            if self.state == 'ACTIVE':
                if self.rect.collidepoint(mouse_pos):
                    self.set_state('HOVERED')
            elif self.state == 'HOVERED':
                if not self.rect.collidepoint(mouse_pos):
                    self.set_state('ACTIVE')

    def set_activity(self, active: bool) -> None:
        """
        Set whether the button is active or inactive
        :param active: true if button is active, otherwise false
        :return: None
        """
        if self.state == 'ACTIVE' and not active:
            self.program.get_event_manager().unsubscribe(pygame.MOUSEMOTION, self)
            self.set_state('INACTIVE')
        elif self.state == 'INACTIVE' and active:
            self.program.get_event_manager().subscribe(pygame.MOUSEMOTION, self)
            self.set_state('ACTIVE')
            self.check_state()


    def set_state(self, state: Literal['ACTIVE', 'HOVERED', 'INACTIVE']) -> None:
        """
        Set the state of the button
        :param state: button state
        :return: None
        """
        self.state = state
        self.image = self.images[Button.BUTTON_STATES[self.state]]

    def events(self, event: pygame.event.Event) -> None:
        super().events(event)
        if event.type == pygame.MOUSEMOTION:
            self.check_state()

    def click_function(self) -> None:
        """
        Function that gets called when the button is pressed
        :return: None
        """
        if self.state != 'INACTIVE':
            self.do()
