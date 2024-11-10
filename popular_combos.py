import dataFiles as df
import pandas as pd
import matplotlib.pyplot as plt

# october = df.septemberCSV

# mac_cheese = (october.loc[october["Parent Menu Selection"]=="Mac and Cheese"])
# deset = (october.loc[october["Parent Menu Selection"]=="Sides/Desserts"])
# mixs = (october.loc[october["Parent Menu Selection"]=="MIX"])
# party_trays = (october.loc[october["Parent Menu Selection"]=="Mac and Cheese Party Tray (Plus FREE Garlic Bread)"])
# sandwhich  = (october.loc[october["Parent Menu Selection"]=="Grilled Cheese Sandwich"])

def find_month(month):
    csv_value = ""
    if month == "april":
        csv_value = df.aprilCSV
    elif month == "august":
        csv_value = df.augustCSV
    elif month == "july":
        csv_value = df.julyCSV
    elif month == "june":
        csv_value = df.juneCSV
    elif month == "may":
        csv_value = df.mayCSV
    elif month == "october":
        csv_value = df.octoberCSV
    else:
        csv_value = df.septemberCSV
    return csv_value

def mac_che(month):
    time = find_month(month)

    mac= (time.loc[time["Parent Menu Selection"]=="Mac and Cheese"])

    cheeses = (mac.loc[mac["Option Group Name"]=="Choose Your Cheese"])
    cheese_counts =  cheeses['Modifier'].value_counts()
    
    meat = (mac.loc[mac["Option Group Name"]=="Choose Your Meats"])
    meat_counts =  meat['Modifier'].value_counts()
   
    drizzle = (mac.loc[mac["Option Group Name"]=="Choose Your Drizzles"])
    drizzle_counts =  drizzle['Modifier'].value_counts()

    noods = (mac.loc[mac["Option Group Name"]=="Noods"])
    noods_counts =  noods['Modifier'].value_counts()

    sides = (mac.loc[mac["Option Group Name"]=="Choose Your Side"])
    sides_count =  sides['Modifier'].value_counts()
    
    topping = (mac.loc[mac["Option Group Name"]=="Choose Your Toppings"])
    topping_count =  topping['Modifier'].value_counts()

    drink = (mac.loc[mac["Option Group Name"]=="Choose Your Drink"])
    drink_count =  drink['Modifier'].value_counts()
    return(cheese_counts,meat_counts,drizzle_counts,noods_counts,sides_count,topping_count,drink_count)

def desert(month):
    time = find_month(month)

    sides = (time.loc[time["Parent Menu Selection"]=="Sides/Desserts"])
    #Choose Your Side
    side = (sides.loc[sides["Option Group Name"]=="Choose Your Side"])
    side_count =  side['Modifier'].value_counts()
    return side_count
def mix(month):
    time = find_month(month)
    cheese_mix = (time.loc[time["Parent Menu Selection"]=="MIX"])
    mix_data = (cheese_mix.loc[cheese_mix["Option Group Name"]=="Mix Bases"])
    mix_data_count =  mix_data['Modifier'].value_counts()
    return mix_data_count
def party_tray(month):
    time = find_month(month)
    tray = (time.loc[time["Parent Menu Selection"]=="Mac and Cheese Party Tray (Plus FREE Garlic Bread)"])
    party = (tray.loc[tray["Option Group Name"]=="Mac and Cheese Options"])
    party_count =  party['Modifier'].value_counts()
    return party_count
def sandwitch(month):
    time = find_month(month)
    sando = (time.loc[time["Parent Menu Selection"]=="Grilled Cheese Sandwich"])
    
    cheeses = (sando.loc[sando["Option Group Name"]=="Choose Your Melted Cheese"])
    cheese_counts =  cheeses['Modifier'].value_counts()
    
    mac = (sando.loc[sando["Option Group Name"]=="Do you want Mac and Cheese added inside?"])
    mac_count =  mac['Modifier'].value_counts()

    #Do you want Mac and Cheese added inside?
    meat = (sando.loc[sando["Option Group Name"]=="Choose Your Meats"])
    meat_counts =  meat['Modifier'].value_counts()
   
    drizzle = (sando.loc[sando["Option Group Name"]=="Choose Your Drizzles"])
    drizzle_counts =  drizzle['Modifier'].value_counts()

    sides = (sando.loc[sando["Option Group Name"]=="Choose Your Side"])
    sides_count =  sides['Modifier'].value_counts()
    
    topping = (sando.loc[sando["Option Group Name"]=="Choose Your Toppings"])
    topping_count =  topping['Modifier'].value_counts()

    drink = (sando.loc[sando["Option Group Name"]=="Choose Your Drink"])
    drink_count =  drink['Modifier'].value_counts()
    return cheese_counts,mac_count,meat_counts,drizzle_counts,sides_count,topping_count,drink_count

if __name__ == "__main__":
    print(mix("july"))



    