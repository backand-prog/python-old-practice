import random

class QA:
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.corrAnsw = correctAnswer
        self.otherAns = otherAnswers


qaList = [
    QA("Bendi hány nadrággal jött le Balatonalmdáiba 3 napra?", "1", ["2", "4", "6"]),
    QA("Milyen hírességgel szexelt Barbi?", 'Éden Máté', ['Keanu Reaves', 'Orlando Bloom', 'Johnny Depp']),
    QA("Marci meleg vagy bisex?", "Igen", ["Bisex", "Meleg", "Egyik sem, mert hetero"])
]

corrCount = 0
random.shuffle(qaList)

print(qaList)

for qaItem in qaList:
    print(qaItem.question)
    print("Possible answers are:")
    possible = qaItem.otherAns + [qaItem.corrAnsw]
    random.shuffle(possible)

    count = 0

    while count < len(possible):
        print(str(count + 1) + ": " + possible[count])
        count += 1

    print("Please enter the number of your answer:")
    userAnsw = input()
    while not userAnsw.isdigit():
        print("That was not a nomber. Please enter the number of you answer:")
    userAnsw = int(userAnsw)
    while not (userAnsw > 0 and userAnsw <=len(possible)):
        print("That number doesn't correspond to any answer. Please enter the number of your answer")
        userAnsw = input()

    if possible[userAnsw-1] == qaItem.corrAnsw:
        print("Your answer was correct.")
        corrCount += 1
    else:
        print("Your answer was wrong.")
        print("Correct anwer was: " + qaItem.corrAnsw)
    print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
