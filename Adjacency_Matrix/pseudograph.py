class PseudoGraph:  # grafo não dirigido
    n_vertices = 0
    matriz = 0
    weights = []

    # construtor
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.matriz = [[0 for i in range(n_vertices)] for j in range(n_vertices)]
        self.weights = [[[] for i in range(n_vertices)] for j in range(n_vertices)]

    def __str__(self):
        graph = ''
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                graph += f'{str(self.matriz[i][j])} '
            graph += '\n'
        return graph

    def print_weights(self):
        graph = ''
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                graph += f'{str(self.weights[i][j])} '
            graph += '\n'
        return graph

    # inserir
    def new_edges(self, vi, vj, weight=1):
        self.matriz[vi][vj] += 1
        self.matriz[vj][vi] += 1
        self.weights[vi][vj].append(weight)
        self.weights[vj][vi].append(weight)

    # remover
    def remove_edge(self, vi, vj, weight=1):
        try:
            # verifica se o peso esta na lista weights na posição dos vertices
            if weight in self.weights[vi][vj]:
                self.matriz[vi][vj] -= 1
                self.matriz[vj][vi] -= 1
                self.weights[vi][vj].remove(weight)
                self.weights[vj][vi].remove(weight)
            else:
                print(f'There is no edge between vertices {vi} and {vj} with specified weight')
        except IndexError:
            print(f'There is no edge between vertices {vi} and {vj}')

    # existe
    def exist_edge(self, vi, vj):
        try:
            return self.matriz[vi][vj] > 0
        except IndexError:
            return False

    # grauVertice
    def get_vertex_degree(self, vertex):
        degree = 0
        for v in range(self.n_vertices):
            degree += self.matriz[v][vertex]
        return degree

    # grauGrafo
    def get_graph_degree(self):
        degree = 0
        for v in range(self.n_vertices):
            degree += self.get_vertex_degree(v)
        return degree

    # temLoop
    def has_loop(self):
        for i in range(self.n_vertices):
            if self.matriz[i][i] != 0:  # a diagonal principal representa os laços do grafo
                return True
        return False

    def has_parallel_edges(self):
        for i in range(self.n_vertices):
            for j in range(i + 1, self.n_vertices):
                if self.matriz[i][j] > 1:
                    return True
        return False

    # é regular
    def is_regular(self):
        first_degree = self.get_vertex_degree(0)
        for i in range(1, self.n_vertices):
            if self.get_vertex_degree(i) != first_degree:
                return False
        return True

    def adjacent(self, vertex):
        adj = []
        for i in range(self.n_vertices):
            if self.matriz[vertex][i] > 0:
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

    def is_complete(self):
        for i in range(self.n_vertices):
            for j in range(i + 1, self.n_vertices):
                if self.matriz[i][j] == 0:
                    return False
        return True

    def is_subgraph(self, graph):
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                if self.matriz[i][j] > 0 and not graph.exist_edge(i, j):
                    return False
        return True

    def pseudo_graph(self):  # quando tem arestas paralelas ou loop
        return self.has_parallel_edges() or self.has_loop()

    def bipartite(self):
        n = self.n_vertices
        color = [None] * n
        color[0] = 0
        print(color)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.matriz[i][j] == 1:  # te aresta entre vi e vj
                    print(color)
                    if color[i] == color[j]:
                        return False
                    elif color[j] is None:
                        color[j] = (color[i] + 1) % 2
        return True

    def is_isomorfo(self, graph):
        pass
