import random


def display_num_or_star(self, display):
    for num in self:
        if num in display:
            print(num, end='')
        else:
            print('*', end='')


def generate_rand_list():
    # Generate random list
    gen_count = 0
    rand_list = []

    while gen_count < 5:
        rand_int = str(random.randint(0, 9))
        if rand_int in rand_list:
            continue
        else:
            rand_list.append(rand_int)
            gen_count += 1

    return rand_list


def guess_the_number():
    count = 0
    display_list = []
    number_list = str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    cake = ''
    score = 0

    rand_list = generate_rand_list()

    # Begin game
    while count < 5:
        user_in = input('\nEnter a guessing number.\n >>> ')

        if user_in == '':
            print('You must enter a number')
            continue
        elif int(user_in) > 9:
            print('You number must be 9 or less.')
            continue
        elif user_in in rand_list:
            if user_in in display_list:
                print('Correct number already exists.')
                continue
            else:
                display_list.append(user_in)
                display_num_or_star(rand_list, display_list)

                print('\nYou got it! 🎂')
                count += 1
                score += 1
        else:
            display_num_or_star(rand_list, display_list)
            print('\nOh no, that was wrong!')
            count += 1

    for score in range(score + 1):
        if score > 0:
            cake += '🎂'

    print(f'\nThe number was: ', end='')

    for i in rand_list:
        print(i, end='')

    print(f'\nYour final score is: {score} {cake}')
