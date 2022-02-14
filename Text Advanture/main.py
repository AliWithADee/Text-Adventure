from room import *
from plot import *

entrance = Room("entrance")
lobby = Room("lobby")

entrance.linkRoom(lobby, Directions.EAST)

actions = entrance.getActions()
for type in actions:
    for action in actions[type]:
        print("{} {}".format(type, action))