from random import randint

numero = randint(0, 9)
print(numero)

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

print("Final do jogo: ")