#Question 1: Accept two integer numbers from a user and return their product and
# if the product is greater than 1000, then return their sum


def two_nums():
    first_num = None
    second_num = None
    while type(first_num) is not int:
        try:
            first_num = int(input("Type in the first number!"))
        except ValueError:
            pass
    while type(second_num) is not int:
        try:
            second_num = int(input("Type in the second number!"))
        except ValueError:
            pass

    nums = [first_num, second_num]
    return nums


def if_bigger_than_1000(nums):

    if nums[0] * nums[1] > 1000:
        to_print = nums[0] + nums[1]
    else:
        to_print = nums[0] * nums[1]
    return to_print


print(if_bigger_than_1000(two_nums()))
