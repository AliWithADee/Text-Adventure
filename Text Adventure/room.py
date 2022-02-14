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


class Description:
    def __init__(self, desc, plotPoints=None) -> None:
        self.desc = desc
        self.plotPoints = plotPoints if plotPoints else []

    def getDescription(self):
        return self.desc

    def isAvailable(self) -> bool:
        for plotPoint in self.plotPoints:
            if not plotPoint.unlocked():
                return False
        return True

    def getPriority(self):
        highest = 1
        for plotPoint in self.plotPoints:
            if plotPoint.getPriority() > highest:
                highest = plotPoint.getPriority()

        return highest


# Scenes:
# Scenarios in which the player can carry out an action.
# Eg:
# - go to a new room
# - inspect something in the room
# - pickup an item
class Scene:
    def __init__(self, name, descriptions):
        self.name = name
        self.descriptions = descriptions
        self.actions = []

    def getName(self):
        return self.name

    def getDescription(self):
        pool = []
        for desc in self.descriptions:
            if desc.isAvailable():
                if (not pool) or (desc.getPriority() > pool[0].getPriority()):
                    pool = [desc]
                elif desc.getPriority() == pool[0].getPriority():
                    pool.append(desc)

        index = random.randint(0, len(pool) - 1)
        chosen = pool[index]
        return chosen.getDescription()

    def getActions(self):
        return self.actions

    def addAction(self, action: Action):
        self.actions.append(action)

    def displayScene(self):
        print("{}\n{}\n".format(self.getName(), self.getDescription()))

        actions = self.getActions()
        for actionType in actions:
            for action in actions[actionType]:
                print("{} {}".format(actionType, action))


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
