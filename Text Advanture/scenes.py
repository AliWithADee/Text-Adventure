import random
import re
from tkinter.messagebox import NO
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

    # Priority Tiers
    # 1 - Unimportant descriptions / filler
    #   - Shown randomly after everything else
    #
    # 2 - Higher significance descriptions that should be shown before unimportant ones
    #   - Shown randomly before tier 1
    #
    # 3 - Very important descriptions
    #   - Always shown, if they are available

    def __init__(self, desc, priorityTier, *conditions):
        self.desc = desc
        self.priorityTier = priorityTier
        self.conditions = conditions

    def getDescription(self):
        return self.desc

    def getPriority(self):
        return self.priorityTier

    def isAvailable(self) -> bool:
        for condition in self.conditions:
            if not condition():
                return False

        return True


# Scenes:
# Scenarios with a range of descriotions, in which the player can carry out an action. Eg:
# - go to a new scene
# - inspect something in the scene
# - pickup an item in the scene
class Scene:
    def __init__(self, plot, name, descriptions):
        self.plot = plot
        self.name = name
        self.descriptions = descriptions
        self.descriptionPool = self.descriptions.copy()
        self.actions = []
        self.features = []

    def getName(self):
        return self.name

    def getDescription(self):
        pool = []
        for desc in self.descriptionPool:
            if desc.isAvailable():
                if not pool:
                    pool = [desc]
                elif desc.getPriority() > pool[0].getPriority():
                    pool = [desc]
                elif desc.getPriority() == pool[0].getPriority():
                    pool.append(desc)

        index = random.randint(0, len(pool) - 1)
        description = pool[index]

        if description.getPriority() <= 2:  # If tier 1 or 2, then remove from pool
            self.descriptionPool.remove(description)
            if self.poolEmpty(): self.resetPool()

        return description.getDescription()
    
    def getActions(self):
        return self.actions
    
    def addAction(self, action):
        self.actions.append(action)
    
    def getFeatures(self):
        return self.features
    
    def populate(self, scene, inspectEvent=None):
        self.features.append(scene)
        self.addAction("inspect " + scene.getName(), scene, inspectEvent)
        scene.addAction("go back", self)

    def poolEmpty(self):
        for desc in self.descriptionPool:
            if desc.isAvailable():
                return False

        return True

    def resetPool(self):
        self.descriptionPool = self.descriptions.copy()


# Rooms:
# Scenes that the player can move between, containing features.
class Room(Scene):
    def __init__(self, plot, name, descriptions) -> None:
        super().__init__(plot, name, descriptions)
        self.neighbours = {}

    def getNeighbours(self):
        return self.neighbours

    def linkRoom(self, room, direction, moveEvent=None):
        self.neighbours[direction] = room
        self.addAction(ChangeSceneAction(self.plot, "move " + direction, room, moveEvent))


# Items:
# Collectables.
class Item(Scene):
    def __init__(self, name, descriptions) -> None:
        super().__init__(name, descriptions)

    def getActions(self):
        actions = super().getActions()
        actions.append(Action("pickup " + self.getName()))
        return actions
