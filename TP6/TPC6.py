# Aplicação para gestão de alunos
# aluno = (nome, id, [notaTPC, notaProj, notaTeste ])
# turma = [aluno]

turma = []
def menu():
    print('''
    - 1: Criar uma turma;
    - 2: Inserir um aluno na turma;
    - 3: Listar a turma;
    - 4: Consultar um aluno por id;
    - 5: Guardar a turma em ficheiro;
    - 6: Carregar uma turma dum ficheiro;
    - 0: Sair da aplicação''')
    return

def criaTurma(turma):
    print("Preenche os seguintes dados:")
    N = int(input(("nº de alunos da turma:")))
    i = 1
    while i <= N:
        print(f"Dados Aluno {i}:")
        nome = input("nome:")
        id = input("id:")
        notaTPC = float(input("nota do TPC:"))
        notaProj = float(input("nota do projeto:"))
        notaTeste = float(input("nota do teste:"))
        aluno = (nome, id, [notaTPC, notaProj, notaTeste ])
        if aluno not in turma:
            turma.append(aluno)
            i = i + 1
        else:
            print("Esse aluno já está nesta turma. Insere um novo aluno.")
    return

def insereAluno(turma, aluno):
    if aluno not in turma:
        turma.append(aluno)
        print(f"O aluno {aluno[0]} foi adicionado à turma.")
    else:
        print("O aluno já está nesta turma.")
    input("Clica em qualquer tecla para voltares ao menu")
    return

def listaTurma(turma):
    if turma == []:
        print("A turma ainda não tem alunos")
    else:
        print("Turma")
        print("Nome | id | notaTPC | notaProj | notaTeste")
        for aluno in turma:
            print(f"{aluno[0]} | {aluno[1]}| {aluno[2][0]} | {aluno[2][1]} | {aluno[2][2]}")
    input("Clica em qualquer tecla para voltares ao menu")
    return

def consultaAluno(turma, idConsulta):
    control = False
    for aluno in turma:
        if idConsulta == aluno[1]:
            print(aluno)
            control = True
    if control == False:
        print("Aluno não encontrado.")
    input("Clica em qualquer tecla para voltares ao menu")
    return

def guardaTurma(turma):
    f = open("turmaficheiro.txt", "w")
    for aluno in turma:
        linha = f"{aluno[0]} | {aluno[1]}| {aluno[2][0]} | {aluno[2][1]} | {aluno[2][2]}\n"
        f.write(linha)
    f.close()
    print("A turma foi guardada no ficheiro turmaficheiro.txt")
    input("Clica em qualquer tecla para voltares ao menu")
    return

def carregaTurma(f1):
    novaturma = []
    ficheiro = open(f1, 'r')
    for linha in ficheiro:
        campos = linha.strip().split("|")
        novaturma.append((campos[0], campos[1], [float(campos[2]), float(campos[3]), float(campos[4])]))
    ficheiro.close()
    return novaturma

def sair():
    print("Obrigada! Volta sempre :)")
    return

def main():
    menu()
    op = int(input("Qual a opção que desejas selecionar?"))
    while op!= 0:
        if op == 1:
            criaTurma(turma)
        elif op == 2:
            print("Insere os dados do aluno que queres adicionar à turma:")
            nome = input("nome:")
            id = input("id:")
            notaTPC = float(input("nota do TPC:"))
            notaProj = float(input("nota do projeto:"))
            notaTeste = float(input("nota do teste:"))
            aluno = (nome, id, [notaTPC, notaProj, notaTeste ])
            insereAluno(turma, aluno)
        elif op == 3:
            listaTurma(turma)
        elif op == 4:
            idConsulta = input("Qual o id do aluno a consultar")
            consultaAluno(turma, idConsulta)
        elif op == 5:
            guardaTurma(turma)
        elif op == 6:
            f1 = input("Em que ficheiro se encontra a turma a carregar?")
            turma = carregaTurma(f1)
            print(turma)
            input("Clica em qualquer tecla para voltares ao menu")
        menu()
        op = int(input("Qual a opção que desejas selecionar?"))
    sair()
    return

main()