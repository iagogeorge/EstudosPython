import adivinhacao
import forca

def escolher_jogo():
    print("************************************")
    print("*******Escolha o seu jogo***********")
    print("************************************")

    print("")

    jogo = input("qual jogo você quer jogar??")
    print("")
    print("")

    if jogo == "1":
        print("jogando forca")
        forca.jogar()
        print("")
    elif jogo == "2":
        print("jogando adivinhação")
        adivinhacao.jogar()
        print("")

if(__name__=="__main__"):
    escolher_jogo()