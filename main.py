import random

"""
generate random list of 5 num
take user input and compare to list
if not in list, output incorrect and if try again
if correct, output correct and ask if try again

ToDo:
    * Display list of nums in [*****] format and incrementally show correct numbers as user takes input.

"""

rand_list = []
count = 0

for count in range(5):
    rand_int = random.randint(0, 5)
    rand_list.append(rand_int)
    count += 1

print(rand_list)

while True:
    try:
        user_in = int(input('Enter a guessing number.\n'))
    except ValueError:
        print("You must enter a number.\n")
        continue
    if user_in in rand_list:
        print('You got it! Go again? (Y/N)')
        user_in = str(input())
        if user_in == 'Y':
            continue
        elif user_in == 'N':
            break
        else:
            user_in = str(input("You need to enter (Y/N); Type \'okay\' to continue please."))
            while True:
                if user_in == 'okay':
                    break
                else:
                    user_in = str(input("You need to enter (Y/N); Type \'okay\' to continue please."))
                    continue
    else:
        print('Oh no, that was wrong! Go again? (Y/N)')
        user_in = str(input())
        if user_in == 'Y':
            continue
        elif user_in == 'N':
            break
        else:
            user_in = str(input("You need to enter (Y/N); Type \'okay\' to continue please."))
            while True:
                if user_in == 'okay':
                    break
                else:
                    user_in = str(input("You need to enter (Y/N); Type \'okay\' to continue please."))
                    continue
