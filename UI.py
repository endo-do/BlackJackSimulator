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
        ______  _               _       ___               _      _____  _                    _         _                
        | ___ \| |             | |     |_  |             | |    /  ___|(_)                  | |       | |               
        | |_/ /| |  __ _   ___ | | __    | |  __ _   ___ | | __ \ `--.  _  _ __ ___   _   _ | |  __ _ | |_   ___   _ __ 
        | ___ \| | / _` | / __|| |/ /    | | / _` | / __|| |/ /  `--. \| || '_ ` _ \ | | | || | / _` || __| / _ \ | '__|
        | |_/ /| || (_| || (__ |   < /\__/ /| (_| || (__ |   <  /\__/ /| || | | | | || |_| || || (_| || |_ | (_) || |   
        \____/ |_| \__,_| \___||_|\_\\____/  \__,_| \___||_|\_\ \____/ |_||_| |_| |_| \__,_||_| \__,_| \__| \___/ |_|   
        """

    def clear():
        """
        Clears the terminal using OS
        """
        os.system('cls' if os.name == 'nt' else 'clear')
