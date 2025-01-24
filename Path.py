""" Path class """


import os


class Path():
    """
    Class to handle all internal paths.

    Args:
        settings (str): The path of the settings yaml.
        audio_dir (str): The path of the adio folder containing all the audio files.
    """
    def __init__(self):
        # paths in UserData


        # paths in GameData
        self.settings = r"GameData\\Settings.yml"
        self.audio_dir = r"GameData\\Audio"

    def initiate(self):
        """
        Add the path of the game folder to the internal paths.
        """
        # get game folder path
        dir = os.path.dirname(os.path.abspath(__file__))
        
        # iterate through every arg and add the game folder path
        for attr_name in vars(self):
            original_path = getattr(self, attr_name)
            setattr(self, attr_name, f"{dir}\\{original_path}")