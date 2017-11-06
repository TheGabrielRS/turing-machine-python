class Estado:

  def __init__(self, indice, final):
    self.indice = indice
    self.final = final
    self.transicoes = []

  def adicionaTransicao(self, transicao):
    self.transicoes.append(transicao)

  def encontraTransicao(self, encontrou):
    for x in range(len(self.transicoes)):
      if encontrou == self.transicoes[x].encontrou:
        return self.transicoes[x]
    return False
