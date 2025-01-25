""" Main file """


from Classes.path import Path
from Classes.ui import UI as UserInterface
from Functions.user_input import get_input
from Functions.audio import play_sound
from Classes.game import Freeplay
from Classes.game import Drill
from Classes.settings import Settings


PATH = Path()
UI = UserInterface()
FREEPLAY = Freeplay()
DRILL = Drill()
SETTINGS = Settings()


if __name__ == "__main__":
    PATH.initiate()
    SETTINGS.load()
    play_sound("intro")
    input()

    while True:
        UI.clear()
        UI.print_title()
        UI.print_banner(left="[e] - exit", middle="Main Menu", styles=["italic", "bold", "normal"])
        UI.print_user_options(["Freeplay", "Drill", "Settings"])
        user_input = get_input()
        if user_input == "1": 
            FREEPLAY.main()