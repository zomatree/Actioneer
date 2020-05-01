import typing


def get_contexts(func: typing.Callable,
                 contexts: typing.List[Any]) -> typing.Dict[str, typing.Any]: ...


async def run_with_contexts(func: typing.Callable, args: typing.List[typing.Any],
                             kwargs: typing.Dict[str, typing.Any]) -> typing.Any: ...
