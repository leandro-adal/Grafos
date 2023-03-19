class Grafo: # grafo não dirigido
  n = 0
  matriz = 0

  # construtor
  def __init__(self,n):
    self.n = n
    self.matriz = [ [ 0 for i in range(n) ] for j in range(n) ]

  # imprimir
  def __str__(self):
    graph = ''
    for i in range(self.n):
      for j in range(self.n):
        graph += str(self.matriz[i][j])+' '
      graph +='\n'
    return graph

  # inserir
  def criar_aresta(self, vi, vj):
    self.matriz[vi][vj] += 1
    self.matriz[vj][vi] += 1

  # remover
  def remover_aresta(self, vi, vj):
    self.matriz[vi][vj] -= -1
    self.matriz[vj][vi] -= -1
  
  # existe
  def existe_aresta(self,vi,vj):
    return self.matriz[vi][vj] > 0

  # grauVertice
  def getGrauVertice(self,vertice):
    grau = 0
    for v in range(self.n):
      grau += self.matriz[v][vertice]
    return grau

  # grauGrafo
  def getGrauGrafo(self):
    grau = 0
    for v in range(self.n):
      grau += self.getGrauVertice(v)
    return grau

  # temLoop
  def temLoop(self):
    for i in range(self.n):
      if self.matriz[i][i] != 0: # a diagonal principal representa os laços do grafo
        return True
    return False

  def temArestasParalelas(self):
    for i in range(self.n):
      for j in range(i+1,self.n):
        if self.matriz[i][j] > 1:
          return True
    return False

  def eh_regular(self):
    primeiro_grau = self.getGrauVertice(0)
    for i in range(1, self.n):
        if self.getGrauVertice(i) != primeiro_grau:
            return False
    return True

  def adjacentes(self, vertice):
    adjacentes = []
    for i in range(self.n):
        if self.matriz[vertice][i] > 0:
            adjacentes.append(i)
    return adjacentes

  def eh_completo(self):
    for i in range(self.n):
        for j in range(i+1, self.n):
            if self.matriz[i][j] == 0:
                return False
    return True

  def bipartido(self):
    n = self.n
    cor = [None]*n
    cor[0] = 0
    print(cor)
    for i in range(n-1):
      for j in range(i+1,n):
        if g.matriz[i][j] == 1:
          print(cor)
          if cor[i] == cor[j]:
            return False
          elif cor[j]==None:
            cor[j] = (cor[i]+1)%2
    return True
  
  def e_simples(self): # um grafo simples não tem arestas paralelas e não tem loops
    if not self.temLoop() and not self.temArestasParalelas():
      return True
    else:
      return False

  def e_multigrafo(self):
    return self.temArestasParalelas and not self.temLoop()

  def e_pseudografo(self):
    return self.temLoop() and self.temArestasParalelas()
