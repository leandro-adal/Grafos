class DirectedMultigraph:
    n_vertices = 0
    matriz = 0
    pesos = []

    # construtor
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.matriz = [[0 for i in range(n_vertices)] for j in range(n_vertices)]
        self.pesos = [[[] for i in range(n_vertices)] for j in range(n_vertices)]

    # imprimir
    def __str__(self):
        graph = ''
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                graph += f'{str(self.matriz[i][j])} '
            graph += '\n'
        return graph

    def print_pesos(self):
        graph = ''
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                graph += f'{str(self.pesos[i][j])} '
            graph += '\n'
        return graph

    # inserir
    def new_edges(self, vi, vj, peso=1):
        self.matriz[vi][vj] += 1
        self.pesos[vi][vj].append(peso)

    # remover
    def remove_edge(self, vi, vj, peso=1):
        try:
            # verifica se o peso esta na lista pesos na posição dos vertices
            if peso in self.pesos[vi][vj]:
                self.matriz[vi][vj] -= 1
                self.pesos[vi][vj].remove(peso)
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
        visitados = [False] * self.n_vertices
        self.dfs(0, visitados)
        for i in range(self.n_vertices):
            if not visitados[i]:
                return False
        return True

    def dfs(self, vertice, visitados):
        visitados[vertice] = True
        adj = self.adjacent(vertice)
        for v in adj:
            if not visitados[v]:
                self.dfs(v, visitados)

    def is_complete(self):
        for i in range(self.n_vertices):
            for j in range(i + 1, self.n_vertices):
                if self.matriz[i][j] == 0:
                    return False
        return True

    def is_subgraph(self, grafo):
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                if self.matriz[i][j] > 0 and not grafo.exist_edge(i, j):
                    return False
        return True

    def e_directed_multigraph(self):  # quando as arestas são dirigidas e tem arestas paralelas
        return self.has_parallel_edges()

    def bipartite(self):
        n = self.n_vertices
        cor = [None] * n
        cor[0] = 0
        print(cor)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.matriz[i][j] == 1:  # te aresta entre vi e vj
                    print(cor)
                    if cor[i] == cor[j]:
                        return False
                    elif cor[j] is None:
                        cor[j] = (cor[i] + 1) % 2
        return True

    def eh_isomorfo(self, grafo):
        pass
