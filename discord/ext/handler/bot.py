import typing
from discord.ext.handler import command, errors, utils
import discord
import re


quote_re = re.compile(r"[\"']")
chunk = re.compile(r"\S+")
MemberUser = typing.Union[discord.User, discord.Member]
Channel = typing.Union[discord.TextChannel, discord.DMChannel]


class BotBase(discord.Client):
    def __init_subclass__(cls, **kwargs):
        cls.logging_level = kwargs.get("logging")
        if cls.logging_level:
            import logging
            logging.basicConfig(level=getattr(logging, self.logging_level, logging.INFO))

        cls._commands = {}
        cls._all_commands = {}

        for name, method in vars(cls).items():
            if not isinstance(method, command.Command):
                continue

            for k, v in kwargs.items():
                setattr(method, k, v)
            method.set_attrs()
            cls._commands[name] = method
            for alias in method.aliases:
                cls._all_commands[alias] = method

    def __init__(self, prefix, contexts = ()):
        self.contexts = contexts
        self.prefix = prefix
        super().__init__()
    
    @property
    def commands(self):
        return self._commands

    async def on_message(self, message):
        await self.run_commands(message)

    async def run_commands(self, message):
        try:
            split = self.split_args(message.content)
            if not split[0].startswith(self.prefix):
                return self.dispatch("no_command", message)
    
            command = split.pop(0)[len(self.prefix):]
            invoked = self._all_commands.get(command, None)
            if not invoked:
                raise errors.NoCommandFound(command)

            args = await self.convert_args(split)
            contexts = [message.author, message.channel, message, message.guild, ]
            self.custom_dispatch("command")
            await utils.run_with_contexts(invoked.func, args, )

        except Exception as e:
            ...

    def split_args(self, s):
        """Will split the raw input into the arguments"""
        args = []
        i = 0
        while i < len(s):
            char = s[i]
            if re.match(quote_re, char):
                try:
                    j = s.index(char, i+1)
                    args.append(s[i + 1:j])
                    i = j
                except ValueError:
                    raise errors.NoClosingQuote("Missing closing quote.")
            else:
                match = chunk.match(s, i)
                if match:
                    args.append(match.group())
                    i = match.end()
            i += 1
        return args

    def custom_dispatch(self, event_name, contexts):
        event_name = f"on_{event_name}"
        try:
            coro = getattr(self, event_name)
        except:
            return

        self._schedule_event(utils.run_with_contexts, event_name, coro, contexts)
