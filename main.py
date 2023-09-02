from art import MINOTAURUS, GAME_OVER, MINOTAURUSBATTLE
print(MINOTAURUS)
print("Welcome to The Labyrinth.")
print("Your mission is to find and destroy the Minotaurus.") 
print("Good luck! You _WILL_ need it.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice = input("You are at the entrance of the labyrinth. Type 'ENTER' to continue.")
if choice == "ENTER" or choice == "Enter" or choice == "enter":
    choice = input("As you enter the labyrinth, you see a fork in the path. You see blood and entrails on the path leading to the right. Type 'LEFT' or 'RIGHT' to continue.")
    if choice == "LEFT" or choice == "Left" or choice == "left":
        choice = input("You walk down the left path and see a door. Type 'OPEN' to continue.")
        if choice == "OPEN" or choice == "Open" or choice == "open":
            print(MINOTAURUSBATTLE)
            choice = input("You open the door and see a Minotaurus. Type 'FIGHT' to continue.")
            if choice == "FIGHT" or choice == "Fight" or choice == "fight":
                choice = input("Which weapon do you choose? Type 'SWORD', 'AXE', 'SPEAR' to continue.")
                if choice == "SPEAR" or choice == "Spear" or choice == "spear":
                    input("You have chosen the spear.  The Minotaurus charges you as you brace the spear in the ground.  The Minotaurus impales itself on the spear and dies.  You have won the game. Type 'END' to continue.")
                elif choice == "SWORD" or choice == "Sword" or choice == "sword":
                    print(GAME_OVER)
                    print("You have chosen the sword.  The Minotaurus charges you as you swing the sword.  The Minotaurus is too fast and impales you with his horns. You died.")
                elif choice == "AXE" or choice == "Axe" or choice == "axe":
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
        print("You have chosen the wrong path and hear galloping behind you. You been killed by the Minotaurus.")
else:
    print(GAME_OVER)
    print("The Minotaurus charges out of the entrance and has killed you.")