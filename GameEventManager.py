import GameEvent

class GameEventManager(object):
    """description of class"""
    ScheduledEvents = []

    @staticmethod
    def AddEvent (gameEvent):
        GameEventManager.ScheduledEvents.append(gameEvent)

