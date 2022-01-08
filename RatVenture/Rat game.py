#Ivan Chang
#P08 S10205569

import random

# +-------------------------
# | Text for various menus | 
# +-------------------------
main_text = ["New Game",\
             "Resume Game",\
             "View Leaderboard",\
             "Exit Game"]

town_text = ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Save Game",\
             "Exit Game"]

open_text = ["View Character",\
             "View Map",\
             "Move",\
             "Sense Orb",\
             "Exit Game"]

fight_text = ["Attack",\
              "Run"]

world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]


# +------------
# | variables | 
# +------------

player_stats = {'player_max_damage': 4, 
                'player_min_damage': 2,
                'player_defence': 1, 
                'player_HP': 20}

rat_stats = {'rat_max_damage': 3,
             'rat_min_damage': 1,
             'rat_defence': 1,
             'rat_HP': 10}

ratking_stats = {'ratking_max_damage': 10,
                 'ratking_min_damage': 6,
                 'ratking_defence': 5,
                 'ratking_HP': 5}

current_x = 0
current_y = 0
new_x = 0
new_y = 0

day = 1

found_orb = False

start_game = True

town_list = [[0,0]]


# +------------
# | functions | 
# +------------


def print_menu(text): # print any menu
    count = 1
    for i in text:
        print('{}) {}'.format(count,i))
        count += 1
        
                
