import csv 
import numpy as np 
import plotly.express as px

def getDataSource(dataPath):
    percentage = []
    number = []
    with open(dataPath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            percentage.append(float(row['Marks In Percentage']))
            number.append(float(row['Days Present']))
    return{"x":percentage , "y":number }

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation -- Co-efficient :", correlation[0,1] )

def setup():
    dataPath = 'm&dp.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFig(dataPath) 

def plotFig(dataPath):
    with open (dataPath) as csv_file:
     df = csv.DictReader(csv_file)
     fig = px.scatter(df, x = "Marks In Percentage" , y ="Days Present")
     fig.show()

setup()           



