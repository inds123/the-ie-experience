from graphics import *
from button import Button

# Initial screen drawing

def titleScreen():
    # drawing the Title Screen
    win = GraphWin("Title screen", 500, 500)
    win.setCoords(-10, 10, 500, 500)
    win.setBackground("lightblue")
    welcome = Text(Point(250, 270), "Welcome to the IE Experience").draw(win)
    welcome.setFill("white")
    welcome.setSize(20)

    # graphic elements of welcome page
    pass

    # Explanation of the game (potentially we can also put this on the screen)
    print("In this minigame you will live the experience of an IE student.")
    print("You will be asked to complete a certain number of tasks to get through a day of classes successfully.")

    # Play button
    play_button = Button(win, Point(250, 220), 50, 20, "Play")
    play_button.activate()
    p = win.getMouse()

    if play_button.clicked(p):
        welcome.undraw()
        play_button.undraw()

    win.getMouse()
    win.close()
    
# Defining classes

# Defining a Player
class Player:
    def __init__(self, name, health, knowledge, will_to_live, hunger):
        self.name = name
        self.health = 40 
        self.knowledge = knowledge
        self.hunger = 40
        self.will_to_live = 40
        self.current_room = bedroom
        self.backpack = Backpack()

    def __str__(self):
        return f"Name: {self.name}"

    def get_status(self):
        return {
            "Health: ": self.health,
            "Knowledge: ": self.knowledge,
            "Will to live: ": self.will_to_live,
            "Hunger: ": self.hunger,
            "Location: ": self.current_room
        }

    # Defining basic functionalities of playerff
    # Each of the following must also check if the player is in the correct room
    # Also must handle cases where the player does not have the item in their backpack
    # Also must handle cases if status is full

    #Defining eating functionality where the players hunger decreases and the will_to_live increases, as its healthy food
    def eat_healthy(self):
        self.hunger = self.hunger - 20
        self.will_to_live = self.will_to_live + 10

# Functions we need
    # Defining eating functionality where the players hunger increases and the will_to_live decreases
    def eat_Junk(self):
        self.hunger = self.hunger + 20
        self.will_to_live = self.will_to_live - 10

    # Defining when the player goes ot the gym how the progress bars are affected (All 3 increase)
    def hit_Gym(self):
        self.health = self.health + 20
        self.will_to_live = self.will_to_live + 10
        self.hunger = self.hunger + 15
def main():
  from graphics import *
  # Initial screen drawing





  # Functions we need  
