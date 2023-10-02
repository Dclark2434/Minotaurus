from art import MINOTAURUS, GAME_OVER, MINOTAURUSBATTLE, VICTORY, GAME_OVER2, DOOR

def game_over(message, art):
    print(art)
    print(message)

def victory(message):
    print(VICTORY)
    input(message)

def start_game():
    print(MINOTAURUS)
    print("Beyond the mists lies the Labyrinth of Desolation, a tortured construct of sorrow and stone.")
    print("Your purpose, a melancholic melody sung by the stars, is to seek and eradicate the twisted aberration: the Minotaurus.")
    print("Venture forth with trepidation, for this serpentine maze drips with the tears of the fallen and craves for more.")
    
    choice = input("The ancient, scarred gateway of the labyrinth beckons. Every brick seems to whisper tales of dread.\nSoftly, into the abyss, murmur 'ENTER' to descend into darkness.\n").lower()
    if choice == "enter":
        labyrinth_entrails()
    else:
        game_over("Even the maze's threshold proves treacherous. The Minotaurus ensures your tale is brief and bleak.")

def labyrinth_entrails():
    choice = input("Deep within the labyrinth's corroded veins, echoes of primordial massacres linger.\nTo your right, the ground weeps with age-old blood, echoing with the broken prayers of long-forgotten champions. \nDo you heed the mournful cries, murmuring 'LEFT'? Do you pivot 'RIGHT', chasing phantoms? Or do you stride 'STRAIGHT' into the chasm's embrace, ready to confront what malevolent forces await?\n").lower()
    if choice == "left":
        ancient_door()
    elif choice == "straight":
        game_over("In your descent into the void, the vast expanse of emptiness envelopes you.\nThe Minotaurus might elude sight, yet the labyrinth itself ensnares your soul, binding you in an unyielding, eternal captivity.", GAME_OVER2)
    else:
        game_over("The chilling resonance of hooves marks the prelude to darkness. The Minotaurus relishes in claiming yet another wandering soul.")

def ancient_door():
    print(DOOR)
    choice = input("An ancient door, its wood warped by screams of yesteryears, stands defiant.\nCan you muster the courage? Whisper 'OPEN' to face the shadows within.\n").lower()
    if choice == "open":
        print(MINOTAURUSBATTLE)
        face_minotaurus()
    else:
        game_over("Though the door remains unyielding, doom is ever-lurking. The Minotaurus, with a roar, marks your tragic end.")

def face_minotaurus():
    choice = input("The grotesque Minotaurus, an embodiment of torment, eyes you with bloodlust.\nWill you challenge fate and darkness alike? Let 'FIGHT' slip past your trembling lips to wage war.\n").lower()
    if choice == "fight":
        weapon_choice()
    else:
        game_over("Courage abandoned, you become yet another forgotten tale. The Minotaurus ensures your silence is eternal.")

def weapon_choice():
    choice = input("Dread hangs thick. Yet, salvation or doom hinges on your armament's choice.\nWhisper the dark anthem of your weapon: 'SWORD', 'AXE', 'SPEAR', 'BOW', 'FIST', or 'CHAINSAW'.\n").lower()
    if choice == "spear":
        victory("Grasping the spear, destiny's chosen tool, you brace as the Minotaurus lunges. It meets its cold end upon your instrument of fate.\nAmidst the labyrinthine despair, you are the solitary beacon of triumph. To depart this forsaken place, gently murmur 'DEPART' to the abyss.")
    elif choice == "sword":
        game_over("With the gleaming blade, you hope to rewrite fate. Yet the Minotaurus, in its cruel agility, ensures your aspirations crumble.\nThe cold steel of its horns introduce you to eternal night.")
    elif choice == "axe":
        game_over("The weighty axe promises power, but the Minotaurus' dance is one of deadly grace.\nIts horns find their home in your heart, ushering you into the void.")
    elif choice == "bow":
        game_over("With the somber bow of midnight's embrace, you notch an arrow woven from the very fabric of forgotten lamentations.\nYet as the shadowy missile seeks its mark, the Minotaurus, blessed by the dark void between two eternities, dances aside, ensuring your descent into an abyss of despair.")
    elif choice == "fist":
        victory("Your fists, bearing the weight of sins and salvations, pulse with a dark aura that seems birthed from the spaces between stars.\nEach blow is a symphony of both creation and cataclysm. Before such primordial might, the Minotaurus crumples, and the very walls of the labyrinth weep in reverence of your ethereal prowess.")
    elif choice == "chainsaw":
        victory("Awakening the chainsaw, its roar is a dirge echoing between heaven and hell. It feasts, not just on flesh, but on the very spirit of the Minotaurus.\nWhen the requiem of battle dwindles, you emerge, not just a victor, but as a bridge between two fires, unyielding and eternal.")
    else:
        game_over("In the face of horror, time waits not for indecision. Your end is swift, rendered by the merciless Minotaurus.")

if __name__ == "__main__":
    start_game()