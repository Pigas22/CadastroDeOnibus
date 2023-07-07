import PySimpleGUI as sg

text_elem = sg.Text(size=(18, 1))

layout = [[sg.Text("Press a key or scroll mouse")],
          [text_elem],
          [sg.Button("OK")]]

window = sg.Window("Keyboard Test", layout,  return_keyboard_events=True, use_default_focus=False)

while True:
    event, value = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        print(event, "exiting")
        break
    text_elem.update(event)