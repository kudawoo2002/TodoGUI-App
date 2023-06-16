import PySimpleGUI as sg
import functions

label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter a Todo", key="addBtn")
add_button = sg.Button("Add")

list_todos = sg.Listbox(values=functions.get_todos(), enable_events=True, size=(45, 10), key="todos")

edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_todos, edit_button]],
                   font=("Helvetica", 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value["addBtn"] + "\n"
            todos.append(new_todos)
            functions.write_todo(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todos = functions.get_todos()
            new_todo = value["todos"][0]
            print("new_todo", new_todo)
            index = todos.index(new_todo)
            todos[index] = value["addBtn"] + "\n"
            functions.write_todo(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["addBtn"].update(value=value['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()


