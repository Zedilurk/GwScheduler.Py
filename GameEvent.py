import json
import datetime

class GameEvent(object):
    """An instance of an event that will be listed in the schedule"""

    def __init__(self, j = None):
        self.EventName = ""
        self.EventTime = ""
        self.EventLocation = ""
        self.Recurring = False
        self.Users = []
        self.AutoResetRoster = False
        self.AutoResetTime = datetime.time(8,0,0)
        self.Private = False
        self.GroupsAllowedToView = []

        if j != None:
            self.__dict__ = json.loads(j)

    def AddUser(self, username):
        self.Users.append(username)

    def RemoveUser(self, username):
        self.Users.remove(username)

    def ResetRoster(self):
        self.Users.clear();


