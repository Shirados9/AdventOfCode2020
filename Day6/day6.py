import os

dirName = os.path.dirname(__file__)
inputFile = os.path.join(dirName, "input.txt")


def part1(data):
    print("Part 1: ")
    counts = []
    for line in data:
        d = {}

        letters = line.replace("\n", "")

        for char in letters:
            if char in d.keys():
                d[char] += 1
            else:
                d[char] = 1
        print(len(d))
        counts.append(len(d))
    print(sum(counts))
    return


def part2(data):
    print("Part 2: ")
    return


def main():
    with open(inputFile) as file:
        data = file.read().split("\n\n")
        part1(data)
        part2(data)


if __name__ == "__main__":
    main()