# Part 1

def topCrates(input, stacks):

    orders = extractOrders(input)

    moveCrates(orders, stacks)
    print(stacks)

    topCratesCode = getTopCrates(stacks)
    print("Top crates are: " + topCratesCode)

    return topCratesCode


def extractOrders(lines):
    return map(extractOrder, lines.split("\n"))


def extractOrder(line):
    splited = line.split(" ")
    order = {
        "moves": int(splited[1]),
        "fr0m": int(splited[3]),
        "to": int(splited[5])
    }
    print(order)
    return order


def moveCrates(orders, stacks):
    for order in orders:
        executeOrder(order, stacks)


def executeOrder(order, stacks):
    moves, fr0m, to = order.values()
    if (moves == 0):
        return
    else:
        crate = stacks[fr0m-1].pop()
        stacks[to-1].append(crate)
        order["moves"] = moves-1
        executeOrder(order, stacks)


def getTopCrates(stacks):
    topCratesCode = ""
    for stack in stacks:
        topCratesCode += stack.pop()

    return topCratesCode


def printOrders(orders):
    for order in orders:
        print(order)


testData = []
testData.append(['Z', 'N'])
testData.append(['M', 'C', 'D'])
testData.append(['P'])

testInput = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

expectedResult = "CMZ"

assert topCrates(
    testInput, testData) == expectedResult, "Should be " + expectedResult

