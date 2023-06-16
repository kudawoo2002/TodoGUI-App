import PySimpleGUI as sg
import functions

label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter a Todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()

