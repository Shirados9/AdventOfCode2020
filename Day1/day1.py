import os

dirName = os.path.dirname(__file__)
inputFile = os.path.join(dirName, "input.txt")


def part1(data):
    print("Part 1: ")
    for line1 in data:
        nr1 = int(line1)
        if nr1 > 2020:
            continue
        for line2 in data:
            nr2 = int(line2)
            if nr2 > 2020:
                continue
            if nr1 + nr2 == 2020:
                solution = nr1 * nr2
                print("The solution is {}.".format(solution))
                return


def part2(data):
    print("Part 2: ")
    for line1 in data:
        nr1 = int(line1)
        if nr1 > 2020:
            continue
        for line2 in data:
            nr2 = int(line2)
            if nr2 > 2020:
                continue
            for line3 in data:
                nr3 = int(line3)
                if nr3 > 2020:
                    continue
                if nr1 + nr2 > 2020:
                    continue
                if nr1 + nr2 + nr3 == 2020:
                    solution = nr1 * nr2 * nr3
                    print("The solution is {}.".format(solution))
                    return


def main():
    with open(inputFile) as file:
        data = file.read().splitlines()
        part1(data)
        part2(data)


if __name__ == "__main__":
    main()