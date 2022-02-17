from plot import *


class Action:
    def __init__(self, plot, name, description, event, *conditions) -> None:
        self.plot = plot
        self.name = name
        self.description = description
        self.event = event
        self.conditions = conditions
    
    def getName(self):
        return self.name
    
    def execute(self):
        self.plot.triggerPlotEvents(self.event)
        return self.description
    
    def isAvailable(self):
        for condition in self.conditions:
            if not condition():
                return False
        
        return True

class ChangeSceneAction(Action):
    def __init__(self, plot, name, nextScene, event, *conditions) -> None:
        super().__init__(plot, name, None, event, conditions)

        self.nextScene = nextScene
    
    def execute(self):
        description = super().execute()
        return self.nextScene, description