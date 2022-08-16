from config.definitions import ROOT_DIR
import keyboard as kb

class Character:
    
    def __init__(self):
        self.inventory = {
        "slot_1" : 0,
        "slot_2" : 0,
        "slot_3" : 0,
        "slot_4" : 0,
        "slot_5" : 0,
        }
        self.health = 100
        self.stamina = 100
        self.position = {
        "x" : 0,
        "y" : 0,
        }
        

    def walk(self,key_pressed = ""):
        if key_pressed == "w":
            self.position["y"] += 1
        elif key_pressed == "a":
            self.position["x"] -= 1
        elif key_pressed == "s":
            self.position["y"] -= 1
        elif key_pressed == "d":
            self.position["x"] += 1
        print(self.position, "Inventory:",self.inventory, "Health:",self.health, "Stamina:",self.stamina)
    
    def run(self,key_pressed = ""):
        if self.stamina > 0:
            if key_pressed == "w":
                self.position["y"] += 2
            elif key_pressed == "a":
                self.position["x"] -= 2
            elif key_pressed == "s":
                self.position["y"] -= 2
            elif key_pressed == "d":
                self.position["x"] += 2
            self.stamina -= 10
        else:
            print("You don't have enough stamina")
    
    def show_stats(self,key_pressed):
        if key_pressed == "i":
            print("Inventory:",self.inventory)
        elif key_pressed == "p":
            print("Position:", self.position)
        elif key_pressed == "q":
            print("Stats:\n","Health:",self.health,"\n","Stamina:",self.stamina,"\n")
            
            
            
player_1 = Character()
#hotkeys for walking:
kb.add_hotkey("w", lambda c="w": player_1.walk(c))
kb.add_hotkey("a", lambda c="a": player_1.walk(c))
kb.add_hotkey("s", lambda c="s": player_1.walk(c))
kb.add_hotkey("d", lambda c="d": player_1.walk(c))
#hotkeys for running:
kb.add_hotkey("shift+w", lambda c="w": player_1.run(c))
kb.add_hotkey("shift+a", lambda c="a": player_1.run(c))
kb.add_hotkey("shift+s", lambda c="s": player_1.run(c))
kb.add_hotkey("shift+d", lambda c="d": player_1.run(c))
#hotkeys for printing character stats, position etc.:
kb.add_hotkey("i", lambda c = "i": player_1.show_stats(c))
kb.add_hotkey("p", lambda c = "p": player_1.show_stats(c))
kb.add_hotkey("q", lambda c = "q": player_1.show_stats(c))


kb.wait("esc")

        