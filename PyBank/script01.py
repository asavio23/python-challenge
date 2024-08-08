import os
import csv

myfile = os.path.join('Resources','budget_data.csv')

#read csv 
with open (myfile) as csv_file:
    csvreader = csv.reader(csv_file, delimiter =",")
    csv_header = next(csvreader)

