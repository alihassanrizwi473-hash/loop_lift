print("well come to the arfa tower")
i = 0
previous_floor = 0
while True:
    i += 1

    
    number = int(input("please enter the number of floor:-"))
    
    if previous_floor < number:
        print("going up")
    elif previous_floor > number:
        print("going down")
    else:
        print("you are already on this floor")

    if number == 1:
        print("you are already on first floor ")
        previous_floor = number
    elif number == 2:
        print("you are on second floor ")
        previous_floor = number
    elif number == 3:
        print("you are on third floor ")
        previous_floor = number
    elif number == 4:
        print("you are on 4th floor ")
        previous_floor = number
    elif number == 5:
        print("you are on 5th floor ")
        previous_floor = number
    elif number == 6:
        print("you are on 6th floor ")
        previous_floor = number
    elif number == 7:
        print("you are on 7th floor ")
        previous_floor = number
    elif number == 8:
        print("you are on 8th floor ")
        previous_floor = number
    elif number == 9:
        print("you are on 9th floor ")
        previous_floor = number
    elif number == 10:
        print("you are on 10th floor ")
        previous_floor = number
    elif number == 11:
        print("you are on 11th floor ")
        previous_floor = number
    elif number == 12:
        print("you are on 12th floor ")
        previous_floor = number
    elif number == 13:
        print("you are on 13th floor ")
        previous_floor = number
    elif number == 14:
        print("you are on 14th floor ")
        previous_floor = number
    elif number == 15:
        print("you are on 15th floor ")
        previous_floor = number
    elif number == 16:
        print("you are on 16th floor ")
        previous_floor = number
    elif number == 17:
        print("you are on 17th floor ")
        previous_floor = number
    else:
        print("go to down the lift.")


