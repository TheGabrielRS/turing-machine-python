from estado import Estado
from palavra import Palavra
from transicao import Transicao

class Maquina:

  def __init__(self):
    self.estadoAtual = None
    self.estados = []
    
  #INTERAÇOES COM O USUARIo
  
  def adicionaEstado(self):
    final = int(input("Esse estado e final? (0 - Sim, 1 - Nao"))
    final = True if final == 0 else False
    self._adicionaEstado(indice, final)

  def definePalavra(self):
    inputPalavra = input("Qual a palavra que a maquina deve validar? ")
    self._definePalavra(inputPalavra)
  
  def mostraPalavra(self):
    self._mostraPalavra()

  def adicionaTransicao(self):
    estadoOrigem = int(input("Em qual estado essa transicao esta? "))
    
    if estadoOrigem > len(self.estados)-1 or len(self.estados) == 0:
      print("Nao ha estado com este indice")
      return False
    
    estadoDestino = int(input("Para que estado ir? "))
    
    if estadoDestino > len(self.estados)-1:
      print("Nao ha estado destino com este indice")
      return False
    
    encontrou = input("O que procurar? ")
    substitui = input("O que inserir quando encontrar? ")
    direcaoFita = input("Para que direcao seguir na fita quando encontrar? (D = Direita, E = Esquerda) ")
    
    if direcaoFita == 'D' or direcaoFita == 'E':
      self._adicionaTransicao(estadoOrigem, Transicao(encontrou, substitui, estadoOrigem, direcaoFita, estadoDestino))
    else:
      print("Direcao invalida")
      return False
      
  #Metodos privados de execucao somente interna, sem interface com o usuario
  
  def _adicionaEstado(self, indice, final): #Adiciona um estado a lista
    self.estados.append(Estado(indice, final))
    
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

  def executaLeitura(self):
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
      print("Palavra invalida")
    else:
      print("Palavra valida")