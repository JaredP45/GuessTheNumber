import random


class Error(Exception):
    pass


class ValueNotInRange(Error):
    pass


class DuplicateValue(Error):
    pass


def display_num_or_star(self, display):
    return_num_list = []
    for num in self:
        if num in display:
            return_num_list.append(num)
        else:
            return_num_list.append('*')
    return return_num_list


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
