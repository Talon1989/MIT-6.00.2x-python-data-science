class Node:
    counter = 0
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name
        Node.counter += 1
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def __str__(self):
        return self.name

    def count(self):
        return self.counter