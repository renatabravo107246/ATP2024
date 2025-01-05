import json
import matplotlib.pyplot as plt
import PySimpleGUI as sg

#CARREGAR DATASET
def loaddata(path_data):
    with open(path_data, encoding='utf-8') as f:
        data = json.load(f)
    return data

#CRIAR PUBLICAÇÃO
def criar_autores():
    authors = []
    X = True
    while X:
        author = {}
        author['name'] = input("Insira o nome do autor: ")
        author['affiliation'] = str(input("Insira a afiliação do autor [pressione 1 caso não queira adicionar]: "))
        if author['affiliation'] == '1':
            author['affiliation'] = None
        authors.append(author)
        resp = ""
        while resp != "n" and resp != "s":
            resp = input("Deseja adicionar mais autores? [s/n] ").strip().lower()
            if resp == 'n':
                X = False
            elif resp != 's':
                print("Opção inválida!")
    return authors

def criar_keywords():
    resp = str(input("Deseja adicionar keywords? [s/n] ").strip().lower())
    if resp == "s":
        keywords = ""
        X = True
        while X:
            keyword = input("Insira uma keyword: ")
            keywords = keywords + keyword + ", "
            resp = ""
            while resp != "n" and resp != "s":
                resp = input("Deseja adicionar outra keyword? [s/n] ").strip().lower()
                if resp == 'n':
                    X = False
                elif resp != 's':
                    print("Opção inválida!")
        keywords = keywords[:-2]
    elif resp == "n":
        keywords = None
    else:
        print("Opção inválida!")
        keywords = criar_keywords()
    return keywords

def criar_data():
    resp = str(input("Deseja adicionar data de publicação? [s/n] ").strip().lower())
    if resp == "s":
        ano = input("Insira o ano: ")
        mes = input("Insira o mês: ")
        dia = input("Insira o dia: ")
        publish_date = ano + "-" + mes + "-" + dia
    elif resp == "n":
        publish_date = None
    else:
        print("Opção inválida!")
        publish_date = criar_data()
    return publish_date

def criar_pub(data, title, abstract, keywords, doi, authors, publish_date, url, pdf):
    pub = {}
    pub['abstract'] = abstract
    if keywords != None:
        pub['keywords'] = keywords
    if authors != None:
        pub['authors'] = authors
    pub['doi'] = doi
    pub['pdf'] = pdf
    if publish_date != None:
        pub['publish_date'] = publish_date
    pub['title'] = title
    pub['url'] = url
    encontrado = False
    for p in data:
        if p.get('doi') == doi or p.get('pdf') == pdf or p.get('url') == url:
            encontrado = True
    if not encontrado:
        data.append(pub)
        print("Publicação adicionada com sucesso!")
    else:
        print("Publicação já existente!")
    return data


#ENCONTRAR PUBLICAÇÃO
def find_pub(data):
    pub = None
    filter = ""
    filter = input("Pretende pesquisar o artigo por: [title/doi] ").strip().lower()
    if filter == 'doi':
        doi = input('Insira o doi do artigo que procura: ')
        for publicacao in data:
            if publicacao.get('doi') == doi:
                pub = publicacao
    elif filter == 'title':
        title = input('Insira o título do artigo que procura: ')
        for publicacao in data:
            if publicacao.get('title') == title:
                pub = publicacao
    else:
        print("Opção inválida!")
        pub = find_pub(data)
    if pub == None:
        print("Publicação não encontrada.")
    return pub


#EDITAR PUBLICAÇÃO
def edit_pub(pub):
    option = 0
    while option != 9:
        print(f"Publicação: {pub}")
        print("O que deseja editar?")
        print("1 - Título")
        print("2 - Resumo")
        print("3 - Palavras-chave")
        print("4 - Autores")
        print("5 - DOI")
        print("6 - Data de publicação")
        print("7 - URL")
        print("8 - PDF")
        print("9 - Sair da Edição")

        option = int(input("Insira a opção desejada: "))

        if option == 1:
            new_title = input("Insira o novo título: ")
            pub['title'] = new_title
        elif option == 2:
            new_abstract = input("Insira o novo resumo: ")
            pub['abstract'] = new_abstract
        elif option == 3:
            new_keywords = input("Insira as novas palavras-chave: ")
            pub['keywords'] = new_keywords
        elif option == 4:
            new_authors = input("Insira os novos autores: ")
            pub['authors'] = new_authors
        elif option == 5:
            new_doi = input("Insira o novo DOI: ")
            pub['doi'] = new_doi
        elif option == 6:
            new_publish_date = input("Insira a nova data de publicação: (ano-mes-dia)")
            pub['publish_date'] = new_publish_date
        elif option == 7:
            new_url = input("Insira a nova URL: ")
            pub['url'] = new_url
        elif option == 8:
            new_pdf = input("Insira o novo PDF: ")
            pub['pdf'] = new_pdf
        elif option == 9:
            print("Publicação editada com sucesso!")
        else:
            print("Opção inválida!")
    return pub


