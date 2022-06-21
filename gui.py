from asyncio import subprocess
import tkinter as tk
from tkinter import font
from tkinter import filedialog
from threading import Thread
from turtle import color
import PySimpleGUI as sg
from subprocess import call

reference_path = ''
dataset_path = ''

def human_detection():
    call("python detect.py --source 0 --classes 0 --imgsz 96", shell=True)

def feature_matching():
    call("python orb_with_dataset.py", shell=True)

t1 = Thread(target=human_detection)
t2 = Thread(target=feature_matching)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
font1 = ("Arial", 20)
font2 = ("Arial", 16)
layout = [  [sg.Text('Human Detection & Feature Matching', font = font1)],
            #[sg.Text('Real-Time Human Detection', font = font)],
            [sg.Button("Choose Dataset Folder", size=(28,1), font = font2)],
            [sg.Button("Choose Reference Image", size=(28,1), font = font2)],

            [sg.Text('PATH:', font = font2, text_color = 'White'),
            sg.Text('', font = font2, key='path', text_color = 'Green')],

            [sg.Button('Detect', size=(13,1), font = font2), sg.Button('Cancel', size=(13,1), font = font2)] 
        ]

# Create the Window
window = sg.Window('Graduation Project', layout, element_justification='c')

input = window['path']

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Detect':
        if reference_path == '' and dataset_path == '':
            sg.Popup('Please choose a dataset folder or a reference image!', keep_on_top=True)
        else:
            # start the threads
            t2.start()
            t1.start()

            # wait for the threads to complete
            t2.join()
            t1.join()

    if event == 'Choose Dataset Folder':
        root = tk.Tk()
        root.withdraw()
        dataset_path = filedialog.askdirectory()
        reference_path = ''
        print('Dataset Folder path: ' + str(dataset_path))
        path_name = 'PATH: ' + str(dataset_path)
        input.update(value=dataset_path)

    if event == 'Choose Reference Image':
        root = tk.Tk()
        root.withdraw()
        reference_path = filedialog.askopenfilename()
        dataset_path = ''
        print('Reference Image path: ' + str(reference_path))
        input.update(value=reference_path)

window.close()