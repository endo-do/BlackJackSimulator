import yaml
from Classes.path import Path
from Functions.utilities import center_prompt


PATH = Path()


class Settings():
    def __init__(self):
        self.audio = True
        self.auto_bet = True
        self.keybinds = {
            "hit":["w", "up"],
            "stand":["s", "down"],
            "double":["d", "right"],
            "split":["a", "left"]
            }
        self.balance = 1000


    def load(self):
        with open(PATH.settings, "r") as f:
            settings = yaml.safe_load(f)
            self.audio = settings["GeneralSettings"]["audio"]
            self.auto_bet = settings["GeneralSettings"]["auto_bet"]
            self.delay = settings["GeneralSettings"]["delay"]
            self.balance = settings["Data"]["balance"]
            for bind in settings["Keybinds"]:
                self.keybinds[bind] = settings["Keybinds"][bind]


    def display_keybinds(self, offset=6):
        line = offset * " " + "¦"
        
        for bind in self.keybinds:
            line += center_prompt(f"[{'/'.join(self.keybinds[bind])}] - {bind}", 19) + "¦"
        
        print(line)
