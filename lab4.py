# unit converting program that converts from one liquid volume to another liquid volume
# This will take a number and a string input and output a string
# input number of units
# input type of volume
# output number in new volume

# Author Errolyn McGahan

# Data source object for volume conversions 
# I would have this as a seperate file and import it in But since this is not going to contain a whole lot I'm leaving it here.
conversions = {
    'tbsp': {'oz': 0.5000027, 'lt': 0.014787, 'tsp': 3.000008, 'tbsp': 1},
    'tsp': {'oz': 0.5000027, 'lt': 0.014787, 'tsp': 1, 'tbsp': 0.3333324},
    'oz': {'oz': 1, 'lt': 0.02957344, 'tsp': 5.999983, 'tbsp': 1.999989},
    'lt': {'oz': 33.81413, 'lt': 1, 'tsp': 202.8842, 'tbsp': 67.62788},
    }

# Display "This is a liquid volume converter"
print("This is a liquid volume converter")

# Module get_unit_type
    # Display conversion types
    # Get input "What would you like to convert from? (tbsp, tsp, oz, lt ) >> "
    # loop until valid input
        # reprompt for input
    # return input
 
def get_unit_type(message):
    print("You can convert teaspoons, tablespoons, ounces, and litres")
    unit_type =  input(message).lower()
    while unit_type not in conversions:
        print("That was an invalid input! ")
        unit_type = input("Enter one of the following (tbsp, tsp, oz, lt ) \n>> ").lower()
    return unit_type 

# Module get_unit_number
    # loop until a valid number is entered
        # set is_float to true at top of loop
        # Try to get input and convert to float
        # Catch errors
            # set is_float to false if error found
        # if is_float true return unit value

def get_unit_number():
    while True:
        is_float = True
        try:
            unit_number = float(input("How many units are we converting? \n>> "))
        except ValueError:
            print("Error: Invalid type please enter a number. ")
            is_float = False
        if is_float:
            return unit_number

# Module get_conversion(unit_type, second_unit_type)
#   Look up dictionary values
#   return looked up value

def get_conversion(unit_type, second_unit_type):
    dict_lookup_value = conversions[unit_type]
    return(dict_lookup_value[second_unit_type])


# Module convert_unit With (unit_number, second_unit_type, unit_number)
    # Get converted_unit to unit_number * unitB

def convert_unit(unit_type, second_unit_type, unit_number):
    return(unit_number * float(get_conversion(unit_type, second_unit_type)))
    
# Module output_conversion ()
    # Display completed conversion
def output_conversion(unit_type, second_unit_type, unit_number, converted_unit):
    print(unit_number, unit_type, "equals", round(converted_unit, 2), second_unit_type)

# Module another_conversion()
    # Get input continue_program "would you like to convet something else? "
    # loop until continue_program is yes or no
        # display input error
        # get new input
    # If continue_program == "no"
       #return False
    # Else If continue_program == "yes"
       #return True

def another_conversion():
    while True:
        continue_program = input("Would you like to convert something? (yes/no) \n>> ").lower()
        if continue_program == "no":
            return False
        elif continue_program == "yes":
            return True
        print("Sorry I could not understand that! ")
    
# Module main
    # Check if user would like to convert something loop 
        # Get starting unit type
        # Get second unit type
        # Get number of units
        # Call convert_unit(unit_type, second_unit_type, unit_number)
        # Call output_conversion(unit_type, second_unit_type, unit_number, converted_unit)
    # Quit program if not.
    # Display goodbye
    
def main():
    while another_conversion():
        unit_type = get_unit_type('What would you like to convert from? (tbsp, tsp, oz, lt ) \n>> ' )
        second_unit_type = get_unit_type("What would you like to convert to? (tbsp, tsp, oz, lt ) \n>> ")
        unit_number = get_unit_number()
        converted_unit = convert_unit(unit_type, second_unit_type, unit_number)
        output_conversion(unit_type, second_unit_type, unit_number, converted_unit)
    print("\nGood bye!\n")        


# Call main
if __name__ == "__main__":
    main()
    