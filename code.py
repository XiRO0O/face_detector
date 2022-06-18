import PySimpleGUI as sg

layout = [
    [sg.Image(key = '-IMAGE-')],
    [sg.Text('People in picture: 0', key = '-TEXT-', expand_x = True, justification = 'c')]    
]

window = sg.Window('Face Detector', layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()