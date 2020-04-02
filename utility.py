
import pandas as pd
import numpy as py

def loadAndCleanData(filename):
    data = pd.read_csv(filename)
    columns = list(data)
    for i in columns:
        data[i].fillna(0,inplace=True)
    return data

def computePDF(feature,filename):
    data1 = pd.read_csv(filename)
    ax1 = data1[feature].plot.kde()
    ax1.set_xlabel(feature)
    
import matplotlib.pyplot as plt

def viewLogDistribution(column,filename):
    data1 = pd.read_csv(filename)
    ax1 = data1[column].plot(kind = 'hist',bins = 20, log = True)
    ax1.set_xlabel(column)

