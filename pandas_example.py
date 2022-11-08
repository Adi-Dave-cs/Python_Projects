# https://pandas.pydata.org/docs/reference/index.html
import pandas as pd
import csv as cs

# using simple file reader 
with open('weather-data.csv') as datafile:
    line = datafile.readlines()
    print(line)


# using simple csv reader from csv module of python
with open('weather-data.csv') as data:
    line = cs.reader(data)
    for row in line:
        print(row)

#using pandas to create dataframe and fetch data from the same. Increases the usability of the data
df = pd.read_csv('weather-data.csv')
row , col = df.shape

# print(df.describe())

def fillvalues(cell):
    if(cell == "n.a." or cell == 'NaN'):
        cell = 'Not acccessible'
    return cell

df1 = pd.read_csv('CAR DETAILS FROM CAR DEKHO.csv')
print(df1.describe())

g = df1.groupby('seller_type')

for seller_type,seller_type_f in g:
    print(seller_type)
    print(seller_type_f)

    