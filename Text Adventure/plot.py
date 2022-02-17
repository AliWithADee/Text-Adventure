import random


class Plot:
    def __init__(self):
        self.plotEvents = {}

    def __allOccurred(self, plotEvents):
        for plotEvent in plotEvents:
            if not self.plotEvents[plotEvent]:
                return False

        return True

    def __noneOccurred(self, plotEvents):
        for plotEvent in plotEvents:
            if self.plotEvents[plotEvent]:
                return False

        return True

    def createPlotEvent(self, plotEvent: str):
        self.plotEvents[plotEvent] = False

    def triggerPlotPoints(self, *events):
        for event in events:
            if event in self.plotEvents:
                self.plotEvents[event] = True

    def allHaveOccurred(self, *plotEvents):
        return lambda: self.__allOccurred(plotEvents)

    def noneHaveOccurred(self, *plotEvents):
        return lambda: self.__noneOccurred(plotEvents)


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
# Scenarios in which the player can carry out an action.
# Eg:
# - go to a new room
# - inspect something in the room
# - pickup an item
class Scene:
    def __init__(self, name, descriptions):
        self.name = name
        self.descriptions = descriptions
        self.mainPool = self.descriptions.copy()

    def getName(self):
        return self.name

    def getDescription(self):
        pool = []
        for desc in self.mainPool:
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
            self.mainPool.remove(description)
            if self.poolEmpty(): self.resetPool()

        return description.getDescription()

    def poolEmpty(self):
        for desc in self.mainPool:
            if desc.isAvailable():
                return False

        return True

    def resetPool(self):
        self.mainPool = self.descriptions.copy()
        print("reset")
