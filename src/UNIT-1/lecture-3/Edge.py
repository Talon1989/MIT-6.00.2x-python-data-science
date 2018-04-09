from Node import Node


class Edge:
    def __init__(self, src, dest):
        assert isinstance(src, Node); assert isinstance(dest, Node);
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()