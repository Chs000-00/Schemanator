# NOTE: requires typing module for older python versions

class KeyValue():
    def __init__(self, key, value) -> None:
        self.key = key
        self.value: type[LowestType] = value

    def toJson(self, depth) -> str:
        return "\"{}\": {}".format()

# TODO: Rename this stuff
class LowestType():
    def __init__(self, value) -> None:
        pass

class LKInt(LowestType):
    def __init__(self, value) -> None:
        super().__init__(value)