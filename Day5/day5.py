import os

dirName = os.path.dirname(__file__)
inputFile = os.path.join(dirName, "input.txt")


def part1(data):
    print("Part 1: ")
    print("The highest seat ID is {}".format(max(data)))
    return


def part2(data):
    print("Part 2: ")
    for c, id in enumerate(data):
        if id == data[c + 1] - 2:
            print("Your seat ID is {}".format(id + 1))
            return
    return


def convertToBinaryString(text):
    ret = []
    for char in text:
        if char == "F" or char == "L":
            ret.append("0")
        elif char == "B" or char == "R":
            ret.append("1")
    return "".join(ret)


def main():
    with open(inputFile) as file:
        data = file.read().splitlines()
        seatIdList = []
        for line in data:
            row = int(convertToBinaryString(line[:7]), 2)
            column = int(convertToBinaryString(line[7:]), 2)

            seatId = row * 8 + column
            seatIdList.append(seatId)
        seatIdList.sort()
        part1(seatIdList)
        part2(seatIdList)


if __name__ == "__main__":
    main()