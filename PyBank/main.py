
import pandas as pd 

import os 

import csv
csvpath= os.path.join(r'PyBank\Resources\budget_data.csv')
with open(csvpath) as csvfile:
  csvreader=csv.reader(csvfile,delimiter=',')
  print(csvreader)

  for row in csvreader:
    print(row)

df=pd.read_csv(r'PyBank\Resources\budget_data.csv')



