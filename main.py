import os


def read_file(path_and_name_file: str):
    """reading the input file and display the characters from the text, for create a list with every character
    param str path_and_name_file
    return a list of the characters of the file or close the program"""
    try:
        data: list = []
        with open(path_and_name_file, "r", encoding="utf-8") as file:
            for text_line in file:
                for characters in text_line:
                    data.append(characters)
        return data
    except FileNotFoundError:
        os.system("color 4")
        print("The name of the file is bad write or the file don't exist.")
        os.system("exit")


def look_for_thymine(protein_list: list):
    """looks at the last index of the list, and checks if it is a t
    param list data
    return true or false """
    amount_proteins: int = len(protein_list)
    if protein_list[amount_proteins - 1] == 't':
        return True
    else:
        return False


def look_for_adenines(list_data: list):
    """Search in the list, if there are two a's row
    param list lista_data
    return true or false """
    count: int = 0
    for proteins in list_data:
        if proteins == 'a':
            count += 1
            if count >= 2:
                return True
        else:
            count = 0
    return False


def look_for_cytokines(protein_list: list):
    """search in the list, if there are two c's row 
    param list lista_data
    return true or false"""
    count: int = 0
    for protein in protein_list:
        if protein == 'c':
            count += 1
            if count >= 2:
                return True
        else:
            count = 0
    return False


def look_for_guanines(protein_list: list):
    """search in the list, if there are three g's row
    param list data_list
    return True or false """
    count: int = 0
    for type_protein in protein_list:
        if type_protein == 'g':
            count += 1
            if count >= 3:
                return False
        else:
            count = 0
    return True


def checks_mutant_or_human(proteins_list: list):
    # say if you are a mutant or human
    if look_for_thymine(proteins_list) is True and look_for_guanines(proteins_list) and \
            (look_for_adenines(proteins_list) is True or look_for_cytokines(proteins_list) is True):
        print("Mutant")
    else:
        print("Human")


def main():
    # execute the program, because is the principal function
    os.system("cls")
    os.system("color 7")
    file_name: str = input("Input the name of the file and path: ")
    proteins: list = read_file(file_name)
    if len(proteins) != 0:
        checks_mutant_or_human(proteins)
    else:
        os.system("color 4")
        print("The file is empty, I can't work with this.")


if __name__ == '__main__':
    main()
