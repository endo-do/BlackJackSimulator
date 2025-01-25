""" UI Class """


import os


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
        self.main_menu_options = "[1] - Freeplay\n[2] - Drill\n[3] - Settings"

    def get_banner(self, left="", middle="", right="", length=19):
        """
        Generates a banner with three brackets and automaticly equal padding

        Args:
            left (str, optional): The title of the left bracket of the banner. Defaults to "".
            middle (str, optional): The title of the middle bracket. Defaults to "".
            right (str, optional): The title of the right bracket. Defaults to "".
            length (int, optional): The total length of each bracket. Defaults to 19.

        Raises:
            ValueError: Raises error if a title exceeds the maximum bracket length.

        Returns:
            str: The generated banner.
        """
        banner = []
        
        for i in (left, middle, right):
        
            if len(i) > length:
                raise ValueError(f"The word '{i}' exceeds the maximum length of 19 chars")
            
            padding = length - len(i)
            right_padding = padding // 2
            left_padding = padding - right_padding
            banner.append(f"{" " * left_padding}{i}{" " * right_padding}")

        result = [self.border]
        result.append(f" |{banner[0]}¦{banner[1]}¦{banner[2]}| ")
        result.append(self.border)
        return "\n".join(result)


    def clear():
        """
        Clears the terminal using OS
        """
        os.system('cls' if os.name == 'nt' else 'clear')
