instructionCycles = {"noop": 1, "addx": 2}


def getInstructionCyclesToFinish(instruction):
    instructionType = instruction.split(" ")[0]
    return instructionCycles[instructionType]


def executeInstruction(instruction, register):
    # print(f"Instruction {instruction}")
    instruction = instruction.split(" ")

    if instruction[0] == "addx":
        register["value"] += int(instruction[1])
        # print(register)


def sumSignalStrengths(input):

    instructions = input.split("\n")
    registerX = {"value": 1}
    interestingSignalCycles = [20, 60, 100, 140, 180, 220]
    signalStrength = 0

    actualCycle = 1
    while len(instructions) > 0:

        instruction = instructions.pop(0)
        cyclesToFinish = getInstructionCyclesToFinish(instruction)
        for cycle in range(cyclesToFinish):
            if actualCycle in interestingSignalCycles:
                # print(f"Cycle {actualCycle}, register: {registerX}")
                signalStrength += actualCycle * registerX["value"]
            actualCycle += 1

        executeInstruction(instruction, registerX)

    return signalStrength


def shouldPixelBeDrown(position, registerValue):
    registerPixelsValues = [registerValue - 1, registerValue, registerValue + 1]
    return position in registerPixelsValues


def drawPixel(row, col, shouldDrawPixel, image):
    if shouldDrawPixel:
        image[row][col] = "#"


def createImage(height, width):
    image = []
    for rowNum in range(height):
        col = []
        for colNum in range(width):
            col.append(".")
        image.append(col)

    return image


def printImage(image):
    for row in image:
        print("".join(row))


def renderImage(input):
    instructions = input.split("\n")
    registerX = {"value": 1}

    imageHeight = 6
    imageWidth = 40
    image = createImage(imageHeight, imageWidth)

    actualCycle = 1
    while len(instructions) > 0:

        instruction = instructions.pop(0)
        cyclesToFinish = getInstructionCyclesToFinish(instruction)

        for cycle in range(cyclesToFinish):
            row = int((actualCycle - 1) / imageWidth)
            col = (actualCycle - 1) % imageWidth
            # print(f"drawing cycle {actualCycle} row {row} col {col}")
            shouldDrawPixel = shouldPixelBeDrown(col, registerX["value"])
            drawPixel(row, col, shouldDrawPixel, image)
            actualCycle += 1

        executeInstruction(instruction, registerX)

    printImage(image)
