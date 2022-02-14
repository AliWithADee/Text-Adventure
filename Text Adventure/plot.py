class PlotPoint:
    def __init__(self, name, priority) -> None:
        self.name = name
        if 1 <= priority <= 100: self.priority = priority
        else: self.priority = 1
        self.occurred = False

    def getName(self):
        return self.name

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority

    def hasOccurred(self):
        return self.occurred

    def occur(self):
        self.occurred = True
