import enum
import random
from plot import * 


class Directions(enum.Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

    def reverse(direction):
        if direction == Directions.NORTH: return Directions.SOUTH
        elif direction == Directions.EAST: return Directions.WEST
        elif direction == Directions.WEST: return Directions.EAST
        return Directions.NORTH


class Room():
    def __init__(self, name, descriptions=[]) -> None:
        self.name = name
        self.descriptions = descriptions
        self.neighbours = {}
        self.actions = {}
        self.features = {}
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        unlocked = []
        for desc in self.descriptions:
            if desc.unlocked():
                unlocked.append(desc)
        
        description = unlocked[random.randint(0, len(unlocked)-1)]
        return description.getDescription()

    def getNeighbours(self):
        return self.neighbours
    
    def getActions(self):
        actions = {}

        moves = {}
        for direction in self.neighbours:
            moves[direction.value] = self.neighbours[direction]
        actions["move"] = moves

        inspections = {}
        for feature in self.features:
            inspections[feature] = self.features[feature]
        actions["inspect"] = inspections

        return actions

    def populate(self, features):
        self.features = features
    
    def linkRoom(self, room, direction):
        if not direction in self.neighbours:
            self.neighbours[direction] = room
            room.linkRoom(self, Directions.reverse(direction))


class RoomDescription():
    def __init__(self, desc, plotPoints=[]) -> None:
        self.desc = desc
        self.plotPoints = plotPoints
    
    def getDescription(self):
        return self.desc

    def unlocked(self) -> bool:
        for plotPoint in self.plotPoints:
            if not plotPoint.unlocked():
                return False
        return True


class RoomFeature():
    def __init__(self, name) -> None:
        self.name = name
    
    def getName(self):
        return self.name

class Item(RoomFeature):
    def __init__(self, name) -> None:
        super().__init__(name)
