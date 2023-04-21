class DirectedGraph:  # sem arestas paralelas e pode ter laços
    n_vertices = 0
    matrix = 0

    # construtor
    def __init__(self, n):
        self.n_vertices = n
        self.matrix = [[0 for i in range(n)] for j in range(n)]

    # imprimir
    def __str__(self):
        graph = ''
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                graph += f'{str(self.matrix[i][j])} '
            graph += '\n'
        return graph

    # inserir
    def new_edges(self, vi, vj, peso=1):
        if not self.exist_edge(vi, vj):
            self.matrix[vi][vj] = peso
        else:
            print(f'Directed graphs do not accept multiple edges')

    # remover
    def remove_edge(self, vi, vj):
        try:
            self.matrix[vi][vj] = 0
        except IndexError:
            print(f'There is no edge between vertices {vi} and {vj}')

    # existe
    def exist_edge(self, vi, vj):
        try:
            return self.matrix[vi][vj] > 0
        except IndexError:
            return False

    # grauVertice
    def get_vertex_degree(self, vertice):
        grau = 0
        for v in range(self.n_vertices):
            grau += self.matrix[v][vertice]
        return grau

    # grauGrafo
    def get_graph_degree(self):
        grau = 0
        for v in range(self.n_vertices):
            grau += self.get_vertex_degree(v)
        return grau

    # temLoop
    def has_loop(self):
        for i in range(self.n_vertices):
            if self.matrix[i][i] != 0:  # a diagonal principal representa os laços do grafo
                return True
        return False

    # Arestas paralelas
    def has_parallel_edges(self):
        for i in range(self.n_vertices):
            for j in range(i + 1, self.n_vertices):
                if self.matrix[i][j] > 1:
                    return True
        return False

    # é regular
    def is_regular(self):
        first_degree = self.get_vertex_degree(0)
        for i in range(1, self.n_vertices):
            if self.get_vertex_degree(i) != first_degree:
                return False
        return True

    # vertices adjacentes
    def adjacent(self, vertice):
        adj = []
        for i in range(self.n_vertices):
            if self.matrix[vertice][i] > 0:
                adj.append(i)
        return adj

    # é conexo
    def is_related(self):
        visited = [False] * self.n_vertices
        self.dfs(0, visited)
        for i in range(self.n_vertices):
            if not visited[i]:
                return False
        return True

    def dfs(self, vertex, visited):
        visited[vertex] = True
        adj = self.adjacent(vertex)
        for v in adj:
            if not visited[v]:
                self.dfs(v, visited)

    # é completo
    def is_complete(self):
        for i in range(self.n_vertices):
            for j in range(i + 1, self.n_vertices):
                if self.matrix[i][j] == 0:
                    return False
        return True

    def is_subgraph(self, grafo):
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                if self.matrix[i][j] > 0 and not grafo.exist_edge(i, j):
                    return False
        return True

    def bipartite(self):
        n = self.n_vertices
        color = [None] * n
        color[0] = 0
        print(color)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.matrix[i][j] >= 1:  # tem aresta entre vi e vj
                    print(color)
                    if color[i] == color[j]:
                        return False
                    elif color[j] is None:
                        color[j] = (color[i] + 1) % 2
        return True

    def is_isomorphic(self, graph):
        pass


g = DirectedGraph(7)
g.new_edges(0, 1, 5)
g.new_edges(0, 1, 9)
g.new_edges(1, 2, 8)
g.new_edges(2, 3, 7)
g.new_edges(3, 4, 6)
g.new_edges(4, 5, 5)
g.new_edges(0, 4, 4)
g.new_edges(1, 3, 3)
g.new_edges(1, 6, 3)
g.remove_edge(1, 6)
g.remove_edge(1, 7)

print(g)
print(g.bipartite())
print(g.exist_edge(4, 7))
print(g.adjacent(4))
print(g.is_related())

g = DirectedGraph(4)
g.new_edges(0, 1)
g.new_edges(0, 3)
g.new_edges(1, 2)
g.new_edges(2, 3)

print(g.bipartite())  # True

g.new_edges(0, 2)

print(g.bipartite())  # False
