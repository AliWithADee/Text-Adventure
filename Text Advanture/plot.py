import random
from scenes import *
from actions import *


class Plot:
    def __init__(self):
        self.scenes = []
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
    
    def createScene(self, name, descriptions):
        scene = Scene(self, name, descriptions)
        self.scenes.append(scene)
        return scene

    def createPlotEvent(self, plotEvent: str):
        self.plotEvents[plotEvent] = False
        return plotEvent

    def triggerPlotEvents(self, *events):
        for event in events:
            if event in self.plotEvents:
                self.plotEvents[event] = True

    def allHaveOccurred(self, *plotEvents):
        return lambda: self.__allOccurred(plotEvents)

    def noneHaveOccurred(self, *plotEvents):
        return lambda: self.__noneOccurred(plotEvents)
