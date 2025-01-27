""" Functions to handle the audio """


import threading
from playsound import playsound
from Classes.path import Path


PATH = Path()
PATH.initiate()


def play_sound(sound, bool):
    """
    Plays the corresponding audio file if audio is enabled in the settings
    
    Args:
        sound (str): The name of the audio file
    """
    if bool:
        threading.Thread(target=lambda: playsound(f"{PATH.audio_dir}/{sound}.mp3")).start()
