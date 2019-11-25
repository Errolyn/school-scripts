# Program to track/list/save people's birthdays
# It takes a set of supplied commands, people names, and birthdates
# It will output the birthdate based on name, and also saving will over write a json file provided with the program which contains some dummy data.

# Author Errolyn McGahan

# import needed librarys
import json
import datetime

# create method read_file (str fileName)
    # open file with read permissions
        # output contents of file
    
def read_file(fileName):
    with open(fileName, 'r') as json_file:
        return(json.load(json_file))

# create method write_file(file name, content)
    # open file with write access
    # write contents to file
    # display "Saved!"
def write_file(fileName, content):
    with open(fileName, 'w') as outfile:
        json.dump(content, outfile)
    print('Saved!')

# create method list_people(people)
    # create array name_list
    # iterate through array of objects
        #add name to name_list
    # output array list
def list_people(people):
    name_list = []
    for person in people['people']:
        name_list.append(person['name'])
    return name_list

# create method get_birthday(name, people)
    # iterate through array of objects
        # check if name matchs person
            # if matches return birthday
    # if not in list return "Info for that person is not available, try adding them."
def get_birthday(name, people):
    for person in people['people']: # array of objects
        if person['name'].lower() == name.lower():
            return person['birthday']
    return('Info for that person is not available, try adding them.')

# create method add_person(people)
#   display "What is the name of the person you would like to add? (type it exactly how you would like to see it in the dictionary)"
#   set the output of get_name to name
#   check for person, call if_person_exists(name, people)
#       display "That person is already in the dictionary, what would like to do?" if the do.
#   otherwise 
#       set date to get_date()
#       create object to add to array
#       add object to array
#       display name, date, "added to dictionary"
def add_person(people):
    print("What is the name of the person you would like to add? (type it exactly how you would like to see it in the dictionary)")
    name = get_name()
    if if_person_exists(name, people):
        print("That person is already in the dictionary, what would like to do?")
    else:
        date = get_date()
        temp_obj = {'name': name, 'birthday': date}
        people['people'].append(temp_obj)
        print(name, date, "added to dictionary")

# create method quit_app
    # set app_state to people
    # read the file and set to file_state
    # compair app and file states if same then quit
    # if different 
    # ask if user wants to save
    # validate input from Users
    # if yes then write file
    # if no then quit
    # otherwise reprompt for input
def quit_app(people):
    app_state = people
    file_state = read_file("birthday_dictionary.json")
    if app_state == file_state:
        return('quit')
    else:
        save_now = input('It looks like you might not have saved your changes, save now? yes/no \n>>> ')
        while True:
            if save_now == 'yes':
                write_file("birthday_dictionary.json", people)
                return('quit')
            elif save_now == 'no':
                return('quit')
            save_now = input('It looks like you might not have saved your changes, save now? yes/no \n>>>')

# create method get_name
    # get input
    # start loop
    #     create array of words in Name
    #     add state variable set to False
    #     loop through word and check if only letters
    #     if word is not alpha then
    #         break loop
    #     prompt for new input
    #     if is valid set state of validated to True
    #     return name
def get_name():
    name = input('\n>>> ')
    while True:
        name_array = name.split(' ')
        validated = False
        for word in name_array:
            if word.isalpha() == False:
                break
            validated = True

        if validated:
            break
        print("Names have to only contain letters, and have at least one character.")
        name = input('Try inputing another name \n>>> ')
    return name

# create method get_date()
    # display "What is the birthday of the person you would like to add?"
    # get data input
    # start loop
    #     add state variable set to False
    #     check if valid date
    #         break loop if valid
    #     else prompt for new input
    #    if valid output date
def get_date():
    print('\nWhat is the birthday of the person you would like to add?\n')
    date = input('Example: 3-31-1986 \n>>> ') 
    while True:
        validated = user_date_validator(date)
        if validated == True:
            break
        print(validated)
        date = input('Try inputing another date \n>>> ')
    return date

# create method if_person_exists(name, people)
# loop over object in array
# compare if name matchs
#     if it does output True
def if_person_exists(name, people):
    for person in people['people']: # This is an array of objects
        if person['name'].lower() == name.lower():
            return True

# create method user_input_validator(userInput)
    # create list of input_options "'list', 'add', 'find', 'save', 'quit'"
    # check if userInput matches options in array
    # if so output True
    # else output False
def user_input_validator(userInput):
    input_options = ['list', 'add', 'find', 'save', 'quit']
    if userInput in input_options:
        return True
    return False

# create method user_date_validator(userInput)
    # check user input versus date time format checker
    # if is doesn't match output error message
    # else return True
def user_date_validator(userInput):
    try:
        datetime.datetime.strptime(userInput, '%m-%d-%Y')
    except ValueError:
        return( ValueError("Incorrect data format, should be MM-DD-YYYY"))
    return True

# create method  user_action_selection(people)
    # display "What would you like to do? <'list', 'add', 'find', 'save', 'quit'> \n>>>"
    # loop on user_input_validator while false prompt for a new input
    # call action_handler
def user_action_selection(people):
    user_option = str(input("\n \nWhat would you like to do? <'list', 'add', 'find', 'save', 'quit'> \n>>> ")).lower()
    print('\n')
    
    while user_input_validator(user_option) == False:
        print("That was not a valid command try again!\n ")
        user_option = str(input("What would you like to do? <'list', 'add', 'find', 'save', 'quit'> \n>>> ")).lower()
        print('\n')

    return action_handler(user_option, people)

# create method action_handler(user_option, people)
    # if user_option is 'list' then
    # call list_people(people) and display list
    # if user_option is "add" then call add_person
    # if user_option is "find" then print the output of get_birthday
    # if user_option is "save" the call write_file with the people array
    # if user_option is "quit" return the output of the quit_app method
def action_handler(user_option, people):
    if user_option == 'list':
        current_people = list_people(people)
        print("\n".join(current_people[1:]))
    if user_option == 'add':
        add_person(people)
    if user_option == 'find':
        print("Who are you looking for?")
        birthday = get_birthday(get_name(), people)
        print("Their birthday is:", birthday )
    if user_option == 'save':
        write_file("birthday_dictionary.json", people)
    if user_option == 'quit':
        return(quit_app(people))

# create method main()
    # display name of app "Birthday Dictionary"
    # display tagline "You can keep track of all your friends birthdays"
    # open datafile for app
    # start app loop
    #     if user_action return quit
    #         terminate app loop
    # display "Good bye"
def main():
    print("\n\nBirthday Dictionary")
    print("You can keep track of all your friends birthdays")
    people = read_file("birthday_dictionary.json")
    while True:
        if user_action_selection(people) == 'quit':
            break
    print("Good bye")
        

# Call main
if __name__ == "__main__":
    main()
