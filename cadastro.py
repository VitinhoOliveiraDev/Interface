# Tela Em Python c/ PySimpleGUI
from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme("Reddit")
layout = [
    [sg.Text("Usuário"), sg.Input(key="usuario")],
    [sg.Text("Senha"), sg.Input(key="senha", password_char="*")],
    [sg.Checkbox("Salvar o login?")],
    [sg.Button("Entrar")],
]

# Janela
janela = sg.Window("Tela de login", layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":
        if valores["usuario"] == "victor" and valores["senha"] == "123456":
            print("Bem vindo a Dev Aprender!")
