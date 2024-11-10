import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import os

# Initialize the Dash app
app = Dash(__name__)
app.title = "Enhanced Interactive Dashboard"

# CSS
app.css.append_css({
    'external_url': 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'
})

# Directory where the CSV files are located
data_directory = "Roni-s-Challenge/Provided Data [FINAL]/"
csv_files = [os.path.join(data_directory, file) for file in os.listdir(data_directory) if file.endswith(".csv")]

# Read and concatenate all CSV files into a single DataFrame
all_data = pd.concat([pd.read_csv(file, encoding='ISO-8859-1') for file in csv_files], ignore_index=True)
all_data['Sent Date'] = pd.to_datetime(all_data['Sent Date'], errors='coerce')
all_data['YearMonth'] = all_data['Sent Date'].dt.to_period('M').astype(str)

# Graphs
monthly_customers = all_data.groupby('YearMonth')['Order ID'].nunique().reset_index()
fig1 = px.line(monthly_customers, x='YearMonth', y='Order ID', markers=True,
               title='Monthly Customers Trend', labels={'YearMonth': 'Month', 'Order ID': 'Number of Customers'})

toppings_data = all_data[all_data['Option Group Name'] == 'Choose Your Toppings']
seasonal_toppings = toppings_data.groupby(['YearMonth', 'Modifier']).size().unstack().fillna(0)
top_5_toppings = seasonal_toppings.sum().nlargest(5).index
fig2 = go.Figure()
for topping in top_5_toppings:
    fig2.add_trace(go.Scatter(x=seasonal_toppings.index, y=seasonal_toppings[topping],
                              mode='lines+markers', name=topping))
fig2.update_layout(title='Seasonal Trends of Top 5 Toppings', xaxis_title='Month', yaxis_title='Selections')

# KPI Section
total_customers = all_data.groupby('YearMonth')['Order ID'].nunique()
average_order_size = all_data.groupby('Order ID').size().mean()
top_menu_item = all_data['Parent Menu Selection'].mode()[0]
monthly_growth = total_customers.pct_change().fillna(0) * 100

# Simplified Heatmap
top_10_modifiers = toppings_data['Modifier'].value_counts().nlargest(10).index
modifier_popularity = toppings_data[toppings_data['Modifier'].isin(top_10_modifiers)]
modifier_heatmap = modifier_popularity.groupby(['YearMonth', 'Modifier']).size().unstack().fillna(0)
fig3 = px.imshow(modifier_heatmap.T, title='Heatmap of Top 10 Modifiers')

# Top Menu Items Bar Chart
top_menu_items = all_data['Parent Menu Selection'].value_counts().nlargest(5)
fig4 = px.bar(top_menu_items, x=top_menu_items.index, y=top_menu_items.values,
              title='Top 5 Menu Items', labels={'x': 'Menu Item', 'y': 'Count'})

# Dropdown for Month Selection
unique_months = sorted(all_data['YearMonth'].unique())

# Layout
app.layout = html.Div(className='container mt-4', children=[
    html.H1("Enhanced Interactive Dashboard", className='text-center mb-4'),
    html.Div(className='card mb-4', children=[
        html.Div(className='card-body', children=[
            html.H4("Key Performance Indicators", className='card-title'),
            html.P(f"Total Customers: {total_customers.sum()}", className='card-text'),
            html.P(f"Average Order Size: {average_order_size:.2f} items", className='card-text'),
            html.P(f"Top-Selling Menu Item: {top_menu_item}", className='card-text'),
            html.P(f"Average Monthly Growth: {monthly_growth.mean():.2f}%", className='card-text')
        ])
    ]),
    html.Div(className='row', children=[
        html.Div(className='col-md-6', children=[
            dcc.Graph(id='monthly-customers-trend', figure=fig1)
        ]),
        html.Div(className='col-md-6', children=[
            dcc.Graph(id='seasonal-toppings-trend', figure=fig2)
        ])
    ]),
    html.Div(className='row', children=[
        html.Div(className='col-md-6', children=[
            dcc.Graph(id='heatmap-modifier-popularity', figure=fig3)
        ]),
        html.Div(className='col-md-6', children=[
            dcc.Graph(id='top-menu-items-bar', figure=fig4)
        ])
    ]),
    html.Div(className='card mt-4', children=[
        html.Div(className='card-body', children=[
            html.Label("Select a Month:", className='form-label'),
            dcc.Dropdown(id='month-dropdown', options=[{'label': month, 'value': month} for month in unique_months],
                         value=unique_months[0], clearable=False),
            dcc.Graph(id='pie-chart-topping-distribution')
        ])
    ]),
    html.Div(id='customer-segmentation-analysis', className='mt-4')
])

# Callbacks
@app.callback(
    Output('pie-chart-topping-distribution', 'figure'),
    Input('month-dropdown', 'value')
)
def update_pie_chart(selected_month):
    monthly_data = all_data[all_data['YearMonth'] == selected_month]
    topping_counts = monthly_data[monthly_data['Option Group Name'] == 'Choose Your Toppings']['Modifier'].value_counts()
    fig = px.pie(topping_counts, values=topping_counts.values, names=topping_counts.index,
                 title=f'Topping Distribution for {selected_month}')
    return fig

@app.callback(
    Output('customer-segmentation-analysis', 'children'),
    Input('month-dropdown', 'value')
)
def update_customer_segmentation(selected_month):
    monthly_data = all_data[all_data['YearMonth'] == selected_month]
    order_sizes = monthly_data.groupby('Order ID').size()
    average_modifiers = monthly_data.groupby('Order ID')['Modifier'].nunique().mean()

    return html.Div([
        html.H4(f"Customer Segmentation Analysis for {selected_month}"),
        html.P(f"Average Order Size: {order_sizes.mean():.2f} items"),
        html.P(f"Average Number of Modifiers per Order: {average_modifiers:.2f}")
    ])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
