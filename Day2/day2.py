import os
from operator import xor

dirName = os.path.dirname(__file__)
inputFile = os.path.join(dirName, 'input.txt')

def part1(data):
    print("Part 1: ")
    validPasswords = 0
    
    for line in data:
        splitted = line.split(" ")
        amount = splitted[0].split('-')
        letter = splitted[1][0]
        password = splitted[2]

        occuranceOfChars = password.count(letter)
        amountMin = int(amount[0])
        amountMax = int(amount[1])

        if occuranceOfChars in range(amountMin, amountMax + 1):
            validPasswords += 1
    print("There are {} correct passwords!".format(validPasswords))
    return

def part2(data):
    print("Part 2: ")
    validPasswords = 0
    
    for line in data:
        splitted = line.split(" ")
        position = splitted[0].split('-')
        letter = splitted[1][0]
        password = splitted[2]

        firstPosition = int(position[0]) - 1
        secondPosition = int(position[1]) - 1

        if xor(password[firstPosition] == letter, password[secondPosition] == letter):
            validPasswords += 1
    print("There are {} correct passwords!".format(validPasswords))
    return


def main():
    with open(inputFile) as file:
        data = file.read().splitlines()
        part1(data)
        part2(data)

if __name__ == "__main__":
    main()