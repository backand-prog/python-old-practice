# Question 2: Given a range of first 10 numbers, Iterate from start number to the end number
# and print the sum of the current number and previous number

def first_num():

    first_num = None

    while type(first_num) is not int:
        try:
            first_num = int(input("Type in the first number!"))
        except TypeError:
            pass

    return first_num


def iterate_for_10(first_num):
    for i in range(first_num, first_num + 10):
        print("Current number: ", i, " Previous number:", i - 1, "Sum: ", i + (i - 1))


iterate_for_10(first_num())
