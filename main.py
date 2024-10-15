from functions import *


def runImport(toSearch):
    __import__(str(toSearch))


def forceIntInput(str=":: ", default=0):
    try:
        num = int(input(str))
    except:
        num = default
        pass

    return num


QUESTIONS = {
    1: "Write a python program to create series first five even number.",
    2: "Write a python program to create series of given tuple (11, 22, 33, 44, 55)",
    3: "Create series from dict that stores classes (6,7,8,9,10) as key and number of students as value",
    4: "Create a series by using np.array and find out index & size of series",
    5: "Rename index 51 from (0,1,2,3) to  ('a', 'b', 'c', 'd')",
    6: "Given two series s1, s2 find the {.given.code.}",
    7: "Create a python program to display attributes of a series.",
    8: "Creating python program using head() and tail() in series.",
    9: "Creating a python program for creating a DataFrame using a nested list.",
    10: "Creating a python program for creating a DataFrame using a dictionarty of lists.",
    11: "Creating a python program for accessing values of rows and columns of a DataFrame.",
    12: "Creating a python program to perform operations on a DataFrame(rename, count, update).",
    13: "Creating a python program to filter the data of a Dataframe.",
    14: "Creating a python program to display the attributes of the DataFrame.",
    15: "Creating a python program to display the data of a DataFrame row-wise and column-wise using iterrow() and iteritems().",
    16: "Creating a python program to perform writing and reading operations in a CSV file.",
    17: "Creating a python program to plotting a line chart.",
    18: "Creating a python program to plotting a bar chart from a CSV file.",
    19: "Creating a python program to plotting a multiple bar chart from a CSV file.",
    20: "Creating a python program to plotting Histogram.",
}


def HandleQuestionPy(type="Python"):
    printHeading("CHOOSE YOUR QUESTION")
    for i, j in QUESTIONS.items():
        print(f"Q{i}. {j}")

    questionNo = forceIntInput(":: ")

    if 0 < questionNo <= len(QUESTIONS):
        cls()

        breaker("=")
        print(f"Q{questionNo}. {QUESTIONS[questionNo]}")
        breaker("=")

        runImport(type + "." + str(questionNo))
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


QUESTIONS_SQL = {
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


def HandleQuestionSQL():
    # TODO
    pass


validOptions = {
    "Python Questions": HandleQuestionPy,
    "CSV": HandleCSV,
    "SQL Questions": HandleQuestionSQL,
}

cls()

printHeading("SELECT A NUMBER")
for i, j in enumerate(validOptions.keys()):
    print(f"{i+1}. {j}")

num = forceIntInput(default=1)

cls()

list(validOptions.values())[num - 1]()
