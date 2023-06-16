
def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos


def write_todo(filepath, todo_arg):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)