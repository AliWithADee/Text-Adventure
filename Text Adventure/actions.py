

# Actions:
# Actions the player can perform that have an effect on the plot.
# Scenes then behave differently depending on the nature of the plot.
class Action:
    def __init__(self, name, description=None, plotPoint=None):
        self.name = name
        self.description = description
        self.plotPoint = plotPoint

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def execute(self):
        if self.plotPoint:
            self.plotPoint.occur()


# An action that changes the current scene to something else.
# Eg: the player moves to a new room
class ChangeSceneAction(Action):
    def __init__(self, name, nextScene, description=None, plotPoint=None):
        super().__init__(name, description, plotPoint)

        self.nextScene = nextScene

    def getNextScene(self):
        return self.nextScene
