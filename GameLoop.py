import random


class Error(Exception):
    """
    Base Class for exceptions
    """
    pass


class ValueNotInRange(Error):
    """
    This will be raised when value is not within 0-9 range.
    """
    pass


class DuplicateValue(Error):
    """
    This will be raised when a duplicate value is found.
    """
    pass


def display_num_or_star(self, display):
    """
    Will display either a number or star if value is in
    random_list and is not a duplicate.
    """
    return_num_list = []
    for num in self:
        if num in display:
            return_num_list.append(num)
        else:
            return_num_list.append('*')
    return return_num_list


def generate_rand_list():
    """
    Generates a rand_list that user guesses against
    """
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
