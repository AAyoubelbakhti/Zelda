
def menu():
    while True:
        clear_screen()
        fondorandom()
        accio = input("Select an option: ")
        ac = accio.lower()
        if ac == "continue":
            if saved_games != None:
                if len(saved_games) == 1:
                    game()
                else:
                    saved_games_menu()
        elif ac == "new game":
            game()
        elif ac == "help":
            menu_help()
        elif ac == "about":
            about()
        elif ac == "exit":
            break
  
