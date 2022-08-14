from _collections import OrderedDict


class Vertex:
    def __init__(self, node):
        self.key = node
        self.nbrs = []

    def add_nbr(self, vertex, cost=0):
        self.nbrs.append({vertex: cost})

    def __str__(self):
        return str(self.key + ' has neighbors: ' + str(self.nbrs))


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        vertex = Vertex(node)
        self.nodes[node] = vertex

    def add_edge(self, u, v, cost=0):
        if u not in self.nodes:
            self.add_node(u)
        if v not in self.nodes:
            self.add_node(v)
        self.nodes[u].nbrs.append({v: cost})

    def sizeOfGraph(self):
        count = 0
        for i in self.nodes:
            count += 1
        return count


G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def BFS(graph, start, size):
    marked = [False] * size
    queue = [start]
    visit = []
    while len(queue) > 0:
        v = queue.pop(0)
        if not marked[v]:
            visit.append(v)
            marked[v] = True
        for w in graph[v]:
            if not marked[w]:
                queue.append(w)

    return visit


print(BFS(G2, 'A', 6))


# def BFS(self, ):


g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
# g.add_edge('A', 'B')
# g.add_edge('A', 'B')


g.print_graph()
g.sizeOfGraph()
# print(len(g))
