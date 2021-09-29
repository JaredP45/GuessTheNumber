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
cake = ''
score = 0

# Generate random list
while len(rand_list) < 5:
    rand_int = str(random.randint(0, 9))
    if rand_int not in rand_list:
        rand_list.append(rand_int)

# Begin game
for i in range(5):
    user_in = input('Enter a guessing number.\n >>> ')
    if user_in in rand_list:
        display_list.append(user_in)
        for num in rand_list:
            if num in display_list:
                print(num, end='')

        print('\nYou got it! 🎂️')
        score += 1
    else:
        for num in rand_list:
            print('*', end='')

        print('\nOh no, that was wrong!')

for score in range(score + 1):
    if score > 0:
        cake += '🎂️'

print(f'Your final score is: { score } { cake }')
