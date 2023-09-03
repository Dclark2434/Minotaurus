# TODO: let's make this game a little more interesting.  Add more choices and more paths to the game.
# TODO: Functions.  I'm planning on making this code more modular.  Create functions for each path or maybe just the game over and victory screens and call them from the main function.

from art import MINOTAURUS, GAME_OVER, MINOTAURUSBATTLE, VICTORY
print(MINOTAURUS)
print("Welcome to The Labyrinth.")
print("Your mission is to find and destroy the Minotaurus.") 
print("Good luck! You _WILL_ need it.")

choice = input("You are at the entrance of the labyrinth. Type 'ENTER' to continue.\n").lower()
if choice == "enter":
    choice = input("As you enter the labyrinth, you see a fork in the path. You see blood and entrails on the path leading to the right. Type 'LEFT' or 'RIGHT' to continue.\n").lower()
    if choice == "left":
        choice = input("You walk down the left path and see a door. Type 'OPEN' to continue.\n").lower()
        if choice == "open":
            print(MINOTAURUSBATTLE)
            choice = input("You open the door and see the Minotaurus. Type 'FIGHT' to continue.\n").lower()
            if choice == "fight":
                choice = input("Which weapon do you choose? Type 'SWORD', 'AXE', 'SPEAR' to continue.\n").lower() # TODO: use dictionary for better readability.
                if choice == "spear":
                    print(VICTORY)
                    input("You have chosen the spear.  The Minotaurus charges you as you brace the spear in the ground.  The Minotaurus impales itself on the spear and dies.  CONGRATUALATIONS! You have won the game. Press ENTER to exit")
                elif choice == "sword":
                    print(GAME_OVER)
                    print("You have chosen the sword.  The Minotaurus charges you as you swing the sword.  The Minotaurus is too fast and impales you with his horns. You died.")
                elif choice == "axe":
                    print(GAME_OVER)
                    print("You have chosen the axe.  The Minotaurus charges you as you swing the axe.  The Minotaurus is too fast and impales you with his horns. You died.")
                else:
                    print(GAME_OVER)
                    print("Your inaction is costly. The Minotaurus grabs you and kills you.")           
            else:
                print(GAME_OVER)
                print("Your inaction is costly. The Minotaurus grabs you and kills you.")
        else:
            print(GAME_OVER)
            print("Your inaction is costly. The Minotaurus bursts through the door and has killed you.")
    else:
        print(GAME_OVER)
        print("You have chosen the wrong path and hear galloping behind you. You have been killed by the Minotaurus.")
else:
    print(GAME_OVER)
    print("The Minotaurus charges out of the entrance and has killed you.")
