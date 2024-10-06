from functions import breaker
import os

def runImport(toSearch):
  __import__(str(toSearch))

questions = {
  "1": "",
  "2": "",
  "3": "",
  "4": "",
  "5": "",
  "6": "",
  "7": "Create a python program to display attributes of a series.",
  "8": "Creating python program using head() and tail() in series.",
  "9": "Creating a python program for creating a DataFrame using a nested list.",
  "10": "Creating a python program for creating a DataFrame using a dictionarty of lists.",
  "11": "Creating a python program for accessing values of rows and columns of a DataFrame.",
  "12": "Creating a python program to perform operations on a DataFrame(rename, count, update).",
  "13": "Creating a python program to filter the data of a Dataframe.",
  "14": "Creating a python program to display the attributes of the DataFrame.",
  "15": "Creating a python program to display the data of a DataFrame row-wise and column-wise using iterrow() and iteritems().",
  "16": "Creating a python program to perform writing and reading operations in a CSV file.",
  "17": "Creating a python program to plotting a line chart.",
  "18": "Creating a python program to plotting a bar chart from a CSV file.",
  "19": "Creating a python program to plotting a multiple bar chart from a CSV file.",
  "20": "Creating a python program to plotting Histogram.",
}


print("CHOOSE YOUR QUESTION")
for i,j in questions.items():
  print(f'Q{i}. {j}')

questionNo = input(":: ")

if (questionNo in questions.keys()):
  os.system('cls')

  breaker("=")
  print(f'Q{questionNo}. {questions[questionNo]}')
  breaker("=")


  runImport(questionNo)
  breaker("=")
