from typing import Callable

import pygame
import constants as const
import root
from enums import ButtonStates


class Text(root.DrawableObject):
    """
    Text element class
    """
    def __init__(self, text: str, position: tuple[int, int], size: int = 20,
                 color: pygame.Color = pygame.Color("BLACK"), allign: str = "center",
                 create_object=True):
        super().__init__()
        self.text: str = text
        self.position: tuple[int, int] = position
        self.size: int = size
        self.color: pygame.Color = color
        self.allign: str = allign
        self.font: pygame.font.Font = pygame.font.Font(const.FONT_NAME, size)
        self.create_surface()
        if create_object:
            self.add_object()

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

    def update_color(self, new_color: pygame.Color) -> None:
        self.color = new_color
        self.create_surface()


class Button(root.ClickableObject):
    """
    Button class
    """
    def __init__(self, text: str, position: tuple[int, int], do: Callable, active: bool=True):
        super().__init__()
        self.state: ButtonStates = ButtonStates.ACTIVE if active else ButtonStates.INACTIVE
        self.images = self.program.assets.get_images('BUTTON')
        self.image = self.images[self.state.value]
        self.rect = self.image.get_rect(**{'center': position})
        self.do: Callable = do
        if active:
            self.program.get_event_manager().subscribe(pygame.MOUSEMOTION, self)
        self.add_child(Text(text, self.rect.center, 24, create_object=False))
        self.add_object()

    def check_state(self) -> None:
        """
        Check if button is hovered
        :return: None
        """
        if self.state != ButtonStates.INACTIVE:
            mouse_pos = self.program.get_scene().state['mouse_pos']
            if self.state == ButtonStates.ACTIVE:
                if self.rect.collidepoint(mouse_pos):
                    self.set_state(ButtonStates.HOVERED)
            elif self.state == ButtonStates.HOVERED:
                if not self.rect.collidepoint(mouse_pos):
                    self.set_state(ButtonStates.ACTIVE)

    def set_activity(self, active: bool) -> None:
        """
        Set whether the button is active or inactive
        :param active: true if button is active, otherwise false
        :return: None
        """
        if self.state == ButtonStates.ACTIVE and not active:
            self.program.get_event_manager().unsubscribe(pygame.MOUSEMOTION, self)
            self.set_state(ButtonStates.INACTIVE)
        elif self.state == ButtonStates.INACTIVE and active:
            self.program.get_event_manager().subscribe(pygame.MOUSEMOTION, self)
            self.set_state(ButtonStates.ACTIVE)
            self.check_state()


    def set_state(self, state: ButtonStates) -> None:
        """
        Set the state of the button
        :param state: button state
        :return: None
        """
        self.state = state
        self.image = self.images[self.state.value]

    def events(self, event: pygame.event.Event) -> None:
        super().events(event)
        if event.type == pygame.MOUSEMOTION:
            self.check_state()

    def click_function(self, position) -> None:
        """
        Function that gets called when the button is pressed
        :return: None
        """
        if self.state != ButtonStates.INACTIVE:
            self.do()


