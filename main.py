from art import MINOTAURUS, GAME_OVER, MINOTAURUSBATTLE, VICTORY, GAME_OVER2, DOOR
import story_bits

#TODO: consider a utility function to handle the input and lower() it

def start_game():
    print(MINOTAURUS)
    print(story_bits.INTRO)
    
    choice = input(story_bits.CHOICE[0]).lower()
    if choice == "enter":
        labyrinth_entrails()
    else:
        game_over(story_bits.ENDING[0], GAME_OVER)

def labyrinth_entrails():
    choice = input(story_bits.CHOICE[1]).lower()
    if choice == "left":
        ancient_door()
    elif choice == "straight":
        game_over(story_bits.ENDING[1], GAME_OVER2)
    else:
        game_over(story_bits.ENDING[2], GAME_OVER)

def ancient_door():
    print(DOOR)
    choice = input(story_bits.CHOICE[2]).lower()
    if choice == "open":
        print(MINOTAURUSBATTLE)
        face_minotaurus()
    else:
        game_over(story_bits.ENDING[3], GAME_OVER)

def face_minotaurus():
    choice = input(story_bits.CHOICE[3]).lower()
    if choice == "fight":
        weapon_choice()
    else:
        game_over(story_bits.ENDING[4], GAME_OVER)

def weapon_choice():
    choice = input(story_bits.CHOICE[4]).lower()
    if choice == "spear":
        victory(story_bits.ENDING[5])
    elif choice == "sword":
        game_over(story_bits.ENDING[6], GAME_OVER)
    elif choice == "axe":
        game_over(story_bits.ENDING[7], GAME_OVER)
    elif choice == "bow":
        game_over(story_bits.ENDING[8], GAME_OVER)
    elif choice == "fist":
        victory(story_bits.ENDING[9])
    elif choice == "chainsaw":
        victory(story_bits.ENDING[10])
    else:
        game_over(story_bits.ENDING[11], GAME_OVER)

def game_over(message, art):
    print(art)
    print(message)

def victory(message):
    print(VICTORY)
    input(message)

if __name__ == "__main__":
    start_game()