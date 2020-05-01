import typing


class Command:
    func: typing.Callable
    attrs: typing.Dict[str, typing.Any]
    aliases = typing.List[str]
    
    def __init__(self, func: typing.Callable, **
                 kwargs: typing.Dict[str, typing.Any]) -> None: ...

    def set_attrs(self) -> None: ...

    def __call__(self, *args: typing.Tuple[str], **
                 kwargs: typing.Dict[str, typing.Any]) -> typing.Any: ...


def command(func: typing.Optional[typing.Callable] = None, **kwargs: typing.Dict[str, typing.Any]) -> Command: ...
