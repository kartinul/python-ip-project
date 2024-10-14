from functions import *
import os


def runImport(toSearch):
    __import__(str(toSearch))


def forceIntInput(str=":: ", default=0):
    try:
        num = int(input(str))
    except:
        num = default
        pass

    return num


QUESTIONS = [
    "",
    "",
    "",
    "",
    "",
    "",
    "Create a python program to display attributes of a series.",
    "Creating python program using head() and tail() in series.",
    "Creating a python program for creating a DataFrame using a nested list.",
    "Creating a python program for creating a DataFrame using a dictionarty of lists.",
    "Creating a python program for accessing values of rows and columns of a DataFrame.",
    "Creating a python program to perform operations on a DataFrame(rename, count, update).",
    "Creating a python program to filter the data of a Dataframe.",
    "Creating a python program to display the attributes of the DataFrame.",
    "Creating a python program to display the data of a DataFrame row-wise and column-wise using iterrow() and iteritems().",
    "Creating a python program to perform writing and reading operations in a CSV file.",
    "Creating a python program to plotting a line chart.",
    "Creating a python program to plotting a bar chart from a CSV file.",
    "Creating a python program to plotting a multiple bar chart from a CSV file.",
    "Creating a python program to plotting Histogram.",
]


def HandleQuestion(type="Python"):
    printHeading("CHOOSE YOUR QUESTION")
    for i, j in enumerate(QUESTIONS):
        print(f"Q{i+ 1}. {j}")

    questionNoIndex = forceIntInput(":: ") - 1

    if 0 < questionNoIndex <= len(QUESTIONS):
        cls()

        breaker("=")
        print(f"Q{questionNoIndex + 1}. {QUESTIONS[questionNoIndex]}")
        breaker("=")

        runImport(type + "." + str(questionNoIndex + 1))
        breaker("=")


CSV_NAME = ["16w.csv", "16r.csv", "18.csv", "19.csv"]


def HandleCSV():
    printHeading("CHOOSE YOUR FILE TO READ")
    for i in CSV_NAME:
        print(f"* {i}")

    csvFile = input(":: ")

    csvFile = csvFile.split(".")[0] + ".csv"

    if csvFile in CSV_NAME:
        cls()
        breaker("=")
        print(csvFile)
        breaker("=")

        with open(f"./CSV/{csvFile}", "r") as f:
            print(f.read())

        breaker("=")


validOptions = {"Questions": HandleQuestion, "CSV": HandleCSV}

cls()

printHeading("SELECT A NUMBER")
for i, j in enumerate(validOptions.keys()):
    print(f"{i+1}. {j}")

num = forceIntInput()

cls()

list(validOptions.values())[num - 1]()
