import pygame
import constants as const


class Scene:
    def __init__(self, **kwargs):
        self.program = const.program

    def start(self):
        pass

    def events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.program.quit()
        self.program.get_object_manager().object_events(events)

    def update(self):
        raise NotImplementedError

    def render(self, screen):
        raise NotImplementedError

    def end(self):
        pass


class SceneManager:
    def __init__(self):
        self.program = const.program
        self.scene = None
        self.object_manager = ObjectManager()

    def go_to(self, scene, **kwargs):
        if self.scene is not None:
            self.scene.end()
            self.object_manager.clear_objects()
        self.scene = scene(**kwargs)
        self.scene.program = self.program
        self.scene.start()


class ObjectManager:
    def __init__(self):
        self.program = const.program
        self.objects = []

    def object_events(self, events):
        for obj in self.objects:
            if callable(getattr(obj, "events", None)):
                obj.events(events)

    def object_update(self):
        for obj in self.objects:
            if callable(getattr(obj, "update", None)):
                obj.update()

    def object_render(self, screen):
        for obj in self.objects:
            if isinstance(obj, DrawableObject):
                obj.render(screen)

    def create_object(self, obj, ):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def clear_objects(self):
        self.objects.clear()


class GameObject:
    def __init__(self):
        self.program = const.program
        self.name = None
        self.child_objects = {}

    def add_child(self, child_obj, child_name=None):
        if child_name is None:
            child_name = len(self.child_objects)
            while child_name in self.child_objects:
                child_name += 1
        self.child_objects[str(child_name)] = child_obj

    def create_object(self, name=None):
        self.name = name
        self.program.get_object_manager().create_object(self)
        for child in self.child_objects.values():
            child.create_object()

    def destroy_object(self):
        for child in self.child_objects.values():
            child.destroy_object()
        self.program.get_object_manager().remove_object(self)


class DrawableObject(GameObject):
    def __init__(self, image, rect):
        super(DrawableObject, self).__init__()
        self.image = image
        self.rect = rect

    def render(self, screen):
        screen.blit(self.image, self.rect)
