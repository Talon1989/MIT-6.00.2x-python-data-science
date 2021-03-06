from Edge import Edge
from Node import Node
from lect3 import Graph

nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))
g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
g.addEdge(Edge(g.getNode('BCA'), g.getNode('CBA')))
g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))
g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))


# ---------------------------------------------------------


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() \
               + ' (' + str(self.weight) + ')'