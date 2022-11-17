# lista c04 ex 2
# Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
# # elementos. Escreva ao final a matriz obtida.


matriz = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]


for i in range(5):
    for j in range(5):
        if i == j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0


for i in range(5):
    print(matriz[i])