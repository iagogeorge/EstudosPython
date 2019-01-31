import random

print("************************************")
print("olá bem vindo ao jogo de adivinhação")
print("************************************")

numero_secreto =  random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000
numero_minimo = 1
numero_maximo  = 100


print("qual o nível de dificuldade?")
print("(1) - fácil (2) - médio (3) - Díficil")

nivel = input("Defina um nível de dificuldade: ")


if int(nivel) == 1:
    total_de_tentativas = 20
elif int(nivel) == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for rodada in  range (1, total_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite um numero entre {} e {} : ". format(numero_minimo, numero_maximo))


    if int(chute) < numero_minimo or int(chute) > numero_maximo:
        print("voce digitou o numero {} que nao está entre os numeros {} e {} tente novamente: "
              . format(chute, numero_minimo, numero_maximo) )
        continue
    acertou = numero_secreto == int(chute)
    maior = int(chute) > numero_secreto
    menor = int(chute) < numero_secreto

    if (acertou):
        print("você acertou!! e fez {} pontos!!".format(pontos))
        break

    else:
        if(maior):
            print("você errou! o seu chute foi maior do que o numero secreto.")
        elif(menor):
            print("você errou! o seu chute  foi menor do que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - int(chute))
        pontos = pontos - pontos_perdidos


    rodada = rodada + 1
print("fim do jogo. Numero secreto: {}".format(numero_secreto))