input = """move 5 from 3 to 6
move 2 from 2 to 5
move 1 from 9 to 1
move 1 from 3 to 1
move 5 from 7 to 5
move 2 from 9 to 8
move 1 from 2 to 8
move 1 from 4 to 2
move 8 from 1 to 6
move 4 from 6 to 9
move 1 from 2 to 1
move 2 from 4 to 8
move 2 from 8 to 4
move 3 from 7 to 5
move 6 from 5 to 3
move 1 from 1 to 8
move 1 from 5 to 7
move 5 from 6 to 9
move 3 from 5 to 8
move 2 from 4 to 3
move 1 from 7 to 8
move 2 from 8 to 6
move 2 from 1 to 8
move 8 from 3 to 8
move 11 from 6 to 3
move 1 from 4 to 7
move 1 from 3 to 7
move 2 from 6 to 1
move 7 from 9 to 7
move 10 from 3 to 5
move 1 from 9 to 3
move 2 from 9 to 5
move 5 from 5 to 2
move 19 from 8 to 6
move 1 from 9 to 6
move 1 from 3 to 8
move 4 from 2 to 6
move 1 from 1 to 4
move 5 from 8 to 9
move 1 from 2 to 1
move 6 from 7 to 2
move 3 from 5 to 8
move 3 from 8 to 1
move 2 from 9 to 6
move 1 from 7 to 8
move 6 from 2 to 7
move 1 from 4 to 8
move 3 from 8 to 4
move 2 from 1 to 5
move 7 from 7 to 6
move 1 from 7 to 2
move 3 from 4 to 6
move 2 from 9 to 2
move 1 from 1 to 8
move 2 from 1 to 3
move 1 from 8 to 7
move 3 from 2 to 5
move 5 from 5 to 8
move 4 from 5 to 3
move 1 from 7 to 8
move 2 from 8 to 1
move 1 from 8 to 5
move 5 from 3 to 5
move 13 from 5 to 1
move 1 from 3 to 4
move 2 from 8 to 3
move 3 from 1 to 4
move 1 from 3 to 1
move 1 from 8 to 1
move 5 from 1 to 9
move 1 from 3 to 7
move 2 from 9 to 6
move 2 from 1 to 7
move 3 from 1 to 5
move 3 from 1 to 5
move 1 from 6 to 1
move 4 from 4 to 3
move 3 from 9 to 1
move 5 from 1 to 7
move 7 from 7 to 8
move 1 from 3 to 9
move 28 from 6 to 8
move 5 from 5 to 9
move 6 from 6 to 1
move 4 from 1 to 8
move 5 from 9 to 1
move 12 from 8 to 7
move 1 from 3 to 8
move 6 from 1 to 4
move 5 from 4 to 1
move 3 from 6 to 4
move 2 from 3 to 4
move 3 from 1 to 5
move 6 from 7 to 1
move 2 from 4 to 9
move 2 from 5 to 4
move 19 from 8 to 1
move 4 from 9 to 5
move 5 from 4 to 3
move 4 from 1 to 4
move 5 from 5 to 1
move 3 from 8 to 5
move 7 from 7 to 3
move 14 from 1 to 8
move 5 from 4 to 2
move 12 from 8 to 7
move 1 from 3 to 6
move 3 from 5 to 9
move 1 from 7 to 8
move 8 from 1 to 2
move 5 from 1 to 2
move 9 from 3 to 4
move 8 from 4 to 6
move 2 from 1 to 9
move 3 from 6 to 1
move 5 from 6 to 7
move 14 from 7 to 1
move 1 from 4 to 7
move 6 from 8 to 2
move 14 from 1 to 4
move 13 from 4 to 9
move 2 from 3 to 5
move 3 from 1 to 7
move 1 from 8 to 4
move 1 from 4 to 1
move 1 from 1 to 3
move 1 from 3 to 4
move 1 from 4 to 1
move 1 from 6 to 9
move 1 from 7 to 6
move 1 from 4 to 5
move 11 from 9 to 3
move 6 from 3 to 8
move 5 from 3 to 1
move 2 from 8 to 4
move 1 from 6 to 2
move 7 from 9 to 2
move 1 from 7 to 2
move 1 from 9 to 8
move 2 from 8 to 6
move 30 from 2 to 3
move 2 from 7 to 2
move 2 from 8 to 2
move 3 from 8 to 7
move 6 from 2 to 5
move 1 from 2 to 5
move 3 from 1 to 8
move 2 from 6 to 7
move 1 from 1 to 9
move 1 from 9 to 3
move 7 from 3 to 1
move 6 from 7 to 8
move 8 from 3 to 9
move 7 from 9 to 1
move 1 from 5 to 8
move 7 from 5 to 9
move 2 from 4 to 2
move 11 from 3 to 6
move 2 from 2 to 7
move 11 from 1 to 8
move 2 from 5 to 4
move 11 from 6 to 4
move 12 from 4 to 9
move 4 from 1 to 5
move 3 from 7 to 9
move 12 from 8 to 4
move 1 from 1 to 7
move 6 from 8 to 3
move 2 from 3 to 5
move 3 from 8 to 4
move 3 from 3 to 7
move 9 from 9 to 7
move 5 from 3 to 9
move 1 from 3 to 2
move 13 from 7 to 5
move 1 from 2 to 6
move 1 from 6 to 1
move 1 from 1 to 6
move 16 from 4 to 5
move 1 from 5 to 6
move 16 from 5 to 4
move 13 from 4 to 5
move 3 from 4 to 2
move 1 from 6 to 7
move 3 from 2 to 1
move 8 from 5 to 2
move 3 from 1 to 4
move 1 from 7 to 9
move 14 from 5 to 1
move 10 from 1 to 5
move 1 from 2 to 8
move 19 from 9 to 1
move 1 from 9 to 1
move 6 from 2 to 7
move 4 from 1 to 7
move 1 from 8 to 6
move 16 from 5 to 3
move 1 from 5 to 4
move 2 from 5 to 2
move 1 from 5 to 6
move 1 from 6 to 5
move 1 from 2 to 4
move 7 from 7 to 2
move 4 from 4 to 7
move 2 from 6 to 2
move 8 from 2 to 9
move 4 from 9 to 2
move 16 from 3 to 7
move 4 from 9 to 7
move 14 from 1 to 3
move 26 from 7 to 8
move 1 from 5 to 4
move 20 from 8 to 4
move 5 from 1 to 8
move 2 from 4 to 6
move 4 from 3 to 2
move 1 from 6 to 5
move 8 from 2 to 4
move 1 from 6 to 5
move 1 from 7 to 8
move 8 from 3 to 1
move 6 from 1 to 9
move 1 from 3 to 6
move 14 from 4 to 1
move 1 from 3 to 8
move 2 from 2 to 1
move 1 from 6 to 8
move 1 from 2 to 8
move 5 from 8 to 1
move 2 from 1 to 6
move 2 from 5 to 9
move 1 from 6 to 3
move 1 from 6 to 1
move 5 from 9 to 2
move 5 from 4 to 1
move 5 from 4 to 2
move 16 from 1 to 8
move 9 from 1 to 4
move 24 from 8 to 6
move 1 from 8 to 7
move 7 from 6 to 5
move 1 from 3 to 4
move 3 from 1 to 8
move 3 from 5 to 8
move 10 from 4 to 8
move 3 from 4 to 6
move 1 from 7 to 4
move 20 from 6 to 7
move 1 from 4 to 9
move 1 from 4 to 9
move 7 from 2 to 3
move 13 from 8 to 9
move 4 from 5 to 9
move 4 from 8 to 5
move 18 from 9 to 2
move 14 from 7 to 5
move 6 from 3 to 8
move 1 from 3 to 2
move 1 from 8 to 6
move 4 from 8 to 2
move 1 from 2 to 3
move 17 from 5 to 3
move 18 from 3 to 5
move 6 from 7 to 2
move 3 from 9 to 7
move 1 from 8 to 6
move 5 from 2 to 5
move 26 from 2 to 7
move 1 from 6 to 9
move 29 from 7 to 9
move 15 from 5 to 2
move 1 from 6 to 7
move 8 from 9 to 2
move 14 from 2 to 6
move 16 from 9 to 1
move 6 from 9 to 1
move 1 from 7 to 1
move 3 from 2 to 1
move 5 from 2 to 6
move 15 from 1 to 4
move 1 from 2 to 8
move 1 from 9 to 7
move 1 from 8 to 6
move 19 from 6 to 7
move 10 from 1 to 8
move 4 from 8 to 3
move 1 from 7 to 5
move 3 from 5 to 3
move 13 from 7 to 6
move 2 from 8 to 9
move 7 from 3 to 6
move 5 from 5 to 3
move 1 from 1 to 6
move 2 from 5 to 1
move 4 from 4 to 8
move 7 from 8 to 7
move 8 from 7 to 3
move 1 from 8 to 4
move 2 from 9 to 2
move 8 from 6 to 5
move 1 from 4 to 5
move 4 from 5 to 4
move 2 from 2 to 8
move 9 from 4 to 5
move 2 from 1 to 9
move 2 from 8 to 9
move 14 from 6 to 4
move 5 from 3 to 4
move 3 from 9 to 7
move 3 from 5 to 3
move 2 from 4 to 8
move 2 from 4 to 7
move 2 from 8 to 9
move 4 from 5 to 8
move 16 from 4 to 6
move 1 from 9 to 6
move 3 from 7 to 5
move 7 from 7 to 5
move 10 from 5 to 1
move 6 from 3 to 8
move 2 from 9 to 3
move 3 from 6 to 9
move 3 from 3 to 6
move 2 from 1 to 7
move 13 from 6 to 2
move 2 from 4 to 5
move 2 from 7 to 6
move 2 from 6 to 7
move 2 from 4 to 1
move 3 from 9 to 5
move 1 from 1 to 4
move 3 from 2 to 5
move 2 from 4 to 1
move 2 from 3 to 2
move 5 from 8 to 5
move 1 from 7 to 2
move 1 from 7 to 1
move 1 from 3 to 5
move 1 from 8 to 7
move 1 from 6 to 7
move 1 from 3 to 5
move 12 from 5 to 6
move 6 from 6 to 2
move 1 from 7 to 4
move 1 from 5 to 7
move 2 from 8 to 9
move 1 from 9 to 6
move 1 from 8 to 9
move 5 from 6 to 9
move 1 from 8 to 1
move 14 from 2 to 4
move 1 from 7 to 1
move 1 from 7 to 2
move 3 from 2 to 3
move 2 from 3 to 4
move 1 from 2 to 4
move 4 from 6 to 2
move 8 from 5 to 8
move 15 from 4 to 8
move 3 from 4 to 8
move 7 from 8 to 4
move 6 from 1 to 3
move 1 from 6 to 1
move 5 from 4 to 8
move 7 from 9 to 1
move 1 from 5 to 6
move 4 from 2 to 6
move 10 from 1 to 8
move 29 from 8 to 3
move 1 from 4 to 5
move 1 from 4 to 6
move 6 from 1 to 4
move 1 from 5 to 8
move 3 from 4 to 2
move 27 from 3 to 7
move 18 from 7 to 9
move 5 from 6 to 3
move 7 from 7 to 4
move 1 from 7 to 8
move 9 from 3 to 5
move 5 from 3 to 6
move 3 from 4 to 2
move 1 from 7 to 2
move 2 from 8 to 4
move 2 from 8 to 6
move 2 from 8 to 6
move 8 from 2 to 1
move 7 from 5 to 4
move 1 from 8 to 9
move 4 from 1 to 5
move 1 from 2 to 9
move 8 from 6 to 3
move 3 from 1 to 8
move 1 from 1 to 7
move 8 from 3 to 6
move 2 from 8 to 3
move 1 from 3 to 6
move 4 from 6 to 7
move 16 from 4 to 2
move 1 from 3 to 5
move 2 from 6 to 4
move 1 from 2 to 3
move 2 from 7 to 3
move 2 from 7 to 8
move 3 from 6 to 7
move 4 from 5 to 2
move 2 from 4 to 2
move 4 from 9 to 8
move 3 from 5 to 1
move 3 from 1 to 6
move 6 from 9 to 1
move 4 from 7 to 9
move 8 from 9 to 5
move 4 from 5 to 2
move 7 from 8 to 6
move 11 from 6 to 8
move 4 from 1 to 2
move 3 from 8 to 9
move 5 from 8 to 7
move 2 from 1 to 6
move 4 from 5 to 6
move 2 from 7 to 9
move 2 from 7 to 3
move 5 from 6 to 2
move 4 from 3 to 1
move 1 from 7 to 2
move 1 from 3 to 2
move 2 from 6 to 7
move 1 from 1 to 6
move 6 from 9 to 6
move 1 from 7 to 6
move 1 from 7 to 6
move 2 from 1 to 7
move 2 from 8 to 6
move 4 from 9 to 2
move 17 from 2 to 6
move 1 from 9 to 4
move 1 from 1 to 3
move 1 from 4 to 1
move 20 from 2 to 8
move 2 from 7 to 6
move 2 from 2 to 5
move 1 from 3 to 1
move 1 from 2 to 5
move 6 from 8 to 6
move 2 from 5 to 6
move 3 from 6 to 4
move 1 from 1 to 4
move 15 from 8 to 2
move 11 from 2 to 9
move 1 from 1 to 3
move 10 from 9 to 4
move 1 from 9 to 8
move 12 from 6 to 3
move 1 from 8 to 7
move 1 from 5 to 4
move 8 from 4 to 7
move 5 from 3 to 4
move 7 from 6 to 4
move 3 from 3 to 6
move 3 from 3 to 2
move 1 from 3 to 6
move 17 from 4 to 3
move 1 from 3 to 4
move 2 from 4 to 9
move 14 from 3 to 6
move 2 from 2 to 7
move 1 from 4 to 9
move 8 from 7 to 6
move 1 from 3 to 4
move 9 from 6 to 2
move 1 from 4 to 2
move 26 from 6 to 2
move 27 from 2 to 6
move 10 from 2 to 4
move 1 from 7 to 6
move 28 from 6 to 2
move 21 from 2 to 4
move 2 from 6 to 7
move 3 from 2 to 1
move 5 from 6 to 5
move 3 from 5 to 2
move 1 from 7 to 4
move 11 from 2 to 4
move 21 from 4 to 9
move 1 from 5 to 8
move 1 from 8 to 6
move 18 from 9 to 7
move 1 from 5 to 7
move 3 from 9 to 8
move 1 from 6 to 7
move 1 from 3 to 5
move 1 from 8 to 3
move 22 from 7 to 5
move 13 from 5 to 1
move 16 from 4 to 5
move 3 from 1 to 4
move 2 from 3 to 9
move 3 from 9 to 7
move 6 from 4 to 6
move 1 from 4 to 2
move 2 from 7 to 3"""

