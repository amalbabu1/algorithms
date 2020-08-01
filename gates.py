class gates:
    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.fn()
        return self.output


class binary(gates):
    def __init__(self, label):
        super().__init__(label)

    def getPinA(self):
        return int(input("pinA"))

    def getpinB(self):
        return int(input("pinB"))


class andGate(binary):
    def __init__(self, label):
        super().__init__(label)

    def fn(self):
        A = self.getPinA()
        B = self.getpinB()
        return A and B


a = andGate("g1")
print(a.getLabel())
print(a.getOutput())
