#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import math
import numpy as np
import pandas as pd
import scipy.stats
#import statsmodel.api as sm
#from statsmodels.formula.api import ols

class Poll:
    def __init__(self, name, df):
        self.outlet = name
        self.data = df.loc[df["Poll"] == name]

    
    

    def getMostRecentPoll(self):
        return self.data.iloc[0]

    def countPoll(self):
        return len(self.data)

    def changeInPoll(self,candidate):
        candidateData = self.data[candidate]
        return candidateData.iloc[0] - candidateData.iloc[len(candidateData) - 1]

    def avgInPoll(self,candidate):
        countVal = 0
        count = 0
        data = self.data[candidate]
        for i in data:
            countVal += i
            count += 1
        return (countVal / count)

    def mean(self, candidate):
        return self.data[candidate].mean()

    def medianInPoll(self,candidate):
        return self.data[candidate].median()

    def correlatedPolls(self,candidate1,candidate2):
        if (self.countPoll() == 1):
            print("Not enough data")
            return 0
        else:
            return self.data[candidate1].corr(self.data[candidate2])

    #def normalizeData(self,dataframe):
        #x = dataframe.copy()
        #for i,datapoint in x.iterrows():
            #datapoint.drop[labels = ["Date","Sample","Spread"], axis = 'columns' inplace = True]
            #print(i)


    #def pollUncertainty(self,candidate):
        #SD
        #return self.data[candidate].std()

        #IQR
        #upper = self.data[candidate].quantile(.75)     
        #lower = self.data[candidate].quantile(.25)

        #return upper - lower

        #Margin of Error ()

    #def computeMarginOfError(self, candidate):
        #n = self.countPoll()
        #sigma = self.data[candidate].std()
        #z = 1.96

        #return z * sigma / math.sqrt(n)


        #comparing differences in data
        #confidence intervals (comparison)
            #tells what the difference is not necessarily how large the difference is or isnt

    #def computeCoinfidenceInterval(data):
        #npArray = 1.0 * np.array(self.data[candidate])
        #stdError = scipy.stats.sem(npArray)
        #n = self.countPoll()
        #return stdError * scipy.stats.t.ppf((1+.95) / 2.0, n-1)

        #Cohens D
            #how larg or small the difference between the range of mean is
         
        #comparing distributions
        #t - test
            # 1 dependent and 1 independent 
                # ind - has two variables
                #compare two distributions and see difference between datasets(values)

    #ANOVA
        #analysis of variants
            #comparing averages
            #comparing more than two independent variables
    
    #def runANOVA(dataframe, vars):
        #model = ols(vars, data=dataframe).fit()
        #aov_table = sm.stats.anova_lm(model, typ = 2)
        #return aov_table