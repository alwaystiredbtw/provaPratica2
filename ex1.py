#Implemente uma funcao que cria uma lista preenchida por zeros

tamanhoL = int(input("Qual o tamanho desejado para a lista?"))


def criaLista(tamanho):
    lista = [0] * tamanho
    return lista

lista = criaLista(tamanhoL)

for i in range(len(lista)):
    lista[i] = int(input(f"Digite o valor da lista na posicao [{i}]:"))

listaReversa = list(reversed(lista))

print(f"Lista: {lista}\nLista reversa: {listaReversa}\nSoma dos valores da lista: {sum(lista)}\nO menor valor da lista:{min(lista)}")