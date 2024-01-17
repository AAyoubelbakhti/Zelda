
def help_new_game():
    messages = []

    help_menu_text = """
* Help,new game * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*       When asked, type your name and press enter                            *
*       if 'Link' is fine for you, just press enter                           *
*                                                                             *
*       Name must be between 3 and 10 characters long and only                *
*       letters, numbers and spaces are allowed                               *
*                                                                             *
*       Type 'back' now to go back to 'Set your name'                         *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

    messages.append(help_menu_text)
    user_input = input("Enter an action: ").lower()

    # Verificamos si el jugador quiere volver a 'New Game'
    if user_input == "back":
        messages.append("Going back to 'Set your name'...")
    else:
        messages.append("Invalid action. Type 'back' to return to 'Set your name'.")
    
    return messages

def inventory_help():
    messages = []


    help_menu_text= """
* Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*       Type 'show inventory main' to show the main inventory                 *
*            (main, weapons, Food)                                            *
*       Type 'eat X' to eat X, where X is a Food item                         *
*       Type 'Cook X' to Cook X, where X is a Food item                       *
*       Type 'equip X' to equip X, where X is a weapon                        *
*       Type 'unequip X' to unequip X, where X is a weapon                    *
*       Type 'back' now to go back to the 'Game'                              *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""


    messages.append(help_menu_text)
    user_input = input("Enter 'back' to resume the game: ").lower()


    if user_input == "back":
        messages.append("going back to the game...")
    else:
        messages.append("Invalid action. Type 'back' to resume the game.")

    return messages

def main_menu_help():
    messages = []

    help_menu_text = """
* Help, main menu * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*       Type 'continue' to continue a saved game                              *
*       Type 'new game' to start a new game                                   *
*       Type 'about' to see information about the game                        *
*       Type 'exit' to exit the game                                          *
*                                                                             *
*                                                                             *
*       Type 'back' now to go back to the 'Main menu'                         *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

    messages.append(help_menu_text)
    user_input = input("Type 'back' to return to the main menu: ").lower()


    if user_input == "back":
        messages.append("Loading...")
    else:
        messages.append("Invalid action. Type 'back' to return to the Main menu")
    
    return messages


def saved_games_help():
    messages = []

    help_menu_text = """
* Help, saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*                                                                             *
*                                                                             *
*       Type 'play X' to continue playing the game 'X'                        *
*       Type 'erase X' to erase the game 'X'                                  *
*       Type 'back' now to go back to the main menu                           *
*                                                                             *
*                                                                             *
*                                                                             *
*       Type 'back' now to go back to 'Saved games'                           *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

    messages.append(help_menu_text)
    user_input = input("Type 'back' to return to the main menu: ").lower()

    if user_input == 'back':
        messages.append("Going back to the Main menu...")
    else:
        messages.append("Invalid action. Type 'back' to return to the main menu")
    
    return messages

def about():
    messages = []

    about_menu_text= """
* About * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             * 
*       Game developed by Team 3, The Link of Zelda :                         *
*                                                                             *
*                                                                             *
*            Ayoub El Bakhti                                                  *
*            Daniel Hirsch                                                    *
*            Denis Fernández                                                  *
*                                                                             *
*                                                                             *
*       Type 'back' now to go back to the 'Main menu'                         *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

    messages.append(about_menu_text)
    user_input = input("Type 'back' to return to the Main menu: ").lower()


    if user_input == "continue":
        messages.append("Loading...")
    else:
        messages.append("Invalid action. Type 'back' to retunr to the game.")

    return messages
