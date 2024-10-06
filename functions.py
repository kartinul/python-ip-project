import os

def breaker(char = '-'):
  print(char * os.get_terminal_size().columns)

