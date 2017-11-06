from maquina import Maquina
import sys
import json

maq = Maquina()
file_name = sys.argv[1]

text = open(file_name)
content = text.read()
jsonmaquina = json.loads(content)

estadoFinal = None
estadoIndex = 0
for estado in jsonmaquina:
	if(jsonmaquina[estadoIndex][0][0] == 'false'):
		estadoFinal = estadoIndex
		maq._adicionaEstado(estadoIndex, False)
	else:
		maq._adicionaEstado(estadoIndex, True)
	estadoIndex+=1

estadoIndex = 0
for estado in jsonmaquina:
	if estadoIndex != estadoFinal:
		for transicao in jsonmaquina[estadoIndex]:
			maq._adicionaTransicao(transicao[0],transicao[2],estadoIndex,int(transicao[1]),transicao[3])
	estadoIndex+=1

maq._definePalavra(sys.argv[2])
print("palavra valida") if maq._executaLeitura() else print("palavra invalida")