#ENCONTRAR PUBLICAÇÕES
def consultar_pubs(data):
    res = []
    filter = input("Pretende pesquisar o artigo por: [title/author/affiliation/publish_date/keywords]").strip().lower()
    if filter == 'title':
        title = input('Insira o título do artigo que procura: ').strip().lower()
        for pub in data:
            if 'title' in pub:
                if title == pub['title'].strip().lower():
                    res.append(pub)
    elif filter == 'author':
        name = input('Insira o nome do autor que procura: ').strip().lower()
        for pub in data:
            if 'authors' in pub:
                for author in pub['authors']:
                    if name == author["name"].strip().lower():
                        res.append(pub) 
    elif filter == 'affiliation':
        affiliation = input('Insira a afiliação do artigo que procura: ').strip().lower()
        for pub in data:
            if 'authors' in pub:
                for author in pub['authors']:
                    if "affiliation" in author.keys() and affiliation == author["affiliation"].strip().lower():
                        res.append(pub)
    elif filter == 'publish_date':
        ano = str(input('Insira o ano de publicação: '))
        mes = str(input('Insira o mês de publicação: '))
        dia = str(input('Insira o dia de publicação: '))
        publish_date = f"{ano}-{mes}-{dia}"
        for pub in data:
            if 'publish_date' in pub.keys():
                if publish_date == pub['publish_date']:
                    res.append(pub)
    elif filter == 'abstract':
        abstract = input('Insira o resumo do artigo que procura: ').strip().lower()
        for pub in data:
            if 'abstract' in pub:
                if abstract == pub['abstract'].strip().lower():
                    res.append(pub)
    elif filter == 'keywords':
        keyword = input('Insira a keyword do artigo que procura: ').strip().lower()
        for pub in data:
            if 'keywords' in pub:
                if keyword in pub['keywords'].strip().lower():
                    res.append(pub)
    else:
        res = consultar_pubs(data)
    if res == []:
        print("Nenhuma publicação encontrada.")
    else:
        for pub in res:
            consultar_pub(pub)
    return res


#CONSULTA PUBLICAÇÃO
def consultar_pub(pub):
    print("-"*100,
        "\nTítulo:", (pub['title'] if 'title' in pub.keys() else "N/A"),
        "\nResumo:", (pub['abstract'] if 'abstract' in pub.keys() else "N/A"),
        "\nPalavras-chave:", (pub['keywords'] if 'keywords' in pub.keys() else "N/A"),
        "\nAutores:"
    )
    i = 1
    if 'authors' in pub.keys():
        for author in pub['authors']:
            name = author['name']
            affiliation = author.get('affiliation', 'N/A')
            print(f"\n    {i} Name: {name}\n    Affiliation: {affiliation}")
            i += 1
    print("\nDOI:", (pub['doi'] if 'doi' in pub.keys() else "N/A"),
        "\nData de Publicação:", (pub['publish_date'] if 'publish_date' in pub.keys() else "N/A"),
        "\nURL:", (pub['url'] if 'url' in pub.keys() else "N/A"),
        "\nPDF:", (pub['pdf'] if 'pdf' in pub.keys() else "N/A"))
    return 


#ELIMINAR PUBLICAÇÃO
def eliminar_pub(data):
    pub = find_pub(data)
    if pub != None:
        data.remove(pub)
        print("Publicação eliminada.")
    return data

#LISTAR AUTORES
# PUBLICAÇÕES POR AUTOR (ORDENAÇÃO/ARTIGOS ASSOCIADOS AO AUTOR)
def listar_autores_alfabetica(data):
    autores = []
    for artigo in data:
        if "authors" in artigo.keys():
            for autor in artigo["authors"]:
                if autor["name"] not in autores:
                    autores.append(autor["name"])
    autores.sort()
    return autores

def listar_autores_frequencia(data):
    autores = {}
    for artigo in data:
        if "authors" in artigo.keys():
            for autor in artigo["authors"]:
                if autor["name"] not in autores.keys():
                    autores[autor["name"]] = 1
                else:
                    autores[autor["name"]] = autores[autor["name"]] + 1
    autores = list(autores.items())
    autores = sorted(autores, key= lambda x:x[1])
    autores = [(author[1], author[0]) for author in autores]
    return autores

def lista_artigos(nome_autor, data):
    artigos = []
    for artigo in data:
        if "authors" in artigo.keys():
            for autor in artigo["authors"]:
                if autor["name"].lower() == nome_autor.lower():
                    artigos.append(artigo)
    return artigos

def listar_autores(data):
    X = True
    while X:
        filter = input("Pretende listar os autores por ordem: [alfabetica/frequencia] ").strip().lower()
        if filter == 'alfabetica':
            authors = listar_autores_alfabetica(data)
            X = False
        elif filter == 'frequencia':
            authors = listar_autores_frequencia(data)
            X = False
        else:
            print("Opção inválida!")
    print("AUTORES:") 
    i = 1
    for author in authors:
        if type(author) == tuple:
            print(f"{i}. {author[0]}-{author[1]}")
        else:
            print(f"{i}.{author}")
        i += 1
    I = True
    while I:
        resp = input("Deseja consultar os artigos de um autor? [s/n]").strip().lower()
        if resp == 's':
            author = input("Insira o nome do autor: ")
            articles = lista_artigos(author, data)
            for article in articles:
                consultar_pub(article)
        elif resp == "n":
            I = False
        else:
            print("Opção inválida!")
    return

#ARMAZENAMENTO DE DADOS
def armazenamento(fnome, data):
    with open(fnome, "w", encoding= "utf-8") as file:
        json.dump(data, file)
    return

#ESTATÍSTICAS
#Distribuição de publicações por ano
def pub_ano(data):
    anos = []
    for artigo in data:
        if 'publish_date' in artigo:
            date = artigo['publish_date']
            partes = date.split('-')
            ano = int(partes[0])
            anos.append(ano)
    anos_dic = {}
    for ano in anos:
        if ano in anos_dic:
            anos_dic[ano] = anos_dic[ano] + 1
        else:
            anos_dic[ano] = 1
    anos_ordenados = sorted(anos_dic.keys())
    quantidade = [anos_dic[ano] for ano in anos_ordenados]
    plt.figure(figsize=(10, 6))
    plt.bar(anos_ordenados, quantidade, color='pink')
    plt.title('Distribuição de publicações por ano')
    plt.xlabel('Ano')
    plt.ylabel('Nº de publicações')
    plt.xticks(anos_ordenados, rotation=45)
    plt.tight_layout()
    plt.show()


