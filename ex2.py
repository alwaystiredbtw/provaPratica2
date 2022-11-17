import random
dado = [1,2,3,4,5,6]
player1 = []
player2 = []
jogada = 1
def menu():
    print("[MENU]\nSelecione as opcoes:\n[1] - Comecar\n[2] - Encerrar")
    escolha = int(input("sua escolha:"))
    if escolha == 1:
        return jogo()
    if escolha == 2:
        return score()        
def randomLista():
    return random.choice(dado)
def jogo():
    global jogada
    num = randomLista()
    if jogada % 2 != 0:
        player1.append(num)
        print(f"Jogador 1 tirou {num}.")
        jogada += 1
    else:
        player2.append(num)
        print(f"Jogador 2 tirou {num}")
        jogada +=1
    jogarNovamente()
def score():
    print(f"Jogadas do Player 1: {player1}\nJogadas do Player 2: {player2}\nSoma Player1: {sum(player1)}\nSoma Player2: {sum(player2)}")
    if sum(player1) > sum(player2):
        print("O jogador 1 venceu !\nObrigado por jogar !")
    if sum(player1) == sum(player2):
        print("Empate !")
    if sum(player1) < sum(player2):
        print("Jogador 2 venceu !\nObrigado por jogar !")
def jogarNovamente():
    print("o que deseja fazer?\n[1] proxima jogada\n[2] menu")
    escolha = int(input(":"))
    match escolha:
        case 1:
            jogo()
        case 2:
            menu()


menu()


    
    