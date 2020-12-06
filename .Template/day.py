import os

dirName = os.path.dirname(__file__)
inputFile = os.path.join(dirName, 'input.txt')

def part1(data):
    print("Part 1: ")
    return

def part2(data):
    print("Part 2: ")
    return

def main():
    with open(inputFile) as file:
        data = file.read().splitlines()
        part1(data)
        part2(data)

if __name__ == "__main__":
    main()