#Distribuição de publicações por mês de um determinado ano
def pub_mes(data, ano_pretendido):
    meses = []
    for artigo in data:
        if 'publish_date' in artigo:
            date = artigo['publish_date']
            partes = date.split('-')
            ano = int(partes[0])
            if ano == ano_pretendido:
                mes = partes[1]
                meses.append(int(mes))
    meses_dic = {}
    for mes in meses:
        if mes in meses_dic:
            meses_dic[mes] = meses_dic[mes] + 1
        else:
            meses_dic[mes] = 1
    meses_ordenados = sorted(meses_dic.keys())
    quantidade = [meses_dic[mes] for mes in meses_ordenados]
    nomes_meses = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Maio', 6: 'Jun', 
                   7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dec'}
    labels = [nomes_meses[m] for m in meses_ordenados]
    plt.figure(figsize=(10, 6))
    plt.bar(meses_ordenados, quantidade, color='pink')
    plt.title(f'Distribuição de publicações por mês em {ano_pretendido}')
    plt.xlabel('Mês')
    plt.ylabel('Nº de publicações')
    plt.xticks(meses_ordenados, labels, rotation=45)
    if len(quantidade) == 1:
        plt.ylim(0, quantidade[0] + 1)
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))
    if len(meses_ordenados) == 1:
        plt.xlim(meses_ordenados[0] - 1.5, meses_ordenados[0] + 1.5)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.tight_layout()
    plt.show()


#Número de publicações por autor (top 20 autores)
def pub_top_autores(data):
    autores = []
    for artigo in data:
        if 'authors' in artigo:
            for autor in artigo['authors']:
                if 'name' in autor:
                    autores.append(autor['name'])
    autores_dic = {}
    for autor in autores:
        if autor in autores_dic:
            autores_dic[autor] = autores_dic[autor] + 1
        else:
            autores_dic[autor] = 1
    top_autores = sorted(autores_dic.items(), key=lambda x: x[1], reverse=True)[:20] #VER
    nomes = [autor[0] for autor in top_autores]
    quantidade = [autor[1] for autor in top_autores]
    plt.figure(figsize=(12, 8))
    plt.barh(nomes, quantidade, color='pink')
    plt.title('Nº de publicações por autor (top 20)')
    plt.xlabel('Nº de publicações')
    plt.ylabel('Autor')
    plt.gca().invert_yaxis() 
    plt.tight_layout()
    plt.show()


#Distribuição de publicações de um autor por anos
def pub_autor_ano(data, autor):
    anos = []
    for artigo in data:
        if 'authors' in artigo:
            for name_affiliation in artigo['authors']:
                if autor == name_affiliation['name']:
                    if 'publish_date' in artigo:
                        date = artigo['publish_date']
                        partes = date.split('-')
                        ano = int(partes[0])
                        anos.append(ano)
    anos_dic = {}
    for ano in anos:
        if ano in anos_dic:
            anos_dic[ano] = anos_dic[ano] + 1
        else:
            anos_dic[ano] = 1
    anos_ordenados = sorted(anos_dic.keys())
    quantidade = [anos_dic[ano] for ano in anos_ordenados]
    plt.figure(figsize=(10, 6))
    plt.bar(anos_ordenados, quantidade, color='pink')
    plt.title(f'Publicações de {autor}')
    plt.xlabel('Ano')
    plt.ylabel('Nº de publicações')
    plt.xticks(anos_ordenados, rotation=45)
    if len(quantidade) == 1:
        plt.ylim(0, quantidade[0] + 1)
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))
    if len(anos_ordenados) == 1:
        plt.xlim(anos_ordenados[0] - 1.5, anos_ordenados[0] + 1.5)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.tight_layout()
    plt.show()


#Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave)
def palavras_chave(data):
    keywords = []
    for artigo in data:
        if 'keywords' in artigo:
            for keyword in artigo['keywords'].split(', '):
                if keyword[-1] == ".":
                    keyword = keyword[:-1]  
                keywords.append(keyword)
    contagem = {}
    for keyword in keywords:
        if keyword in contagem:
            contagem[keyword] = contagem[keyword] + 1
        else:
            contagem[keyword] = 1
    palavras_ordenadas = sorted(contagem.items(), key=lambda x: x[1], reverse=True) #VER
    top_palavras = palavras_ordenadas[:20]
    palavras = [item[0] for item in top_palavras]
    frequencias = [item[1] for item in top_palavras]
    plt.figure(figsize=(12, 8))
    plt.barh(palavras, frequencias, color='pink')
    plt.title('Top 20 palavras-chave')
    plt.xlabel('Frequência')
    plt.ylabel('Palavras-chave')
    plt.gca().invert_yaxis() 
    plt.tight_layout()
    plt.show()


