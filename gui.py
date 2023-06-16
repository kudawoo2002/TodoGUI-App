import PySimpleGUI as sg
import functions
import time

clock = sg.Text("", key="clock")
label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter a Todo", key="addBtn")
add_button = sg.Button("Add")

list_todos = sg.Listbox(values=functions.get_todos(), enable_events=True, size=(45, 10), key="todos")

edit_button = sg.Button("Edit")

complete_btn = sg.Button("Complete")

exit_btn = sg.Button('Exit')

window = sg.Window("My To-Do App",
                   layout=[[clock],[label], [input_box, add_button], [list_todos, edit_button, complete_btn],[exit_btn]],
                   font=("Helvetica", 20))

while True:
    event, value = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value["addBtn"] + "\n"
            todos.append(new_todos)
            functions.write_todo(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todos = functions.get_todos()
                new_todo = value["todos"][0]
                print("new_todo", new_todo)
                index = todos.index(new_todo)
                todos[index] = value["addBtn"]
                functions.write_todo(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select and item from the listbox")

        case "todos":
            window["addBtn"].update(value=value['todos'][0])
        case "Complete":
            try:
                todo_complete = value["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.write_todo(todos)
                window["todos"].update(values=todos)
                window["addBtn"].update(value="")
            except IndexError:
                sg.popup("Please select and item from the listbox")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()


