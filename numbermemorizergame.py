import PySimpleGUI as sg
import random
layout = [[sg.Button("GENERATE")], 
          [sg.Input(key='-GUESS-', do_not_clear=False)],
          [sg.Button("GUESS")]]
def regen():
    gen = str(random.randrange(1000000, 9999999))
    return gen

# Create the window
window = sg.Window("Number Memorizer Game", layout)

# Create an event loop
while True:
    event, values = window.read() 
    if event =="GENERATE":
        gen = regen()
        sg.popup_timed(gen)
        str(gen)
    if event == "GUESS":
        if values["-GUESS-"] == gen:
            sg.popup_timed("Correct")
            regen()
        else:
             sg.popup_timed("wrong")
    if event == sg.WIN_CLOSED:
        break

window.close()
