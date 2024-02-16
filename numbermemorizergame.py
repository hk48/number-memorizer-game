import PySimpleGUI as sg
import random
layout = [[sg.Button("GENERATE")], 
          [sg.Input(key='-GUESS-', do_not_clear=False)],
          [sg.Button("GUESS")],
          [sg.Text('Record:')], [sg.Text("", key='-WINS-')],]
def regen():
    #to do: let user pass number of digits
    gen = str(random.randrange(1, 9))
    return gen

wins = "" 
def winner(s):
    global wins
    for ele in s:
        wins += ele
    return wins

# Create the window
window = sg.Window("Number Memorizer Game", layout,grab_anywhere=True)

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
            winner("W ")
            window['-WINS-'].update(wins[::-1])
        else:
             sg.popup_timed("Wrong. Number was: ", gen)
             winner("L ")
             window['-WINS-'].update(wins[::-1])
             gen = regen()
    if event == sg.WIN_CLOSED:
        break

window.close()
