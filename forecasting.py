import pandas as pd
import matplotlib.pyplot as plt
import glob

# Load all monthly CSV files
file_paths = glob.glob("/mnt/data/*.csv")
data_frames = {}
for file_path in file_paths:
    month = file_path.split("/")[-1].split(".")[0]
    data_frames[month] = pd.read_csv(file_path, encoding='ISO-8859-1')

# Combine all data into a single DataFrame
combined_df = pd.concat(data_frames.values(), ignore_index=True)

# Convert 'Sent Date' to datetime format
combined_df['Sent Date'] = pd.to_datetime(combined_df['Sent Date'], errors='coerce')
combined_df = combined_df.dropna(subset=['Sent Date'])

# Extract month and season information
combined_df['Month'] = combined_df['Sent Date'].dt.month

# Define a function to map months to seasons
def get_season(month):
    if month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'
    else:
        return 'Winter'

# Add a 'Season' column
combined_df['Season'] = combined_df['Month'].apply(get_season)

# Filter for rows related to toppings
toppings_df = combined_df[combined_df['Option Group Name'].str.contains('Toppings', case=False, na=False)]

# Group by 'Season' and 'Modifier' (topping name) to calculate frequency
seasonal_toppings = toppings_df.groupby(['Season', 'Modifier'])['Order #'].count().reset_index()
seasonal_toppings.columns = ['Season', 'Topping', 'Frequency']

# Find the top 10 most popular toppings for each season
top_toppings_by_season = seasonal_toppings.sort_values(by=['Season', 'Frequency'], ascending=[True, False]).groupby('Season').head(10)

# Plot the most popular toppings for each season
plt.figure(figsize=(14, 8))
for season in top_toppings_by_season['Season'].unique():
    season_data = top_toppings_by_season[top_toppings_by_season['Season'] == season]
    plt.bar(season_data['Topping'], season_data['Frequency'], label=season)

plt.title("Top 10 Most Popular Toppings by Season")
plt.xlabel("Topping")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.legend(title="Season")
plt.grid()
plt.show()
