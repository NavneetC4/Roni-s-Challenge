import dataFiles
import bussinessDuringDay
from matplotlib import pyplot as plt

# Turn on interactive mode
plt.ion()
fig, ax = plt.subplots()

def main():
    choice = ""
    while choice.lower() != "stop":
        print("Select a plot to display:")
        print("1. Traffic Over the Course of a Day")
        print("0. Exit")

        choice = input("Enter your choice by its number: ")

        if choice == '1':
            plot_traffic(ax)
        elif choice == '0':
            print("Exiting...")
            plt.close()
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

def plot_traffic(ax):
    ax.clear()
    ax.bar(bussinessDuringDay.timeOfDayCounts.keys(), bussinessDuringDay.timeOfDayCounts.values())
    ax.set_title('Traffic Over the Course of a Day')
    plt.draw()

if __name__ == "__main__":
    main()
    plt.show(block=True)  # Keep the window open