stacks = []
stacks.append(['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'])
stacks.append(['N', 'B', 'L'])
stacks.append(['J', 'C', 'H', 'T', 'L', 'V'])
stacks.append(['S', 'P', 'J', 'W'])
stacks.append(['Z', 'S', 'C', 'F', 'T', 'L', 'R'])
stacks.append(['W', 'D', 'G', 'B', 'H', 'N', 'Z'])
stacks.append(['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'])
stacks.append(['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'])
stacks.append(['R', 'P', 'M', 'L', 'H'])

topCrates(input, stacks)


# Part 2

def executeOrder(order, stacks):
    moves, fr0m, to = order.values()
    movingCrates = []
    for i in range(moves):
        movingCrates.insert(0, stacks[fr0m-1].pop())

    print(movingCrates)
    stacks[to-1].extend(movingCrates)


testData = []
testData.append(['Z', 'N'])
testData.append(['M', 'C', 'D'])
testData.append(['P'])

testInput = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

expectedResult = "MCD"

assert topCrates(
    testInput, testData) == expectedResult, "Should be " + expectedResult

stacks = []
stacks.append(['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'])
stacks.append(['N', 'B', 'L'])
stacks.append(['J', 'C', 'H', 'T', 'L', 'V'])
stacks.append(['S', 'P', 'J', 'W'])
stacks.append(['Z', 'S', 'C', 'F', 'T', 'L', 'R'])
stacks.append(['W', 'D', 'G', 'B', 'H', 'N', 'Z'])
stacks.append(['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'])
stacks.append(['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'])
stacks.append(['R', 'P', 'M', 'L', 'H'])

topCrates(input, stacks)
