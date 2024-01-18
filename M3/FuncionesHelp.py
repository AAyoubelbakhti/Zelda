from FuncionesPrompt import addToPrompt,clearPrompt,drawPrompt, prompt


def help_new_game():

    print("""
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
""")
    drawPrompt()

    user_input = input("Enter an action: ").lower()
    addToPrompt(user_input)

    # Verificamos si el jugador quiere volver a 'New Game'
    if user_input == "back":
        print("Going back to 'Set your name'...")
        new_game_menu()
    else:
        print("Invalid action. Type 'back' to return to 'Set your name'.")

def inventory_help():

    print("""
* Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*       Type 'show inventory main' to show the main inventory                 *
*            (main, weapons, Food)                                            *
*       Type 'eat X' to eat X, where X is a Food item                         *
*       Type 'Cook X' to Cook X, where X is a Food item                       *
*       Type 'equip X' to equip X, where X is a weapon                        *
*       Type 'unequip X' to unequip X, where X is a weapon                    *
*       Type 'back' now to go back to the 'Game'                              *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")
    drawPrompt()

    user_input = input("Enter 'back' to resume the game: ").lower()
    addToPrompt(user_input)

    if user_input == "back":
        print("going back to the game...")
        game()
    else:
        print("Invalid action. Type 'back' to resume the game.")


def main_menu_help():

    print("""
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
""")
    drawPrompt()
    user_input = input("Type 'back' to return to the main menu: ").lower()
    addToPrompt(user_input)

    if user_input == "back":
        print("Loading...")
        main()
    else:
        print("Invalid action. Type 'back' to return to the Main menu")

def saved_games_help():
    print("""
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
""")
    drawPrompt()
    user_input = input("Type 'back' to return to the main menu: ").lower()
    addToPrompt(user_input)

    if user_input == 'back':
        print("Going back to the Main menu...")
        main()
    else:
        print("Invalid action. Type 'back' to return to the main menu")

def about():
    print("""
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
""")
    drawPrompt()
    user_input = input("Type 'back' to return to the Main menu: ").lower()
    addToPrompt(user_input)

    if user_input == "continue":
        print("Loading...")
        main()
    else:
        print("Invalid action. Type 'back' to retunr to the game.")


