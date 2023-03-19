class Grafo:

  n_arestas = 0 
  m_vertices = 0
  matriz = 0

  def __init__(self,m_vertices,n_arestas):
      self.n_arestas = n_arestas
      self.m_vertices = m_vertices
      self.matriz = [ [ 0 for i in range(n_arestas) ] for j in range(m_vertices) ]

  def __str__(self):
    graph = ''
    for i in range(self.m_vertices):
      for j in range(self.n_arestas):
        graph += str(self.matriz[i][j])+' '
      graph +='\n'
    return graph

  def criar_aresta(self,vi,vj,aresta):
    self.matriz[vi][aresta] +=1
    self.matriz[vj][aresta] +=1

  def remover_aresta(self,vi,vj,aresta):
    self.matriz[vi][aresta] -=1
    self.matriz[vj][aresta] -=1

  def existe_aresta(self,vi,vj,aresta): #
    return self.matriz[vi][aresta] != 0 and self.matriz[vj][aresta] != 0

  def getAresta(self,vi,vj): #verifica se existe aresta entre 2 vertices e se houver a retorna
    for aresta in range(self.n_arestas):
      if self.existe_aresta(vi,vj,aresta):
        return aresta
    return -1

  def getGrauVertice(self,vertice): 
    grau = 0
    for aresta in range(self.n_arestas):
      grau += self.matriz[vertice][aresta]
    return grau

  def getGrauGrafo(self):
    grau = 0
    for v in range(self.m_vertices):
      grau += self.getGrauVertice(v)
    return grau

  def temLoop(self):# Se algum vertice tiver valor maior que 2
    for v in range(self.m_vertices):
      for aresta in range(self.n_arestas):
        if self.matriz[v][aresta] > 1:
          return True
    return False

  def temArestasParalelas(self):# Se os mesmo vertice forem conectados mais de uma vez
    for i in range(self.m_vertices):
        for j in range(i+1, self.m_vertices): 
            qt_arestas_conectando = 0
            for aresta in range(self.n_arestas):
                if self.matriz[i][aresta] > 0 and self.matriz[j][aresta] > 0: #Se o vertice anterior e o atual forem maiores que 1 eles são conectados
                    qt_arestas_conectando += 1
            if qt_arestas_conectando > 1: # se for maior tem arestas paralelas
                return True
    return False

  def vertices_conectados(self, aresta): # Lista todos os vertices em que a aresta incide
    vertices = []
    for i in range(self.m_vertices):
        for j in range(self.n_arestas):
            if self.matriz[i][j] != 0 and j == aresta:
                vertices.append(i)
    return vertices

  def e_completo(self): # todo vertice é adjacente
    for i in range(self.m_vertices):
        for j in range(self.m_vertices):
            if i != j and not self.existe_aresta(i, j, self.getAresta(i, j)):
                return False
    return True

  def getAdjacentes(self, v):
    adjacentes = []
    for aresta in range(self.n_arestas):
        if self.matriz[v][aresta] != 0:
            for i in range(self.m_vertices):
                if i != v and self.matriz[i][aresta] != 0:
                    adjacentes.append(i)
    return adjacentes

  # grafo regular   - Se todos os vertices tem o mesmo grau
  def eh_regular(self):
    grau = self.getGrauVertice(0)
    for v in range(1, self.m_vertices):
        if self.getGrauVertice(v) != grau:
            return False
    return True
  
  def e_simples(self):#i
    if self.temLoop() or self.temArestasParalelas():
      return False
    else:
      return True

  def e_pseudografo(self):
    return self.temLoop() and self.temArestasParalelas()

  def e_multigrafo(self):
    return self.temArestasParalelas and not self.temLoop()
