from distutils import text_file



def write_file(file_name, file_content):
    full_file_name = file_name + ".txt"
    with open(full_file_name, mode= "w") as text_file:
        text_file.write(file_content)

def append_file(file_name, file_content):
    full_file_name = file_name + ".txt"
    with open(full_file_name, mode= "a") as text_file:
        text_file.write(file_content)

def read_file(file_name):
    full_file_name = file_name + ".txt"
    with open(full_file_name, mode= "r") as text_file:
        content = text_file.read()
    return content
