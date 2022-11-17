linhas = int(input("Quantas linhas deseja na matriz?"))
colunas = int(input("Quantas colunas deseja na matriz?"))
impares = []
listaValor = []
def criaMatriz(l, c):
    matriz = []
    for i in range(l):
        matriz.append(c * [0])
    return matriz
    

matriz = criaMatriz(linhas,colunas)
print(matriz)

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input(f"Digite um valor para a posicao {[i],[j]}"))

def achaValores():
    for i,linha in enumerate(matriz):
        for j,valor in enumerate(linha):
            listaValor.append(valor)
            if valor % 2 != 0:
                impares.append(valor)

achaValores()

for i,valor in enumerate(matriz):
    print(valor)

print(f"A matriz tem {len(impares)} numeros impares!\nO menor valor eh {min(listaValor)}")

