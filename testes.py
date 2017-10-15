from maquina import Maquina

#Testes utilizando os metodos internos


"""A decima letra a esquerda deve ser a letra A
maq = Maquina()

maq._adicionaEstado(Estado(0,True))#q0
maq._adicionaEstado(Estado(1,True))#q1
maq._adicionaEstado(Estado(2,True))#q2
maq._adicionaEstado(Estado(3,True))#q3
maq._adicionaEstado(Estado(4,True))#q4
maq._adicionaEstado(Estado(5,True))#q5
maq._adicionaEstado(Estado(6,True))#q6
maq._adicionaEstado(Estado(7,True))#q7
maq._adicionaEstado(Estado(8,True))#q8
maq._adicionaEstado(Estado(9,True))#q9
maq._adicionaEstado(Estado(10,True))#qd
maq._adicionaEstado(Estado(11,False))#qf

maq._adicionaTransicao(0, Transicao('_', '_', 0, 'E', 1))
maq._adicionaTransicao(0, Transicao('a', 'a', 0, 'D', 0))
maq._adicionaTransicao(0, Transicao('b', 'b', 0, 'D', 0))

for x in range(0,11):
  maq._adicionaTransicao(x, Transicao('a', 'a', x, 'E', x+1))
  maq._adicionaTransicao(x, Transicao('b', 'b', x, 'E', x+1))
  
maq._definePalavra(Palavra("aaaaaaaaaa_"))

maq.executaLeitura()
"""

#A quantidade de A deve ser a mesma de B
maq = Maquina()

#q0
maq._adicionaEstado(0, True)
#q1
maq._adicionaEstado(1, True)
#q2
maq._adicionaEstado(2, True)
#q3
maq._adicionaEstado(3, True)
#q4
maq._adicionaEstado(4, False)

#Transicoes q3
maq._adicionaTransicao('a','A',3,2,'E')
maq._adicionaTransicao('b','b',3,3,'D')
maq._adicionaTransicao('A','A',3,3,'D')
maq._adicionaTransicao('B','B',3,3,'D')

#Transicoes q2
maq._adicionaTransicao('*','*',2,0,'D')
maq._adicionaTransicao('a','a',2,2,'E')
maq._adicionaTransicao('b','b',2,2,'E')
maq._adicionaTransicao('A','A',2,2,'E')
maq._adicionaTransicao('B','B',2,2,'E')


#Transicoes q1
maq._adicionaTransicao('a','a',1,1,'D')
maq._adicionaTransicao('b','B',1,2,'E')
maq._adicionaTransicao('A','A',1,1,'D')
maq._adicionaTransicao('B','B',1,1,'D')

#Transicoes q0
maq._adicionaTransicao('a','A',0,1,'D')
maq._adicionaTransicao('b','B',0,3,'D')
maq._adicionaTransicao('A','A',0,0,'D')
maq._adicionaTransicao('B','B',0,0,'D')
maq._adicionaTransicao('_','_',0,4,'D')
maq._adicionaTransicao('*','*',0,0,'D')

maq._definePalavra("*aabbaa_")

maq.executaLeitura()