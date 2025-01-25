""" Main file """


from Path import Path
from UI import UI as UserInterface


PATH = Path()
UI = UserInterface()


if __name__ == "__main__":
    PATH.initiate()

    while True:
        UI.title()
        