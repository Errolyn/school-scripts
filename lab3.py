# unit converting program that converts Tablespoons and tea spoons to Ounces
# This will take a number and a string input and output a string
# input number of tablespoons or teaspoons
# input if tablespoon or teaspoon
# output number of ounces

# Author Errolyn McGahan

# output "This is a tablespoon and teaspoon to ounces converter"
print("This is a tablespoon and teaspoon to ounces converter ")

# Module set_unit_type
    # Get input "Enter either teaspoon or tablespoon (tsp, tbsp) >> "
    # loop until input is either tsp or tbsp
        # reprompt for input
    # return input
 
def set_unit_type():
    unit_type = unit_type = input("Enter either teaspoon or tablespoon (tsp, tbsp) >> ")
    while ((unit_type != "tbsp") & (unit_type != "tsp")):
        print("That was an invalid input! ")
        unit_type = unit_type = input("Enter either teaspoon or tablespoon (tsp, tbsp) >> ")
    return unit_type

# Module set_unit_number
    # loop until a valid number is entered
        # set is_float to true at top of loop
        # Try to get input and convert to float
        # Catch errors
            # set is_float to false if error found
        # if is_float true return unit value

def set_unit_number():
    while True:
        is_float = True
        try:
            unit_number = float(input("how many units are we converting? >> "))
        except ValueError:
            print("Error: Invalid type please enter a number. ")
            is_float = False
        if is_float:
            return unit_number



# Module select_conversion_type With (UnitType)
    # If tbsp Then set conversion_unit To 0.5000027
    # Else if tsp Then set conversion_unit TO 0.1666671

        
def select_conversion_type(unitType):
    if unitType == "tbsp":
        return(0.5000027)
    elif unitType == "tsp":
        return(0.1666671)

# Module convert_to_ounces With (unit_number, unitB)
    # Set converted_unit to unit_number * unitB

def convert_to_ounces(unit_type, unit_number):
    converted_unit = unit_number * float(select_conversion_type(unit_type))
    print(unit_number, unit_type, "equals", round(converted_unit, 2), "ounces")

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
        continue_program = input("Would you like to convert something? (yes/no) >> ")
        if continue_program == "no":
            return(False)
        elif continue_program == "yes":
            return(True)
        print("Sorry I could not understand that! ")
            


    
# Module main
    # Get unit type either teaspoon or tablespoon (tsp, tbsp)
    # Set unit_type to input
    # Get number of units
    # Set unit_number to input
    # Call convert_to_ounces
    # Call convert_to_ounces(unit_type, unit_number)
    # Output unit_number, unit_type, "equals", converted_unit, "ounces"
    
def main():
    while another_conversion():
        unit_type = set_unit_type()
        unit_number = set_unit_number()
        convert_to_ounces(unit_type, unit_number)
    print("Good bye!")        
    
# Call main

main()
    