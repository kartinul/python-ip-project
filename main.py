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
    "Write a python program to create series first five even number.",
    "Write a python program to create series of given tuple (11, 22, 33, 44, 55)",
    "Create series from dict that stores classes (6,7,8,9,10) as key and number of students as value",
    "Create a series by using np.array and find out index & size of series",
    "Rename index 51 from (0,1,2,3) to  ('a', 'b', 'c', 'd')",
    "Given two series s1, s2 find the {.given.code.}",
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

questionsSQL = {
    1: "Create database company1",
    2: "Create table Employee(EmpId, EmpName, DOJ, Salary, City, Email)",
    3: "Add 5 records into table",
    4: "Find out information of employees those salary is more than 50,000",
    5: "Update City of 1st Employee",
    6: "Delete last record from your table",
    7: ["Math functions", ["Power", "(ii)Round", "(iii)Mod"]],
    8: ["Convert EmpName to uppercase", "Apply mid() on emp_id"],
    9: ["Find out date from DOJ", "Find out day name from DOJ"],
    10: [
        "Find out max and min salary from employee table",
        "Count total employees those are coming from Vapi",
    ],
    11: "Make group of employees that are coming from same city",
}

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

num = forceIntInput(default=1)

cls()

list(validOptions.values())[num - 1]()
