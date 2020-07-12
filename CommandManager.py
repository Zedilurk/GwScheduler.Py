from CommandArgument import CommandArgument
from GameEventManager import GameEventManager
from GameEvent import GameEvent
from Serializer import Serializer

class CommandManager(object):
    """description of class"""

    def Parse (self, text):
        # initial command string
        #       ex/ $registerevent args => registerevent
        command = text.split(' ')[0]

        # remaining commands split on commas
        #       ex/ $registerevent Scrims, 3pm, OG Hall => [Scrims, 3pm, OG Hall]
        remainingCommandBody = text[len(command):]
        commandArguments = remainingCommandBody.split(',')
        arguments = []

        for section in commandArguments:
            pieces = section.split(':')
            
            name = ""
            value = ""

            if (len(pieces) > 1):
                name = pieces[0]

                for x in range(1, len(pieces)):
                    value += pieces[x]
            else:
                value = section

            arg = CommandArgument(name, value.strip())
            arguments.append(arg)

        return command, arguments;

    # notes to self
    #    does Python support reflection?
    #    does Python support Regex?
    #    Use regex to match before ':' use reflection to find that property
    #    Use regex to match after ':' and set the value of the property
    #    If no property name, try to fill in value of next null property?

    # command arguments
    #for section in commandSections:

    #    sectionName = ""
    #    sectionValue = ""

    #    if (section.contains(':')):
    #        sectionPieces = section.split(':')

    #        if (len(sectionPieces) == 2):
    #            sectionName = sectionPieces[0]
    #            sectionValue = sectionPieces[1]
    #    else:
    #        sectionValue = section


    def React (self, command, user, arguments):
        """Dispatch method"""
        method_name = 'command_' + str(command)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid command")
        # Call the method as we return it
        return method(arguments, user)

    def command_join (self, arguments, user):
        match = None
        commandResponse = "";
        for event in GameEventManager.ScheduledEvents:
            if (event.EventName.lower() == arguments[0].Value.lower()):
                match = event
        
        if (match != None):
            if (user in match.Users) == False:
                match.AddUser(user)
                commandResponse = "You've signed up for the " + event.EventName + " event! Have fun!"
                print("Adding " + user + " to " + event.EventName + " roster.")
                Serializer.SaveToFile();
            else:
                commandResponse = "Good news! You're already signed up for the " + event.EventName + " event!"
                print("User named " + user + " already exists in " + event.EventName + " roster.")
        else:
            commandResponse = "That's odd...No event by the name of " + event.EventName + " could be found. Perhaps it could be under a different name?"
            print("An event by the name of " + event.EventName + " could not be found.")

        return commandResponse;

    def command_leave (self, arguments, user):
        match = None
        commandResponse = "";
        for event in GameEventManager.ScheduledEvents:
            if (event.EventName.lower() == arguments[0].Value.lower()):
                match = event
        
        if (match != None):
            if user in match.Users:
                match.RemoveUser(user)
                commandResponse = "You have left the " + event.EventName + " roster!"
                print("Removing " + user + " from " + event.EventName + " roster.")
                Serializer.SaveToFile();
            else:
                commandResponse = "You don't appear to be currently signed up for the " + event.EventName + " event."
                print("User named " + user + " is not currently present in " + event.EventName + " roster.")
        else:
            commandResponse = "That's odd...No event by the name of " + event.EventName + " could be found. Perhaps it could be under a different name?"
            print("An event by the name of " + event.EventName + " could not be found.")

        return commandResponse;

    def command_roster (self, arguments, user):
        match = None
        commandResponse = "";

        for event in GameEventManager.ScheduledEvents:
            if (event.EventName.lower() == arguments[0].Value.lower()):
                match = event
        
        if (match != None):
            user_str_list = "```\r"
            for user in match.Users:
                user_str_list += user

                if (user != match.Users[len(match.Users) - 1]):
                    user_str_list += "\r\n"

            user_str_list += "```";
            commandResponse = user_str_list
            print("User " + user + " has requested a roster print out for the " + event.EventName + " event")
        else:
            commandResponse = "That's odd...No event by the name of " + event.EventName + " could be found. Perhaps it could be under a different name?"
            print("An event by the name of " + event.EventName + " could not be found.")

        return commandResponse;

    def command_reset (self, arguments, user):
        return "";

    def command_register (self, arguments, user):  
        match = None
        commandResponse = "";
        for event in GameEventManager.ScheduledEvents:
            if (event.EventName.lower() == arguments[0].Value.lower()):
                match = event

        if (match == None):
            newEvent = GameEvent()
            newEvent.EventName = arguments[0].Value
            GameEventManager.AddEvent(newEvent)
            print("Creating new event: " + newEvent.EventName)
            Serializer.SaveToFile();
        else:
            commandResponse = "An event by the name of " + event.EventName + " already exists. Try joining that event using $join or choose a different name for your event."
            print("An event by the name of " + event.EventName + " already exists.")

        return commandResponse;

    def command_cancel (self, arguments, user):
        return "";

    def command_change (self, arguments, user):
        return "";

    def command_schedule (self, arguments, user):
        return "";

    def command_feedback (self, arguments, user):
        return "";

    def command_debugthrow (self, arguments, user):
        return "";

    def command_help (self, arguments, user):
        return "";

        

