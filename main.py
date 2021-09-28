import random

"""
generate random list of 5 num
take user input and compare to list
if not in list, output incorrect and if try again
if correct, output correct and ask if try again

ToDo:
    * Fix display numbers [*****] where guessing number duplicates don't exist.
    * If the number of guessed numbers is 5, then program completes.

"""
rand_list = []
display_list = []
count = 0

while len(rand_list) < 5:
    rand_int = random.randint(0, 9)
    if rand_int not in rand_list:
        rand_list.append(rand_int)

while True:
    try:
        user_in = int(input('Enter a guessing number.\n >>> '))
    except ValueError:
        print("You must enter a number.\n >>> ")
        continue

    if user_in in rand_list:
        display_list.append(user_in)

        for num in rand_list:
            if num in display_list:
                print(num, end='')
            else:
                print('*', end='')

        print('\nYou got it! 🎂️ Go again? (Y/N)\n >>> ')
        user_in = str(input())
        if user_in == 'Y':
            continue
        elif user_in == 'N':
            break
        else:
            user_in = str(input("You need to enter (Y/N); Type \'okay\' to continue please. \n >>> "))
            while True:
                if user_in == 'okay':
                    break
                else:
                    user_in = str(input("You need to enter (Y/N); Type \'okay\' to continue please. \n >>> "))
                    continue
    else:
        print('\nOh no, that was wrong! Go again? (Y/N)\n >>> ')

        for num in rand_list:
            if num in display_list:
                print(num, sep='-', end='')
            else:
                print('*', sep='-', end='')

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
