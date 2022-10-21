import os

def read_file(path_and_name_file: str):
    """reading the input file and display the characters from the text, for create a list with every characters
    param str path_and_name_file
    return a list of the characters of the file or None"""
    try:
        data: list = []
        with open(path_and_name_file, "r", encoding = "utf-8") as file:
            for text_line in file:
                for characters in text_line:
                    data.append(characters)
        return data
    except FileNotFoundError as error:
        os.system("color 4")
        print("The name of the file is bad write or the file don't exist.")
        os.system("exit")

def search_timina(data: list):
    """looks at the last index of the list, and checks if it is a t
    param list data
    return true or false """
    amount_proteins: int = len(data)
    if data[amount_proteins - 1] == 't': return True
    else: return False  

def search_adeinas(list_data: list):
    """earch in the list, if there are two a's row 
    param list lista_data
    return true or false """
    count: int = 0
    for characters in list_data:
        if characters == 'a':
            count += 1
            if count >= 2: return True
        else: count = 0
    return False

def search_citosina(list_data: list):
    """search in the list, if there are two c's row 
    param list lista_data
    return true or false"""
    count: list = 0
    for characters in list_data:
        if characters == 'c':
            count += 1
            if count >= 2: return True
        else: count = 0
    return False

def search_guaninas(data_list: list):
    """search in the list, if there are three g's row
    param list data_list
    return True or false """
    count: int = 0
    for characters in data_list:
        if characters == 'g':
            count += 1
            if count >= 3: return False
        else: count = 0
    return True

def checks_mutant_or_human(data: list):
    if search_timina(data) == True and search_guaninas(data) and(search_adeinas(data) == True or search_citosina(data) == True):
        print("Mutant")
    else:
        print("Human")


def main():
    # execute the program, because is the principal function
    os.system("cls")
    os.system("color 7")
    file_name: str = input("Input the name of the file and path: ")
    proteinas: list = read_file(file_name)
    if len(proteinas) != 0: checks_mutant_or_human(proteinas)
    else:
        os.system("color 4")
        print("This file is empty, I can't work with this.")


if __name__ == '__main__':
    main()