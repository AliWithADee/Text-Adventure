from room import *
from actions import *
from plot import *


def displayScene(scene: Scene):
    name = scene.getName()
    desc = scene.getDescription()
    print("{}\n{}\n".format(name, desc))

    actions = scene.getActions()
    for action in actions:
        print(action.getName())


def main():
    bedroom = Room("bedroom", [
        Description("The bedroom was red.")
    ])

    table = Area(bedroom, "table", [
        Description("The table was round.")
    ])

    displayScene(table)







if __name__ == '__main__':
    main()
