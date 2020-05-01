import typing
from discord.ext.handler import command
import discord
import re


quote_re: re.Pattern
chunk: re.Pattern
MemberUser: typing.Union


class BotBase(discord.Client):
    logging_level: str
    _all_commands: typing.Dict[str, command.Command]
    _commands: typing.Dict[str, command.Command]

    def __init_subclass__(cls, **kwargs: typing.Dict[str, typing.Any]) -> None: ...

    def __init__(self, prefix, contexts: typing.Tuple[typing.Any] = ()) -> None: ...

    @property
    def commands(self) -> typing.Dict[str, command.Command]: ...

    async def on_message(self, message: discord.Message) -> None: ... 

    async def run_commands(self, message: discord.Message) -> None: ...

    def split_args(self, s: str) -> typing.List[str]: ...
