import dataFiles as df
import pandas as pd
import matplotlib.pyplot as plt
october = df.octoberCSV
mac_cheese = (october.loc[october["Parent Menu Selection"]=="Mac and Cheese"])
desert = (october.loc[october["Parent Menu Selection"]=="Sides/Desserts"])
mix = (october.loc[october["Parent Menu Selection"]=="MIX"])
party_tray = (october.loc[october["Parent Menu Selection"]=="Mac and Cheese Party Tray (Plus FREE Garlic Bread)"])
sandwhich  = (october.loc[october["Parent Menu Selection"]=="Grilled Cheese Sandwich"])

def mac_che(mac):
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
    
    drink = (mac.loc[mac["Option Group Name"]=="Choose Your Drink"])
    drink_count =  drink['Modifier'].value_counts()

    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 4))
    plt.subplots_adjust(wspace= .25, hspace= .75)
    cheese_counts.plot(kind='bar', ax=axes[0][0], color='skyblue')
    axes[0][0].set_title('Cheese Distribution in Mac and Cheese')
    #axes[0][0].set_ylabel('Count')

    meat_counts.plot(kind='bar', ax=axes[0][1], color='salmon')
    axes[0][1].set_title('Meat Distribution in Mac and Cheese')
    #axes[0][1].set_ylabel('Count')


    drizzle_counts.plot(kind='bar', ax=axes[0][2], color='grey')
    axes[0][2].set_title('Drizzle Distribution in Mac and Cheese')
    #axes[0][2].set_ylabel('Count')

    noods_counts.plot(kind='bar', ax=axes[1][0], color='yellow')
    axes[1][0].set_title('Noodle Distribution in Mac and Cheese')
    #axes[1][0].set_ylabel('Count')

    sides_count.plot(kind='bar', ax=axes[1][1], color='green')
    axes[1][1].set_title('Sides Distribution with Mac and Cheese')
    #axes[1][1].set_ylabel('Count')
    axes[1][1].set_xlabel('')

    drink_count.plot(kind='bar', ax=axes[1][2], color='pink')
    axes[1][2].set_title('Drink Distribution with Mac and Cheese')
    # axes[1][2].set_ylabel('Count')
    axes[1][2].set_xlabel('')
    axes[1][0].set_xlabel('')
    axes[0][0].set_xlabel('')
    axes[0][1].set_xlabel('')
    axes[0][2].set_xlabel('')
    
    # Annotate the bars with the counts
    for i in axes[0][0].containers:
        axes[0][0].bar_label(i)
    for i in axes[0][1].containers:
        axes[0][1].bar_label(i)
    for i in axes[0][2].containers:
        axes[0][2].bar_label(i)
    for i in axes[1][0].containers:
        axes[1][0].bar_label(i)
    for i in axes[1][1].containers:
        axes[1][1].bar_label(i)
    for i in axes[1][2].containers:
        axes[1][2].bar_label(i)

    plt.tight_layout()
    plt.show()

mac_che(mac_cheese)
    