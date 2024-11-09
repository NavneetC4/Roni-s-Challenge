import dataFiles as df
import pandas as pd
import matplotlib.pyplot as plt
october = df.octoberCSV
mac_cheese = []
desert = []
party_tray = []
mix = []
sandwhich = []
mac_cheese = (october.loc[october["Parent Menu Selection"]=="Mac and Cheese"])
desert = (october.loc[october["Parent Menu Selection"]=="Sides/Desserts"])
mix = (october.loc[october["Parent Menu Selection"]=="MIX"])
party_tray = (october.loc[october["Parent Menu Selection"]=="Mac and Cheese Party Tray (Plus FREE Garlic Bread)"])
sandwhich  = (october.loc[october["Parent Menu Selection"]=="Grilled Cheese Sandwich"])

def mac_che(mac):
    cheeses = (mac.loc[mac["Option Group Name"]=="Choose Your Cheese"])
    cheese_counts =  cheeses['Modifier'].value_counts()
<<<<<<< Updated upstream
    cheese_counts.plot(kind='bar')
  
    meat = (mac.loc[mac["Option Group Name"]=="Choose Your Meats"])
    meat_counts =  meat['Modifier'].value_counts()
    meat_counts.plot(kind='bar')

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
=======
    #cheese_counts.plot(kind='bar')
  
    meat = (mac.loc[mac["Option Group Name"]=="Choose Your Meats"])
    meat_counts =  meat['Modifier'].value_counts()
    # meat_counts.plot(kind='bar')
    
    drizzle = (mac.loc[mac["Option Group Name"]=="Choose Your Drizzles"])
    drizzle_counts =  drizzle['Modifier'].value_counts()

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 5))
>>>>>>> Stashed changes
    cheese_counts.plot(kind='bar', ax=axes[0], color='skyblue')
    axes[0].set_title('Cheese Distribution in Mac and Cheese')
    axes[0].set_xlabel('Cheese Types')
    axes[0].set_ylabel('Count')

    meat_counts.plot(kind='bar', ax=axes[1], color='salmon')
    axes[1].set_title('Meat Distribution in Mac and Cheese')
    axes[1].set_xlabel('Meat Types')
    axes[1].set_ylabel('Count')

<<<<<<< Updated upstream
=======
    drizzle_counts.plot(kind='bar', ax=axes[2], color='grey')
    axes[2].set_title('Drizzle Distribution in Mac and Cheese')
    axes[2].set_xlabel('Drizzle Types')
    axes[2].set_ylabel('Count')

>>>>>>> Stashed changes
    # Annotate the bars with the counts
    for i in axes[0].containers:
        axes[0].bar_label(i)
    for i in axes[1].containers:
        axes[1].bar_label(i)
<<<<<<< Updated upstream

    plt.tight_layout()
    plt.show()s
=======
    for i in axes[2].containers:
        axes[2].bar_label(i)

    plt.tight_layout()
    plt.show()
>>>>>>> Stashed changes

    
mac_che(mac_cheese)