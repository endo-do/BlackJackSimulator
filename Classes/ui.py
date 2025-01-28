""" UI Class """


import os
from Functions.utilities import style_text
from Functions.utilities import center_prompt

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

    def print_banner(self, left_prompt="", middle_prompt="", right_prompt="",
                     left_style="normal", middle_style="normal", right_style="normal",
                     length=19, ):
        """
        Generates and prints a banner with three brackets and automaticly equal padding

        Args:
            left_prompt (str, optional): The title of the left bracket. Defaults to "".
            middle_prompt (str, optional): The title of the middle bracket. Defaults to "".
            right_prompt (str, optional): The title of the right bracket. Defaults to "".
            left_style (str, optional): The style of the left title. Defaults to 'normal'.
            middle_style (str, optional): The style of the middle title. Defaults to 'normal'.
            right_style (str, optional): The style of the right title. Defaults to 'normal'.
            length (int, optional): The total length of each bracket. Defaults to 19.
            

        Raises:
            ValueError: Raises error if a title exceeds the maximum bracket length.
        """
        banner = []
        styles = (left_style, middle_style, right_style)

        for index, prompt in enumerate((left_prompt, middle_prompt, right_prompt)):
        
            if len(prompt) > length:
                raise ValueError(f"The word '{prompt}' exceeds the maximum length of 19 chars")
            
            prompt = center_prompt(prompt, length)
            prompt = style_text(prompt, styles[index])
            banner.append(prompt)

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
