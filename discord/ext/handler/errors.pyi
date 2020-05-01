class CommandError(Exception): ...


class CommandParsingError(CommandError): ...


class NoClosingQuote(CommandError): ...


class NoCommandFound(CommandError):
    command: str
