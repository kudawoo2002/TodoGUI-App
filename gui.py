import PySimpleGUI as sg
import functions

label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter a Todo", key="addBtn")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, value = window.read()
    print(event)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value["addBtn"] + "\n"
            todos.append(new_todos)
            functions.write_todo(todos)
        case sg.WIN_CLOSED:
            break

window.close()


