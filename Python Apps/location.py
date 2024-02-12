from utility import typename
import inspect
from position import EarthPosition

def auto_repr(cls):
    print(f"Decorating {cls.__name__} with auto_repr")
    members = vars(cls)
    for name, member in members.items():
        print(name, member)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")

    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig = inspect.signature(cls.__init__)
    parameters_names = list(sig.parameters)[1:]

    if not all(
        isinstance(members.get(name, None), property)
        for name in parameters_names
    ):
        raise TypeError(f"Cannot apply auto_repr to {cls.__name__} because not all "
                        "__init__ parameters have matching properties")
    
    def synthesized_repr(self):
        return "{typename(self)}({args})".format(
            typename=typename(self),
            args=", ".join("{name}={value!r}".format(
                name=name,
                value=gatattr(self, name)
            ) for name in parameters_names)
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls

@auto_repr
class Location:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __str__(self):
        return self.name

hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.15))