import dataFiles
import pandas as pd


listOfMonths = [dataFiles.aprilCSV,dataFiles.mayCSV,dataFiles.juneCSV,dataFiles.julyCSV,dataFiles.augustCSV,dataFiles.septemberCSV,dataFiles.octoberCSV]

dict = {
    "userID": [],
    "userModifiers":[]
}

#Define outside here so its not being aletered
extractUserID = ""

for dataframes in listOfMonths:
    extractMonth = id(dataframes)
    for index,rows in dataframes.iterrows():
        try:
            extractUserID = rows["Order ID"] +"_" + f"{extractMonth}"
            
            # Use the user id as the key, then the value is a dictionary that stores the a string with the user's modifiers
            # the second value is the count
            
            if(not (extractUserID in dict["userID"]) ):
                #intialize the dictionary that stores what a user has ordered
                dict["userID"] += [extractUserID]
                dict["userModifiers"]+=[rows["Modifier"]]
            else:
                dict["userModifiers"][dict["userID"].index(extractUserID)] += ","+rows["Modifier"]
        except:
            continue
    

dictToDf = pd.DataFrame(dict)

countDf = dictToDf["userModifiers"].value_counts()
print(countDf)

#Get only those elemetns with commas in them to find the top combos
comboDF = countDf[countDf.index.str.contains(",")].iloc[0:10]













