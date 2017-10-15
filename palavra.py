class Palavra:

  def __init__(self, palavra):
    self.palavra = list(palavra)
    self.cursor = 0

  def direita(self):
    if self.cursor < len(self.palavra)-1:
      self.cursor += 1

  def esquerda(self):
    if self.cursor > 0:
      self.cursor -= 1

  def atual(self):
    return self.palavra[self.cursor]
    
  def substitui(self, letra):
      self.palavra[self.cursor] = letra

  def getPalavra(self):
    return self.palavra
