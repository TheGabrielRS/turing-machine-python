class Transicao:

  def __init__(self, encontrou, substitui, estadoOrigem, estadoDestino, direcaoFita):
    self.encontrou = encontrou
    self.substitui = substitui
    self.estadoDestino = estadoDestino
    self.estadoOrigem = estadoOrigem   
    if direcaoFita == 'D':
      self.direcaoFita = True
    else:
      self.direcaoFita = False
