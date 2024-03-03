class MixinLog:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        list_repr = []

        for item in self.__dict__.values():
            value = f"'{item}'"
            list_repr.append(value)
        return f"{self.__class__.__name__}({', '.join(list_repr)})"
