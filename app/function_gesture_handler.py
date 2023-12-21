
from game.game import Game
from lists.gestures_list import list_gesture

from utils import *


async def gesture_handler(game: Game, gesture:str):
    print(f"Gesture received: {gesture}")
    name_of_gesture = gesture["recognized"][1]
    confidence = gesture["confidence"].replace(",", ".")
    if float(confidence) < 0.7:
        game.tts(random_not_understand())
    elif name_of_gesture in list_gesture:
        if name_of_gesture == "HANDRIGHTUPHELP":
            game.help()
        elif name_of_gesture == "HANDSUPGIVEUP":
            game.give_up_game()
        elif name_of_gesture == "HANDSFRONTSELECT":
            game.join_game()
        elif name_of_gesture == "HANDLEFTSHOULDERLEVELDECREASE":
            game.change_color_number(number=1, increase=False)
        elif name_of_gesture == "HANDRIGHTSHOULDERLEVELINCREASE":
            game.change_color_number(number=1, increase=True)
        elif name_of_gesture == "HANDSDIFFERENTDIRECTIONSCLOSE":    
            game.end_turn()
        elif name_of_gesture == "HANDONEDIRECTIONROLLDICE":
            game.roll_dice()
    else:
        game.tts(random_not_understand_the_gesture())
        print(f"Command not found: {gesture}")