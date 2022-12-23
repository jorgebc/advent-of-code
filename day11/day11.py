from decimal import Decimal
import math


def throwItem(fr0m, to, itemWorryLevel):
    fr0m["items"].pop(0)
    to["items"].append(itemWorryLevel)


def relief(worryLevel):
    return math.floor(worryLevel / 3)


def reelief(worryLevel):
    superModulo = 19 * 5 * 11 * 17 * 7 * 13 * 3 * 2
    return worryLevel % superModulo


def getFactoredNum(num):
    factors = []
    for i in range(1, 20):
        if num % i == 0:
            factors.append(i)

    product = 1
    for number in set(factors):
        product *= number

    return product


def inspectNextItemWorryLevel(monkey, withRelief):
    monkey["inspectedItems"] += 1
    item = monkey["items"][0]
    worryLevel = monkey["operation"](item)
    if withRelief:
        return relief(worryLevel)
    else:
        return reelief(worryLevel)


def monkeyToThrow(monkey, worryLevel):
    testValue = monkey["test"]

    if worryLevel % testValue == 0:
        return monkey["testTrueMonkey"]
    else:
        return monkey["testFalseMonkey"]


def turn(monkey, monkeys, withRelief):
    for numItem in range(len(monkey["items"])):
        itemWorryLevel = inspectNextItemWorryLevel(monkey, withRelief)
        toMonkey = monkeyToThrow(monkey, itemWorryLevel)
        throwItem(monkey, monkeys[toMonkey], itemWorryLevel)


def r0und(monkeys, withRelief):
    for monkey in monkeys:
        turn(monkey, monkeys, withRelief)


def printMonkeys(monkeys):
    for monkey in monkeys:
        print(monkey)
        print("\n")


def getHighestInspectedItemsCount(monkeys):
    highestInspectedItemsCount = []

    for monkey in monkeys:
        highestInspectedItemsCount.append(monkey["inspectedItems"])

    highestInspectedItemsCount.sort(reverse=True)
    return highestInspectedItemsCount[:2]


def calculateMonkeyBusinessLevel(monkeys, rounds, withRelief):

    for roundNum in range(rounds):
        print(roundNum)
        r0und(monkeys, withRelief)

    highestInspectedItemsCount = getHighestInspectedItemsCount(monkeys)
    print(highestInspectedItemsCount)
    return highestInspectedItemsCount[0] * highestInspectedItemsCount[1]
