""" Main file """


from Classes.path import Path
from Classes.ui import UI as UserInterface
from Classes.freeplay import Freeplay
from Classes.drill import Drill
from Classes.settings import Settings
from Functions.user_input import get_input
from Functions.audio import play_sound


PATH = Path()
UI = UserInterface()
SETTINGS = Settings()
DRILL = Drill(SETTINGS, UI)
FREEPLAY = Freeplay(SETTINGS, UI)


if __name__ == "__main__":
    PATH.initiate()
    SETTINGS.load()
    play_sound("intro", SETTINGS.audio)

    while True:
        UI.set_banner(prompt_1="[e] exit", prompt_2=" [1] Freeplay", prompt_3=f"[2] Drill", prompt_4="[3] Settings", style_1="italic")
        UI.main()
        user_input = get_input()
        if user_input == "1": 
            play_sound("select", SETTINGS.audio)
            FREEPLAY.main()
