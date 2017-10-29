# turing-machine-python

Esse programa é a implementação de uma máquina de Turing.

# Classes

## Estado

Estado é a junção de várias transições. O estado pode ser o final da máquina.

## Transicao

Cada etapa da validação de uma palavra é realizada pela identificação da posição com uma transição.
Uma transição consiste em substituir o símbolo encontrado por um outro símbolo.
A transição também indica qual o estado que se deve dirigir e qual a direção que o indicador da fita deve andar.

## Palavra

A palavra é o que deve ser validado. Há duas direções para se seguir em uma palavra: esquerda e direita.

## Máquina

Na máquina constam todas as regras já estruturadas, com Estados, Transições e uma Palavra para ser validada.
