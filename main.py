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
DRILL = Drill(SETTINGS)
FREEPLAY = Freeplay(SETTINGS)


if __name__ == "__main__":
    PATH.initiate()
    SETTINGS.load()
    play_sound("intro", SETTINGS.audio)

    while True:
        UI.clear()
        UI.print_title()
        UI.print_banner(left_prompt="[e] - exit", middle_prompt="Main Menu", left_style="italic", middle_style="bold")
        UI.print_user_options(["Freeplay", "Drill", "Settings"])
        user_input = get_input()
        if user_input == "1": 
            FREEPLAY.main()            
