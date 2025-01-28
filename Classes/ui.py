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
        self.title = [
        " ____  _            _        _            _     ",
        "|  _ \| |          | |      | |          | |    ",
        "| |_) | | __ _  ___| | __   | | __ _  ___| | __ ",
        "|  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ / ",
        "| |_) | | (_| | (__|   <  __| | (_| | (__|   <  ",
        "|____/|_|\__,_|\___|_|\_\|___/ \__,_|\___|_|\_\ ",
        ""
        ]
        self.border = "      " + "~" * 81
        self.banner = []

    
    def main(self):
        self.clear()
        self.print_title()
        self.print_banner()

    
    def set_banner(self, prompt_1="", prompt_2="", prompt_3="", prompt_4="",
                     style_1="normal", style_2="normal", style_3="normal", style_4="normal",
                     length=19):
        """
        Generates and prints a banner with three brackets and automaticly equal padding

        Args:
            prompt_1 (str, optional): The title of the left bracket. Defaults to "".
            prompt_2 (str, optional): The title of the middle bracket. Defaults to "".
            prompt_3 (str, optional): The title of the right bracket. Defaults to "".
            style_1 (str, optional): The style of the left title. Defaults to 'normal'.
            style_2 (str, optional): The style of the middle title. Defaults to 'normal'.
            style_3 (str, optional): The style of the right title. Defaults to 'normal'.
            length (int, optional): The total length of each bracket. Defaults to 19.
            

        Raises:
            ValueError: Raises error if a title exceeds the maximum bracket length.
        """
        banner = []
        styles = (style_1, style_2, style_3, style_4)

        for index, prompt in enumerate((prompt_1, prompt_2, prompt_3, prompt_4)):
        
            if len(prompt) > length:
                raise ValueError(f"The word '{prompt}' exceeds the maximum length of 19 chars")
            
            prompt = center_prompt(prompt, length)
            prompt = style_text(prompt, styles[index])
            banner.append(prompt)

        display = []
        display.append(self.border)
        display.append(f"      |{banner[0]}¦{banner[1]}¦{banner[2]}|{banner[3]}|      ")
        display.append(self.border)

        self.banner = display
        

    def print_banner(self):
        """
        Prints the banner
        """
        for i in self.banner:
            print(i)

    
    def print_title(self):
        """
        Prints the title
        """
        for i in self.title:
            print(center_prompt(i, 93))


    def clear(self):
        """
        Clears the terminal using OS
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    def clear_lines(self, n):
        """
        Delete the last n lines in the terminal

        Args:
            n (int): amount of lines that should be cleared.
        """
        for _ in range(n):
            print("\033[F\033[K", end="")


    def print_user_options(self, options, offset=0):
        """
        Prints a list of user options in a formatted menu.

        Args:
            offset (int): Amount of offset at the left side.
            options (list): The list in wich all the to be displayed options are stored.
        """
        print()
        for index, i in enumerate(options):
            print(f"{" " * offset}[{index+1}] - {i}")
        print()
