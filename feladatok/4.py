# Question 4: Given a string and an integer number n, remove
# characters from a string starting from zero up to n and return a new string


def get_str():
    str = input("Give a string!")

    return str


def get_num():

    number = None

    while type(number) is not int:
        try:
            number = int(input("Give a num!"))
        except ValueError:
            pass

    return number


def remove_chars():

    string_to_cut = get_str()
    number_of_chars = len(string_to_cut) + 1

    while number_of_chars >= len(string_to_cut):
        number_of_chars = get_num()

        if number_of_chars >= len(string_to_cut):
            print("Number of characters must be less than length of the string!")

    new_string = string_to_cut[number_of_chars:]

    return new_string


print(remove_chars())
