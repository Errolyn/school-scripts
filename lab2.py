__author__ = 'Sam McGahan'

# Aquarium Weight Calculator

# Input list: length, height, width, water type
# Outputs: gallons and weight

# Sudo Code:

# Display welcome message
# Get users water type
# Check for valid water type and prompt for new entry if input is not valid with error message

# Get users aquarium dimensions: length, width, height
# Check for valid dimensions and prompt for new entry if they are not valid

# Create weight and volume and weight calculation function
# Do math for volume assign to volume variable ( h * w * l )
# Convert volume to gallons ( volume / 231 ) assign to gallons variable
# get weight ( gallon * water_wight ) assign to aquarium_weight variable
# print results in a human readable format, formatting numbers to 2 decimal points

# Check if the water type is salt or fresh
# call weight calculation function with needed variables passed in.

print("Thank you for using Aquarium Weight Calculator. You can calculate the approximate"
      "weight of rectangle or square Aquariums.")

print("What type of water will be in your tank?")
water_type = input('"s" for salt or "f" for fresh >> ')
while not water_type == "s" and not water_type == "f":
    print('That was not a valid input please only select "s" or "f".')
    water_type = input('"s" for salt or "f" for fresh >> ')


print("Let's get your aquarium's dimensions")
aquarium_height = int(input("what is the height in inches? >> "))
aquarium_length = int(input("what is the length in inches? >> "))
aquarium_width = int(input("what is the width in inches? >> "))

while 1:
    if aquarium_height <= 0:
        print("Please select a number larger than 0")
        aquarium_height = int(input("what is the height in inches? >> "))
    elif aquarium_length <= 0:
        print("Please select a number larger than 0")
        aquarium_length = int(input("what is the length in inches? >> "))
    elif aquarium_width <= 0:
        print("Please select a number larger than 0")
        aquarium_width = int(input("what is the width in inches? >> "))
    else:
        break


def weight_calc(height, length, width, weight):
    volume = height * width * length
    gallons = volume / 231
    aquarium_weight = gallons * weight
    print("Your aquarium can hold %.2f gallons of water which weights about %.2f pounds" % (gallons, aquarium_weight))


if water_type == "s":
    weight_calc(aquarium_height, aquarium_length, aquarium_width, 8.55)
elif water_type == "f":
    weight_calc(aquarium_height, aquarium_length, aquarium_width, 8.33)
