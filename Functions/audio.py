""" Functions to handle the audio """


import threading
from playsound import playsound
from Classes.settings import Settings
from Classes.path import Path


SETTINGS = Settings()
PATH = Path()


PATH.initiate()
SETTINGS.load()


def play_sound(sound):
    """
    Plays the corresponding audio file if audio is enabled in the settings
    
    Args:
        sound (str): The name of the audio file
    """
    if SETTINGS.audio:
        threading.Thread(target=lambda: playsound(f"{PATH.audio_dir}/{sound}.mp3")).start()
