from inspect import iscoroutinefunction


class Command:
    def __init__(self, func, **kwargs):
        self.func = func
        self.attrs = kwargs
        self.aliases = []

    def set_attrs(self):
        for k, v in self.attrs.items():
            setattr(self, k, v)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def command(func = None, **kwargs):
    def predicate(_func):
        return Command(_func, **kwargs)
    return predicate(func) if iscoroutinefunction(func) else predicate

