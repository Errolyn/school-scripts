# def findValue(nums, size, value): 
  
#     for index in range(size - 1): 
  
#         if nums[index] == value: 
#             return index 

#     return -1


# def main():
#     print(findValue([1,2,3,4,5,6,7], 6, 4))

# main()




def output_answer(found, index):

    if found:
        print("That name was found at subscript ", index)
    else:
        print("That name was not found in the array.")

def findName(names, found):
    index = 0
    searchValue = input("Enter a name to search for in the array. \n>>> ")

    while found == False and index <= len(names) - 1:
        if names[index].lower() == searchValue.lower():
            found = True
        else:
            index += 1
    if found:
        return index
    else:
        return found

def main():
    names = ["Sally", "Tom", "Sameer", "Rishika", "Fernando", "Camilio"]
    found = False
    index = findName(names, found)
    if index != False and index != 0:
        found = True
    output_answer(found, index)

main()