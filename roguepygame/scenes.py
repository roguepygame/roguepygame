import constants as const
import root


class MainMenu(root.Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self):
        pass

    def render(self, screen):
        screen.fill("LIGHTGRAY")
