import os


def breaker(char="-"):
    print(char * os.get_terminal_size().columns)


def printHeading(str, end=":\n\n"):
    endChar = "\033[0m"
    underline = "\033[4m"
    print(underline + str + endChar, end=end)


def cls():
    os.system("cls")


def runImport(toSearch):
    __import__(str(toSearch))


def forceIntInput(str=":: ", default=0):
    try:
        num = int(input(str))
    except:
        num = default
        pass

    return num
