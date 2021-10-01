import random

"""
generate random list of 5 num
take user input and compare to list
if not in list, output incorrect and if try again
if correct, output correct and ask if try again

ToDo:
    * Reduce redundancy
    * Reorganize/refactor code to follow OOP
"""

rand_list = []
display_list = []
number_list = str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
cake = ''
count = 0
score = 0

# Generate random list
while count < 5:
    rand_int = str(random.randint(0, 9))
    if rand_int in rand_list:
        continue
    else:
        rand_list.append(rand_int)
        count += 1

count = 0
# Begin game
while count < 5:
    user_in = input('\nEnter a guessing number.\n >>> ')
    if user_in not in number_list:
        print('You must enter a number')
        continue

    if user_in in rand_list:
        display_list.append(user_in)
        for num in rand_list:
            if num in display_list:
                print(num, end='')
            else:
                print('*', end='')

        print('\nYou got it! 🎂️')
        count += 1
        score += 1
    else:
        for num in rand_list:
            if num in display_list:
                print(num, end='')
            else:
                print('*', end='')
        print('\nOh no, that was wrong!')
        count += 1

for score in range(score + 1):
    if score > 0:
        cake += '🎂️'

print(f'\nThe number was: ', end='')
for i in rand_list: print(i, end='')
print(f'\nYour final score is: {score} {cake}')
