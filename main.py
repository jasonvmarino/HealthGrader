import os
from csvhandler import *

list_of_csv = []
test = os.getcwd()
for file in os.listdir(test):
    if file.endswith(".csv"):
        list_of_csv.append(file)

#print(list_of_csv)  #Debug for testing list of files

for items in list_of_csv:
    file = csv_file(items)
    file.read()
    file.print()