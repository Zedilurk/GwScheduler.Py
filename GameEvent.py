class GameEvent(object):
    """An instance of an event that will be listed in the schedule"""

    def __init__(self, eventName):
        self.EventName = eventName
        self.EventTime = ""
        self.EventLocation = ""
        self.Recurring = False
        self.Users = []
        self.AutoResetRoster = False
        self.AutoResetTime = ""
        self.Private = False
        self.GroupsAllowedToView = []

    def AddUser(self, username):
        self.Users.append(username)


