import yaml
from Classes.path import Path
PATH = Path()


class Settings():
    def __init__(self):
        self.audio = True
        self.keybinds = {
            "hit":["w", "up"],
            "stand":["s", "down"],
            "double":["d", "right"],
            "split":["a", "left"]
            }


    def load(self):
        with open(PATH.settings, "r") as f:
            settings = yaml.safe_load(f)
            self.audio = settings["GeneralSettings"]["audio"]
            for bind in settings["Keybinds"]:
                self.keybinds[bind] = settings["Keybinds"][bind]


    def display_keybinds(self, offset=6):
        for bind in self.keybinds:
            print(f"{" " * offset}[{'/'.join(self.keybinds[bind])}] - {bind}")
