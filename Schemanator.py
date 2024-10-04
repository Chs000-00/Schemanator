class KeyValue():
    def __init__(self, key, value):
        self.key: string = key
        super().__init__(key, value)

class KInt(KeyValue):
    def __init__(self, key, value):
        self.value: int = value

    def toJson(self, depth):
        pass

    def toJson5(self, depth):
        pass

    def toXml(self, depth):
        pass

    def toToml(self, depth):
        pass

    def toYaml(self, depth):
        pass

class KString(KeyValue):
    def __init__(self, value):
        self.value: string = value

    def toJson(self, depth):
        pass

    def toJson5(self, depth):
        pass

    def toXml(self, depth):
        pass

    def toToml(self, depth):
        pass

    def toYaml(self, depth):
        pass


class KList(KeyValue):
    def __init__(self, value):
        self.value: list = value

    def toJson(self, depth):
        out = "["
        for o in self.value:
            out.append(o.toJson(depth+1))

        out.append("]")
        return out
            

    def toJson5(self, depth):
        pass

    def toXml(self, depth):
        pass

    def toToml(self, depth):
        pass

    def toYaml(self, depth):
        pass

# TODO: Allow extending KDict to require values
class KDict(KeyValue):
    def __init__(self, value):
        self.value: dict = value

    def toJson(self, depth):
        pass

    def toJson5(self, depth):
        pass

    def toXml(self, depth):
        pass

    def toToml(self, depth):
        pass

    def toYaml(self, depth):
        pass