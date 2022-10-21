class ADN():
    # protein ADN data  to detect mutans
    def __init__(self): 
        self.proteina
    
    def set_proteinas(self, new_protein):
        self.proteina = new_protein
    
    def get_protein():
        return self.proteina
    
    def show_for_cmd():
        print(self.proteina)



def read_file(path_and_name_file: str):
    """read the input file and display the characters from the text
    param str path_and_name_file"""
    data = ADN()
    with open(path_and_name_file, "r", encoding = "utf-8") as file:
        for text_line in file:
             for characters in text_line:
                data.set_proteinas(characters)
    print(get_protein())
                                
        
def main():
    file_name: str = input("Input the name of the file and path: ")
    read_file(file_name)


if __name__ == '__main__':
    main()