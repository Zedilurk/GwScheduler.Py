import CommandArgument
import GameEventManager
import GameEvent

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

            arg = CommandArgument.CommandArgument(name, value)
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
        for event in GameEventManager.GameEventManager.ScheduledEvents:
            if (event.EventName.lower() == arguments[0].Value.lower()):
                match = event
        
        if (match != None):
            match.AddUser(user)

        return "";

    def command_leave (self, arguments, user):
        return "";

    def command_roster (self, arguments, user):
        return "";

    def command_reset (self, arguments, user):
        return "";

    def command_register (self, arguments, user):  
        match = None
        for event in GameEventManager.GameEventManager.ScheduledEvents:
            if (event.EventName.lower() == arguments[0].Value.lower()):
                match = event

        if (match == None):
            newEvent = GameEvent.GameEvent(arguments[0].Value)
            GameEventManager.GameEventManager.AddEvent(newEvent)
            
        return "";

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

        

