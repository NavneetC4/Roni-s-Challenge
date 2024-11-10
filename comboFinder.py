import dataFiles
import pandas as pd
import numpy as np

def main():
    # List of dataframes for each month
    list_of_months = [
        dataFiles.aprilCSV, dataFiles.mayCSV, dataFiles.juneCSV,
        dataFiles.julyCSV, dataFiles.augustCSV, dataFiles.septemberCSV,
        dataFiles.octoberCSV
    ]

    # Initialize dictionary with NumPy array for userID and list for userModifiers
    data_dict = {
        "userID": np.array([], dtype=str),
        "userModifiers": []
    }

    # Combine all monthly dataframes into one
    combined_df = pd.concat(list_of_months, ignore_index=True)

    # Iterate through each row in the combined dataframe
    for index, row in combined_df.iterrows():
        try:
            extract_user_id = row["Order ID"] + "_" + row["Sent Date"][5:7]
            if extract_user_id not in data_dict["userID"]:
                # Initialize the entry in the dictionary
                data_dict["userID"] = np.append(data_dict["userID"], extract_user_id)
                data_dict["userModifiers"].append(row["Modifier"])
            else:
                # Update the existing entry
                idx = np.where(data_dict["userID"] == extract_user_id)[0][0]
                data_dict["userModifiers"][idx] += "," + row["Modifier"]
        except:
            continue

    # Convert dictionary to DataFrame
    dict_to_df = pd.DataFrame(data_dict)

    # Count the occurrences of each combination of userModifiers
    count_df = dict_to_df["userModifiers"].value_counts()

    # Get the top 10 combinations that contain commas
    combo_df = count_df[count_df.index.str.contains(",")].iloc[0:10]


if __name__ == "__main__":
    main()
