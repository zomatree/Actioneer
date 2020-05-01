class CommandError(Exception):
    """Any error inside an error"""


class CommandParsingError(CommandError):
    """Any error inside the parsing of commands"""


class NoClosingQuote(CommandError):
    """Missing end quote"""


class NoCommandFound(CommandError):
    """No command found with that name"""
    def __init__(self, command, *args, **kwargs):
        self.command = command
        super().__init__(*args, **kwargs)
