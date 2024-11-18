def medias(t):
    res = []
    for dia in t:
        media = (dia[1] + dia[2]) / 2
        res.append((dia[0], media))    
    return res

def guardaTabMeteo(t, fnome):
    f = open(fnome, "w")
    for data, tmin, tmax, pluv in t:
        linha = f"{data[0]}::{data[1]}::{data[2]}::{tmin}::{tmax}::{pluv}\n"
        f.write(linha)
    f.close()
    return "Ficheiro guardado com sucesso!!"

def carregaTabMeteo(fnome):
    res = []
    f = open(fnome)
    for linha in f:
        if linha != "":
            campos = linha.split("::")
            data = (int(campos[0]), int(campos[1]), int(campos[2]))
            res.append((data, float(campos[3]), float(campos[4]), float(campos[5])))
    f.close()
    return res

def minMin(t):
    minima = t[0][1]
    for _,tmin,*_ in t[1:]:
        if tmin < minima:
            minima = tmin
    return minima

def amplTerm(t):
    res = []
    for dia in t:
        amp = dia[2] - dia[1]
        res.append((dia[0], amp))
    return res 

def maxChuva(t):
    maxp =t[0][3]
    maxd =t[0][0]
    for data,_,_,precip in t[1:]: 
        if maxp < precip:
            maxp = precip
            maxd = data
    return ((maxd, maxp))

def diasChuvosos(t):
    p = float(input("Insere o valor de x"))
    res = []
    for data,_,_,precip in t: 
        if precip > p:
            res.append([data, precip])
    return res

def maxPeriodoCalor(t):
    p = float(input("Insere o valor de x"))
    res = 0
    cons = 0
    for _,_,_,precip in t:
        if precip < p:
            res += 1
            if res > cons:
                cons = res
        else:
            res = 0
    return cons

def grafTabMeteo(t):
    import matplotlib.pyplot as plt

    # x dia
    # y temperaturas
    x1 = []
    y1 = []
    x2 = []
    y2 = [] 
    for data,tmin,tmax,_ in t:
        #Linha 1
        y1.append(int(tmin))
        x1.append(str(data))
        #linha2
        y2.append(int(tmax))
        x2.append(str(data))

    plt.xlabel('Data')
    plt.ylabel('Temperatura (ºC)')
    plt.title('Gráfico de temperaturas máxima e mínima')
    plt.plot(x1, y1, label = 'Linha 1 - Temperatura mínima', color='skyblue', marker='o')
    plt.plot(x2, y2, label="Linha 2 - Temperatura máxima", color='red', marker='o')
    plt.legend()
    plt.show()

    # x dia
    # y pluviosidade
    x1 = []
    y1 = []
    for data,_,_,pluv in t:
        y1.append(float(pluv))
        x1.append(str(data))

    plt.xlabel('Data')
    plt.ylabel('Pluviosidade')
    plt.title('Gráfico de pluviosidade')
    plt.plot(x1, y1)
    plt.legend()
    plt.show()
    return

def menu():
    print('''
    (1) Temperatura média diária
    (2) Guardar tabela em ficheiro
    (3) Carregar tabela a partir de um ficheiro
    (4) Temperatura mínima mais baixa registada na tabela
    (5) Amplitude térmica diária
    (6) Valor máximo de precipitação
    (7) Dias com precipitação superior a p
    (8) Maior nº consecutivo de dias com precipitação abaixo de p
    (9) Gráficos da temperatura mínima, máxima e de pluviosidade    
    (0) Sair
    ''')

def main():
    menu()
    op = int(input("Que opção desejas selecionar?"))
    tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 20), ((2022,1,22), 7, 17, 30)]
    while op != 0:
        if op == 1:
            print(medias(tabMeteo1))
        elif op == 2:
            print(guardaTabMeteo(tabMeteo1, "meteorologia.txt"))
        elif op == 3:
            print(carregaTabMeteo("meteorologia.txt"))
        elif op == 4:
            print(minMin(tabMeteo1))
        elif op == 5:
            print(amplTerm(tabMeteo1))
        elif op == 6:
            print(maxChuva(tabMeteo1))
        elif op == 7:
            print(diasChuvosos(tabMeteo1))
        elif op == 8:
            print(maxPeriodoCalor(tabMeteo1))
        elif op == 9:
            grafTabMeteo(tabMeteo1)
        input("Clica numa tecla para voltares ao menu")
        menu()
        op = int(input("Que opção desejas selecionar?"))

    if op == 0:
        print("Obrigada, volta sempre :)")

main()

        