#Distribuição de palavras-chave mais frequente por ano
def palavras_chave_ano(data, ano_pretendido):
    artigos_ano = [artigo for artigo in data if 'publish_date' in artigo and str(ano_pretendido) in artigo['publish_date'][:4]]
    keywords = []
    for artigo in artigos_ano:
        if 'keywords' in artigo and artigo['keywords']:
            for keyword in artigo['keywords'].split(', '):
                if keyword[-1] == ".":
                    keyword = keyword[:-1]
                keywords.append(keyword)
    contagem_keywords = {}
    for keyword in keywords:
        if keyword in contagem_keywords:
            contagem_keywords[keyword] = contagem_keywords[keyword] + 1
        else:
            contagem_keywords[keyword] = 1
    keywords_usadas = sorted(contagem_keywords.items(), key=lambda x: x[1], reverse=True)
    if len(keywords_usadas) > 5:
        keywords_mais_usadas = keywords_usadas[:5]
    else:
        keywords_mais_usadas = keywords_usadas
    keywords = [item[0] for item in keywords_mais_usadas]
    frequencias = [item[1] for item in keywords_mais_usadas]
    plt.figure(figsize=(10, 6))
    plt.bar(keywords, frequencias, color='pink')
    plt.title(f'Top 5 keywords mais usadas em {ano_pretendido}', fontsize=14)
    plt.xlabel('Keywords', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
     


#IMPORTAR PUBLICAÇÕES
def importing(newfile, data):
    with open(newfile, encoding='utf-8') as f:
        new_data = json.load(f)
    if type(new_data) == list:
        count = 0
        for pub in new_data:
            if pub not in data:
                data.append(pub)
                count += 1
            else:
                print("A publicação já existe no dataset, por isso não foi importada.")
    else:
        print("O formato do informação no ficheiro é inválido.")
    print(f"Foram importadas {count} publicações.")
    return data


#PUBLICAÇÕES POR PALAVRA-CHAVE (ORDENAÇÃO/ARTIGOS ASSOCIADOS À PALAVRA)
def lista_keywords_alfabetica(data):
    keywords = []
    for artigo in data:
        if "keywords" in artigo.keys():
            keywords_artigo = artigo["keywords"].split(", ")
            for keyword in keywords_artigo:
                if keyword not in keywords:
                    keywords.append(keyword)
    keywords.sort()
    return keywords

def listar_keywords_frequencia(data):
    keywords = {}
    for artigo in data:
        if "keywords" in artigo.keys():
            keywords_artigo = artigo["keywords"].split(", ")
            for keyword in keywords_artigo:
                if keyword not in keywords.keys():
                    keywords[keyword] = 1
                else:
                    keywords[keyword] = keywords[keyword] + 1
    keywords = list(keywords.items())
    keywords = sorted(keywords, key= lambda x:x[1])
    keywords = [(keyword[1], keyword[0]) for keyword in keywords]
    return keywords

def lista_artigos_keywords(keyword, data):
    artigos = []
    for artigo in data:
        if "keywords" in artigo.keys() and keyword in artigo["keywords"]:
            artigos.append(artigo)
    return artigos


#CRIAR PUBLICAÇÃO
def publication(data, title, abstract, keywords, doi, authors, publish_date, url, pdf):
    pub = {}
    pub['abstract'] = abstract
    if keywords != None:
        pub['keywords'] = keywords
    pub['authors'] = authors
    pub['doi'] = doi
    pub['pdf'] = pdf
    if publish_date != None:
        pub['publish_date'] = publish_date
    pub['title'] = title
    pub['url'] = url
    encontrado = False
    for p in data:
        if p.get('doi') == doi or p.get('pdf') == pdf or p.get('url') == url:
            encontrado = True
    if not encontrado:       
        data.append(pub)
        sg.popup("A sua publicação foi adicionada.")
    else:
        sg.popup("A sua publicação já existe.")
    return data


#IMPORTAÇÃO DE PUBLICAÇÕES
def importar(fnome, data):
    with open(fnome, "r", encoding= "utf-8") as file:
        ficheiro = json.load(file)
    for artigo in ficheiro:
        data.append(artigo)
    return data


#JANELA CREATE
def abrir_janela_criar_pub(data): 
        font = ("Calibri", 12)
        authors = []
        keywords = []
        autores = []
        list_box_authors = sg.Listbox(autores, font=font, size=(20,5), expand_x=True, enable_events=True)
        list_box_keywords = sg.Listbox(keywords, font=font, size=(20,5), expand_x=True, enable_events=True)

        autor_layout = [[sg.Text('Author Name*:', font=font, size=(14,1)), sg.Input(key='name', expand_x=True, font=font)],
                        [sg.Text('Author Affiliation:', font=font, size=(14,1)), sg.Input(key='affiliation', expand_x=True, font=font)]]
        autor_layout_but = [[sg.Button("Add", font=("Calibri", 10), key="add_author", size=(4,3))]]

        layout =[[sg.Text('Title*:', font=font, size=(14,1)), sg.Input(key='title', size=(80,1), font=font)],
                 [sg.Text('Abstract*:', font=font, size=(14,1)), sg.Input(key='abstract', size=(80,1), font=font)],
                 [sg.Text('Keyword:', font=font, size=(14,1)), sg.Input(key='keyword', expand_x=True, font=font), sg.Button("Add", key="add_keyword", font=("Calibri", 10))],
                 [list_box_keywords, sg.Button("Remove", key="remove_keyword", font=("Calibri", 10), size=(8,6))],
                 [sg.Text('DOI*:', font=font, size=(14,1)), sg.Input(key='doi', size=(80,1), font=font)],
                 [[sg.Column(autor_layout, element_justification="left", expand_x=True),
                   sg.VSep(),
                   sg.Column(autor_layout_but, element_justification="right")]],
                 [list_box_authors, sg.Button("Remove", key="remove_author", font=("Calibri", 10), size=(8,6))],
                           [sg.Text('Publish Date:', font=font, size=(14,1)), sg.Input(key='date', expand_x=True, font=font, readonly=True, background_color="#FFD700", text_color="black"), sg.CalendarButton("Choose Date", size=(23,1), font=("Calibri", 10), format='%Y-%m-%d', close_when_date_chosen=True, target='date')],
                 [sg.Text('URL*:', font=font, size=(14,1)), sg.Input(key='url', size=(80,1), font=font)],
                 [sg.Text('PDF*:', font=font, size=(14,1)), sg.Input(key='pdf', size=(80,1), font=font)],
                 [sg.Button('Create', key='create', font=font, button_color=("#044343", "pink")), sg.Button('Cancel', key='cancel', font=font, button_color=("#044343", "pink")), sg.Push(), sg.Text("* = campos obrigatórios", font=("Calibri", 9))]
        ]

        janela_criar_pub = sg.Window(f"Criar nova publicação:", layout,
                                  modal=True, font=('Helvetica', 20),
                                  location=(200,50))
        
        stop = False
        while not stop:
            event,values = janela_criar_pub.read()
            if event == sg.WINDOW_CLOSED or event == 'cancel':
                stop = True

            elif event == 'add_keyword':
                keyword = values['keyword']
                if keyword == '':
                    sg.popup('Insira a keyword!')
                else:
                    if keyword not in keywords:
                        keywords.append(keyword)
                        list_box_keywords.update(keywords)
                    else:
                        sg.popup('Essa keyword já foi adicionada.')

            elif event == 'remove_keyword':
                try:
                    value = list_box_keywords.get()[0]
                    keywords.remove(value)
                    list_box_keywords.update(keywords)
                except Exception:
                    sg.popup('Selecione primeiro uma keyword para remover.')

            elif event == 'add_author':
                    name = values['name']
                    affiliation = values['affiliation']
                    if name == '':
                        sg.popup('Insira o nome do autor!')
                    elif affiliation == '':
                        author = {'name': name}
                        if author not in authors:
                            authors.append(author)
                            autores.append("name: " + name)
                            list_box_authors.update(autores)
                        else:
                            sg.popup('Esse autor já foi adicionado.')
                    else:
                        author = {'name': name, 'affiliation': affiliation}
                        if author not in authors:
                            authors.append(author)
                            autores.append("name: " + name + ", affiliation: " + affiliation)
                            list_box_authors.update(autores)
                        else:
                            sg.popup('Esse autor já foi adicionado.')

            elif event == 'remove_author':
                try:
                    value = list_box_authors.get()[0]
                    authors.remove(value)
                    list_box_authors.update(authors)
                except Exception:
                    sg.popup('Selecione primeiro um autor para remover.')
            
            elif event == 'create':
                if values['title'] == '':
                    sg.popup('Insira o título da publicação!')
                elif values['abstract'] == '':
                    sg.popup('Insira o resumo da publicação!')
                elif values['doi'] == '':
                    sg.popup('Insira o DOI da publicação!')
                elif values['url'] == '':
                    sg.popup('Insira a URL da publicação!')
                elif values['pdf'] == '':
                    sg.popup('Insira o PDF da publicação!')
                elif authors == []:
                    sg.popup('Insira pelo menos um autor!')
                else:
                    title = values['title']
                    abstract = values['abstract']
                    doi = values['doi']
                    url = values['url']
                    pdf = values['pdf']
                    if values['date'] == '':
                        date_pub = None
                    else:
                        date_pub = values['date']
                    if keywords == []:
                        str_keywords = None
                    else:
                        str_keywords = ', '.join(keywords)
                    data = publication(data, title, abstract, str_keywords, doi, authors, date_pub, url, pdf)
                    stop = True
        janela_criar_pub.close()
        return data

#JANELA CONSULTAR PUBLICAÇÃO
def abrir_janela_consultar_pub(dataset):
    font = ("Calibri", 12)
    filters = []
    results = []
    list_box_filters = sg.Listbox(values=filters, size=(80, 3), key='filters_list', enable_events=True, font=font)
    list_box_results = sg.Listbox(values=results, size=(20,25), expand_x=True, key='result_list', enable_events=True, font=font)
    layout = [
        [sg.Combo(['Title', 'Author (Name)','Author (Affiliation)' ,'Keyword','Publish Date'], key='search_filter', readonly=True, font=font), sg.InputText(key='search_value', font=font, expand_x=True), sg.Button('Add Filter', key='add_filter', font=("Calibri", 10))],
        [list_box_filters, sg.Button('Remove Filter', key='remove_filter', font=("Calibri", 10), size=(8,3))],
        [sg.Button('Pesquisar', key='search', font=("Calibri", 10), expand_x=True)],
        [list_box_results],
        [sg.Button('Export Results', key='export_results', font=("Calibri", 10), button_color=("#044343", "pink")), sg.Button('Cancelar', key='cancelar', font=("Calibri", 10), button_color=("#044343", "pink"))]
    ]

    janela_consultar_pub = sg.Window('Consultar Publicação', layout, modal=True, font=('Helvetica', 20), location=(0,0))

    stop = False
    while not stop:
        event, values = janela_consultar_pub.read()
        if event == sg.WINDOW_CLOSED or event == 'cancelar':
            stop = True
        elif event == 'add_filter':
            list_box_filters.update(filters)
            search_filter = values['search_filter']
            search_value = values['search_value'].lower()
            if not search_filter:
                sg.popup('Selecione um filtro para adicionar.')
            elif not search_value:
                sg.popup('Insira um valor para o filtro.')
            else:
                filter = (search_filter, ":", search_value)
                if filter not in filters:
                    filters.append(filter)
                    list_box_filters.update(filters)
                else:
                    sg.popup('Esse filtro já foi adicionado.')
        elif event == 'remove_filter':
            list_box_filters.update(filters)
            try:
                value = values['filters_list'][0]
                filters.remove(value)
                list_box_filters.update(filters)
            except IndexError:
                sg.popup('Selecione primeiro um filtro para remover.')
        elif event == 'search':
            results = dataset
            for search_filter, _, search_value in filters:
                if search_filter == 'Title':
                    results = [pub for pub in results if search_value == pub.get('title', '').lower()]
                elif search_filter == 'Author (Name)':
                    results = [pub for pub in results for author in pub.get('authors', []) if search_value == author.get('name', '').lower()]
                elif search_filter == 'Author (Affiliation)':
                    results = [pub for pub in results for author in pub.get('authors', []) if search_value == author.get('affiliation', '').lower()]
                elif search_filter == 'Keyword':
                    results_teste = results
                    results = []
                    for pub in results_teste:
                        if 'keywords' in pub.keys():
                            keywords = pub['keywords'].lower().strip().split(', ')
                            if search_value.lower() in keywords:
                                results.append(pub)
                elif search_filter == 'Publish Date':
                    results = [pub for pub in results if search_value == pub.get('publish_date', '').lower()]
            if not results:
                results = ['No results found.']
            list_box_results.update(results)
        elif event == 'result_list':
            if results and results[0] != 'No results found.':
                selected_pub = values['result_list'][0]
                janeladetalhes(selected_pub, dataset)
            else:
                sg.popup('Não existem publicações.')
        elif event == 'export_results':
            if results and results[0] != 'No results found.':
                filename = sg.popup_get_file('Escolha o nome do ficheiro para exportar os resultados', save_as=True, default_extension='.json')
                if filename:
                    armazenamento(filename, results)
            else:
                sg.popup('Não existem publicações para exportar.')
    janela_consultar_pub.close()
    return dataset

def janeladetalhes(selected_pub, data):
    authors = selected_pub.get("authors")
    author_elements = []
    for author in authors:
        author_elements.append([sg.Text("Name:"), sg.Text(author.get("name"))])
        author_elements.append([sg.Text("Affiliation:"), sg.Text(author.get("affiliation"))])
    layout_d = [[sg.Text("Title:"), sg.Text(selected_pub.get("title"))],
                        [sg.Text("Abstract:"), sg.Multiline(selected_pub.get("abstract"), size=(20,5), expand_x=True, disabled=True)],
                        [sg.Text("Keywords:"), sg.Text(selected_pub.get("keywords"))],
                        [sg.Text("Authors:")],
                        *author_elements,
                        [sg.Text("Publish Date:"), sg.Text(selected_pub.get("publish_date"))],
                        [sg.Text("DOI:"), sg.Text(selected_pub.get("doi"))],
                        [sg.Text("URL:"), sg.Text(selected_pub.get("url"))],
                        [sg.Text("PDF:"), sg.Text(selected_pub.get("pdf"))],
                        [sg.Button('Close', button_color=("#044343", "pink"), key="close"), sg.Button('Edit', button_color=("#044343", "pink"), key="Edit"), sg.Button('Delete', button_color=("#044343", "pink"), key="delete"), sg.Button('Export', button_color=("#044343", "pink"), key="export")],
    ]
    layout_detalhes = [[sg.Column(layout_d, scrollable=True, size=(1000, 500))]]
    janela_detalhes = sg.Window('Detalhes da Publicação', layout_detalhes, modal=True, location=(0,0))
    stop_consult = False
    while not stop_consult:
        event_detalhes, _ = janela_detalhes.read()
        if event_detalhes == sg.WINDOW_CLOSED or event_detalhes == 'close':
            stop_consult = True
        elif event_detalhes == 'export':
            filename = sg.popup_get_file('Escolha o nome do ficheiro para exportar a publicação', save_as=True, default_extension='.json')
            if filename:
                armazenamento(filename, selected_pub)
                sg.popup('Publicação exportada com sucesso.')
        elif event_detalhes == 'delete':
            confirm = sg.popup_yes_no('Tem a certeza que deseja eliminar esta publicação?')
            if confirm == 'Yes':
                data.remove(selected_pub)
                sg.popup('Publicação eliminada com sucesso! Para atualizar a lista de publicações, por favor, clique em pesquisar novamente.')
        elif event_detalhes == 'Edit':
            janela_detalhes.hide()
            authors = selected_pub.get('authors')
            autores = []
            for author in authors:
                name = author.get('name')
                affiliation = author.get('affiliation')
                if affiliation:
                    autores.append("name: " + name + ", affiliation: " + affiliation)
                else:
                    autores.append("name: " + name)
            keywords = selected_pub.get('keywords').split(', ') if selected_pub.get('keywords') else []
            list_box_authors = sg.Listbox(autores, expand_x=True, size=(40,3), enable_events=True)
            list_box_keywords = sg.Listbox(keywords, expand_x=True, size=(40,3), enable_events=True)

            layout_edit =[[sg.Text('Title:        '), sg.Input(selected_pub.get('title'),key='title')],
                    [sg.Text('Abstract:     '), sg.Input(selected_pub.get('abstract'),key='abstract')],
                    [sg.Text('Keywords:     '), sg.Input(key='keywords')],
                    [sg.Button("Add", key="add_keyword"), sg.Button("Remove", key="remove_keyword")],
                    [list_box_keywords],
                    [sg.Text('DOI:          '), sg.Input(selected_pub.get('doi'),key='doi')],
                    [sg.Text("Author")],
                    [sg.Text('Name:         '), sg.Input(key='name')],
                    [sg.Text('Affiliation:  '), sg.Input(key='affiliation')],
                    [sg.Button("Add", key="add_author"), sg.Button("Remove", key="remove_author")],
                    [list_box_authors],
                    [sg.Text('Publish Date: '), sg.Input(selected_pub.get("publish_date"), key='date', expand_x=True, readonly=True, background_color="#FFD700", text_color="black"), sg.CalendarButton("Choose Date", size=(23,1), font=("Calibri", 10), format='%Y-%m-%d', close_when_date_chosen=True)],
                    [sg.Text('URL:          '), sg.Input(selected_pub.get('url'),key='url')],
                    [sg.Text('PDF:          '), sg.Input(selected_pub.get('pdf'),key='pdf')],
                    [sg.Button('Save', button_color=("#044343", "pink")), sg.Button('Cancel', button_color=("#044343", "pink"))]
            ]
            janela_editar = sg.Window('Editar Publicação', layout_edit, modal=True)
            stop_edit = False
            while not stop_edit:
                event_editar, values_editar = janela_editar.read()
                if event_editar == sg.WINDOW_CLOSED or event_editar == 'Cancel':
                    stop_edit = True
                elif event_editar == 'add_keyword':
                    keyword = values_editar['keywords']
                    if keyword == '':
                        sg.popup('Insira a keyword!')
                    else:
                        if keyword not in keywords:
                            keywords.append(keyword)
                            list_box_keywords.update(keywords)
                        else:
                            sg.popup('Essa keyword já foi adicionada.')
                elif event_editar == 'remove_keyword':
                    try:
                        value = list_box_keywords.get()[0]
                        keywords.remove(value)
                        list_box_keywords.update(keywords)
                    except Exception:
                        sg.popup('Selecione primeiro uma keyword para remover.')
                elif event_editar == 'add_author':
                    name = values_editar['name']
                    affiliation = values_editar['affiliation']
                    if name == '':
                        sg.popup('Insira o nome do autor!')
                    elif affiliation == '':
                        author = {'name': name}
                        if author not in authors:
                            authors.append(author)
                            autores.append("name: " + name)
                            list_box_authors.update(authors)
                        else:
                            sg.popup('Esse autor já foi adicionado.')
                    else:
                        author = {'name': name, 'affiliation': affiliation}
                        if author not in authors:
                            authors.append(author)
                            autores.append("name: " + name + ", affiliation: " + affiliation)
                            list_box_authors.update(authors)
                        else:
                            sg.popup('Esse autor já foi adicionado.')
                elif event_editar == 'remove_author':
                    try:
                        value = list_box_authors.get()[0]
                        authors.remove(value)
                        list_box_authors.update(authors)
                    except Exception:
                        sg.popup('Selecione primeiro uma keyword para remover.')
                elif event_editar == 'Save':
                    keyword_str = ""
                    for keyword in keywords:
                        keyword_str = keyword_str + keyword + ", "
                    keyword_str = keyword_str[:-2]
                    selected_pub['title'] = values_editar['title']
                    selected_pub['abstract'] = values_editar['abstract']
                    selected_pub['keywords'] = keyword_str
                    selected_pub['doi'] = values_editar['doi']
                    selected_pub['authors'] = authors
                    selected_pub['publish_date'] = values_editar['date']
                    selected_pub['url'] = values_editar['url']
                    selected_pub['pdf'] = values_editar['pdf']
                    sg.popup('Publicação atualizada com sucesso! Para atualizar a lista de publicações, por favor, clique em pesquisar novamente.')
                    stop_edit = True
            janela_editar.close()
            janeladetalhes(selected_pub, data)
        janela_detalhes.close()
    return 

#JANELA DE PESQUISA DE AUTORES
def abrir_janela_pesquisar_autores(data):
    font = ("Calibri", 12)
    authors = []
    articles = []
    list_box_autores = sg.Listbox(values=authors, size=(70, 30), font=font, key="-AUTHOR-", enable_events=True)
    list_box_articles = sg.Listbox(values=articles, size=(70, 32), font=font, key="-ARTICLE-", enable_events=True)

    column1_layout = [
        [sg.Text('AUTORES', font=font)],
        [list_box_autores],
        [sg.Text("ORDENAÇÃO:", font=("Calibri", 10)), sg.Button('Alfabética', key='-ORDEMALFA-', font=font, button_color=("#044343", "pink")), sg.Button('Frequência', key='-FREQUENCIA-', font=font, button_color=("#044343", "pink"))]
    ]
    
    column2_layout = [[sg.Text('ARTIGOS', font=font)], 
                      [list_box_articles]]
    
    layout=[[sg.Column(column1_layout), 
             sg.VSep(),
             sg.Column(column2_layout)]]
    
    window = sg.Window('Pesquisar Autores', layout, modal=True, location=(0,0))

    stop = False
    while not stop:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close':
            stop = True
        elif event == '-ORDEMALFA-':
            authors = listar_autores_alfabetica(data)
            list_box_autores.update(authors)
        elif event == '-FREQUENCIA-':
            authors = listar_autores_frequencia(data)
            list_box_autores.update(authors)
        elif event == "-AUTHOR-":
            if authors != []:
                author = values["-AUTHOR-"][0]
                if type(author) == tuple:
                    author = author[1]
                articles = lista_artigos(author, data)
                list_box_articles.update(articles)
            else:
                sg.popup("Selecione uma forma de ordenação de autores.")
        elif event == "-ARTICLE-":
            if articles != []:
                article = values["-ARTICLE-"][0]
                janeladetalhes(article, data)
            else:
                sg.popup("Selecione um autor.")  
    window.close()

#LISTAR KEYWORDS
def abrir_janela_pesquisar_keywords(data):
    font = ("Calibri", 12)
    keywords = []
    articles = []
    list_box_keywords = sg.Listbox(values=keywords, size=(70, 30), font=font, key="-KEYWORD-", enable_events=True)
    list_box_articles = sg.Listbox(values=articles, size=(70, 32), font=font, key="-ARTICLE-", enable_events=True)

    column1_layout = [
        [sg.Text('KEYWORDS', font=font)],
        [list_box_keywords],
        [sg.Text("ORDENAÇÃO:", font=("Calibri", 10)), sg.Button('Alfabética', key='-ORDEMALFA-', font=font, button_color=("#044343", "pink")), sg.Button('Frequência', key='-FREQUENCIA-', font=font, button_color=("#044343", "pink"))]
    ]
    
    column2_layout = [[sg.Text('ARTIGOS', font=font)], 
                      [list_box_articles]]
    
    layout=[[sg.Column(column1_layout), 
             sg.VSep(),
             sg.Column(column2_layout)]]
    
    window = sg.Window('Pesquisar Keywords', layout, modal=True, location=(0,0))

    stop = False
    while not stop:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close':
            stop = True
        elif event == '-ORDEMALFA-':
            keywords = lista_keywords_alfabetica(data)
            list_box_keywords.update(keywords)
        elif event == '-FREQUENCIA-':
            keywords = listar_keywords_frequencia(data)
            list_box_keywords.update(keywords)
        elif event == "-KEYWORD-":
            if keywords != []:
                keyword = values["-KEYWORD-"][0]
                if type(keyword) == tuple:
                    keyword = keyword[1]
                articles = lista_artigos_keywords(keyword, data)
                list_box_articles.update(articles)
            else:
                sg.popup("Selecione uma forma de ordenação de keywords.")
        elif event == "-ARTICLE-":
            if articles != []:
                article = values["-ARTICLE-"][0]
                janeladetalhes(article, data) 
            else:
                sg.popup("Selecione uma keyword.") 
    window.close()


#JANELA DE SELEÇÃO DE ANO
def abrir_janela_ano(dataset):
    anos = []
    for artigo in dataset:
        if 'publish_date' in artigo:
            ano = int(artigo['publish_date'].split('-')[0])
            if ano not in anos:
                anos.append(ano)
    anos.sort()
    layout = [
        [sg.Text("Selecione o ano que quer analisar")],
        [sg.Listbox(anos, size=(20, len(anos)), key='-ANO-', enable_events=True)],
        [sg.Button("OK",button_color=("#044343", "pink")), sg.Button("Cancelar", button_color=("#044343", "pink"))]
    ]
    janela_ano = sg.Window("Selecionar Ano", layout)
    ano_selecionado = None 
    stop = False 
    while not stop:
        event, values = janela_ano.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            stop = True
        elif event == "OK":
            if values['-ANO-']:
                ano_selecionado = values['-ANO-'][0]
                stop = True
            else:
                sg.popup_error("Por favor, selecione um ano.")
    janela_ano.close()
    return ano_selecionado


#JANELA DE SELEÇÃO DE AUTOR
def abrir_janela_autor(dataset):
    autores = []
    for artigo in dataset:
        if 'authors' in artigo and 'publish_date' in artigo:
            for name_affiliation in artigo['authors']:
                autor = name_affiliation['name']  
                if autor not in autores:
                    autores.append(autor)
    autores.sort()
    layout = [
        [sg.Text("Selecione o autor que quer analisar")],
        [sg.Listbox(autores, size=(40, 20), key='-AUTOR-', enable_events=True)],
        [sg.Button("OK", button_color=("#044343", "pink")), sg.Button("Cancelar", button_color=("#044343", "pink"))]
    ]
    janela_autor = sg.Window("Selecionar Autor", layout)
    autor_selecionado = None
    stop = False 
    while not stop:
        event, values = janela_autor.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            stop = True
        elif event == "OK":
            if values['-AUTOR-']:
                autor_selecionado = values['-AUTOR-'][0]
                stop = True
            else:
                sg.popup_error("Selecione primeiro um autor.")
    janela_autor.close()
    return autor_selecionado


#JANELA DE SELEÇÃO DE ANO QUE TENHA KEYWORDS
def abrir_janela_ano_keywords(dataset):
    anos = []
    for artigo in dataset:
        if 'publish_date' in artigo and 'keywords' in artigo:
            ano = int(artigo['publish_date'].split('-')[0])
            if ano not in anos:
                anos.append(ano)
    anos.sort()
    layout = [
        [sg.Text("Selecione o ano que quer analisar")],
        [sg.Listbox(anos, size=(20, len(anos)), key='-ANO-', enable_events=True)],
        [sg.Button("OK",button_color=("#044343", "pink")), sg.Button("Cancelar", button_color=("#044343", "pink"))]
    ]
    janela_ano = sg.Window("Selecionar Ano", layout)
    ano_selecionado = None 
    stop = False 
    while not stop:
        event, values = janela_ano.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            stop = True
        elif event == "OK":
            if values['-ANO-']:
                ano_selecionado = values['-ANO-'][0]
                stop = True
            else:
                sg.popup_error("Por favor, selecione um ano.")
    janela_ano.close()
    return ano_selecionado
    

def abrir_janela_ajuda():
    help_text = """
    Bem-vindo ao sistema de gestão de publicações médicas!

    • File

    - Upload: Permite carregar um ficheiro de dados.

    - Import: Permite  importar novos registos dum outro ficheiro que 
                 tenha a mesma estrutura do ficheiro de suporte.

    - Save: Permite guardar as alterações feitas no dataset, no ficheiro
               inicialmente carregado.
                 
    - Save As: Permite exportar para um ficheiro à sua escolha todos os 
                    registos do dataset.
                 
    • Actions

    - Create: Permite criar uma nova publicação.

    - Delete: Permite eliminar uma publicação existente.

    - Edit: Permite editar uma publicação existente.

    
    • Search

    - Publications: Permite pesquisar publicações por título, autor, 
                         afiliação, data de publicação, resumo e palavras-chave.
                         Pode exportar os resultados da pesquisa para um 
                         ficheiro. 
                         Se desejar, pode ainda eliminar ou editar a publicação
                         pesquisada.


    - Authors: Permite listar os autores e aceder aos artigos de cada
                   autor da lista. Os autores aparecem ordenados pela
                   frequência dos seus artigos publicados e/ou por
                   ordem alfabética.

    - Keywords: Permite a pesquisa e visualização das palavras-chave do
                      dataset. As palavras-chave devem estar ordenadas
                      pelo seu número de ocorrências nos artigos e/ou
                      por ordem alfabética. O sistema deve também permitir
                      visualizar a lista das publicações associadas a cada
                      palavra-chave.

        - Export: Permite exportar a publicação selecionada para um
                      ficheiro.

        - Export results: Permite exportar os resultados da pesquisa 
                                para um ficheiro.

                      
    • Stats

    Permite a visalização das seguintes estatísticas:
    - Distribuição de publicações por ano;
    - Distribuição de publicações por mês de um determinado ano;
    - Número de publicações por autor (top 20 autores);
    - Distribuição de publicações de um autor por anos;
    - Distribuição de palavras-chave pela sua frequência (top 20 
    palavras-chave);
    - Distribuição de palavras-chave mais frequente por ano.
    """

    
    layout = [
        [sg.Text("Help", font=("Helvetica", 14))],
        [sg.Multiline(help_text, size=(60, 20), disabled=True, key="HELP_TEXT")], 
        [sg.Button("Close", button_color=("#044343", "pink"))]
    ]
    janela_ajuda = sg.Window("Help", layout, modal=True, keep_on_top=True)  
    stop = False
    while not stop:
        event_help, _ = janela_ajuda.read()
        if event_help in (sg.WINDOW_CLOSED, "Fechar"):
            stop = True  
    
    janela_ajuda.close()
