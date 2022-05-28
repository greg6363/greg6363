#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import math
import numpy as np


# In[ ]:


def printNoneReturnRatios(dataframe, prop = 0.8):
    print("Running printNoneReturnRatios:")
    count = 0
    highNoneCols = list()
    for column in dataframe:
        none_prop = sum(pd.isnull(dataframe[column])) / dataframe.shape[0]
        if none_prop >= prop:
            count += 1
            print(column + ": " + str(none_prop))
            highNoneCols.append(column)
    print("Remove " + str(count) + " columns with high proportion of 'None' values")
    print("---------------------------------------------")
    return highNoneCols


# In[ ]:


def printNoneRatios(dataframe, prop = 0.8):
    print("Running printNoneRatios:")
    count = 0
    for column in dataframe:
        none_prop = sum(pd.isnull(dataframe[column])) / dataframe.shape[0]
        if none_prop >= prop:
            print(column + ": " + str(none_prop))
            count += 1
    print(str(count) + " columns with high proportion of 'None' values")


# In[ ]:


def listHighLevels(dataframe, levels_threshold = 53):
    print("Running listHighLevels:")
    count=0
    highLevCols=list()
    for column in dataframe.select_dtypes(include='object'):
        if(dataframe[column].nunique()>levels_threshold):
            count+=1
            print(column + ": " + str(dataframe[column].nunique()))
            highLevCols.append(column)
    print("Remove " + str(count) + " columns with high levels")
    print("---------------------------------------------")
    return highLevCols


# In[ ]:


def listOneLevel(dataframe):
    print("Running listOneLevel:")
    count=0
    oneLevCols=list()
    for column in dataframe.select_dtypes(include='object'):
        if(dataframe[column].nunique()<2):
            count+=1
            print(column + " " + str(dataframe[column].nunique()))
            oneLevCols.append(column)
    print("Remove " + str(count) + " columns with one level")
    print("---------------------------------------------")
    return oneLevCols


# In[ ]:


def printMaxElementReturnRatios(dataframe, prop=0.98):
    print("Running listMaxElementReturnRatios:")
    count=0
    highMaxElementCols=list()
    for column in dataframe.select_dtypes(include='object'):
        max_ele_prop=max(dataframe[column].value_counts())/len(dataframe.index)
        if(max_ele_prop>prop):
            count+=1
            print(column)
            highMaxElementCols.append(column)
            print(max_ele_prop)
    print("Remove " + str(count) + " columns with one element having too much proportion")
    print("---------------------------------------------")
    return highMaxElementCols


# In[ ]:


#Function to clean inf and booleans
def cleanupInfNABool(dataframe):
    dataframe.replace([np.inf, -np.inf, 'NA'], np.nan,inplace=True)
    dataframe.loc[:,dataframe.dtypes=='bool'] = dataframe.applymap(lambda x: 1 if x==True else 0)  
    return dataframe    


# In[ ]:


def transfer_bool_to_int(col):
    if col == None:
        return None
    else:
        return (col=="true")*1


# In[ ]:


def transfer_bool_to_int(dataframe):
    count=0
    transferCols=list()
    for column in dataframe.select_dtypes(exclude='number'):
        TF_sum=sum(dataframe[column].str.lower().isin(["true", "false"]))
        if(TF_sum>0):
            count+=1
            print(column)
            dataframe[column]=np.where((dataframe[column].isnull())|(dataframe[column]==None)|(dataframe[column]==""), np.nan,
                                       np.where(dataframe[column].str.lower()=="true", 1, 0))
            dataframe.rename(columns = {column:column+"_trans"}, inplace=True)
            transferCols.append(column)
            print(TF_sum)
    print(count)


# In[ ]:


def YearCalculator(latter, former):
    year = round((latter-former).dt.days/365.25, 2)
    return (year)


# In[ ]:




