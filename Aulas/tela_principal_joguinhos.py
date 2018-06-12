import forca
import advinhacao

print("*********************************")
print("******Bem vindo ao PyGame!!!*****")
print("*********************************")

print("Escolha o seu jogo!!!")

escolha = int(input("(1) - Jogo da Advinhação: (2) - Jogo da forca: "))

if(escolha == 1):
    print("Jogaando Advinhação: ")
    advinhacao.jogar()
elif(escolha == 2):
    print("Jogando Forca: ")
    forca.jogar()
else:
    print("Escolha inválida, fechando PyGame:")
    breakpoint(exit())