import glob

myfiles_paths = glob.glob("doc/*.*")

for file_path in myfiles_paths:

    with open(file_path, 'r') as file:
        data = file.read()
    print(data)