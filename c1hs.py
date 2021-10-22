import csv 
import numpy as np 
import plotly.express as px 

def getDataSource(dataPath):
    ml = []
    hrs = []
    with open(dataPath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ml.append(float(row['Coffee in ml'])) 
            hrs.append(float(row['sleep in hours']))
    return{"x":ml,"y":hrs}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])   
    print("Correlation -- Co-efficient :", correlation[0,1] )


def setup():
    dataPath = 'c&hs.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFig(dataPath) 

def plotFig(dataPath):
    with open (dataPath) as csv_file:
     df = csv.DictReader(csv_file)
     fig = px.bar(df, x = "Coffee in ml" , y ="sleep in hours")
     fig.show()

setup()           


