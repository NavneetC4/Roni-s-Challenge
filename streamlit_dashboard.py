import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import os
import subprocess

# Set Streamlit page configuration
st.set_page_config(page_title="Enhanced Interactive Dashboard", layout="wide")

# Directory where the CSV files are located
data_directory = "Provided Data [FINAL]"
csv_files = [os.path.join(data_directory, file) for file in os.listdir(data_directory) if file.endswith(".csv")]

# Define theme and color palette
dark_theme_layout = {
    "plot_bgcolor": "#1c1c1c",
    "paper_bgcolor": "#1c1c1c",
    "font": {"color": "#ffffff"},
    "xaxis": {"gridcolor": "#444444"},
    "yaxis": {"gridcolor": "#444444"},
}

neon_colors = ["#0ff", "#f0f", "#0f0", "#ff0"]

# Read and concatenate all CSV files into a single DataFrame
all_data = pd.concat([pd.read_csv(file, encoding='ISO-8859-1') for file in csv_files], ignore_index=True)
all_data['Sent Date'] = pd.to_datetime(all_data['Sent Date'], errors='coerce')
all_data['YearMonth'] = all_data['Sent Date'].dt.to_period('M').astype(str)

# KPI Section
total_customers = all_data.groupby('YearMonth')['Order ID'].nunique()
average_order_size = all_data.groupby('Order ID').size().mean()
top_menu_item = all_data['Parent Menu Selection'].mode()[0]
monthly_growth = total_customers.pct_change().fillna(0) * 100

# Display KPIs
st.title("Enhanced Interactive Dashboard")
st.markdown("### Key Performance Indicators")
st.metric("Total Customers", total_customers.sum())
st.metric("Average Order Size", f"{average_order_size:.2f} items")
st.metric("Top-Selling Menu Item", top_menu_item)
st.metric("Average Monthly Growth", f"{monthly_growth.mean():.2f}%")

# Monthly Customers Trend
monthly_customers = all_data.groupby('YearMonth')['Order ID'].nunique().reset_index()
fig1 = px.line(
    monthly_customers,
    x='YearMonth',
    y='Order ID',
    markers=True,
    title='Monthly Customers Trend',
    labels={'YearMonth': 'Month', 'Order ID': 'Number of Customers'}
)
fig1.update_traces(
    line=dict(color=neon_colors[0], width=3),
    marker=dict(color=neon_colors[1], size=10, line=dict(color=neon_colors[2], width=2))
)
fig1.update_layout(dark_theme_layout)
st.plotly_chart(fig1)

# Seasonal Toppings Trend
toppings_data = all_data[all_data['Option Group Name'] == 'Choose Your Toppings']
seasonal_toppings = toppings_data.groupby(['YearMonth', 'Modifier']).size().unstack().fillna(0)
top_5_toppings = seasonal_toppings.sum().nlargest(5).index
fig2 = go.Figure()
for topping in top_5_toppings:
    fig2.add_trace(go.Scatter(
        x=seasonal_toppings.index,
        y=seasonal_toppings[topping],
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(size=10, line=dict(width=2)),
        name=topping
    ))
fig2.update_layout(dark_theme_layout, title='Seasonal Trends of Top 5 Toppings')
st.plotly_chart(fig2)

# Heatmap of Top 10 Modifiers
top_10_modifiers = toppings_data['Modifier'].value_counts().nlargest(10).index
modifier_popularity = toppings_data[toppings_data['Modifier'].isin(top_10_modifiers)]
modifier_heatmap = modifier_popularity.groupby(['YearMonth', 'Modifier']).size().unstack().fillna(0)
fig3 = px.imshow(
    modifier_heatmap.T,
    aspect="auto",
    title='Heatmap of Top 10 Modifiers',
    color_continuous_scale='Viridis'
)
fig3.update_layout(dark_theme_layout)
st.plotly_chart(fig3)

# Top Menu Items Bar Chart
top_menu_items = all_data['Parent Menu Selection'].value_counts().nlargest(5)
fig4 = px.bar(
    top_menu_items,
    x=top_menu_items.index,
    y=top_menu_items.values,
    title='Top 5 Menu Items',
    labels={'x': 'Menu Item', 'y': 'Count'},
    color_discrete_sequence=['#87CEEB']
)
fig4.update_layout(dark_theme_layout)
st.plotly_chart(fig4)

# Month Dropdown for Pie Chart
unique_months = sorted(all_data['YearMonth'].unique())
selected_month = st.selectbox("Select a Month:", unique_months)

# Pie Chart for Topping Distribution
monthly_data = all_data[all_data['YearMonth'] == selected_month]
topping_counts = monthly_data[monthly_data['Option Group Name'] == 'Choose Your Toppings']['Modifier'].value_counts()
fig5 = px.pie(
    topping_counts,
    values=topping_counts.values,
    names=topping_counts.index,
    title=f'Topping Distribution for {selected_month}',
    color_discrete_sequence=px.colors.sequential.RdBu
)
fig5.update_layout(dark_theme_layout)
st.plotly_chart(fig5)

# Customer Segmentation Analysis
st.markdown(f"### Customer Segmentation Analysis for {selected_month}")
order_sizes = monthly_data.groupby('Order ID').size()
average_modifiers = monthly_data.groupby('Order ID')['Modifier'].nunique().mean()
st.write(f"Average Order Size: {order_sizes.mean():.2f} items")
st.write(f"Average Number of Modifiers per Order: {average_modifiers:.2f}")

# Button to go back to the main dashboard
if st.button("Back to Main Dashboard"):
    st.write("Redirecting to Main Dashboard...")
    subprocess.Popen(["streamlit", "run", "main.py"])
