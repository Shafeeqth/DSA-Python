#Graph trail

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print('Vertex already exist in the graph')

    def add_edges(self, v1, v2):
        if v1 not in self.graph:
            print(v1, "not exist in graph")
        elif v2 not in self.graph:
            print(v2, "not in graph")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def delte_vertex(self, vertex):
        if vertex not in self.graph:
            print('Vertex not found in the Graph')
            return
        for ver in self.graph:
            if vertex in self.graph[ver]:
                self.graph[ver].remove(vertex)
            del self.graph[vertex]

    def delete_edge(self, v1, v2):
        if v1 not in self.graph:
            print(v1, "not in graph")
        elif v2 not in self.graph:
            print(v2, " not in graph")
        self.graph[v1].remove(v2)
        self.graph[v2].remove(v1)

    def DFS(self, node, visited = set()):
        if node not in self.graph:
            print('Node is not found')
            return
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for x in self.graph[node]:
                self.DFS(x, visited)

    def BFS(self, node):
        visited = set()
        queue = [node]

        while queue:
            val = queue.pop(0)

            print(val, end=" ")

            for x in self.graph[val]:
                if x not in visited:
                    queue.append(x)
                    visited.add(x)



    def __str__(self):
        return str(self.graph)


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex("D")
graph.add_edges("C", "D")
# graph.add_edges("", "D")
graph.add_edges("A", "C")
graph.add_edges("B", "D")
graph.add_edges("A", "B")
print(graph)



# graph.DFS("A")
graph.BFS("A")