def print_board(): # print board and print player position
    
    global current_y, current_x
    
    #removing 'H' to the map
    if world_map[current_y][current_x] == 'H/T':
        world_map[current_y][current_x] = world_map[current_y][current_x].replace(world_map[current_y][current_x],'T')
        current_y = new_y
        current_x = new_x

    elif world_map[current_y][current_x] == 'H/K':
        world_map[current_y][current_x] = world_map[current_y][current_x].replace(world_map[current_y][current_x],'K')
        current_y = new_y
        current_x = new_x
        
    elif world_map[current_y][current_x] == 'H':
        world_map[current_y][current_x] = world_map[current_y][current_x].replace(world_map[current_y][current_x],' ')
        current_y = new_y
        current_x = new_x
  
    #adding 'H' to the map
    if world_map[new_y][new_x] == 'T':
        world_map[new_y][new_x] = world_map[new_y][new_x].replace(world_map[new_y][new_x],'H/T')
        current_y = new_y
        current_x = new_x

    elif world_map[new_y][new_x] == ' ':
        world_map[new_y][new_x] = world_map[new_y][new_x].replace(world_map[new_y][new_x],'H')
        current_y = new_y
        current_x = new_x
        
    elif world_map[new_y][new_x] == 'K':
        world_map[new_y][new_x] = world_map[new_y][new_x].replace(world_map[new_y][new_x],'H/K')
        current_y = new_y
        current_x = new_x

    #printing the board
    for i in world_map:
        print('+---+---+---+---+---+---+---+---+')
        print('|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    print('+---+---+---+---+---+---+---+---+')
    
    
def move():
    
    global day, new_x, new_y
  
    print_board()
    
    print('\n')
    direction = input('W = up; A = left; S = down; D = right: ').upper()
    while direction != 'W' and direction != 'A' and direction != 'S' and direction != 'D':
        print('\nPlease enter a valid key')
        direction = input('W = up; A = left; S = down; D = right: ').upper()
    
    if direction == 'W':
        if current_y == 0 or current_x == range(0,8): #boundaries
            print('Unable to move up, please enter different key')
            move()
        else: #move
            new_y = current_y - 1
            print_board()
            day += 1
    elif direction == 'A':
        if current_x == 0 or current_y == range(0,8): #boundaries
            print('Unable to move left, please enter different key')
            move()
        else: #move
            new_x = current_x - 1
            print_board()
            day += 1
    elif direction == 'S':
        if current_y == 7 or current_x == range(0,8): #boundaries
            print('Unable to move down, please enter different key')
            move()
        else: #move
            new_y = current_y + 1
            print_board()
            day += 1
    elif direction == 'D':
        if current_x == 7 or current_y == range(0,8): #boundaries
            print('Unable to move left, please enter different key')
            move()
        else: #move
            new_x = current_x + 1
            print_board()
            day += 1

    if world_map[current_y][current_x] == 'H':
        rat_encounter()
        combat_menu()
    elif world_map[current_y][current_x] == 'H/T':
        town_menu()
    elif world_map[current_y][current_x] == 'H/K':
        ratking_encounter()
        boss_fight()
        
        
def town_menu():
    
    global day, start_game
    
    print('Day {}: You are in a town.'.format(day))
    
    print_menu(town_text)
    option = input('Enter option: ')
    
    while option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6':
        print('\nPlease enter a valid option')
        option = input('Enter option: ')
    
    if option == '1': #display stats
        print('\nThe Hero')
        print('  Damage: {}-{}'.format(player_stats['player_min_damage'],player_stats['player_max_damage']))
        print(' Defence: {}'.format(player_stats['player_defence']))
        print('      HP: {}\n'.format(player_stats['player_HP']))
        if found_orb == True:
            print('You are holding the Orb of Power.\n')
        town_menu()

        
    elif option == '2': #display board
        print_board()
        town_menu()
    
    elif option == '3': #move
        move()
   
    elif option == '4': #rest
        player_stats['player_HP'] = 20
        print('\nYou are fully healed.')
        day += 1
        town_menu()
        
    elif option == '5': #save
        save_game()
        print('Game Saved.\n')
        town_menu()
        
    elif option == '6': #exit
        print('Game Exited.')
        start_game = False
        
        
def rat_encounter(): #encountering a rat
    rat_stats['rat_HP'] = 10
    print('\nDay {}: You are out in the open.'.format(day))
    print('Encounter - Rat')
    print('Damage: {}-{}'.format(rat_stats['rat_min_damage'],rat_stats['rat_max_damage']))
    print('Defence: {}'.format(rat_stats['rat_defence']))
    print('HP: {}'.format(rat_stats['rat_HP']))   
    
    
def combat_menu(): #fighting an enemy
    
    global found_orb, start_game
    
    rat_damage = random.randint(rat_stats['rat_min_damage'],rat_stats['rat_max_damage']) #variable of random int of rat's damage
    player_damage = random.randint(player_stats['player_min_damage'],player_stats['player_max_damage']) #variable of random int of player's damage
    
    print_menu(fight_text)
    option = input('Enter option: ')

    while option != '1' and option != '2':
        print('\nPlease enter a valid option')
        option = input('Enter option: ')
    
    if option == '1':   
        if rat_stats['rat_HP'] > 0 and player_stats['player_HP'] > 0: #check if player and rat is still alive
            rat_stats['rat_HP'] -= (player_damage - rat_stats['rat_defence']) #attack rat
            print('\nYou deal {} damage to the Rat'.format(player_damage - rat_stats['rat_defence'])) #print damage dealt by player

            if rat_stats['rat_HP'] > 0: #check if rat is still alive
                player_stats['player_HP'] -= max(0,(rat_damage - player_stats['player_defence'])) #damage cannot go below 0
                print('Ouch! The Rat hit you for {} damage!'.format(max(0,(rat_damage - player_stats['player_defence'])))) #print damage dealt by rat
                
                if player_stats['player_HP'] > 0:
                    print('You have {} HP left.'.format(player_stats['player_HP']))
                    print('Encounter - Rat')
                    print('Damage: {}-{}'.format(rat_stats['rat_min_damage'],rat_stats['rat_max_damage']))
                    print('Defence: {}'.format(rat_stats['rat_defence']))
                    print('HP: {}\n'.format(rat_stats['rat_HP']))

                    combat_menu()

                else:
                    print('You died, game over')
                    start_game = False
            else:
                print('The Rat is dead! You are victorious!\n')
                open_menu()

    elif option == '2': #cannot use open_menu() function as rat will attack player if he moves after running
        print('\nYou run and hide.')
        run()
            
            
def run():
    
    global start_game
    
    rat_damage = random.randint(rat_stats['rat_min_damage'],rat_stats['rat_max_damage']) #variable of random int of rat's damage
    
    rat_stats['rat_HP'] = 10
    print_menu(open_text)
    option = input('Enter option: ')

    while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
        print('\nPlease enter a valid option')
        option = input('Enter option: ')

    if option == '1':
        print('\nThe Hero')
        print('  Damage: {}-{}'.format(player_stats['player_min_damage'],player_stats['player_max_damage']))
        print(' Defence: {}'.format(player_stats['player_defence']))
        print('      HP: {}\n'.format(player_stats['player_HP']))
        if found_orb == True:
            print('You are holding the Orb of Power.\n')
        run()

    elif option == '2':
        print('\n')
        print_board()
        run()

    elif option == '3':
        player_stats['player_HP'] -= max(0,(rat_damage - player_stats['player_defence']))
        print('Ouch! The Rat hit you for {} damage!'.format(max(0,(rat_damage - player_stats['player_defence']))))

        if player_stats['player_HP'] <= 0:
            print('You died, game over')
            start_game = False
        else:
            move()

    elif option == '4':
        sense_orb()
        run()

    elif option == '5':
        print('Game Exited.')
        start_game = False            
                
def open_menu():
    
    global start_game
    
    print('Day {}: You are out in the open.'.format(day))
    print_menu(open_text)
    option = input('Enter option: ')

    while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
        print('\nPlease enter a valid option')
        option = input('Enter option: ')

    if option == '1':
        print('\nThe Hero')
        print('  Damage: {}-{}'.format(player_stats['player_min_damage'],player_stats['player_max_damage']))
        print(' Defence: {}'.format(player_stats['player_defence']))
        print('      HP: {}\n'.format(player_stats['player_HP']))
        if found_orb == True:
            print('You are holding the Orb of Power.\n')
        open_menu()


    elif option == '2':
        print('\n')
        print_board()
        open_menu()

    elif option == '3':
        move()

    elif option == '4':
        sense_orb()
        open_menu()
        
    elif option == '5':
        print('Game Exited.')
        start_game = False   
            
def sense_orb():
    global found_orb, day
    
    if found_orb == True:
        print('You already have the Orb of Power.\n')
        
    elif current_x == orb_x and current_y == orb_y:
        found_orb = True
        player_stats['player_min_damage'] += 5
        player_stats['player_max_damage'] += 5
        player_stats['player_defence'] += 5
        print('\nYou found the Orb of Power!')
        print('Your attack increases by 5!')
        print('Your defence increases by 5!\n')
        day += 1
        #print('Day {}: You are out in the open.'.format(day))
        
    else:
        print('\n')
        if current_x == orb_x: #if orb is in the same column as player
            if current_y < orb_y: #south
                print('You sense that the Orb of Power is to the south.')
            elif current_y > orb_y: #north
                print('You sense that the Orb of Power is to the north.')

        elif current_y == orb_y: #if orb is in the same row as player
            if current_x < orb_x: #east
                print('You sense that the Orb of Power is to the east.')
            elif current_x > orb_x: #west
                print('You sense that the Orb of Power is to the west.')

        elif current_x > orb_x: #if orb is to the right
            if current_y > orb_y: #northwest
                print('You sense that the Orb of Power is to the northwest.')
            elif current_y < orb_y: #southwest
                print('You sense that the Orb of Power is to the southwest.')

        elif current_x < orb_x: #if orb is to the left
            if current_y < orb_y: #southeast
                print('You sense that the Orb of Power is to the southeast.')
            elif current_y > orb_y: #northeast
                print('You sense that the Orb of Power is to the northeast.')
        day += 1
        #print('Day {}: You are out in the open.'.format(day))

def run_from_ratking():
    
    global start_game
    ratking_damage = random.randint(ratking_stats['ratking_min_damage'],ratking_stats['ratking_max_damage']) #variable of random int of rat king's damage
    
    ratking_stats['ratking_HP'] = 25
    print_menu(open_text)
    option = input('Enter option: ')

    while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
        print('\nPlease enter a valid option')
        option = input('Enter option: ')

    if option == '1':
        print('\nThe Hero')
        print('  Damage: {}-{}'.format(player_stats['player_min_damage'],player_stats['player_max_damage']))
        print(' Defence: {}'.format(player_stats['player_defence']))
        print('      HP: {}\n'.format(player_stats['player_HP']))
        if found_orb == True:
            print('You are holding the Orb of Power.\n')
        run_from_ratking()


    elif option == '2':
        print('\n')
        print_board()
        run_from_ratking()

    elif option == '3':
        player_stats['player_HP'] -= max(0,(ratking_damage - player_stats['player_defence'])) #damage cannot go below 0
        print('Ouch! The Rat King hit you for {} damage!'.format(max(0,(ratking_damage - player_stats['player_defence'])))) #print damage dealt by rat king

        if player_stats['player_HP'] <= 0:
            print('You died, game over')
            start_game = False
        else:
            move()

    elif option == '4':
        sense_orb()
        run_from_ratking()

    elif option == '5':
        print('Game Exited.')
        start_game = False
        
def ratking_encounter():
    
    print('Day {}: You see the Rat King!'.format(day))
    print('Encounter! - Rat King')
    print('Damage: {}-{}'.format(ratking_stats['ratking_min_damage'],ratking_stats['ratking_max_damage']))
    print('Defence: {}'.format(ratking_stats['ratking_defence']))
    print('HP: {}'.format(ratking_stats['ratking_HP']))
    if found_orb == False:
        print('You do not have the Orb of Power - the Rat King is immune!')

    
def boss_fight() : 
    
    global start_game
    ratking_damage = random.randint(ratking_stats['ratking_min_damage'],ratking_stats['ratking_max_damage']) #variable of random int of rat king's damage
    player_damage = random.randint(player_stats['player_min_damage'],player_stats['player_max_damage']) #variable of random int of player's damage
    
    print_menu(fight_text)
    option = input('Enter option: ')

    while option != '1' and option != '2':
        print('\nPlease enter a valid option')
        option = input('Enter option: ')
    
    if option == '1':   
        
        if ratking_stats['ratking_HP'] > 0 and player_stats['player_HP'] > 0: #check if player and ratking is still alive
            ratking_stats['ratking_HP'] -= max(0,(player_damage - ratking_stats['ratking_defence'])) #attack ratking
            print('\nYou deal {} damage to the Rat King'.format(max(0,(player_damage - ratking_stats['ratking_defence'])))) #print damage dealt by player

            if ratking_stats['ratking_HP'] > 0: #check if ratking is still alive
                player_stats['player_HP'] -= max(0,(ratking_damage - player_stats['player_defence'])) #damage cannot go below 0
                print('Ouch! The Rat King hit you for {} damage!'.format(max(0,(ratking_damage - player_stats['player_defence'])))) #print damage dealt by rat king
                
                if player_stats['player_HP'] > 0:
                    print('You have {} HP left.'.format(player_stats['player_HP']))
                    print('Encounter - Rat King')
                    print('Damage: {}-{}'.format(ratking_stats['ratking_min_damage'],ratking_stats['ratking_max_damage']))
                    print('Defence: {}'.format(ratking_stats['ratking_defence']))
                    print('HP: {}\n'.format(ratking_stats['ratking_HP']))

                    boss_fight() #repeat fight until rat king or player is dead

                else:
                    print('You died, game over')
                    start_game = False
            else:
                print('The Rat King is dead! You are victorious!')
                print('Congratulations, you have defeated the Rat King!')
                print('The world is saved! You win!\n')
                add_to_leaderboard()
                load_leaderboard()
                start_game = False

    elif option == '2':
        print('\nYou run and hide.')
        run_from_ratking()
        
def save_game():
    file = open('save_game.txt','w')

    file.write(str(player_stats['player_max_damage'])+ '\n')
    file.write(str(player_stats['player_min_damage'])+ '\n')
    file.write(str(player_stats['player_defence'])+ '\n')
    file.write(str(player_stats['player_HP'])+ '\n')

    file.write(str(ratking_stats['ratking_max_damage'])+ '\n')
    file.write(str(ratking_stats['ratking_min_damage'])+ '\n')
    file.write(str(ratking_stats['ratking_defence'])+ '\n')
    file.write(str(ratking_stats['ratking_HP'])+ '\n')

    file.write(str(current_x)+ '\n')
    file.write(str(current_y)+ '\n')
    file.write(str(new_x)+ '\n')
    file.write(str(new_y)+ '\n')

    file.write(str(day)+ '\n')

    file.write(str(orb_x)+ '\n')
    file.write(str(orb_y)+ '\n')

    file.write(str(found_orb)+ '\n')

    file.close()
    
    
def load_game():
    try:
        loaded_variables = []
        global current_x, current_y, new_x, new_y, day, orb_x, orb_y, found_orb

        file = open("save_game.txt", "r")

        for line in file:
            line = line.strip('\n')
            loaded_variables.append(line)

        file.close()              

        player_stats['player_max_damage'] = int(loaded_variables[0])
        player_stats['player_min_damage'] = int(loaded_variables[1])
        player_stats['player_defence'] = int(loaded_variables[2])
        player_stats['player_HP'] = int(loaded_variables[3])

        ratking_stats['ratking_max_damage'] = int(loaded_variables[4])
        ratking_stats['ratking_min_damage'] = int(loaded_variables[5])
        ratking_stats['ratking_defence'] = int(loaded_variables[6])
        ratking_stats['ratking_HP'] = int(loaded_variables[7])

        current_x = int(loaded_variables[8])
        current_y = int(loaded_variables[9])
        new_x = int(loaded_variables[10])
        new_y = int(loaded_variables[11])

        day = int(loaded_variables[12])

        orb_x = int(loaded_variables[13])
        orb_y = int(loaded_variables[14])

        if loaded_variables[15] == 'True':
            found_orb = True
        else:
            found_orb = False
        
        town_menu()
        
    except IndexError:
        print('No game saved. Please enter another option.\n')
        

def add_to_leaderboard():
    
    global day
    leaderboard_list = []

    #open file, split spaces, remove '\n' and append to list
    file = open('leaderboard.txt')
    for line in file:
        line = line.strip()
        line = line.split('--->')
        leaderboard_list.append(line)
    file.close()


    #convert all days to int
    for sublist in leaderboard_list:
        sublist[1] = int(sublist[1])

    
    #check if text file is empty
    try:
        #if no, sort days of list from lowest to highest
        length = len(leaderboard_list) 
        for i in range(0,length): 
            for j in range(0, length-i-1): 
                if (leaderboard_list[j][1] > leaderboard_list[j + 1][1]): 
                    x = leaderboard_list[j] 
                    leaderboard_list[j]= leaderboard_list[j + 1] 
                    leaderboard_list[j + 1]= x
                    
        try:
            #check again if text file is empty
            #if not,
            if day <= int(leaderboard_list[4][1]):
                #check if player's score quailfies to be in leaderboards
                print('Congratulations! You made it to the leaderboards!')
                name = input('Please enter a name to be saved: ')
                leaderboard_list.pop(4)
                leaderboard_list.append([name,day])
            else:
                #if not:
                print('You did not make it to the leaderbords') 

        
        except IndexError:
            #if yes, player is automatically put in the leaderbords
            print('Congratulations! You made it to the leaderboards!')
            name = input('Please enter a name to be saved: ')
            leaderboard_list.append([name,day])
    
    
    except IndexError:
        #if yes, player is automatically put in the leaderbords
        print('Congratulations! You made it to the leaderboards!')
        name = input('Please enter a name to be saved: ')
        leaderboard_list.append([name,day])


    
    try:
        #sort again before writting information into text file unless ther is only one highscore
        l = len(leaderboard_list) 
        for i in range(0,l): 
            for j in range(0, l-i-1): 
                if (leaderboard_list[j][1] > leaderboard_list[j + 1][1]): 
                    x = leaderboard_list[j] 
                    leaderboard_list[j]= leaderboard_list[j + 1] 
                    leaderboard_list[j + 1] = x
                    
    except IndexError:
        pass
    
    #convert all days to strings to be placed into text file
    for sublist in leaderboard_list:
        sublist[1] = str(sublist[1])

    #updating leaderboard info
    file = open('leaderboard.txt','w')
    for sublist in leaderboard_list:
        for element in sublist:
            file.write(element)
            if element.isdigit() == False:
                file.write('--->')
        file.write('\n')
    file.close()


def load_leaderboard():
    
    leaderboard_list = []
    
    #open file, split spaces, remove '\n' and append to list
    file = open('leaderboard.txt')
    for line in file:
        line = line.strip()
        line = line.split('--->')
        leaderboard_list.append(line)
    file.close()

    if leaderboard_list == []:
        #if there is no highscore it will not print leaderboard table
        print('\nRatventure Leaderboard')
        print('------------------------')
        print('(No highscore yet)\n')
        
    else:
        #print leaderboards in a table
        try:
            position = 1
            print('\nRatventure Leaderboard')
            print('------------------------')
            for sublist in leaderboard_list:
                print('{}. {:<19} {}'.format(position,sublist[0],sublist[1]))
                position += 1 
            print('\n')
            
        except IndexError:
            #text file has no info
            print('(No highscore yet)\n')


def randomize_orb():
    global orb_x, orb_y
    
    orb_x = random.randint(0,7)
    orb_y = random.randint(0,7)
    
    if orb_x <= 3 and orb_y <= 3:
        randomize_orb()
    elif world_map[orb_y][orb_x] == 'T' or world_map[orb_y][orb_x] == 'K':
        randomize_orb()




#------------------------------
while start_game == True:
    print("")
    print("Welcome to Ratventure!")
    print("----------------------")

    print_menu(main_text)

    option = input('Enter option: ')

    while option != '1' and option != '2' and option != '3' and option != '4':
        print('\nPlease enter a valid option')
        option = input('Enter option: ')

    if option == '1':
        randomize_orb()
        print('\n')
        town_menu()

    elif option == '2':
        print('\n')
        load_game()
        
    elif option == '3':
        load_leaderboard()

    elif option == '4':
        print('Game Exited.')
        start_game = False
        
