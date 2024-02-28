def citireFisier(fileName):
    with open(fileName, "r") as file:
        content = file.read()
    return content

file = citireFisier("data.txt")
print(file)
