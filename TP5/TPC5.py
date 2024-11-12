#Aplicação para gerir um cinema

sala = ()
def menu():
    print("""
        1) Filmes em exibição
        2) Lugar disponível
        3) Vender bilhete
        4) Disponibilidade do Cinema
        5) Criar Sala
        0) Sair
          """)
    return

def filmes_exi(cinema):
    if cinema == []:
        print("O cinema não tem filmes em exibição")
    else:
        print("Filmes em exibição:")
        for sala in cinema:
            print(f"Filme: {sala[2]}")
    input("Prime qualquer tecla para voltares ao menu")

def lugardisponivel(cinema, filme, lugar):
    lugar_disponivel = False
    for sala in cinema:
        if sala[2] == filme:
            return lugar not in sala[1] and 0 < lugar <= sala[0]
    return False

def vendebilhete(cinema, filme, lugar):
    for sala in cinema:
        if sala[2]== filme:
            if lugar not in sala[1] and 0 < lugar <= sala[0]:
                sala[1].append(lugar)
                print(f"Compraste o bilhete para o lugar {lugar} do filme {filme} com sucesso!")
                return cinema
            else:
                print("Esse lugar já não está disponível ou não existe")
                return cinema
    print("Esse filme não está em exibição")
    return cinema

def listardisponibilidades(cinema):
    if cinema == []:
        print("O cinema ainda não tem salas.")
    else:
        for sala in cinema:
            lugares_disponiveis= sala[0] - len(sala[1])
            print(f"Filme: {sala[2]} | Lugares disponíveis: {lugares_disponiveis}")
    input("Prime qualquer tecla para voltares ao menu")
    return

def inserirSala(cinema, sala):
    for s in cinema:
        if s[2] == sala[2]:
            print(f"O filme {sala[2]} já está a ser exibido noutra sala")
            return cinema
    cinema.append(sala)
    print(f"A sala com o filme '{sala[2]}' com {sala[0]} lugares foi adicionada ao cinema")
    input("Prime qualquer tecla para voltares ao menu")
    return cinema

def main():
    cinema = []
    menu()
    opcao = int(input("Seleciona uma opção!"))

    while opcao != 0:
        if opcao == 1:
            filmes_exi(cinema)
        elif opcao == 2:
            filme = input("Qual é o filme que queres ver?")
            lugar = int(input("Qual é o lugar?"))
            disponibilidade = lugardisponivel (cinema, filme, lugar)
            print(disponibilidade)
            input("Prime qualquer tecla para voltares ao menu")
        elif opcao == 3:
            filme = input("Qual é o filme que queres ver?")
            lugar = int(input("Qual é o lugar?"))
            cinema = vendebilhete(cinema, filme, lugar)
            input("Prime qualquer tecla para voltares ao menu")
        elif opcao == 4:
            listardisponibilidades(cinema)
        elif opcao == 5:
            nlugares = int(input("Quantos lugares tem a sala?"))
            filme = input("Qual é o filme exibido na sala?")
            nova_sala = [nlugares, [], filme]
            cinema = inserirSala(cinema, nova_sala)
            
        menu()
        opcao = int(input("Seleciona uma opção!"))
    print("Obrigada! Volte sempre :)")
    return

main()

