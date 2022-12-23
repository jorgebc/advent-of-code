from day19 import runProduction

blueprint = {
    "ore": {"ore": 4},
    "clay": {"ore": 2},
    "obsidian": {"ore": 3, "clay": 14},
    "geode": {"ore": 2, "obsidian": 7},
}


runProduction(blueprint)
