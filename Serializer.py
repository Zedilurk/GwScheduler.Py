import json;
import glob, os;
from GameEvent import GameEvent
from GameEventManager import GameEventManager;

class Serializer(object):
    """description of class"""

    @staticmethod
    def SaveToFile():
        for gameEvent in GameEventManager.ScheduledEvents:
            name = gameEvent.EventName
            project_root = os.path.dirname(os.path.abspath(__file__))
            filePath = project_root + '\\Events\\' + name + '_eventdata.json'
            with open(filePath, 'w') as outfile:
                json.dump(gameEvent.__dict__, outfile, indent=4, sort_keys=True, default=str)

    @staticmethod
    def LoadFromFile():
        project_root = os.path.dirname(os.path.abspath(__file__))
        os.chdir(project_root + "/Events")
        for file in glob.glob("*.json"):
            with open(file, 'r') as json_file:
                gameEvent = GameEvent(json_file.read())
                GameEventManager.AddEvent(gameEvent)

