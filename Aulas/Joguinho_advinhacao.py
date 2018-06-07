from random import randint

numero = randint(0, 9)

chute = int(input("Digite um numero de 0 a 9: "))
if numero == chute:
    print("Você Acertou: ")
else:
    print("Você errou: ")

print("Final do jogo: ")