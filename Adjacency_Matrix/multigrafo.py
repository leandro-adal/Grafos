class Multigrafo:  # grafo não dirigido
    n_vertices = 0
    matriz_ponderada = 0

    # construtor
    def __init__(self, n):
        self.n_vertices = n
        self.matriz_ponderada = [[[0, []] for i in range(n)] for j in range(n)]

    # imprimir
    def __str__(self):
        graph = ''
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                graph += f'{str(self.matriz_ponderada[i][j][0])} '
            graph += '\n'
        return graph

    def print_pesos(self):
        graph = ''
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                graph += f'{str(self.matriz_ponderada[i][j][1])} '
            graph += '\n'
        return graph

    # inserir
    def criar_aresta(self, vi, vj, peso=1):
        if vi != vj:
            self.matriz_ponderada[vi][vj][0] += 1
            self.matriz_ponderada[vj][vi][0] += 1
            self.matriz_ponderada[vi][vj][1].append(peso)
            self.matriz_ponderada[vj][vi][1].append(peso)
        else:
            print('Loops are not allowed in simple graphs')

    # remover
    def remover_aresta(self, vi, vj, peso=1):
        try:
            pesos_aresta = self.matriz_ponderada[vj][vi][1]
            if self.existe_aresta(vi, vj) and peso in pesos_aresta:
                self.matriz_ponderada[vi][vj][0] -= 1
                self.matriz_ponderada[vj][vi][0] -= 1
                self.matriz_ponderada[vi][vj][1].remove(peso)
                self.matriz_ponderada[vj][vi][1].remove(peso)
            else:
                print(f'Não existe uma aresta entre {vi} e {vj} com o peso: {peso}')
        except IndexError:
            print(f'Não existe aresta entre os vertices {vi} e {vj}')

    # existe
    def existe_aresta(self, vi, vj):
        try:
            return self.matriz_ponderada[vi][vj][0] > 0
        except IndexError:
            return False

    # grauVertice
    def get_grau_vertice(self, vertice):
        grau = 0
        for v in range(self.n_vertices):
            grau += self.matriz_ponderada[v][vertice][0]
        return grau

    # grauGrafo
    def get_grau_grafo(self):
        grau = 0
        for v in range(self.n_vertices):
            grau += self.get_grau_vertice(v)
        return grau

    def eh_regular(self):
        primeiro_grau = self.get_grau_vertice(0)
        for i in range(1, self.n_vertices):
            if self.get_grau_vertice(i) != primeiro_grau:
                return False
        return True

    # Verifica quais são os vertices adjacentes de um vertice
    def adjacentes(self, vertice):
        adjacentes = []
        for i in range(self.n_vertices):
            if self.matriz_ponderada[vertice][i][0] > 0:
                adjacentes.append(i)
        return adjacentes

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
                if self.matriz_ponderada[i][j][0] == 0:
                    return False
        return True

    # Se o grafo recebido tiver os mesmos vertices, arestas e nos terminais ele é um subgrafo
    def eh_subgrafo(self, grafo):
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                if self.matriz_ponderada[i][j][0] > 0 and not grafo.existe_aresta(i, j):
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
                if self.existe_aresta(i, j):  # tem aresta entre vi e vj
                    print(cor)
                    if cor[i] == cor[j]:
                        return False
                    elif cor[j] is None:
                        cor[j] = (cor[i] + 1) % 2
        return True

    def eh_isomorfo(self, grafo):
        pass
