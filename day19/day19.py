from operator import itemgetter

# Creates the robot creation planification based on a robot factory blueprint.
#
# @param blueprint the robot factory blueprint
#
def createRobotPlanification(blueprint):
    return {"ore": 0, "clay": 4, "obsidian": 2}


# Check if a robot can be created with the available resources
#
# @param type robot type
# @param resources actual resources
# @param blueprint robot factory blueprint
#
def canCreateRobot(type, resources, blueprint):

    robotCosts = blueprint[type]
    robotResourceTypes = robotCosts.keys()

    robotCanBeCreated = True

    for resourceType in robotResourceTypes:
        resourceAmountNeeded = robotCosts[resourceType]
        resourceAmount = resources[resourceType]
        robotCanBeCreated = resourceAmount >= resourceAmountNeeded

    if robotCanBeCreated:
        print(f"Spend xxxx to start building a {type}-collecting robot.")

    return robotCanBeCreated


def adjustResources(resources, robotTypeConstructed, blueprint):
    if robotTypeConstructed != "none":

        robotCosts = blueprint[robotTypeConstructed]
        robotResourceTypes = robotCosts.keys()

        for resourceType in robotResourceTypes:
            resourceAmountNeeded = robotCosts[resourceType]
            resources[resourceType] -= resourceAmountNeeded


def adjustRobotPlanification(robotPlanification, robotTypeToConstruct):
    if robotTypeToConstruct != "none" and robotTypeToConstruct != "geode":
        robotPlanification[robotTypeToConstruct] -= 1


# Calculates the next robot that should be created,
# based on the available resources and robot creation planification.
# Creates the robot if possible and updates the available resources.
#
# @param resources actual resources
# @param robotPlanification robot creation planification
# @param blueprint robot factory blueprint
#
def createRobot(resources, robotPlanification, blueprint):

    ore, clay, obsidian = itemgetter("ore", "clay", "obsidian")(robotPlanification)
    robotTypeToConstruct = "none"

    if ore > 0:
        if canCreateRobot("ore", resources, blueprint):
            robotTypeToConstruct = "ore"

    elif clay > 0:
        if canCreateRobot("clay", resources, blueprint):
            robotTypeToConstruct = "clay"

    elif obsidian > 0:
        if canCreateRobot("obsidian", resources, blueprint):
            robotTypeToConstruct = "obsidian"

    elif canCreateRobot("geode", resources, blueprint):
        robotTypeToConstruct = "geode"

    adjustResources(resources, robotTypeToConstruct, blueprint)
    adjustRobotPlanification(robotPlanification, robotTypeToConstruct)

    return robotTypeToConstruct


#
# Updates the resources with the collected resources in one minute.
#
# @param robots available robots
# @param resources actual resources
#
def collectResources(robots, resources):
    robotTypes = robots.keys()

    for type in robotTypes:
        numRobots = robots[type]
        resources[type] += numRobots

        if numRobots > 0:
            print(
                f"{numRobots} {type}-collecting robot collects {numRobots} {type}; you now have {resources[type]} {type}."
            )


#
# Adds a new robot to the extraction line.
#
# @param robots available robots
# @param type the robot type to be created
#
def addRobotToLine(robots, type):

    if type == "none":
        return

    robots[type] += 1

    print(
        f"The new {type}-collecting robot is ready; you now have {robots[type]} of them."
    )


def runProduction(blueprint):

    productionTime = 24
    resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}

    robotPlanification = createRobotPlanification(blueprint)

    for minute in range(productionTime):
        print(f"== Minute {minute+1} ==")

        if minute + 1 != productionTime:
            robotTypeCreated = createRobot(resources, robotPlanification, blueprint)

        collectResources(robots, resources)

        if minute + 1 != productionTime:
            addRobotToLine(robots, robotTypeCreated)

        print("\n")
