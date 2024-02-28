def citireFisier(fileName):
    with open(fileName, "r") as file:
        content = file.read()
    return content


def eliminareSemnePunctuatie(file):
    new_file = ''.join([char for char in file if char not in ['.', '?', '!', ',', "'", '-', ';', ':']])
    return new_file


def transformToUpper(file):
    new_file = file.upper()
    return new_file


def stergereNumere(file):
    new_s = ''.join([char for char in file if not char.isdigit()])
    return new_s


def main():
    file = citireFisier("data.txt")
    elimSemne = eliminareSemnePunctuatie(file)
    upperFile = transformToUpper(file)
    filefaraNumere = stergereNumere(file)
    print(f"Text file fara semne de punctuatie: {elimSemne}")
    print(f"Text file uppercase: {upperFile}")
    print(f"Text file fara numere: {filefaraNumere}")


if __name__ == "__main__":
    main()


