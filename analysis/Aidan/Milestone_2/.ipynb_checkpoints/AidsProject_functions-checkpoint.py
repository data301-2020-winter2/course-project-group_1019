import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas_profiling as pdp

#dataclean = loadCleanFile()

def load_and_process():
  #this function loads the csv to process it
  rawdata = pd.read_csv("https://github.com/data301-2020-winter2/course-project-group_1019/blob/main/data/raw/Video_Games_Sales_as_at_22_Dec_2016.csv?raw=true.csv") 
  # Preview the basic information of the loaded data 
  
  # Establishing a new dataset that will be dataclean from the rawdata dataset


  #removes the users scores with values tbd
  for rownumber in rawdata.index:
    if rawdata.User_Score[rownumber]== 'tbd':
      rawdata.User_Score[rownumber] = 'NaN'

  dataclean = rawdata.dropna()
  dataclean.index = range(0,len(dataclean.index))

  # Set columns Genre and Rating to be categories and check the info again
  
  dataclean['Name'] = dataclean['Name'].astype("string")
  dataclean['Platform'] = dataclean['Platform'].astype("category")
  dataclean['Year_of_Release'] = dataclean['Year_of_Release'].astype('int64')
  dataclean['Genre'] = dataclean['Genre'].astype('category')
  dataclean['Publisher'] = dataclean['Publisher'].astype("string")
  dataclean['NA_Sales'] = dataclean['NA_Sales'].astype("float")
  dataclean['EU_Sales'] = dataclean['EU_Sales'].astype("float")
  dataclean['JP_Sales'] = dataclean['JP_Sales'].astype("float")
  dataclean['Other_Sales'] = dataclean['Other_Sales'].astype("float")
  dataclean['Global_Sales']= dataclean['Global_Sales'].astype("float")
  dataclean['Critic_Score'] = dataclean['Critic_Score'].astype("float")
  dataclean['Critic_Count'] = dataclean['Critic_Count'].astype("float")
  dataclean['User_Score'] = dataclean['User_Score'].astype("float")
  dataclean['User_Count'] = dataclean['User_Count'].astype("float")
  dataclean['Developer'] = dataclean['Developer'].astype('string')
  dataclean['Rating'] = dataclean['Rating'].astype('category')
  
  return dataclean

def sortconsole(df):  ##filters for Name, Platform, Year of Release, Genre, Publisher, EU_Sales, etc. removes incomplete values, and sorts by Platform, then by name, only considers the listed columns
    df1 = df.filter(['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'EU_Sales', 'NA_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score', 'User_Score']).dropna().sort_values(by =['Platform','Name'])
    df1.index = range(0,len(df1.index))
    return df1

def available(df):
  #adds 4 columns with either 1 or 0, if 0 then the game is not available in the region #designated by the column name
  #uses a for loop for each region to see if sales are non-zero
  #
    NA = []
    for i in range(0,len(df.index)):
        if df['NA_Sales'][i] == 0.00:
            NA.append(0)
        else:
            NA.append(1)
    df['NA'] = NA
    
    JP = []
    for i in range(0,len(df.index)):
        if df['JP_Sales'][i] == 0.00:
            JP.append(0)
        else:
            JP.append(1)
    df['JP'] = JP
    
    EU = []
    for i in range(0,len(df.index)):
        if df['EU_Sales'][i] == 0.00:
            EU.append(0)
        else:
            EU.append(1)
    df['EU'] = EU
    
    OTHER = []
    for i in range(0,len(df.index)):
        if df['Other_Sales'][i] == 0.00:
            OTHER.append(0)
        else:
            OTHER.append(1)
    df['OTHER'] = OTHER
    return df



def popular(df):
  # removes consoles with less than 80 games listed
  # takes the value count of the 'Platform' column and takes a slice with rows less than
  #
    counts = df['Platform'].value_counts()
    to_remove = counts[counts <= 80].index
    df = df[~df.Platform.isin(to_remove)]
    return df





