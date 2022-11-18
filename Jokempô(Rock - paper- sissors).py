import random
import os

def resultado(ganhou, empate, perdeu):
    os.system("cls")
    print("\nResultado:")
    print(f"Vitórias: {ganhou}")
    print(f"Empates: {empate}")
    print(f"Derrotas: {perdeu}\n")
    

def escolha(numero):
    if numero == 1:
        return "pedra"
    elif numero == 2:
        return "Papel"
    else:
        return "Tesoura"

def jogar():
    opcao = 0
    ganhou = 0
    perdeu = 0
    empate = 0

    while opcao != 4:
        resposta = input("Escolha uma opção:\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura\n 4 - Zerar\nOpção: ")
        
        if resposta:
            opcao = int(resposta)
        else:
            opcao = 99

        if opcao == 4:
            break
        elif opcao >= 1 and opcao <= 3:
            maquina = random.randint(1, 3)
            escolha_maquina = escolha(maquina)
            escolha_jogador = escolha(opcao)

            print(f"\nVocê: {escolha_jogador}\nMáquina: {escolha_maquina}\n")

            if opcao == 1:
                if maquina == 3:
                    ganhou += 1
                    print("Uhuu, você ganhou!!")
                elif maquina == 1:
                    empate += 1
                    print("Empatou")
                else:
                    perdeu += 1
                    print("Perdeu")
            
            elif opcao == 2:
                if maquina == 1:
                    ganhou += 1
                    print("Uhuu, você ganhou!!")
                elif maquina == 2:
                    empate += 1
                    print("Empatou")
                else:
                    perdeu += 1
                    print("Perdeu")
            
            elif opcao == 3:
                if maquina == 2:
                    ganhou += 1
                    print("Uhuu, você ganhou!!")
                elif maquina == 3:
                    empate += 1
                    print("Empatou")
                else:
                    perdeu += 1
                    print("Perdeu")
        
        else:
            print("Opção inválida")

        resultado(ganhou, empate, perdeu)

    resultado(ganhou, empate, perdeu)
    print("Jogo Encerrado, muito obrigado!\n")

while True:
    print("Jokempô(Rock - paper- sissors) - Aloísio")
    
    print("Escolha uma opção:")
    opcao_jogo = int(input("1 - Iniciar Jogo \n2 - Para sair\n"))

    if opcao_jogo == 1:
        jogar()
    else:
        print("Você está desligando o jogo, muito obrigado e volte sempre!")
        input()
        break
