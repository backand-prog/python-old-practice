#  Question 3: Accept string from a user and display only those characters which are present at an even index number.

#
# def only_evens(str):
#     for i in range(0, len(str) - 1, 2):
#         print(len(str))
#         print("Index: [ ", i, " ] ", str[i])
#
#
# word_to_use = input("Add a string")
#
# only_evens(word_to_use)

str = "pynative"
for i in range(len(str)):
    if i % 2 == 0:
        print(str[i])