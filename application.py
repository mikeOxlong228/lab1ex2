def citireFisier(fileName):
    with open(fileName, "r") as file:
        content = file.read()
    return content

file = citireFisier("data.txt")
print(file)

def eliminareSemnePunctuatie(file):
    new_s = ''.join([char for char in file if char not in ['.', '?', '!', ',', "'", '-', ';', ':']])
    return new_s

new_file = eliminareSemnePunctuatie(file)
print(new_file)
