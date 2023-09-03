# TODO: let's make this game a little more interesting.  Add more choices and more paths to the game.
# TODO: Functions.  I'm planning on making this code more modular.  Create functions for each path or maybe just the game over and victory screens and call them from the main function.

from art import MINOTAURUS, GAME_OVER, MINOTAURUSBATTLE, VICTORY

print(MINOTAURUS)
print("Beyond the mists lies the Labyrinth of Desolation, a tortured construct of sorrow and stone.")
print("Your purpose, a melancholic melody sung by the stars, is to seek and eradicate the twisted aberration: the Minotaurus.")
print("Venture forth with trepidation, for this serpentine maze drips with the tears of the fallen and craves for more.")

choice1 = input("The ancient, scarred gateway of the labyrinth beckons. Every brick seems to whisper tales of dread. Softly, into the abyss, murmur 'ENTER' to descend into darkness.\n").lower()

if choice1 == "enter":
    choice2 = input("The labyrinth's entrails unfurl a grim tableau. To your right, a path soaked with blood, littered with fragments of hope long lost. Do you defy the gore and whisper 'LEFT', or is the macabre allure of 'RIGHT' too strong to resist?\n").lower()
    if choice2 == "left":
        choice3 = input("An ancient door, its wood warped by screams of yesteryears, stands defiant. Can you muster the courage? Whisper 'OPEN' to face the shadows within.\n").lower()
        if choice3 == "open":
            print(MINOTAURUSBATTLE)
            choice4 = input("The grotesque Minotaurus, an embodiment of torment, eyes you with bloodlust. Will you challenge fate and darkness alike? Let 'FIGHT' slip past your trembling lips to wage war.\n").lower()
            if choice4 == "fight":
                choice5 = input("Dread hangs thick. Yet, salvation or doom hinges on your armament's choice. Whisper the dark anthem of your weapon: 'SWORD', 'AXE', or 'SPEAR'.\n").lower()
                if choice5 == "spear":
                    print(VICTORY)
                    input("Grasping the spear, destiny's chosen tool, you brace as the Minotaurus lunges. It meets its cold end upon your instrument of fate. Amidst the labyrinthine despair, you are the solitary beacon of triumph. To depart this forsaken place, gently murmur 'DEPART' to the abyss.\n")
                elif choice5 == "sword":
                    print(GAME_OVER)
                    print("With the gleaming blade, you hope to rewrite fate. Yet the Minotaurus, in its cruel agility, ensures your aspirations crumble. The cold steel of its horns introduce you to eternal night.")
                elif choice5 == "axe":
                    print(GAME_OVER)
                    print("The weighty axe promises power, but the Minotaurus' dance is one of deadly grace. Its horns find their home in your heart, ushering you into the void.")
                else:
                    print(GAME_OVER)
                    print("In the face of horror, time waits not for indecision. Your end is swift, rendered by the merciless Minotaurus.")
            else:
                print(GAME_OVER)
                print("Courage abandoned, you become yet another forgotten tale. The Minotaurus ensures your silence is eternal.")
        else:
            print(GAME_OVER)
            print("Though the door remains unyielding, doom is ever-lurking. The Minotaurus, with a roar, marks your tragic end.")
    else:
        print(GAME_OVER)
        print("The chilling resonance of hooves marks the prelude to darkness. The Minotaurus relishes in claiming yet another wandering soul.")
else:
    print(GAME_OVER)
    print("Even the maze's threshold proves treacherous. The Minotaurus ensures your tale is brief and bleak.")