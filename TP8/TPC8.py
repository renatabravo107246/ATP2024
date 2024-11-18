#8.1 listas em compreensão

# a) Lista formada pelos elementos que não são comuns às duas listas:

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
ncomuns = [x for x in lista1 + lista2 if x not in lista1 or x not in lista2]
print(ncomuns)

# b) Lista formada pelas palavras do texto compostas por mais de 3 letras:

texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = [x for x in texto.split() if len(x)>3]
print(lista)

# c) Lista formada por pares do tipo (índice, valor) com os valores da lista dada:
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(ind, valor) for ind, valor in enumerate(lista)] 
print(listaRes) 

#8.2

# a) Número de vezes em que a substring aparece na string, sem que haja sobreposição de substrings
def strCount(s, subs):
    n = 0
    i = 0
    while i <= len(s) - len(subs):
        if s[i:i+len(subs)] == subs:
            n = n + 1
            i = i + len(subs)
        else: 
            i = i + 1
    return n
print(strCount("catcowcat", "cat"))
print(strCount("catcowcat", "cow"))
print(strCount("catcowcat", "dog"))

# b) Produto dos 3 menores números
def produtoM3(lista):
    menores = [] 
    produto = 1
    while len(menores) < 3:
        menor = lista[0]
        for x in lista:
            if x < menor:
                menor = x
        menores.append(menor)
        lista.remove(menor)
    for x in menores:
        produto = produto * x
    return f"{produto} = {menores[0]} * {menores[1]} * {menores[2]}"
print(produtoM3([12,3,7,10,12,8,9]))

# c) Soma consecutiva dos dígitos 
def reduxInt(n):
    while n >= 10:
        soma = 0
        for digito in str(n):
            soma = soma + int(digito)
        n = soma
    return n
print (reduxInt(38))

# d) Índice da primeira ocorrência na string
def myIndexOf(s1, s2):
    i = 0
    resultado = -1
    while i <= len(s1) - len(s2):
        if s1[i:i+len(s2)] == s2:
            resultado = i
        i = i + 1
    return resultado
print(myIndexOf("Hoje está um belo dia de sol!", "belo"))
print(myIndexOf("Hoje está um belo dia de sol!", "chuva"))

#8.3 Rede Social

# a) Quantos posts estão registados
def quantosPost(redeSocial):
    return len(redeSocial)

# b) Lista de posts de um determinado autor
def postsAutor(redeSocial, autor):
    posts_do_autor = [post for post in redeSocial if post["autor"] == autor]
    return posts_do_autor

# c) Lista de autores de posts ordenada alfabeticamente
def autores(redeSocial): 
    lista= []
    for post in redeSocial:
        if "autor" in post:
            lista.append(post["autor"])
    lista.sort()
    return  lista

# d) Acrescentar novo post
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    id = f"p{len(redeSocial)+1}"
    post = {"id" : id, "conteudo" : conteudo, "autor" : autor, 'dataCriacao': dataCriacao, 'comentarios': comentarios}
    redeSocial.append(post)
    return redeSocial

# e) Remover um post consuante o ID
def remPost(redeSocial, id):
    return [post for post in redeSocial if post["id"] != id]

# f) Distribuição de posts por autor
def postsPorAutor(redeSocial):
    dist = {}
    for post in redeSocial:
        autor = post.get("autor")
        if autor in dist:
            dist[autor] = dist[autor] + 1
        else:
            dist[autor] = 1
    return dist

# g) Lista de posts comentados por um autor
def comentadoPor(redeSocial, autor):
    posts_comentados = []
    for post in redeSocial:
        if "comentarios" in post:
            for comentario in post["comentarios"]:
                if comentario.get("autor") == autor:
                   posts_comentados.append(post)
    return posts_comentados
