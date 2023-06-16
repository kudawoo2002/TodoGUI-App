import time
from functions import get_todos, write_todo

prompt = "Please type add, show, edit, complete or exit: "
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todo.txt")
        todos.append(todo + "\n")

        write_todo("todo.txt", todos)

    elif user_action.startswith("show"):

        todos = get_todos("todo.txt")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()
            number = user_action[5:]
            number = int(number) - 1
            new_todo = input("Please enter todo: ")
            todos[number] = new_todo

            write_todo("todo.txt", todos)

        except ValueError:
            print("Command is invalid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = user_action[9:]
            todos = get_todos("todo.txt")

            todos.pop(int(number) - 1)

            write_todo("todo.txt", todos)

        except IndexError:
            print("Tere's no item with that number!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is invalid!")

print("Bye!!")



