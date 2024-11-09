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

listOfMonths = [dataFiles.aprilCSV,dataFiles.mayCSV,dataFiles.juneCSV,dataFiles.julyCSV,dataFiles.augustCSV,dataFiles.septemberCSV,dataFiles.octoberCSV]

def addToDict(timeObj):
    if time(10,0) <= timeObj < time(11,0):  
        timeOfDayCounts["10-11"]+=1
    elif time(11,0) <= timeObj < time(12,0):  
        timeOfDayCounts["11-12"]+=1
    elif time(12,0) <= timeObj < time(13,0):  
        timeOfDayCounts["12-13"]+=1
    elif time(13,0) <= timeObj < time(14,0):  
        timeOfDayCounts["13-14"]+=1
    elif time(14,0) <= timeObj < time(15,0):  
        timeOfDayCounts["14-15"]+=1
    elif time(15,0) <= timeObj < time(16,0):  
        timeOfDayCounts["15-16"]+=1
    elif time(16,0) <= timeObj < time(17,0):  
        timeOfDayCounts["16-17"]+=1
    elif time(17,0) <= timeObj < time(18,0):  
        timeOfDayCounts["17-18"]+=1
    elif time(18,0) <= timeObj < time(19,0):  
        timeOfDayCounts["18-19"]+=1
    elif time(19,0) <= timeObj < time(20,0):  
        timeOfDayCounts["19-20"]+=1
    elif time(20,0) <= timeObj < time(21,0):  
        timeOfDayCounts["20-21"]+=1
    elif time(21,0) <= timeObj < time(22,0):  
        timeOfDayCounts["21-22"]+=1

#Create a function that extracts checks the time and adds it to the right diciontary
for dataframes in listOfMonths:
    for index,rows in dataframes.iterrows():
        extractTime = rows["Sent Date"]
        try:
            extractTime  = extractTime[extractTime.index(" "):]
            splitTime = extractTime.split(":")
            timeObj = time(int(splitTime[0]),int(splitTime[1]))
            addToDict(timeObj)
        except AttributeError:
            continue


#If this is script then execute and display the data.
if(__name__ == "__main__"):
    from matplotlib import pyplot as plt
    plt.bar(timeOfDayCounts.keys(),timeOfDayCounts.values())
    plt.show()
        
        
        
        
        

        
        
        
        


