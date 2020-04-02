from utility import *
from poll import Poll

import scipy
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#1. Considering the circumstances now, I believe Joe Biden will win the election primarily because 
    #he has aggregated many endorsements over the course over the primary election period. However,
    #I believe that Bernie Sanders has many more coherent and fundamental ideas encompassing his 
    #campaign. I voted for Bernie is the last election, and believe him to generally speak in a more
    #holestic tone when regarding any topic that affects the whole public like medicaire for all and
    #minor criminal prosection expungement. 

#2 & 3
    #observation
        #Each poll has a sample number and date to correspond to the poll done. 
        #There are multiple polls from the same place taken over differing time periods
        #Sanders and Biden had most of the votes for each column

#Problem Set 4: #4
#df = loadAndCleanData("pollingData.csv")
#print(df)




#Problem Set 4: #5 and #6
def normalizeData(df):
    sumList = []
   
    for i,row in df.iterrows():
        row.drop(labels = ["Poll","Date","Sample","Spread"], inplace = True)
        sumList.append(100 - sum(row))

    df["Undecided"] = sumList
    return(df)

def printNormalized():
    df = loadAndCleanData("pollingData.csv")
    normalizeData(df)

print("This is the normalized dataset: ")
printNormalized()
print("\n")





'''
#Problem Set 4: #7
def plotCandidate(candidate,df):
    plt.scatter(y = df[candidate], x = df[candidate])
    plt.show()

def printPlots():
    df1 = loadAndCleanData("pollingData.csv")
    df2 = normalizeData(df1)

    for column in df2.columns:
        if column not in ["Poll","Date","Sample","Spread","Undecided"]:
            plotCandidate(column, df2)
            plt.show()

printPlots()
'''






#Problem Set 4: #8 and #9
def statsPerCandidate(candidate, df):
    return(df[candidate].mean())

def printAvg():
    df1 = loadAndCleanData("pollingData.csv")
    normalizeData(df1)
    for column in df1.columns:
        if column not in ["Poll","Date","Sample","Spread"]:
            print("Candidate: " + column + " \t Average: " +  str(statsPerCandidate(column,df1)))
print("These are average polling numbers: ")
printAvg()
print("\n")






#Problem Set 4: #10 and #11
def cleanSample(df):
    sampleType = []
    sampleSize = []

    for i in df["Sample"]:
        sampleType.append(i[-2:])
        sampleSize.append(i[:-2])

    df["Sample Type"] = sampleType
    df["Sample Size"] = sampleSize

    return df

def printCleanSample():
    df1 = loadAndCleanData("pollingData.csv")
    df1 = normalizeData(df1)
    print(cleanSample(df1))

print("This is a clean sample of the data: ")
printCleanSample()
print("\t")





#Problem Set 4: #12, #13, and #14
def computePollWeight(dataframe, poll):
    x = dataframe[poll]
    xSum = sum(x)
    y = sum(dataframe["Sample Size"].astype(int))
    return xSum/y

def weightedStatsPerCandidate():
    print("These are weighted averages of candidate polling data: " + "\n")

    dataframe = loadAndCleanData("pollingData.csv")
    x = cleanSample(dataframe)
    x["Sample Size"] = x["Sample Size"].astype(int)

    for column in x.columns:
        if column not in ["Poll","Date","Sample","Spread","Undecided","Sample Type","Sample Size"]:
            print("Candidate: " + str(column) + "\t Weighted Average: "  +str(computePollWeight(x,column)) + "\n")


weightedStatsPerCandidate()






# Problem Set 4: #15 and #16
def computeCorrelation(candidate1,candidate2, dataframe):
    return dataframe[candidate1].corr(dataframe[candidate2])

def printCorrelation():
    print("These are correlations: ")
    dataframe = loadAndCleanData("pollingData.csv")
    df = cleanSample(dataframe)

    names = []
    for name in df.columns:
        if name not in ["Poll","Date","Sample","Spread","Undecided","Sample Type","Sample Size"]:
            names.append(name)

    repeat = []
    for name1 in names:
        print()
        for name2 in names:
            if name1 != name2:
                if [name1, name2] not in repeat and [name2,name1] not in repeat:
                    print(name1 +" vs."+ name2 + "  " + str(computeCorrelation(name1,name2,df)))
                    #print(computeCorrelation(name1,name2,df))

printCorrelation()






#Problem Set 4: #17 and #18
def superTuesday(dataframe, candidates):
    bidenST = []
    sandersST = []

    for i, row in dataframe.iterrows():
        bCount = row["Biden"]
        sCount = row["Sanders"]
        for candidate in candidates:
            if candidate != "Biden" and candidate != "Sanders":
                bCorr = computeCorrelation("Biden", candidate, dataframe)
                sCorr = computeCorrelation("Sanders", candidate, dataframe)
                if abs(bCorr) > abs(sCorr):
                    bCount += row[candidate]
                else:
                    sCount += row[candidate]
        bidenST.append(bCount)
        sandersST.append(sCount)

    dataframe["BidenST"] = bidenST
    dataframe["SandersST"] = sandersST

    return dataframe

def printST():
    dataframe = loadAndCleanData("pollingData.csv")
    df = cleanSample(dataframe)
    names = []
    for name in df.columns:
        if name not in ["Poll","Date","Sample","Spread","Undecided","Sample Type","Sample Size"]:
            names.append(name)

    x = superTuesday(df, names)
    print(x)
    print("Biden: " +str(x["BidenST"].mean()) +"\n"+ "Sanders: " +str(x["SandersST"].mean()))
    print("Biden Weighted Mean: " + str(computePollWeight(df, "BidenST")) + "\n" +
     "Sanders Weighted Mean: " + str(computePollWeight(df, "SandersST")))

printST()
print("Based on this data it seems Biden will win the Democratic nomination")
print()





#Problem Set 4: #19
'''
def getConfidenceInterval(column):
    npArray = 1.0 * np.array(column)
    stdError = scipy.stats.sem(npArray)
    n = len(column)
    return stdError * scipy.stats.t.ppf((1+.95) / 2.0, n-1)

def printCI():
    dataframe = loadAndCleanData("pollingData.csv")
    df = cleanSample(dataframe)
    names = []
    for name in df.columns:
        if name not in ["Poll","Date","Sample","Spread","Undecided","Sample Type","Sample Size"]:
            names.append(name)

    x = superTuesday(df, names)

    print(getConfidenceInterval(x['BidenST']))
    print(getConfidenceInterval(x['SanderST']))

printCI()
'''





#Problem Set 4: #20
def runTTest(df1, df2):
    return scipy.stats.ttest_ind(df1,df2)

def printTTest():
    dataframe = loadAndCleanData("pollingData.csv")
    df = cleanSample(dataframe)
    names = []
    for name in df.columns:
        if name not in ["Poll","Date","Sample","Spread","Undecided","Sample Type","Sample Size"]:
            names.append(name)

    x = superTuesday(df, names)
    print(runTTest(x["Biden"], x["Sanders"]))
    print(runTTest(x["BidenST"], x["SandersST"]))

printTTest()