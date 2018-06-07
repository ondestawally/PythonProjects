from random import randint

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero = randint(0, 9)


tentativas = 3

while(tentativas > 0):
    chute = int(input("Digite um numero de 0 a 9: "))

    numero_certo = numero == chute
    maior = chute > numero
    menor = chute < numero

    if (numero_certo):
        print("Você acertou: ")
    else:
        if(maior):
            print("Seu chute foi maior: ")
        elif(menor):
            print("Seu chute foi Menor: ")
    tentativas = tentativas - 1

print("Final do jogo: ")