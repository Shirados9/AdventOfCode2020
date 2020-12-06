import os
import re

dirName = os.path.dirname(__file__)
inputFile = os.path.join(dirName, "input.txt")


def part1(data):
    print("Part 1: ")
    valid = 0

    for entry in data:
        if containsRequiredFields(entry):
            valid += 1
    print("Found {} valid passports!".format(valid))
    return


def part2(data):
    print("Part 2: ")
    valid = 0
    for entry in data:
        if containsRequiredFields(entry) and validate(entry):
            valid += 1
    print("Found {} valid passports!".format(valid))
    return


def containsRequiredFields(entry):
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for field in requiredFields:
        if field not in entry.keys():
            return False
    return True


def validate(entry):
    isValid = True

    if "byr" in entry.keys():
        year = int(entry["byr"])
        isValid = year >= 1920 and year <= 2002

    if "iyr" in entry.keys() and isValid:
        year = int(entry["iyr"])
        isValid = year >= 2010 and year <= 2020

    if "eyr" in entry.keys() and isValid:
        year = int(entry["eyr"])
        isValid = year >= 2020 and year <= 2030

    if "hgt" in entry.keys() and isValid:
        height = entry["hgt"]

        if height[-2:] == "cm":
            heightInt = int(height[:-2])
            isValid = heightInt >= 150 and heightInt <= 193

        elif height[-2:] == "in":
            heightInt = int(height[:-2])
            isValid = heightInt >= 59 and heightInt <= 76

        else:
            isValid = False

    if "hcl" in entry.keys() and isValid:
        hairColor = entry["hcl"]
        if re.search("^#[0-9a-fA-F]{6}$", hairColor):
            isValid = True
        else:
            isValid = False

    if "ecl" in entry.keys() and isValid:
        eyeColor = entry["ecl"]
        isValid = (
            eyeColor == "amb"
            or eyeColor == "blu"
            or eyeColor == "brn"
            or eyeColor == "gry"
            or eyeColor == "grn"
            or eyeColor == "hzl"
            or eyeColor == "oth"
        )

    if "pid" in entry.keys() and isValid:
        passportID = entry["pid"]
        isValid = len(passportID) == 9 and passportID.isnumeric()
    else:
        return False

    return isValid


def cleanInputData():
    with open(inputFile) as file:
        data = file.read().split("\n\n")
        cleanData = []

        for line in data:
            entry = line.replace("\n", " ")
            entry = entry.split(" ")
            dict = {}

            for field in entry:
                pairs = field.split(":")
                dict[pairs[0]] = pairs[1]
            cleanData.append(dict)

    # c = open(os.path.join(dirName, 'cleanInput.txt'), "w")
    # c.write(str(cleanData))
    return cleanData


def main():

    part1(cleanInputData())
    part2(cleanInputData())


if __name__ == "__main__":
    main()