import PySimpleGUI as sg
import cv2
from cv2 import COLOR_BGR2GRAY

layout = [
    [sg.Image(key = '-IMAGE-')],
    [sg.Text('People in picture: 0', key = '-TEXT-', expand_x = True, justification = 'c')]    
]

window = sg.Window('Face Detector', layout)

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    event,values = window.read(timeout = 0)
    if event == sg.WIN_CLOSED:
        break

    _, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    imgbytes = cv2.imencode('.png',gray)[1].tobytes()
    window['-IMAGE-'].update(data = imgbytes)

window.close()