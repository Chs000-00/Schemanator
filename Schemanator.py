class KeydValue():
    def __init__(self, key, value):
        self.key: string = key
        super().__init__(key, value)



class Sint(KeydValue):
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
        
class Sstring(KeydValue):
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
