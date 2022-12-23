import os


def getInputFromFile(path):
    file_path = os.path.join(os.getcwd(), path)
    # Open the file in read-only mode
    inputFile = open(file_path, "r")

    # Read the entire file content
    input = inputFile.read()

    # Close the file
    inputFile.close()

    return input
