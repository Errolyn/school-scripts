# Author Errolyn McGahan


import random

class Monster:
    def __init__(self, name, monsterType, size, hp):
        self.name = name
        self.monsterType = monsterType
        self.size = size
        self.hp = hp
    
    def recieved_damage(self, dmg):
        self.hp -= dmg

    def increased_hp(self, heal):
        self.hp += heal
        
    def display_stats(self):
        return(f"{' '.join(self.name)} is a {self.monsterType}, and they are of a {self.size} size, and have {self.hp} hp left.")
    
    def dead(self):
        return self.hp <= 0

### Generate monster stats ###        

def generate_hitpoints(low, high):
    return(random.randint(low, high))

def generate_name():
    first_names = ["Alasaila", "Cotto", "Laquet", "Qualmea", "Ruhta", "Wraith", "Ungwale", "Grundle", "Henery", "Karen", "Tim", "Joshua", "Progenitus", "Marty", "Tom"]
    titles = ["Orc Chief", "Gobblin Chief", "Theif", "Cruel", "Dark", "Wise", "Wasteful", "Grim", "Strong", "Ghost Whiperer", "Cranky", "Breath of Death"]
    first_name = first_names[random.randint(0, len(first_names)) - 1]
    title = titles[random.randint(0, len(titles)) - 1]
    print(first_name, "the", title)
    return(first_name, "the", title)

def generate_monster_type():
    monster_types = ["human", "orc", "goblin", "ghost"]
    return(monster_types[random.randint(0, len(monster_types)) - 1])

def generate_size():
    sizes = ["small", "medium", "large", "giant"]
    return(sizes[random.randint(0, len(sizes)) - 1])

def generate_battle(enemys):
    monsters = [None] * enemys
    monster_type = generate_monster_type()
    monster_size = generate_size()
    for enemy in range(enemys):
        monsters[enemy] = Monster(generate_name(), monster_type, monster_size, generate_hitpoints(5, 100))
    return monsters



### User Command Handlers ###

def display_monsters(monsters):
    number = 1
    for monster in monsters:
        print(f"{number}: {monster.display_stats()}")
        number += 1

def attack_monster(monster, dmg):
    name = " ".join(monster.name)
    monster.recieved_damage(dmg)
    if monster.dead():
        print("You killed", name)
    else:
        print(name, "has", monster.hp, "hp left.")

def  remove_dead_monsters(monsters):
    for monster in monsters:
        if monster.dead():
            monsters.remove(monster)

# create method user_input_validator(userInput)
    # create list of input_options "'d', 'a', 'q'"
    # check if userInput matches options in array
    # if so output True
    # else output False
def user_input_validator(userInput, input_options):
    if userInput in input_options:
        return True
    return False


# create method  user_action_selection(people)
    # display "Your available commands are: <battle details(d), attack(a), quit(q)> \n>>>"
    # loop on user_input_validator while false prompt for a new input
    # call action_handler
def user_action_selection(monsters):
    user_option = str(input("\n \nYour available commands are: <battle details(d), attack(a), quit(q)> \n>>> ")).lower()
    possible_inputs = ['d', 'a', 'q']
    print('\n')
    
    while user_input_validator(user_option, possible_inputs) == False:
        print("That was not a valid command try again!\n ")
        user_option = str(input("Your available commands are: <battle details(d), attack(a), quit(q)> \n>>> ")).lower()
        print('\n')

    return action_handler(user_option, monsters)

def attack_handler(monsters):
    dmg = None

    while dmg is None:
        try:
            dmg = int(input("How much damage are you doing to the monster? \n>>> "))
        except ValueError:
            print("I need a number")

    display_monsters(monsters)
    while True:
        try:
            monster_number = int(input("What monster would you like to kill? \n>>> "))
        except ValueError:
            print("That is not a number")
        if monster_number > (len(monsters)):
            print("There is no monster with that number")
        else:
            break
    print(monster_number)
    return(attack_monster(monsters[(monster_number-1)], dmg))


# create method action_handler(user_option, people)
    # if user_option is 'list' then
    # call list_people(people) and display list
    # if user_option is "add" then call add_person
    # if user_option is "find" then print the output of get_birthday
    # if user_option is "save" the call write_file with the people array
    # if user_option is "quit" return the output of the quit_app method
def action_handler(user_option, monsters):
    if user_option == 'd':
        display_monsters(monsters)
    if user_option == 'a':
        attack_handler(monsters)
        remove_dead_monsters(monsters)
        if len(monsters) == 0:
            print("You killed all the monsters!")
            return('quit')
    if user_option == 'q':
        return('quit')


### PROGRAM RUNNER ###
def main():
    monsters = generate_battle(random.randint(1, 10))
    print("Welcome to the Dungeon Battle simulator")
    
    while True:
        if user_action_selection(monsters) == 'quit':
            break
    print("Good bye")




if __name__ == "__main__":
    main()