import random
from actions import *
from plot import *


class Direction:
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


def reverse(direction) -> str:
    if direction == Direction.NORTH:
        return Direction.SOUTH
    elif direction == Direction.EAST:
        return Direction.WEST
    elif direction == Direction.WEST:
        return Direction.EAST
    return Direction.NORTH


# Rooms:
# Scenes that the player can move between, containing features.
class Room(Scene):
    def __init__(self, name, descriptions) -> None:
        super().__init__(name, descriptions)
        self.neighbours = {}
        self.features = []

    def getNeighbours(self):
        return self.neighbours

    def linkRoom(self, room, direction):
        self.neighbours[direction] = room
        self.addAction(ChangeSceneAction("move " + direction, room))

        opposite = reverse(direction)
        if opposite not in room.getNeighbours():
            room.linkRoom(self, opposite)

    def populate(self, feature):
        self.features.append(feature)
        self.addAction(ChangeSceneAction("inspect " + feature.getName(), feature))
        feature.addAction(ChangeSceneAction("go back", self))


# Features:
# A scene within a scene.
class Feature(Scene):
    def __init__(self, name, descriptions) -> None:
        super().__init__(name, descriptions)


# Items:
# Collectable features.
class Item(Feature):
    def __init__(self, name, descriptions) -> None:
        super().__init__(name, descriptions)

    def getActions(self):
        actions = super().getActions()
        actions.append(Action("pickup " + self.getName()))
        return actions


# Areas:
# A feature containing items.
class Area(Feature):
    def __init__(self, name, descriptions) -> None:
        super().__init__(name, descriptions)

        self.items = []

    def populate(self, item):
        self.items.append(item)
        self.addAction(ChangeSceneAction("inspect " + item.getName(), item))
        item.addAction(ChangeSceneAction("go back", self))
