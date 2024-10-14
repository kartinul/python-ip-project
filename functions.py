import os


def breaker(char="-"):
    print(char * os.get_terminal_size().columns)


def printHeading(str, end=":\n\n"):
    endChar = "\033[0m"
    underline = "\033[4m"
    print(underline + str + endChar, end=end)


def cls():
    os.system("cls")