class TextBox(root.ClickableObject):
    START_POSITION = (10, 0)

    def __init__(self, position):
        super().__init__()
        self.image = self.program.assets.get_image('TEXTBOX')
        self.rect = self.image.get_rect(**{'center': position})
        self.text_string = ''
        self.text_object = TextBox.TextObject(self.text_string, self.rect.move(*TextBox.START_POSITION).midleft, allign='midleft', create_object=False)
        self.selected = False
        self.add_child(self.text_object)
        self.caret = TextBox.Caret(self)
        self.add_child(self.caret)
        self.add_object()

    def events(self, event: pygame.event.Event) -> None:
        super().events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.caret.move_caret(delta=-1)
            elif event.key == pygame.K_RIGHT:
                self.caret.move_caret(delta=1)
            elif event.key == pygame.K_BACKSPACE:
                if self.caret.caret_position > 0:
                    self.text_string = self.text_string[:self.caret.caret_position - 1] + self.text_string[self.caret.caret_position:]
                    self.text_object.update_text(self.text_string)
                    self.caret.move_caret(delta=-1)
            elif event.key == pygame.K_DELETE:
                if self.caret.caret_position < len(self.text_string):
                    self.text_string = self.text_string[:self.caret.caret_position] + self.text_string[self.caret.caret_position + 1:]
                    self.text_object.update_text(self.text_string)
            elif event.key == pygame.K_HOME:
                self.caret.move_caret(position=0)
            elif event.key == pygame.K_END:
                self.caret.move_caret(position=len(self.text_string))
            elif event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                self.set_selected(False)
        if event.type == pygame.TEXTINPUT:
            self.text_string = self.text_string[:self.caret.caret_position] + event.text + self.text_string[self.caret.caret_position:]
            self.text_object.update_text(self.text_string)
            self.caret.move_caret(delta=1)

    def click_function(self, position: tuple[int, int]):
        if not self.selected:
            self.set_selected(True)
        self.caret.move_caret(position=TextBox.get_click_position(self.text_object, position[0] + self.text_object.start_x - self.rect.x - TextBox.START_POSITION[0]))

    def clicked_outside(self, position: tuple[int, int]):
        if self.selected:
            self.set_selected(False)

    def set_selected(self, value: bool):
        self.selected = value
        self.caret.set_active(self.selected)
        if self.selected:
            self.program.get_event_manager().subscribe(pygame.KEYDOWN, self)
            self.program.get_event_manager().subscribe(pygame.TEXTINPUT, self)
        else:
            self.program.get_event_manager().unsubscribe(pygame.KEYDOWN, self)
            self.program.get_event_manager().unsubscribe(pygame.TEXTINPUT, self)

    class Caret(root.DrawableObject):
        def __init__(self, textbox: 'TextBox'):
            super().__init__()
            self.textbox = textbox
            self.image = pygame.Surface((1, 30))
            self.start_position = textbox.rect.move(TextBox.START_POSITION).midleft
            self.rect = self.image.get_rect(**{'center': self.start_position})
            self.layer = self.textbox.layer + 1
            self.caret_position = 12
            self.active = False
            self.display = False
            self.timer = root.Timer(600, self.swap_display, start=False, first_check=True).add_object()

        def render(self, screen: pygame.Surface) -> None:
            if self.display:
                super().render(screen)

        def set_active(self, value: bool):
            self.active = value
            if self.active:
                self.display = True
                self.timer.start_timer()
            else:
                self.display = False
                self.timer.stop_timer()

        def swap_display(self):
            self.display = not self.display

        def move_caret(self, position=-1, delta=0):
            if position != -1:
                self.caret_position = pygame.math.clamp(position, 0, len(self.textbox.text_string))
            if delta:
                self.caret_position = pygame.math.clamp(self.caret_position + delta, 0, len(self.textbox.text_string))
            self.timer.restart_timer()
            self.display = False
            self.rect.x = self.start_position[0] + self.textbox.text_object.font.size(self.textbox.text_string)[0] - self.textbox.text_object.font.size(self.textbox.text_string[self.caret_position:])[0]
            # Move left  side
            if self.rect.x < self.start_position[0] + self.textbox.text_object.start_x:
                self.textbox.text_object.move_start_x(self.rect.x - self.start_position[0])
            # Move right side
            if self.rect.x - self.start_position[0] > TextBox.TextObject.MAX_WIDTH + self.textbox.text_object.start_x:
                self.textbox.text_object.move_start_x(self.rect.x - self.start_position[0] - TextBox.TextObject.MAX_WIDTH)
            if self.textbox.text_object.shown_rect.width < self.textbox.text_object.MAX_WIDTH < self.textbox.text_object.rect.width:
                self.textbox.text_object.move_start_x(self.textbox.text_object.rect.width - self.textbox.text_object.MAX_WIDTH)
            if self.textbox.text_object.rect.width < self.textbox.text_object.MAX_WIDTH:
                self.textbox.text_object.move_start_x(0)
            # Move caret
            self.rect.x -= self.textbox.text_object.start_x

    class TextObject(Text):
        MAX_WIDTH = 180

        def __init__(self, text: str, position: tuple[int, int], size: int = 20,
                 color: pygame.Color = pygame.Color("BLACK"), allign: str = "center",
                 create_object=True):
            self.start_x = 0
            self.shown_rect = pygame.Rect(0, 0, 0, 0)
            super().__init__(text, position, size, color, allign, create_object)
            self.shown_rect.height = self.font.get_height()

        def calculate_shown_rect(self):
            self.shown_rect.x = self.start_x
            self.shown_rect.width = min(self.rect.width - self.start_x, TextBox.TextObject.MAX_WIDTH)

        def move_start_x(self, value):
            self.start_x = value
            self.calculate_shown_rect()

        def create_surface(self) -> None:
            super().create_surface()
            self.calculate_shown_rect()

        def render(self, screen: pygame.Surface) -> None:
            screen.blit(self.image, self.rect, self.shown_rect)

    @staticmethod
    def get_click_position(text_object: TextObject, click_x: int) -> int:
        positions = [0]
        current = 0
        for letter_size in text_object.font.metrics(text_object.text):
            current += letter_size[4]
            positions.append(current)

        # Binary search
        if click_x <= positions[0]:
            return 0
        if click_x >= positions[-1]:
            return len(text_object.text)
        low = 0
        high = len(text_object.text) - 1
        while low <= high:
            mid = (high + low) // 2
            if click_x < positions[mid]:
                high = mid - 1
            elif click_x > positions[mid]:
                low = mid + 1
            else:
                return mid
        return low if positions[low] - click_x < click_x - positions[high] else high

