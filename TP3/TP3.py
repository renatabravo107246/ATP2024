# menu
def menu():
    print("Bem-vindo ao jogo dos 21 fósforos!")
    print("Cada jogador retira, à vez, no mínimo 1 e no máximo 4 fósforos.")
    print("Quem retirar o último fósforo perde. Boa sorte!")
    print("1. Quero ser o primeiro a jogar!")
    print("2. Quero ser o segundo a jogar!")
    print("3. SAIR.")

# utilizador é o primeiro a jogar
def pri():
    fosf = 21
    while fosf > 1:
        salto = int(input("Quantos fósforos retiras?"))
        while salto > 4 or salto < 1:
            print("Só pode retirar entre 1 a 4 fósforos")
            salto = int(input("Quantos fósforos retiras?"))
        fosf = fosf - salto
        comp = 5 - salto
        fosf = fosf - comp
        print(f"Eu retiro {comp} fósforos. É a tua vez, sobram {fosf}.")
    print ("Perdeste porque ficaste com o último fósforo.")

# utilizador é o segundo a jogar
def seg():
    from random import randint
    fosf = 21
    while fosf > 1:
        comp = randint(1,4)
        fosf = fosf - comp
        salto = int(input(f"Eu retiro {comp} fósforos. Sobram {fosf}. Quantos retiras?"))
        while salto > 4 or salto < 1:
            print("Só pode retirar entre 1 a 4 fósforos")
        salto = int(input("Quantos fósforos retiras?"))
        fosf = fosf - salto
        if fosf == 1:
            print ("Fiquei com o último fósforo. Ganhaste, parabéns!")

        if salto != 5- comp :
            if fosf > 16: 
                comp = fosf - 16
            elif fosf > 11:
                comp = fosf - 11
            elif fosf > 5:
                comp = fosf - 5
            elif fosf > 1:
                comp = fosf - 1

            fosf = fosf - comp
            while fosf > 1:
                salto = int(input(f"Eu retiro {comp} fósforos. Sobram {fosf}. Quantos retiras?"))
                while salto > 4:
                    print("Só pode retirar até 4 fósforos")
                    salto = int(input("Quantos fósforos retiras?"))
                while salto < 1:
                    print("Tens de retirar, pelo menos, 1 fósforo.")
                    salto = int(input("Quantos fósforos retiras?"))
                fosf = fosf - salto
                comp = 5 - salto
                fosf = fosf - comp
                
            print("Perdeste porque ficaste com o último fósforo.")

def terc():
    print("Obrigada! Volte sempre :)")
    

# jogo dos 21 fósforos

menu()
opcao = int(input("Selecione uma das opções."))

while opcao != 3:
    if opcao == 1:
        pri()
    elif opcao == 2:
        seg()
    else:
        print("Opção inválida.")
    menu()
    opcao = int(input("Selecione uma das opções."))
terc()
