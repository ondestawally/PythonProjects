from random import randint

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero = randint(0, 20)
rodadas = 0
pontuacao = 100

print(numero)
print("Selecione o tipo de jogo: ")
dificuldade = int(input(" (1) - Fácil, (2) - Médio, (3) - Difícil: "))

if(dificuldade == 1):
    tentativas = 5
elif(dificuldade == 2):
    tentativas = 3
elif(dificuldade == 3):
    tentativas = 2
else:
    print("Escolha inválida fechando jogo")
    breakpoint(exit())

for rodadas in range(1, tentativas + 1):
    print("Tentativa {} de {} ".format(rodadas, tentativas))
    chute = int(input("Digite um numero de 0 a 20: "))

    if (chute < 1 or chute > 21):
        print("Número inválido: tente outra vez:")
        continue
    numero_certo = numero == chute
    maior = chute > numero
    menor = chute < numero


    if (numero_certo):
        print("Você acertou: ")
        break
    else:
        if(maior):
            print("Seu chute foi maior: ")
        elif(menor):
            print("Seu chute foi Menor: ")
        pontos_perdidos = abs(numero - chute)
        pontuacao = pontuacao - pontos_perdidos
print("Sua pontuação final é: {}".format(pontuacao))
print("Final do jogo: ")