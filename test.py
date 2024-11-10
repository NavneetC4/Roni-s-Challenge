import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os


# Directory for data files
data_directory = "Provided Data [FINAL]"
csv_files = [os.path.join(data_directory, file) for file in os.listdir(data_directory) if file.endswith(".csv")]

# Load and concatenate CSV files into a single DataFrame
all_data = pd.concat([pd.read_csv(file, encoding='ISO-8859-1') for file in csv_files], ignore_index=True)
all_data['Sent Date'] = pd.to_datetime(all_data['Sent Date'], errors='coerce')
all_data['YearMonth'] = all_data['Sent Date'].dt.to_period('M').astype(str)

# Add Overview Section with KPIs and Visualizations from Dash Code


# KPIs
st.subheader("Key Performance Indicators")
total_customers = all_data.groupby('YearMonth')['Order ID'].nunique().sum()
average_order_size = all_data.groupby('Order ID').size().mean()
top_menu_item = all_data['Parent Menu Selection'].mode()[0]
monthly_growth = all_data.groupby('YearMonth')['Order ID'].nunique().pct_change().fillna(0) * 100
avg_monthly_growth = monthly_growth.mean()

st.write(f"Total Customers: {total_customers}")
st.write(f"Average Order Size: {average_order_size:.2f} items")
st.write(f"Top-Selling Menu Item: {top_menu_item}")
st.write(f"Average Monthly Growth: {avg_monthly_growth:.2f}%")

# Monthly Customers Trend
monthly_customers = all_data.groupby('YearMonth')['Order ID'].nunique().reset_index()
fig1 = px.line(monthly_customers, x='YearMonth', y='Order ID', markers=True,
                title='Monthly Customers Trend', labels={'YearMonth': 'Month', 'Order ID': 'Number of Customers'})
st.plotly_chart(fig1)

# Seasonal Trends of Top 5 Toppings
toppings_data = all_data[all_data['Option Group Name'] == 'Choose Your Toppings']
seasonal_toppings = toppings_data.groupby(['YearMonth', 'Modifier']).size().unstack().fillna(0)
top_5_toppings = seasonal_toppings.sum().nlargest(5).index
fig2 = go.Figure()
for topping in top_5_toppings:
    fig2.add_trace(go.Scatter(x=seasonal_toppings.index, y=seasonal_toppings[topping],
                                mode='lines+markers', name=topping))
fig2.update_layout(title='Seasonal Trends of Top 5 Toppings', xaxis_title='Month', yaxis_title='Selections')
st.plotly_chart(fig2)

# Heatmap of Top 10 Modifiers
top_10_modifiers = toppings_data['Modifier'].value_counts().nlargest(10).index
modifier_popularity = toppings_data[toppings_data['Modifier'].isin(top_10_modifiers)]
modifier_heatmap = modifier_popularity.groupby(['YearMonth', 'Modifier']).size().unstack().fillna(0)
fig3 = px.imshow(modifier_heatmap.T, title='Heatmap of Top 10 Modifiers')
st.plotly_chart(fig3)

# Top 5 Menu Items
top_menu_items = all_data['Parent Menu Selection'].value_counts().nlargest(5)
fig4 = px.bar(top_menu_items, x=top_menu_items.index, y=top_menu_items.values,
                title='Top 5 Menu Items', labels={'x': 'Menu Item', 'y': 'Count'})
st.plotly_chart(fig4)

# Month Selection Dropdown and Pie Chart for Topping Distribution
unique_months = sorted(all_data['YearMonth'].unique())
selected_month = st.selectbox("Select a Month for Topping Distribution:", unique_months)

# Pie Chart for Topping Distribution
monthly_data = all_data[all_data['YearMonth'] == selected_month]
topping_counts = monthly_data[monthly_data['Option Group Name'] == 'Choose Your Toppings']['Modifier'].value_counts()
fig5 = px.pie(topping_counts, values=topping_counts.values, names=topping_counts.index,
                title=f'Topping Distribution for {selected_month}')
st.plotly_chart(fig5)

# Customer Segmentation Analysis
order_sizes = monthly_data.groupby('Order ID').size()
average_modifiers = monthly_data.groupby('Order ID')['Modifier'].nunique().mean()

st.subheader(f"Customer Segmentation Analysis for {selected_month}")
st.write(f"Average Order Size: {order_sizes.mean():.2f} items")
st.write(f"Average Number of Modifiers per Order: {average_modifiers:.2f}")

# Original Streamlit sections go here, unchanged from your initial Streamlit code.
