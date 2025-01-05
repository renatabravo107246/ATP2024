import PySimpleGUI as sg
import json
import projeto as mp
import threading

dataset = []

sg.theme('dark green 4')

menu_def = [["File", ["Upload", "Import", "Save","Save As"]],
            ["Actions", ["Create", "Delete", "Edit"]],
            ["Search", ["Publications", "Authors", "Keywords"]],
            ["Stats", ["Distribution of publications by year", 
                        "Distribution of publications by month", 
                        "Number of publications per author (top 20 authors)",
                        "Distribution of an author's publications by years",
                        "Number of publications per keyword (top 20 keywords)",
                        "Distribution of most frequent keyword per year"]],
            ["Help"]]

layout = [[sg.Menu(menu_def, font=("Helvetica", 8))],
          [sg.Text(text='Sistema de gestão de publicações médicas',
   font=('Arial Bold', 30),
   size=20,
   expand_x=True,
   justification='center',
   text_color='light pink',
   background_color=sg.theme_background_color())],
            [sg.HSep()],
            [sg.Output(size=(80, 20), key="-DADOS-", background_color="#044343", text_color="#044343")]]


window = sg.Window("Sistema de gestão de publicações médicas", layout, font=("Helvetica", 24), location=(0, 0), resizable = True).Finalize()
window.Maximize()


ficheiro = sg.popup_get_file("Selecione o ficheiro JSON",
                                     file_types=[("JSON Files", "*.json")])
if ficheiro:
        try:
            dataset = mp.loaddata(ficheiro)
            sg.popup_timed("Ficheiro carregado!", auto_close=True, auto_close_duration=5)
        except Exception as e:
            sg.popup_error(f"Erro ao carregar o arquivo: {e}")

stop = False

