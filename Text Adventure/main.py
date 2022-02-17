from plot import *


def main():
    plot = Plot()
    plot.createPlotEvent("been in dining room")
    plot.createPlotEvent("met monster")
    plot.createPlotEvent("met monster again")
    plot.createPlotEvent("killed monster")
    plot.createPlotEvent("can leave")

    diningRoom = Scene("Dining Room", [
        Description("The dining room is red.", 1),
        Description("Best not waste time in here. I should probably leave now.", 3,
                    plot.allHaveOccurred("can leave")),
        Description("The dining room is big.", 1),
        Description("I hope I don't see the monster again.", 2,
                    plot.allHaveOccurred("met monster"), plot.noneHaveOccurred("killed monster")),
        Description("The dining room is square.", 1),
        Description("The dining room is tall.", 1),
        Description("Aha the dining room again. What a nice room!", 1,
                    plot.allHaveOccurred("been in dining room")),
        Description("I hope I don't see the monster a third time!", 2,
                    plot.allHaveOccurred("met monster again"), plot.noneHaveOccurred("killed monster")),
        Description("Glad I won't be seeing that monster ever again.", 2,
                    plot.allHaveOccurred("killed monster")),
        Description("Best not waste time in here. I should probably leave now.", 3,
                    plot.allHaveOccurred("can leave"))
    ])

    iterations = 20

    print("Just entered\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotPoints("been in dining room")
    print("Been in dining room at least once\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotPoints("met monster")
    print("Met monster once\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotPoints("met monster again")
    print("Met monster again\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotPoints("killed monster")
    print("Killed the monster\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotPoints("can leave")
    print("Can leave the house now\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()



if __name__ == '__main__':
    main()
