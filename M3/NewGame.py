def get_player_name(player_name):
    messages = []
    while True:
        name_input= input(f"Whats your name {player_name}? ")

        if not name_input: #En caso de que el jugador no ponga nada le dejaremos "Link" por defecto
            return messages, "Link"
        
        if name_input.lower == "back":
            messages.append("Going back to the Main menu...")
            return messages, None
        
        if name_input.isalnum() or name_input.isspace():
            return messages, name_input
        
        else:
            messages.append(f"{name_input} is not a valid name")

def new_game_menu(player_name):
    messages = []

    new_game_menu_text = f"""
* New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*       Set your name ({player_name})?                                        *
*                                                                             *
*                                                                             *
*                                                                             *
*       Type 'back' now to go back to the 'Main menu'                         *
*                                                                             *
*                                                                             *
* Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
    
    messages.append(new_game_menu_text)
    messages.append(get_player_name(player_name))


    if messages[-1][1] is not None:
        messages.append(f"Welcome to the game, {messages[-1][1]}!")
    
    return messages

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