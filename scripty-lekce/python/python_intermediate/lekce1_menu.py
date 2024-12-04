print("\_ *** Hokej nás baví *** _/")
print("Program pro správu hráčů hokejového klubu.")
selection = None
hockey_club = []

while selection != 0:
    print("[1] Výpis hráčů hokejového klubu")
    print("[2] Přidání hráče do klubu")
    print("[3] Vyřazení hráče z členství v klubu")
    print("[4] Seřazení seznamu hráčů")
    print("[0] Ukončení programu")
    
    selection = input("Vyber si jednu z možností... ")
    
    if selection.isnumeric():
        selection = int(selection)
        
        if selection == 1:
            print(f"Zvolil jsi možnost #{selection}.")
            print("Seznam členů klubu je: ")
            print(hockey_club)
        
        elif selection == 2:
            print(f"Zvolil jsi možnost #{selection}.")
            player_name = input("Zadej jméno hráče... ")
            hockey_club.append(player_name)
        
        elif selection == 3:
            print(f"Zvolil jsi možnost #{selection}.")
            delete_player_number = int(input("Zadej pořadové číslo hráče pro ukončení jeho členství... "))
            
            if 0 < delete_player_number <= len(hockey_club):
                del hockey_club[delete_player_number - 1]
            else:
                print("Chyba: Hráč s tímto číslem neexistuje.")
        
        elif selection == 4:
            print(f"Zvolil jsi možnost #{selection}.")
            hockey_club.sort()
            print(hockey_club)
        
        elif selection == 0:
            print("Program byl ukončen.")
        
        else:
            print("Neznámá volba.")
    else:
        print("Neznámá volba.")
