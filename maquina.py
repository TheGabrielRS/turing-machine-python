from estado import Estado
from palavra import Palavra
from transicao import Transicao

class Maquina:

  def __init__(self):
    self.estadoAtual = None
    self.estados = []
    
  def _adicionaEstado(self, indice, final): #Adiciona um estado a lista
    self.estados.append(Estado(indice, final))
	
  def _mostraEstados(self):
    for estado in self.estados:
      print(estado.indice)

  def _vaParaEstado(self, estado): #Define o estadoAtual como o estado indicado pela transicao
    self.estadoAtual = self.estados[estado]

  def _definePalavra(self, inputPalavra): #Define a palavra e insere as indicações de início e fim
    self.palavra = Palavra(inputPalavra)

  def _mostraPalavra(self): #Mostra a palavra atual
    print(self.palavra.getPalavra())
    
  def _posicaoPalavra(self): #Retorna a letra que está sendo apontada
    return self.palavra.atual()
    
  def _substituiPosicaoPalavra(self, substitui): #Faz a troca proposta pela transição
    self.palavra.substitui(substitui)
    
  def _moveCursor(self, move): #Move o cursor para esquerda ou direita
    if move:
      self.palavra.direita()
    else:
      self.palavra.esquerda()

  def _adicionaTransicao(self, encontrou, substitui, estadoOrigem, estadoDestino, direcaoFita): #Adiciona uma transição para algum estado
    self.estados[estadoOrigem].adicionaTransicao(Transicao(encontrou, substitui, estadoOrigem, estadoDestino, direcaoFita))
    
  def _buscaTransicao(self): #Busca a transição do estado atual para a posição atual do cursor
    return self.estadoAtual.encontraTransicao(self._posicaoPalavra())

  def _executaLeitura(self):
    self.estadoAtual = self.estados[0]
    while self.estadoAtual.final:
      transicao = self._buscaTransicao()
      if transicao != False:
        if transicao.encontrou != transicao.substitui:
          self._substituiPosicaoPalavra(transicao.substitui)
        self._moveCursor(transicao.direcaoFita)
        if self.estadoAtual != transicao.estadoDestino:
          self._vaParaEstado(transicao.estadoDestino)
      else:
        break
    if self.estadoAtual.final:
      return False
      #print("Palavra invalida")
    else:
      return True
      #print("Palavra valida")
