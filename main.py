import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import dataFiles as df
from popular_combos import *
import comboFinder  

# Define color variables
background_color = "#0f1117"
text_color = "white"

# Apply CSS for background and text color
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background-color: {background_color};
            color: {text_color};
        }}
        .sidebar .sidebar-content {{
            background-color: #1a1d23;
        }}
        .css-10trblm, .css-hxt7ib, .css-1cpxqw2 {{
            color: {text_color};
        }}
        .css-1q8dd3e {{
            color: {text_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)


def load_data(month):
    # Fetch various data based on the month
    mac_data = mac_che(month)
    desert_data = desert(month)
    mix_data = mix(month)
    party_tray_data = party_tray(month)
    sandwitch_data = sandwitch(month)

    return {
        "mac_data": mac_data,
        "desert_data": desert_data,
        "mix_data": mix_data,
        "party_tray_data": party_tray_data,
        "sandwitch_data": sandwitch_data,
    }

# Function to show Popular Combos
def show_PopularCombos():
    plt.close('all')  # Close all existing plot windows
    fig, axs = plt.subplots()
    combo_df = comboFinder.comboDF.reset_index()
    combo_df.columns = ['Modifiers', 'Counts']

    comboDfx = combo_df["Modifiers"]
    comboDfy = combo_df["Counts"]

    # Adjust the size as needed
    axs.bar(comboDfx, comboDfy, color='skyblue', edgecolor='black')
    
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    st.pyplot(fig)

# Set up Streamlit dashboard
st.title("Monthly Menu Dashboard")

# Sidebar for month selection including "Overview"
month = st.sidebar.selectbox("Select Month", ["Overview", "April", "August", "July", "June", "May", "October", "September"])

# Display Popular Combos when "Overview" is selected
if month == "Overview":
    st.subheader("Popular Combos")
    show_PopularCombos()
else:
    # Load data for selected month
    data = load_data(month)

    # KPI Metrics - Example using total count of each category
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label="Total Mac & Cheese Orders", value=int(data['mac_data'][7].sum()))
    kpi2.metric(label="Total Dessert Orders", value=int(data['desert_data'][1].sum()))
    kpi3.metric(label="Total Sandwitch Orders", value=int(data['sandwitch_data'][1].sum()))

    # Chart: Weekly Orders for Mac & Cheese
    st.subheader("Mac and Cheese Orders per Week")
    weekly_mac_orders = data['mac_data'][7]
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(background_color)
    ax.set_facecolor(background_color)
    weekly_mac_orders.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_xlabel("Week", color=text_color)
    ax.set_ylabel("Orders", color=text_color)
    ax.tick_params(colors=text_color)
    st.pyplot(fig)

    # Donut Chart for Cheese Options
    st.subheader("Mac & Cheese - Cheese Selection")
    cheese_counts = data['mac_data'][0]
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(background_color)
    ax.set_facecolor(background_color)
    ax.pie(
        cheese_counts, labels=cheese_counts.index, autopct='%1.1f%%', startangle=140, 
        colors=["#66b3ff", "#99ff99", "#ffcc99", "#ff6666"], wedgeprops=dict(width=0.3)
    )
    plt.setp(ax.texts, color=text_color)  # Set text color for pie chart
    st.pyplot(fig)

    # Chart for Dessert Side Options
    st.subheader("Dessert Side Options")
    side_counts = data['desert_data'][0]
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(background_color)
    ax.set_facecolor(background_color)
    side_counts.plot(kind='bar', ax=ax, color='coral')
    ax.set_xlabel("Side Option", color=text_color)
    ax.set_ylabel("Count", color=text_color)
    ax.tick_params(colors=text_color)
    st.pyplot(fig)

    # MIX Options Data Table
    st.subheader("MIX Base Options Count")
    st.table(data['mix_data'][0])

    # Party Tray Options
    st.subheader("Party Tray Options Count")
    party_counts = data['party_tray_data'][0]
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(background_color)
    ax.set_facecolor(background_color)
    party_counts.plot(kind='bar', ax=ax, color='lightgreen')
    ax.set_xlabel("Party Tray Option", color=text_color)
    ax.set_ylabel("Count", color=text_color)
    ax.tick_params(colors=text_color)
    st.pyplot(fig)

    # Grilled Cheese Sandwich Data Breakdown
    st.subheader("Grilled Cheese Sandwich - Cheese, Meat, and Toppings")
    cheese_counts, mac_count, meat_counts, drizzle_counts, sides_count, topping_count, drink_count, weekly_sandwich_orders = data['sandwitch_data']

    # Create multiple bar charts for sandwich options
    fig, axs = plt.subplots(2, 3, figsize=(15, 8))
    fig.patch.set_facecolor(background_color)
    for ax in axs.flatten():
        ax.set_facecolor(background_color)

    cheese_counts.plot(kind='bar', ax=axs[0, 0], color='dodgerblue', title='Cheese Choices')
    meat_counts.plot(kind='bar', ax=axs[0, 1], color='salmon', title='Meat Choices')
    topping_count.plot(kind='bar', ax=axs[0, 2], color='purple', title='Toppings')
    sides_count.plot(kind='bar', ax=axs[1, 0], color='gold', title='Sides')
    drink_count.plot(kind='bar', ax=axs[1, 1], color='orange', title='Drinks')
    axs[1, 2].remove()  # Remove the unused subplot

    for ax in axs.flatten():
        if ax:
            ax.title.set_color(text_color)
            ax.tick_params(colors=text_color)
            ax.set_xlabel(ax.get_xlabel(), color=text_color)
            ax.set_ylabel(ax.get_ylabel(), color=text_color)

    plt.tight_layout()
    st.pyplot(fig)

    # Summary Table
    st.subheader("Weekly Orders for Sandwiches")
    st.table(weekly_sandwich_orders)
