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

  def _definePalavra(self, inputPalavra): #Define a palavra e insere as indicaÃ§Ãµes de inÃ­cio e fim
    self.palavra = Palavra(inputPalavra)

  def _mostraPalavra(self): #Mostra a palavra atual
    print(self.palavra.getPalavra())
    
  def _posicaoPalavra(self): #Retorna a letra que estÃ¡ sendo apontada
    return self.palavra.atual()
    
  def _substituiPosicaoPalavra(self, substitui): #Faz a troca proposta pela transiÃ§Ã£o
    self.palavra.substitui(substitui)
    
  def _moveCursor(self, move): #Move o cursor para esquerda ou direita
    if move:
      self.palavra.direita()
    else:
      self.palavra.esquerda()

  def _adicionaTransicao(self, encontrou, substitui, estadoOrigem, estadoDestino, direcaoFita): #Adiciona uma transiÃ§Ã£o para algum estado
    self.estados[estadoOrigem].adicionaTransicao(Transicao(encontrou, substitui, estadoOrigem, estadoDestino, direcaoFita))
    
  def _buscaTransicao(self): #Busca a transiÃ§Ã£o do estado atual para a posiÃ§Ã£o atual do cursor
    return self.estadoAtual.encontraTransicao(self._posicaoPalavra())

  def _executaLeitura(self):
    self.estadoAtual = self.estados[0] #inicia pelo estado 0
    while self.estadoAtual.final: #enquanto nao for o estado final
      transicao = self._buscaTransicao() #busca uma transicao no estado correspondente de acordo com a posicao atual do cursor
      if transicao != False: #caso nao haja uma transicÃ£o para o que foi encontrado, sai do while
        if transicao.encontrou != transicao.substitui: #so realiza a alteracao caso os valores sejam diferentes
          self._substituiPosicaoPalavra(transicao.substitui) #realiza a substituicao da letra na devida posicao
          palavra = self._mostraPalavra()
          if palavra != None:
             print(palavra) #mostra a palavra somente quando ha alteracao
        self._moveCursor(transicao.direcaoFita) #move a fita
        if self.estadoAtual != transicao.estadoDestino: #so altera o estado caso eles sejam diferentes
          self._vaParaEstado(transicao.estadoDestino) #altera o estado atual
      else:
        break #aqui sai do while
    if self.estadoAtual.final: #verifica se a saida do while foi por ser a transicao final ou por nao haver transicao programada
      return False
      #print("Palavra invalida")
    else:
      return True
      #print("Palavra valida")
