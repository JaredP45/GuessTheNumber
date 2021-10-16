from GameLoop import guess_the_number

"""
generate random list of 5 num
take user input and compare to list
if not in list, output incorrect and ask if try again
if correct, output correct and ask if try again

ToDo:
    * Fix game loop where user can enter same correct number and 
        score still increments.
"""

if __name__ == '__main__':
    guess_the_number()

    user_input = input('\nWould you like to play again? y/n\n')
    while user_input != 'q':
        if user_input == 'y' or user_input == 'yes':
            guess_the_number()
        elif user_input == 'n' or user_input == 'no' or user_input == 'q':
            break
        else:
            print('Enter the correct value please.')
        user_input = input('Would you like to play again? y/n')
