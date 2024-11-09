# Look through the csv files and record counts for each time block in a histogram and show which times of day are the
# most popular.

#Import the CSV
import dataFiles
import pandas as pd
from datetime import time


#Create keys for each time block and store the count for each.
timeOfDayCounts = {
    "10-11":0,
    "11-12":0,
    "12-13":0,
    "13-14":0,
    "14-15":0,
    "15-16":0,
    "16-17":0,
    "17-18":0,
    "18-19":0,
    "19-20":0,
    "12-13":0,
    "13-14":0,
    "14-15":0,
    "15-16":0,
    "16-17":0,
    "17-18":0,
    "18-19":0,
    "19-20":0,
    "20-21":0,
    "21-22":0
}

#Iterate through all the csv files and check the time and add it the right variable.

listOfMonths = [dataFiles.aprilCSV,dataFiles.mayCSV,dataFiles.juneCSV,dataFiles.julyCSV,dataFiles.augustCSV,dataFiles.septemberCSV,dataFiles.octoberCSV,dataFiles]

for dataframes in listOfMonths:
    for index,rows in dataframes.iterrows():
        extractTime = rows["Sent Date"]
        extractTime  = extractTime [extractTime.index(" "):]
        splitTime = extractTime.split(":")
        timeObj = time(int(splitTime[0]),splitTime[1],splitTime[2])
        
        
        
        
        

        
        
        
        


