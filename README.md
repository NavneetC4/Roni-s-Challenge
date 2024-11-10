# Roni-s-Challenge

## Inspiration
We were inspired to take on this project given it's beginner-friendly nature and opportunities for creativity. The functionality of the dashboard was originally inspired by the need to evaluate the data in terms of the month and provide "monthly specials" for Roni's to explore.

## What it does
Our dashboard provides the user with the ability to navigate different evaluations of data per month. Given the different categories of modifiers for either Mac and Cheese and Grilled Cheese Sandwiches, our dashboard shows the most common drizzles, meats, cheeses, and toppings used as modifiers each month (including special consideration for mixing cheese bases). Given this information, we suggest that Roni's create a monthly special based off of the most popular items. We have provided the most popular combos in the "Overview" tab.

Second, we provide an evaluation of the amount of party trays per month. Roni's is encouraged to evaluate their most popular party tray and diversify 

Additionally, the dashboard looks at how much Mac and Cheese is ordered per week, per month. As previously stated, users will be able to toggle through the data evaluations for each month using a dropdown menu.

The dashboard also looks at the busiest times of day over all the months provided in the dataset. This can help Roni's with scheduling employees and predicting (and preparing for) rush hours in the future.


## How we built it
1.bussinessDuringDay
This module iterates through the list of csv dataframes, and for each time block (ex 10-11am) it records a count for every order taken during that time period. This can help Roni to determine when peak hours are to have more employees on hand, and during slow hours so that Roni’s can give special durings those times (ex happy hour) so that they drive more sales.

2.comboFinder
This module iterates through a dataframe containing all the months data, and gives each customer a unique id corresponding to their customer id and month that they ordered in. Then the data frame counts the occurrences of the customers specific modifiers. This in turn determines what the most popular combo that customers order. This could help Roni’s to implement combos into their meals so that customers can quickly say a number and employees can create an empty number corresponding to that meal.

3.dataFiles
dataFiles is a module that imports pandas to read all the relevant csv. This module is then imported into the various classes that need to read the csv. This increases performance as we do not need more files to import pandas and read the csv individually. 

4. popular_combos
This module iterates through the CSV based on a given month, sorts through the CSV to isolate data for each element, Mac and Cheese, Desserts, Cheese mix, party tray and Grilled Cheese Sandwich. The sorted data is then processed and finds the number of each modifier in each element.  Using this information it returns the number of modifier instances in an element as a pandas series. This can help Roni’s to identify the most popular modifier for each element in different months and help more accurately predict the stock required in the future.


## Challenges we ran into
Our biggest challenge was that GitHub hindered us in some cases instead of adding an advantage. Since we were relatively new to it, there were some issues coordinating properly. After we separated to work on our side of the project, combining the files at the end was quite difficult.

We also have issues with performance when handling large quantities of data. Using numpy and pandas libraries helped to improve performance instead of using native python objects like lists.

## Accomplishments that we're proud of
Although we encountered the previously mentioned challenges, our biggest achievement was facing them head-on and solving any issues that crossed our path. We worked through our use of GitHub and were able to improve performance significantly from where we started.

## What we learned

We learned how to use git to effectively manage every individual's codes and later to merge the files to create a final project. In addition, we learned how to use pandas libraries to manage data and perform sorting operations and how to use matplotlib to plot data in various manners like histograms, bar graphs, and plots. 

Some more minor insights, include using time objects to compare times.

##Video Preview of our program
https://youtu.be/-hX0GaUtWI8

