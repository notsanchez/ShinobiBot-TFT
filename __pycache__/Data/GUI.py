import PySimpleGUI as sg
import webbrowser

new = 2;

url = "https://www.youtube.com/watch?v=J1Y-g-t2NzE"
url1 = "https://discord.gg/GTSCHYB"

# Layout
Layout = [
    [sg.Button('Discord', size=(20,5)), sg.Button('Tutorial', size=(20,5))],
    [],
    [],
    [sg.Button('Start', size=(15,5), )],
    [sg.Checkbox('Auto Login', key='marcou',)],

]

# Janela
janela = sg.Window('ShinobiBot', Layout, size=(500,500))
# Ler os eventos

while True:
    eventos, valores = janela.read()
    # Quando abrir o bot
    if eventos == 'Start':
        import main
        break
    # Quando Clicar no Tutorial
    if eventos == 'Tutorial':
        webbrowser.open(url, new=new);
    # Quando clicar no discord
    if eventos == 'Discord':
        webbrowser.open(url1, new=new);
    if eventos == 'Start' and 'Auto Login':
        print('SIM')
    if eventos == sg.WINDOW_CLOSED:
        break
