class GameEvent(object):
    """An instance of an event that will be listed in the schedule"""
    EventName = ""
    EventTime = ""
    EventLocation = ""
    Recurring = False
    Users = []

    AutoResetRoster = False
    AutoResetTime = ""

    Private = False
    GroupsAllowedToView = []

    def AddUser(username):
        Users.append(username)


