import os

dirName = os.path.dirname(__file__)
inputFile = os.path.join(dirName, 'input.txt')

def part1(data):
    print("Part 1: ")
    x, y, trees = 0, 0, 0

    for line in data:
        lineLength = len(line)
        currentPosition = line[x%lineLength]
        if currentPosition == "#":
            trees += 1
        x += 3
        y += 1

    print("Number of trees encountered: {}".format(trees))
    return

def part2(data):
    print("Part 2: ")
    x, y = [0,0,0,0,0], [0,0,0,0,0]
    moves = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    trees = [0,0,0,0,0]

    for i, line in enumerate(data):
        lineLength = len(line)

        for j, move in enumerate(moves):
            if j == 4 and i % 2 != 0:
                continue

            currentX = x[j]
            currentY = y[j]

            currentPosition = line[currentX%lineLength]
            if currentPosition == "#":
                trees[j] += 1

            x[j] += int(move[0])
            y[j] += int(move[1])

    print("Number of trees: {}".format(trees))

    result = 1
    for tree in trees:
        result *= tree

    print("Trees multiplied together: {}".format(result))
    return

def main():
    with open(inputFile) as file:
        data = file.read().splitlines()
        part1(data)
        part2(data)

if __name__ == "__main__":
    main()