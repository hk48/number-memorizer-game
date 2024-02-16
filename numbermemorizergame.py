import PySimpleGUI as sg
import random
wins = 0
layout = [[sg.Button("GENERATE")], 
          [sg.Input(key='-GUESS-', do_not_clear=False)],
          [sg.Button("GUESS")]]
generated7 = (str(random.randrange(1000000, 9999999)))
# Create the window

window = sg.Window("Number Memorizer Game", layout)

# Create an event loop
while True:
    event, values = window.read() 
    if event =="GENERATE":
        sg.popup_timed(generated7)
    if event == "GUESS":
        if values["-GUESS-"] == generated7:
            sg.popup_timed("Correct")
            generated7
        else:
             sg.popup_timed("wrong")


    if event == sg.WIN_CLOSED:
        break

window.close()
