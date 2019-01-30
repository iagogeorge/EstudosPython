import random

print("************************************")
print("olá bem vindo ao jogo de adivinhação")
print("************************************")

numero_secreto =  random.randrange(1, 101)
total_de_tentativas = 3
numero_minimo = 1
numero_maximo  = 100


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
        print("você acertou!!")
        break

    else:
        if(maior):
            print("você errou! o seu chute foi maior do que o numero secreto.")
        elif(menor):
            print("você errou! o seu chute  foi menor do que o numero secreto.")


    rodada = rodada + 1
print("fim do jogo. Numero secreto: {}".format(numero_secreto))