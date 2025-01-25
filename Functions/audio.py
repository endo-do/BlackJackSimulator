import threading
from playsound import playsound
from Classes.settings import Settings
from Classes.path import Path
SETTINGS = Settings()
SETTINGS.load()
PATH = Path()
PATH.initiate()

def play_sound(sound):
    print(SETTINGS.audio)
    if SETTINGS.audio:
            threading.Thread(target=lambda: playsound(f"{PATH.audio_dir}/{sound}.mp3")).start()
