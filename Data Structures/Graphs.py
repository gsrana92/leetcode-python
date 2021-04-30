from _collections import OrderedDict
from enum import Enum


class State(Enum):
    def __init__(self):
        unvisited = 1
        visited = 2
        visiting = 3


class Vertex:
    def __init__(self, vertex):
        self.key = vertex
        self.neighbors = list()

    def add_neighbors(self, nbr, cost=0):
        self.neighbors.append({nbr: cost})

    def __str__(self):
        #for i in self.neighbors:
          #  print(self.key + " has a neighbor  " + str(*i.keys()) + ' with weight ' + str(*i.values()))
        return str(self.key + " has neighbors " + str(self.neighbors))


class Graph:
    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, node):
        vertex = Vertex(node)
        self.nodes[node] = vertex
        return vertex

    def add_edge(self, u, v, weight=0):
        if u not in self.nodes:
            self.add_node(u)
        if v not in self.nodes:
            self.add_node(v)

        self.nodes[u].neighbors.append({v: weight})

    def dfs(self, start):
        visited = set()
        stack = [start]

        while stack:


    def print_graph(self):

        for i in self.nodes:
            print(str(self.nodes[i]))
        print('list of nodes ' + str(list(self.nodes)))
       # print(self.nodes)


#a = Vertex("X")
#a.add_neighbors("Y")
#a.add_neighbors("Z", 3)
#print(a)
#print('\n')

g = Graph()
#g.add_edge("A", "B", 1)
#g.add_edge("A", "C")
#g.add_edge("B", "D", 2)
#g.add_edge("B", "F", 3)
#g.add_edge("D", "G", 4)
#g.add_edge("F", "H", 4)
#g.add_edge("C", "E", 2)

for edges in ['AB', 'AC', 'BD', 'BF', 'DG', 'FH', 'CE']:
    g.add_edge(edges[:1], edges[1:])

g.print_graph()
#print(dfs())
# g.print_graph()
