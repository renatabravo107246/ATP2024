def menu():
    print("(1) Criar Lista ")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) estaOrdenada por ordem crescente")
    print("(8) estaOrdenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

import random 
lista = []

def criar():
    lista = []
    N = int(input("Introduz o número de elementos da lista: "))
    lista = [random.randrange(1,101) for n in range(N)]
    print(lista)
    input("Clica numa tecla para voltares ao menu")
    return lista

def ler():
    lista = []
    N = int(input("Introduz o número de elementos da lista: "))
    i = 1
    while i <= N :
        n = int(input(f"Introduza o elemento da lista {i}/{N}: "))
        lista.append(n)
        i = i + 1
    print(lista)
    input("Clica numa tecla para voltares ao menu. ")
    return lista

def soma(lista):
    print(lista)
    N = len(lista)
    i = 0
    soma = 0
    while i < N :
        n = lista[i]
        soma = soma + n
        i = i + 1
    print (f"A soma dos elementos da lista é {soma}.")
    input("Clica numa tecla para voltares ao menu. ")

def media(lista):
    print(lista)
    N = len(lista)
    i = 0
    soma = 0
    while i < N :
        n = lista[i]
        soma = soma + n
        i = i + 1
    print (f"A média dos elementos da lista é {soma/N}.")
    input("Clica numa tecla para voltares ao menu. ")

def maior(lista):
    print(lista)
    maior = lista[0]
    for n in lista[1:]:
        if n > maior:
            maior = n
    print(f"O maior número é {maior}.")
    input("Clica numa tecla para voltares ao menu. ")
        
def menor(lista):
    print(lista)
    menor = lista[0]
    for n in lista[1:]:
        if n < menor:
            menor = n
    print(f"O menor número é {menor}.")
    input("Clica numa tecla para voltares ao menu. ")

def cresc(lista):
    print(lista)
    i = 0
    N = len(lista)
    while i < N - 1:
        if lista[i] > lista[i + 1]:
            print("A lista NÃO está ordenada por ordem crescente.")
            input("Clica numa tecla para voltares ao menu. ")
            return
        i = i + 1
    print("A lista está ordenada por ordem crescente.")
    input("Clica numa tecla para voltares ao menu. ")

def decresc(lista):
    print(lista)
    i = 0
    N = len(lista)
    while i < N - 1:
        if lista[i] < lista[i + 1]:
            print("A lista NÃO está ordenada por ordem decrescente.")
            input("Clica numa tecla para voltares ao menu. ")
            return
        i = i + 1
    print("A lista está ordenada por ordem decrescente.")
    input("Clica numa tecla para voltares ao menu. ")

def proc(lista):
    print(lista)
    x = int(input("Qual é o elemento que queres procurar?"))
    pos = -1
    for i in range(len(lista)):
        if lista[i] == x:
            pos = i + 1
    if pos == -1:
        print("-1")
    else:
        print(f"O elemento {x} encontra-se na {pos}º posição (índice = {i}). ")  
    input("Clica numa tecla para voltares ao menu. ")

def sair():
    print(f"A lista guardada é {lista}")
    print("Obrigada! Volta sempre :)")

def main():
    lista = []
    opcao = -1
    while opcao != 0 :
        menu()
        opcao = int(input("Seleciona uma opção: "))
        if opcao in [3,4,5,6,7,8,9]:
            if lista == []:
                print("Tens de criar uma lista primeiro! Seleciona 1 ou 2 no menu.")
                input("Clica numa tecla para voltares ao menu. ")
            else:
                if opcao == 3:
                    soma(lista)
                elif opcao == 4:
                    media(lista)
                elif opcao == 5:
                    maior(lista)
                elif opcao == 6:
                    menor(lista)
                elif opcao == 7:
                    cresc(lista)
                elif opcao == 8:
                    decresc(lista)
                elif opcao == 9:
                    proc(lista)
        elif opcao == 1:
            lista= criar()
        elif opcao == 2:
            lista = ler()
        elif opcao not in [0,1,2,3,4,5,6,7,8,9]: 
            print("Opção inválida :(")
            input("Clica para voltares ao menu. ")
    sair()

main()
