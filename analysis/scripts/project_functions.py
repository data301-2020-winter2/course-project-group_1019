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
  print(rawdata.info())
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
  print(dataclean.info())
  return dataclean

def getTotalCountOfGames():
  return len(dataclean.index)

def getUniqueTotalCountofGames():
  #returns the total count of unique games
  print('this works')
  return

def getAverageSalesWorldWide():
  #
  return
def getAverageSalesNA_Sales():
  #return the total 
  return 
def getAverageUserScore():
  return
def getAverageCriticScore():
  return 

def getUniquePublishersCount():
  return

def getUniqueDevelopersCount():
  return

def getUniqueDevelopers():
  #returns an Array of Unique Developers
 return 
def getUniquePlatformsCount():
  return





