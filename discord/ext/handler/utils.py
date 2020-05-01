import inspect
from discord.utils import find

def get_contexts(func, contexts):
    r = {}
    kwargs = {v.annotation: k for k, v in inspect.signature(func).parameters.items() if v.kind is inspect.Parameter.KEYWORD_ONLY}
    for annot, kwarg in kwargs.items():
        value = find(lambda context: isinstance(context, annot), contexts)
        r[kwarg] = value
    print(r)
    return r


async def run_with_contexts(func, args, kwargs):
    kwargs = get_contexts(func, kwargs)
    return await func(*args, **kwargs)



def test(*, bruh: int):
    print(bruh)


test(**get_contexts(test, ["bruh"]))