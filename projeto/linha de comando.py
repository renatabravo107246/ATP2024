import json
import matplotlib.pyplot as plt 
import projeto as mp

#MENU
def mostrar_menu():
    print("""
            1 - Criar Publicação
            2 - Editar Publicação
            3 - Consultar Publicação
            4 - Consultar Publicações
            5 - Eliminar Publicação
            6 - Relatório de Estatística
            7 - Listar Autores
            8 - Importar Publicações
            9 - Guardar Publicações
            10 - Help
            0 - Sair""")
    
def menu_stats():
    print("""Relatórios de Estatística:
          
        1 - Distribuição de publicações por ano.
        2 - Distribuição de publicações por mês de um determinado ano.
        3 - Número de publicações por autor (top 20 autores).
        4 - Distribuição de publicações de um autor por anos.
        5 - Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave).
        6 - Distribuição de palavras-chave mais frequente por ano.
          
""")


def menu():
    print("Bem-vindo ao Sistema de Gestão de Publicações Médicas.")
    path = input("Insira o caminho do ficheiro: ")
    dataset = mp.loaddata(path)
    stop = False

    while not stop:
        mostrar_menu()
        option = int(input("Insira a opção desejada: "))

        if option == 1:
            title = input("Insira o título da publicação: ")
            abstract = input("Insira o resumo da publicação: ")
            keywords = mp.criar_keywords()
            doi = input("Insira o DOI da publicação: ")
            authors = mp.criar_autores()
            publish_date = mp.criar_data()
            url = input("Insira a URL da publicação: ")
            pdf = input("Insira o PDF da publicação: ")
            dataset = mp.criar_pub(dataset, title, abstract, keywords, doi, authors, publish_date, url, pdf)
        
        elif option == 2:
            pub = mp.find_pub(dataset)
            if pub != None:
                new_pub = mp.edit_pub(pub)
                dataset.remove(pub)
                dataset.append(new_pub)
            else: 
                print("Publicação não encontrada.")

        elif option == 3:
            pub = mp.find_pub(dataset)
            if pub != None:
                mp.consultar_pub(pub)
            else:
                print("Publicação não encontrada.")
        
        elif option == 4:
            mp.consultar_pubs(dataset)
        
        elif option == 5:
            dataset = mp.eliminar_pub(dataset)
        
        elif option == 6:
            menu_stats()
            option = 0
            stop_stats = False
            while not stop:
                option = int(input("Insira a opção desejada: "))
                if option == 1:
                    mp.pub_ano(dataset)
                elif option == 2:
                    mp.pub_mes(dataset, int(input("Insira o ano pretendido: ")))
                elif option == 3:
                    mp.pub_top_autores(dataset)
                elif option == 4:
                    mp.pub_autor_ano(dataset, input("Insira o nome do autor: "))
                elif option == 5:
                    mp.palavras_chave(dataset)
                elif option == 6:
                    mp.palavras_chave_ano(dataset, int(input("Insira o ano pretendido: ")))
    
                if input("Deseja visualizar outro gráfico? [s/n]").strip().lower() == 'n':
                    stop_stats = True
        
        elif option == 7:
            mp.listar_autores(dataset)
        
        elif option == 8:
            newfile = input("Insira o nome do ficheiro (com extensão .json): ")
            dataset = mp.importing(newfile, dataset)
        
        elif option == 9:
            filename = input("Insira o nome do ficheiro (com extensão .json): ")
            mp.armazenamento(filename, dataset)
        
        elif option == 10:
            print("""Help:
                Criar Publicação: Permite adicionar uma nova publicação à base de dados.
                Editar Publicação: Permite editar uma publicação existente.
                Consultar Publicação: Permite pesquisar uma publicação existente.
                Consultar Publicações: Permite pesquisar publicações existentes.
                Eliminar Publicação: Permite apagar uma publicação existente.
                Relatório de Estatística: Permite gerar um relatório estatístico.
                Listar Autores: Permite listar todos os autores, bem como as suas publicações.
                Importar Publicações: Permite importar publicações de um ficheiro para a base de dados.
                Guardar Publicações: Permite guardar as publicações num ficheiro.""")
        
        elif option == 0:
            resp = input("""Tem a certeza que deseja sair? [s/n]
                (Se não guardou as alterações, estas serão perdidas.)""").strip().lower()
            
            if resp == 's':
                print("Sistema de Gestão de Publicações Médicas encerrado.")
                stop = True

            elif resp == 'n':
                print("Operação cancelada.")

            else:
                print("Opção inválida.")

menu()
