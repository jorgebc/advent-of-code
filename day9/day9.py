def moveHead(direction, head):
    if direction == "U":
        head["y"] += 1

    if direction == "R":
        head["x"] += 1

    if direction == "D":
        head["y"] -= 1

    if direction == "L":
        head["x"] -= 1


def calculateMove(head, tail):
    distanceX = int(head["x"] - tail["x"])
    distanceY = int(head["y"] - tail["y"])

    if (
        abs(distanceX) == 1
        and abs(distanceY) == 1
        or abs(distanceX) == 0
        and abs(distanceY) == 0
    ):
        return {"x": 0, "y": 0}

    if abs(distanceX) == 0 or abs(distanceY) == 0:
        if abs(distanceX) == 1 or abs(distanceY) == 1:
            return {"x": 0, "y": 0}

        if distanceX != 0:
            if distanceX > 1:
                return {"x": 1, "y": 0}
            elif distanceX < -1:
                return {"x": -1, "y": 0}

        elif distanceY != 0:
            if distanceY > 1:
                return {"x": 0, "y": 1}
            if distanceY < -1:
                return {"x": 0, "y": -1}

    return {
        "x": int(distanceX / abs(distanceX)),
        "y": int(distanceY / abs(distanceY)),
    }


def moveTail(head, tail, tailSteps):

    move = calculateMove(head, tail)

    tail["x"] += move["x"]
    tail["y"] += move["y"]

    position = str(tail["x"]) + "|" + str(tail["y"])
    if position not in tailSteps:
        # print(position)
        tailSteps.append(position)


def calculateTailVisitedPositions(input):
    headMoves = input.split("\n")

    head = {
        "x": 0,
        "y": 0,
    }

    tail = {
        "x": 0,
        "y": 0,
    }

    tailSteps = []

    for move in headMoves:
        direction, steps = move.split(" ")
        for step in range(int(steps)):
            moveHead(direction, head)
            moveTail(head, tail, tailSteps)

    return len(tailSteps)


def moveTailV2(head, tail):

    move = calculateMove(head, tail)

    tail["x"] += move["x"]
    tail["y"] += move["y"]

    return str(tail["x"]) + "|" + str(tail["y"])


def calculateTailVisitedPositionsV2(input, knots):
    headMoves = input.split("\n")

    rope = []
    for knot in range(knots):
        rope.append(
            {
                "x": 0,
                "y": 0,
            }
        )

    tailSteps = []

    for move in headMoves:
        direction, steps = move.split(" ")

        for step in range(int(steps)):
            # printRope(rope)
            # print(f"\n")
            moveHead(direction, rope[0])
            # print(f"head {rope[0]}")

            for knot in range(1, knots):
                # print(knot)
                # print(f"head tail {rope[knot-1]}")
                # print(f"tail {rope[knot]}")
                position = moveTailV2(rope[knot - 1], rope[knot])

                isTail = knot == knots - 1
                if isTail:
                    if position not in tailSteps:
                        # print(position)
                        tailSteps.append(position)

    return len(tailSteps)


def printRope(rope):
    print(rope)
