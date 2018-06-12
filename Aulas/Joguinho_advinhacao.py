from random import randint

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero = randint(0, 9)

rodadas = 1
tentativas = 3

for rodadas in range(1, tentativas + 1):
    print("Tentativa {} de {} ".format(rodadas, tentativas))
    chute = int(input("Digite um numero de 0 a 9: "))

    if (chute < 1 or chute > 9):
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


print("Final do jogo: ")