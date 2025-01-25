""" UI Class """


import os
from Functions.utilities import style_text

class UI:
    """
    UI Class to store all the UI elements

    Args:
        title (str): The title of the app in ascsii art
    """
    def __init__(self):
        self.title = """
         ____  _            _        _            _    
        |  _ \| |          | |      | |          | |   
        | |_) | | __ _  ___| | __   | | __ _  ___| | __
        |  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
        | |_) | | (_| | (__|   <  __| | (_| | (__|   < 
        |____/|_|\__,_|\___|_|\_\|___/ \__,_|\___|_|\_\ 
        """
        self.border = "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  "

    def print_banner(self, left="", middle="", right="", length=19, styles = ["normal", "normal", "normal"]):
        """
        Generates and prints a banner with three brackets and automaticly equal padding

        Args:
            left (str, optional): The title of the left bracket. Defaults to "".
            middle (str, optional): The title of the middle bracket. Defaults to "".
            right (str, optional): AThe title of the right bracket. Defaults to "".
            length (int, optional): The total length of each bracket. Defaults to 19.
            styles  (list, optional): A list containing the text styles of each title.
                                      Defaults to ["normal", "normal", "normal"]

        Raises:
            ValueError: Raises error if a title exceeds the maximum bracket length.
        """
        banner = []
        
        for index, i in enumerate((left, middle, right)):
        
            if len(i) > length:
                raise ValueError(f"The word '{i}' exceeds the maximum length of 19 chars")
            
            padding = length - len(i)
            right_padding = padding // 2
            left_padding = padding - right_padding
            i = style_text(i, styles[index])
            banner.append(f"{" " * left_padding}{i}{" " * right_padding}")

        print(self.border)
        print(f" |{banner[0]}¦{banner[1]}¦{banner[2]}| ")
        print(self.border)
        

    def print_title(self):
        """
        Prints the title
        """
        print(self.title)


    def clear(self):
        """
        Clears the terminal using OS
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    def print_user_options(self, options):
        """
        Prints a list of user options in a formatted menu.

        Args:
            options (list): The list in wich all the to be displayed options are stored.
        """
        print()
        for index, i in enumerate(options):
            print(f"[{index+1}] - {i}")
        print()
