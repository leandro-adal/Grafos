class PseudoGraph:
    n_edges = 0
    m_vertices = 0
    matrix = 0
    weights = []

    def __init__(self, m_vertices, n_edges):
        self.n_edges = n_edges
        self.m_vertices = m_vertices
        self.matrix = [[0 for i in range(n_edges)] for j in range(m_vertices)]
        self.weights = [0 for i in range(n_edges)]

    def __str__(self):
        graph = ''
        for i in range(self.m_vertices):
            for j in range(self.n_edges):
                graph += f'{str(self.matrix[i][j])} '
            graph += '\n'
        return graph

    def new_edge(self, vi, vj, edge, weight=0):
        self.matrix[vi][edge] += 1
        self.matrix[vj][edge] += 1
        self.weights[edge] = weight

    def remove_edge(self, vi, vj, edge):
        self.matrix[vi][edge] -= 1
        self.matrix[vj][edge] -= 1
        self.weights[edge] = 0

    # verifica se existe aresta entre 2 vertices
    def exist_edge(self, vi, vj, edge):  # i
        return self.matrix[vi][edge] != 0 and self.matrix[vj][edge] != 0

    # verifica se existe aresta entre 2 vertices se existir a retorna
    def get_edge(self, vi, vj):
        for edge in range(self.n_edges):
            if self.exist_edge(vi, vj, edge):
                return edge
        return -1

    def get_vertex_degree(self, vertex):
        degree = 0
        for edge in range(self.n_edges):
            degree += self.matrix[vertex][edge]
        return degree

    def get_graph_degree(self):
        degree = 0
        for v in range(self.m_vertices):
            degree += self.get_vertex_degree(v)
        return degree

    def has_loop(self):  # Se algum vertice tiver valor maior que 1
        for vertex in range(self.m_vertices):
            for edge in range(self.n_edges):
                if self.matrix[vertex][edge] > 1:
                    return True
        return False

    def has_parallel_edges(self):  # Se os mesmo vertice forem conectados mais de uma vez
        for vi in range(self.m_vertices):
            for vj in range(vi + 1, self.m_vertices):
                edges_connecting = 0
                # Percorre as arestas, pois caso hajam paralelas elas estarão na mesma posição 'vi' e 'vj'
                for edge in range(self.n_edges):
                    # Se o vertice anterior e o atual forem maiores que 0 eles estão conectados
                    if self.matrix[vi][edge] > 0 and self.matrix[vj][edge] > 0:
                        edges_connecting += 1
                # se as arestas conectadas for maior que 1 existe arestas paralelas
                if edges_connecting > 1:
                    return True
        return False

    def modify_edge_weight(self, edge, new_weight):
        self.weights[edge] = new_weight

    def get_weight_edge(self, edge):
        return self.weights[edge]

    # Lista todos os vertices que a aresta passa
    def connected_by_edges(self, edge):
        vertices = []
        for i in range(self.m_vertices):
            for j in range(self.n_edges):
                # uma aresta so conecta 2 vertices então não precisa percorrer a lista inteira
                if len(vertices) > 2:
                    break
                elif self.matrix[i][j] != 0 and j == edge:
                    vertices.append(i)
        return vertices

    def is_bipartite(self):
        if self.is_connected():
            n_vertices = self.m_vertices
            colors = [-1] * n_vertices  # Inicializa todas as colors como -1
            row = []  # fila
            for i in range(n_vertices):
                if colors[i] == -1:
                    colors[i] = 0
                    row.append(i)
                    while row:
                        v = row.pop(0)
                        for adj in self.get_adjacent(v):
                            if colors[adj] == -1:
                                colors[adj] = 1 - colors[v]  # Atribui uma cor oposta à do vértice atual
                                row.append(adj)
                            elif colors[adj] == colors[v]:
                                return False
            return True

        else:
            return False

    def is_connected(self):
        n = self.m_vertices
        visited = [False] * n
        self.deep_search(0, visited)
        for i in range(n):
            if not visited[i]:
                return False
        return True

    def deep_search(self, vertex, visited):
        visited[vertex] = True
        for vi in range(self.m_vertices):
            if self.matrix[vertex][vi] != 0 and not visited[vi]:
                self.deep_search(vi, visited)

    def is_complete(self):  # to-do vertice é adjacente
        for vi in range(self.m_vertices):
            for vj in range(self.m_vertices):
                if vi != vj and not self.exist_edge(vi, vj, self.get_edge(vi, vj)):
                    return False
        return True

    def get_adjacent(self, vertex):
        adjacent = []
        for edge in range(self.n_edges):
            if self.matrix[vertex][edge] != 0:
                for vi in range(self.m_vertices):
                    if vi != vertex and self.matrix[vi][edge] != 0:
                        adjacent.append(vi)
        return adjacent

    def is_subgraph(self, graph):
        # Verifica se os vértices do grafo menor também existem no grafo maior
        for i in range(graph.m_vertices):
            if i not in range(self.m_vertices):
                return False

        # Verifica se as arestas do grafo menor também existem no grafo maior
        for i in range(graph.m_vertices):
            for j in graph.get_adjacent(i):
                if not self.exist_edge(i, j, graph.get_edge(i, j)):
                    return False

        return True

    def is_simple(self):  # i
        if self.has_loop() or self.has_parallel_edges():
            return False
        else:
            return True

    def is_pseudograph(self):
        return self.has_loop() or self.has_parallel_edges()

    # se é um grafo com pesos nas arestas
    def is_weighted(self):
        for i in range(len(self.weights)):
            if self.weights[i] != 0:
                return True
        return False

    # grafo regular - Se todos os vertices tem o mesmo grau
    def is_regular(self):
        degree = self.get_vertex_degree(0)
        for v in range(1, self.m_vertices):
            if self.get_vertex_degree(v) != degree:
                return False
        return True
