class Grafo:
    n_vertices = 0
    matriz = 0
    pesos = []

    # construtor
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.matriz = [[0 for i in range(n_vertices)] for j in range(n_vertices)]

    # imprimir
    def __str__(self):
        grafo = ''
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                grafo += str(self.matriz[i][j]) + ' '
            grafo += '\n'
        return grafo

    # Não pode laço ou arestas paralelas em grafos simples
    def criar_aresta(self, vi, vj, peso=1):
        if vi != vj:
            self.matriz[vi][vj] = peso
            self.matriz[vj][vi] = peso
        else:
            print('Loops are not allowed in simple graphs')

    def remover_aresta(self, vi, vj):
        self.matriz[vi][vj] = 0
        self.matriz[vj][vi] = 0

    def existe_aresta(self, vi, vj):
        try:
            return self.matriz[vi][vj] > 0
        except IndexError:
            return False

    # Quantidade de aresta que incidem no vertice
    def get_grau_vertice(self, vertice):
        grau = 0
        for v in range(self.n_vertices):
            if self.matriz[v][vertice] > 1:
                grau += 1
        return grau

    # Soma dos graus dos vertices
    def get_grau_grafo(self):
        grau = 0
        for v in range(self.n_vertices):
            grau += self.get_grau_vertice(v)
        return grau

    # Quando todos os vértices têm o mesmo grau
    def eh_regular(self):
        primeiro_grau = self.get_grau_vertice(0)
        for i in range(1, self.n_vertices):
            if self.get_grau_vertice(i) != primeiro_grau:
                return False
        return True

    # Verifica quais são os vertices adjacentes de um vertice
    def adjacentes(self, vertice):
        adj = []
        for i in range(self.n_vertices):
            if self.matriz[vertice][i] > 0:
                adj.append(i)
        return adj

    # Quando a partir de um vertice não possível chegar em algum outro vertice
    def eh_conexo(self):
        visitados = [False] * self.n_vertices
        self.dfs(0, visitados)
        for i in range(self.n_vertices):
            if not visitados[i]:
                # Ou seja, há algum vertice que não pode ser alcançado a partir do vertice 0
                return False
        return True

    # Algoritmo Depth-First Search - busca em profundidade
    def dfs(self, vertice, visitados):
        visitados[vertice] = True
        adj = self.adjacentes(vertice)  # retorna uma lista dos vertices adjacentes
        for v in adj:
            if not visitados[v]:
                self.dfs(v, visitados)  # O torna visitado

    # Um grafo simples com n_vertices vertices em que to-do vertice é adjacente a todos os outros vertices
    def eh_completo(self):
        for i in range(self.n_vertices):
            for j in range(i + 1, self.n_vertices):
                if self.matriz[i][j] == 0:
                    return False
        return True

    # Se o grafo recebido tiver os mesmos vertices, arestas e nos terminais ele é um subgrafo
    def eh_subgrafo(self, grafo):
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                if self.matriz[i][j] > 0 and not grafo.existe_aresta(i, j):
                    return False
        return True

    # Se é possível dividir os vertices em dois conjuntos e cada aresta incidir em ambos conjuntos
    def bipartido(self):
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
                    elif cor[j] == None:
                        cor[j] = (cor[i] + 1) % 2
        return True

    def eh_isomorfo(self, grafo):
        pass


g = Grafo(7)
g.criar_aresta(0, 1, 5)
g.criar_aresta(0, 1, 9)
g.criar_aresta(1, 2, 8)
g.criar_aresta(2, 3, 7)
g.criar_aresta(3, 4, 6)
g.criar_aresta(4, 5, 5)
g.criar_aresta(0, 4, 4)
g.criar_aresta(1, 3, 3)

print(g)
print(g.bipartido())
print(g.existe_aresta(4, 7))
print(g.adjacentes(4))
print(g.eh_conexo())