while not stop:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == sg.WIN_CLOSED:
        if dataset:
            response = sg.popup_yes_no("Deseja guardar as alterações antes de sair?", no_titlebar=True)
            if response == 'Yes':
                if ficheiro:
                    try:
                        mp.armazenamento(ficheiro, dataset)
                    except Exception as e:
                        sg.popup_error(f"Erro ao salvar o arquivo: {e}")
                else:
                    newfile = sg.popup_get_file("Selecione o ficheiro JSON",
                                        file_types=[("JSON Files", "*.json")], save_as=True)
                    if newfile:
                        try:
                            mp.armazenamento(newfile, dataset)
                            sg.popup_timed("Ficheiro salvo!", auto_close=True, auto_close_duration=5)
                        except Exception as e:
                            sg.popup_error(f"Erro ao salvar o arquivo: {e}")
    
        stop = True
    elif event == "Upload":
        if ficheiro:
            response = sg.popup_yes_no("Já carregou um ficheiro. Deseja trocar o ficheiro atual? Irá perder o seu progresso.", no_titlebar=True)
            if response == 'Yes':
                ficheiro = sg.popup_get_file("Selecione o ficheiro JSON",
                                             file_types=[("JSON Files", "*.json")], no_window=True)
                try:
                    if ficheiro:
                        dataset = mp.loaddata(ficheiro)
                        sg.popup_timed("Ficheiro carregado!", auto_close=True, auto_close_duration=5)
                except Exception as e:
                    sg.popup_error(f"Erro ao carregar o arquivo: {e}")
        else:
            ficheiro = sg.popup_get_file("Selecione o ficheiro JSON",
                                        file_types=[("JSON Files", "*.json")], no_window=True)
            try:
                if ficheiro:
                    dataset = mp.loaddata(ficheiro)
                    sg.popup_timed("Ficheiro carregado!", auto_close=True, auto_close_duration=5)
        
            except Exception as e:
                        sg.popup_error(f"Erro ao carregar o arquivo: {e}")
    elif event == "Create":
                try: 
                    dataset = mp.abrir_janela_criar_pub(dataset)
                except Exception as e:
                    sg.popup_error(f"Erro ao criar nova publicação: {e}")
    elif event == "Help":
                try:
                    mp.abrir_janela_ajuda()
                except Exception as e:
                    sg.popup_error(f"Erro ao abrir janela de ajuda: {e}")
    else:
        if dataset == []:
              sg.popup("Primeiro necessita de dar upload a um ficheiro.")
        else:
            if event == "Import":
                extrafile = sg.popup_get_file("Selecione o ficheiro JSON",
                                     file_types=[("JSON Files", "*.json")], no_window=True)

                try:
                    if extrafile:
                        data = mp.loaddata(extrafile)
                        if type(data) != list:
                            sg.popup("Ficheiro inválido.")
                        else:
                            count = 0
                            for i in data:
                                if i not in dataset:
                                    dataset.append(i)
                                else:
                                    count = count + 1
                            sg.popup_timed("Ficheiro importado!", auto_close=True, auto_close_duration=5)
                            if count != 0:
                                sg.popup(f"{count} publicações já existiam no dataset e não foram importadas.")
                except Exception as e:
                    sg.popup_error(f"Erro ao importar o arquivo: {e}")
            elif event == "Save":
                if ficheiro:
                        try:
                            mp.armazenamento(ficheiro, dataset)
                            sg.popup_timed("Ficheiro salvo!", auto_close=True, auto_close_duration=5)
                        except Exception as e:
                            sg.popup_error(f"Erro ao salvar o arquivo: {e}")
                else:
                        if dataset:
                            newfile = sg.popup_get_file("Selecione o ficheiro JSON",
                                                file_types=[("JSON Files", "*.json")], save_as=True)
                            if newfile:
                                try:
                                    mp.armazenamento(newfile, dataset)
                                    sg.popup_timed("Ficheiro salvo!", auto_close=True, auto_close_duration=5)
                                except Exception as e:
                                    sg.popup_error(f"Erro ao salvar o arquivo: {e}")
                        else:
                            sg.popup("Nenhum ficheiro carregado para salvar.")


            elif event == "Save As":
                newfile = sg.popup_get_file("Selecione o ficheiro JSON",
                                                file_types=[("JSON Files", "*.json")], save_as=True)
                if newfile:
                    try:
                        mp.armazenamento(newfile, dataset)
                        sg.popup_timed("Ficheiro salvo!", auto_close=True, auto_close_duration=5)
                    except Exception as e:
                        sg.popup_error(f"Erro ao salvar o arquivo: {e}")
            elif event == "Delete":
                sg.popup("Selecione a publicação que pretende eliminar.")
                dataset = mp.abrir_janela_consultar_pub(dataset)
            elif event == "Edit":
                sg.popup("Selecione a publicação que pretende editar.")
                dataset = mp.abrir_janela_consultar_pub(dataset)
            elif event == "Publications":
                try: 
                    dataset = mp.abrir_janela_consultar_pub(dataset)
                except Exception as e:
                    sg.popup_error(f"Erro ao editar publicação: {e}")
            elif event == "Authors":
                try:
                    mp.abrir_janela_pesquisar_autores(dataset)
                except Exception as e:
                    sg.popup_error(f"Erro ao pesquisar autores: {e}")
            elif event == "Keywords":
                try:
                    mp.abrir_janela_pesquisar_keywords(dataset)
                except Exception as e:
                    sg.popup_error(f"Erro ao pesquisar keywords: {e}")
            elif event == "Distribution of publications by year":
                try:
                    threading.Thread(target=mp.pub_ano, args=(dataset,), daemon=True).start()
                except Exception as e:
                    sg.popup_error(f"Erro ao criar gráfico: {e}")
                finally:
                    window.Maximize()
                    window.refresh()
            elif event == "Distribution of publications by month": 
                try:
                    ano = mp.abrir_janela_ano(dataset)
                    if ano:
                        threading.Thread(target=mp.pub_mes, args=(dataset, ano), daemon=True).start()
                except Exception as e:
                    sg.popup_error(f"Erro ao criar gráfico: {e}")
                finally:
                    window.Maximize()
                    window.refresh()
            elif event == "Number of publications per author (top 20 authors)":
                try:
                    threading.Thread(target=mp.pub_top_autores, args=(dataset,), daemon=True).start()
                except Exception as e:
                    sg.popup_error(f"Erro ao criar gráfico: {e}")
                finally:
                    window.Maximize()
                    window.refresh()
            elif event == "Distribution of an author's publications by years": 
                try:
                    autor = mp.abrir_janela_autor(dataset)
                    if autor:
                        threading.Thread(target=mp.pub_autor_ano, args=(dataset, autor), daemon=True).start()
                except Exception as e:
                    sg.popup_error(f"Erro ao criar gráfico: {e}")
                finally:
                    window.Maximize()
                    window.refresh()
            elif event == "Number of publications per keyword (top 20 keywords)":
                try:
                    threading.Thread(target=mp.palavras_chave, args=(dataset,), daemon=True).start()
                except Exception as e:
                    sg.popup_error(f"Erro ao criar gráfico: {e}")
                finally:
                    window.Maximize()
                    window.refresh()
            elif event == "Distribution of most frequent keyword per year":
                try:
                    ano = mp.abrir_janela_ano_keywords(dataset)
                    if ano:
                        threading.Thread(target=mp.palavras_chave_ano, args=(dataset, ano), daemon=True).start()
                except Exception as e:
                    sg.popup_error(f"Erro ao criar gráfico: {e}")
                finally:
                    window.Maximize()
                    window.refresh()
window.close()
