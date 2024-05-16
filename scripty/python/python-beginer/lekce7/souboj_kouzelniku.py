# Import potřebných knihoven
import random
import time
import os

# Nastavení hodnot pro zdraví hráče a počítače
min_health = 0
max_health = 20
player_health = max_health
bot_health = max_health

# Definice jednoduchých a složitých kouzel
# každé kouzlo je seznam obsahující jméno, poškození a uzdravení
simple_spells = [['fireball', 10, 0], ['metabolism', 0, 8], ['silence', 0, 0]]
complicated_spells = [['strength', 9, 3], ['vitality', 4, 8]]

# Indexy pro jednotlivé hodnoty v seznamu kouzel
name = 0
damage = 1
heal = 2

# ASCII umění pro vizuální efekty
# ASCII umění pro začátek, konec hry, posunutí úrovně a nové kolo
start_ascii = '''
<ASCII umění pro začátek hry>
'''

gameover_ascii = '''
<ASCII umění pro konec hry>
'''

end_ascii = '''
<ASCII umění pro konec hry>
'''

level_up_ascii = '''
<ASCII umění pro posunutí úrovně>
'''

new_round_ascii = '''
<ASCII umění pro nové kolo>
'''

win_ascii = '''
<ASCII umění pro výhru>
'''

# Hlavní herní smyčka
while True:
    # Hráč volí, zda chce začít hru
    print(start_ascii, '\n[Y] - Yes\n[N] - No\n')
    select = input('Start Wizard Duel? Your select: ')
    if select == 'N' or select == 'n':
        break
    elif (not select == 'Y') and (not select == 'y'):
        print('Error! Try again.')
    else:
        # Příprava nové hry
        os.system('cls')
        spells = simple_spells
        a = len(simple_spells)
        del spells[a:]
        print('''
        ==========================================
        ================ OPTIONS =================
        Spell Damage Healing''')
        count = 1
        for row in spells:
            print(f'\n{[count]}', end=' - ')
            count+=1
            for elem in row:
                print('\t', elem, end='')
        print('''
        ==========================================
        ------- WIZARD DUEL -------''')
        print(new_round_ascii)
        # Start nové hry
        for round in range(1, 6):
            # Hráč vybírá kouzlo
            choice = True
            while choice:
                player_select = input('\nSelect spell: ')
                print(player_select)
                if player_select > '0' and player_select <= str(len(spells)) and len(player_select)==1:
                    player_select = int(player_select)
                    player_select = player_select - 1
                    bot_select = random.randint(0, len(spells)-1)
                    choice = False
                else:
                    print('Error! Try again.')
            play_1 = spells[player_select][name]
            play_2 = spells[bot_select][name]
            print(f'''----ROUND No {round}----{play_1.upper()} ----- {play_2.upper()}''')
            # Použití kouzla a aktualizace zdraví
            if play_1 == 'silence' and play_2 == 'silence':
                continue
            elif play_1 == 'silence':
                player_select = bot_select
                player_health += spells[bot_select][damage]
            elif play_2 == 'silence':
                bot_select = player_select
                bot_health += spells[player_select][damage]
            player_health += spells[player_select][heal]
            player_health -= spells[bot_select][damage]
            bot_health += spells[bot_select][heal]
            bot_health -= spells[player_select][damage]
            # Omezení zdraví na maximální a minimální hodnoty
            if player_health > max_health and bot_health > max_health:
                player_health = max_health
                bot_health = max_health
            elif player_health > max_health:
                player_health = max_health
            elif bot_health > max_health:
                bot_health = max_health
            print(f''' PLAYER vs BOT {player_health} {bot_health}''')
            # Kontrola konce hry
            if player_health < min_health or bot_health < min_health:
                break
            # Odemknutí složitějších kouzel po třech kolech
            if round == 3:
                os.system('cls')
                print(f'''
                {level_up_ascii}
                ==========================================
                ============== NEW FEATUES ===============
                Spell Damage Healing''')
                spells += complicated_spells
                count = 1
                for row in spells:
                    print(f'\n{[count]}', end=' - ')
                    count+=1
                    for elem in row:
                        print('\t', elem, end='')
                print('\n==================================')
        # Konec hry
        os.system('cls')
        print(gameover_ascii)
        if player_health > bot_health:
            print('Congratulations! You win!\n', win_ascii)
        elif player_health < bot_health:
            print('Sorry... The computer wins!')
        else:
            print('Draw!')
        time.sleep(5)
# Ukončení programu
os.system('cls')
print(end_ascii)
