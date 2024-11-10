import dataFiles
import bussinessDuringDay
import popular_combos
from matplotlib import pyplot as plt



def main():
    choice = ""
    while choice.lower() != "stop":
        print("Select a plot to display or type Stop:")
        print("1. Traffic Over the Course of a Day")
        print("2. Popular Combos")
        print("0. Exit")

        choice = input("Enter your choice by its number: ")

        if choice == '1':
            plot_traffic()
        elif choice == '2':
            plot_popular_combos()
        elif choice == '0':
            print("Exiting...")
            plt.close('all')
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

def plot_traffic():
    plt.close('all')  # Close all existing plot windows
    fig, ax = plt.subplots()
    ax.bar(bussinessDuringDay.timeOfDayCounts.keys(), bussinessDuringDay.timeOfDayCounts.values())
    ax.set_title('Traffic Over the Course of a Day')
    plt.show()

def plot_popular_combos():
    plt.close('all')  # Close all existing plot windows
    fig, axs = plt.subplots(2, 4, figsize=(15, 10))
    plt.subplots_adjust(wspace=0.25, hspace=0.75)
    
    cheese_counts, meat_counts, drizzle_counts, noods_counts, sides_count, topping_count, drink_count, bought_per_week = popular_combos.mac_che()
    
    
    cheese_counts.plot(kind='bar', ax=axs[0, 0], color='skyblue')
    axs[0, 0].set_title('Cheese Distribution in Mac and Cheese')

    meat_counts.plot(kind='bar', ax=axs[0, 1], color='salmon')
    axs[0, 1].set_title('Meat Distribution in Mac and Cheese')

    drizzle_counts.plot(kind='bar', ax=axs[0, 2], color='grey')
    axs[0, 2].set_title('Drizzle Distribution in Mac and Cheese')

    bought_per_week.plot(kind='bar', ax=axs[0, 3], color='pink')
    axs[0, 3].set_title('Mac n Cheese Bought Per Day')
    axs[0, 3].set_xticklabels(axs[0, 3].get_xticklabels(), rotation=90)

    noods_counts.plot(kind='bar', ax=axs[1, 0], color='yellow')
    axs[1, 0].set_title('Noodle Distribution in Mac and Cheese')

    sides_count.plot(kind='bar', ax=axs[1, 1], color='green')
    axs[1, 1].set_title('Sides Distribution with Mac and Cheese')

    drink_count.plot(kind='bar', ax=axs[1, 2], color='pink')
    axs[1, 2].set_title('Drink Distribution with Mac and Cheese')

    topping_count.plot(kind='bar', ax=axs[1, 3], color='purple')
    axs[1, 3].set_title('Topping Distribution with Mac and Cheese')

    # Annotate the bars with the counts
    for ax in axs.flatten():
        for container in ax.containers:
            ax.bar_label(container)

    plt.show()

if __name__ == "__main__":
    main()
