from plot import *


def main():
    plot = Plot()
    beenInDiningRoom = plot.createPlotEvent("been in dining room")
    metMonster = plot.createPlotEvent("met monster")
    metMonsterAgain = plot.createPlotEvent("met monster again")
    killedMonster = plot.createPlotEvent("killed monster")
    canLeave = plot.createPlotEvent("can leave")

    diningRoom = plot.createScene("Dining Room", [
        Description("The dining room is red.", 1),
        Description("Best not waste time in here. I should probably leave now.", 3,
                    plot.allHaveOccurred(canLeave)),
        Description("The dining room is big.", 1),
        Description("I hope I don't see the monster again.", 2,
                    plot.allHaveOccurred(metMonster), plot.noneHaveOccurred(killedMonster, metMonsterAgain)),
        Description("The dining room is square.", 1),
        Description("The dining room is tall.", 1),
        Description("Aha the dining room again. What a nice room!", 1,
                    plot.allHaveOccurred(beenInDiningRoom)),
        Description("I hope I don't see the monster a third time!", 2,
                    plot.allHaveOccurred(metMonsterAgain), plot.noneHaveOccurred(killedMonster)),
        Description("Glad I won't be seeing that monster ever again.", 2,
                    plot.allHaveOccurred(killedMonster))
    ])

    iterations = 20

    print("Just entered\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotEvents(beenInDiningRoom)
    print("Been in dining room at least once\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotEvents(metMonster)
    print("Met monster once\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotEvents(metMonsterAgain)
    print("Met monster again\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotEvents(killedMonster)
    print("Killed the monster\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()
    print()

    plot.triggerPlotEvents(canLeave)
    print("Can leave the house now\n=======================================")
    for i in range(iterations):
        print(diningRoom.getDescription())
        print()



if __name__ == '__main__':
    main()
