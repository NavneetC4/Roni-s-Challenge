import matplotlib.pyplot as plt
import numpy as np

# Example data and variables
x = np.linspace(0, 10, 100)
y = np.sin(x)
total_plots = 10
plots_per_page = 2
current_page = 0

# Function to plot a page of subplots
def plot_page(page):
    plt.clf()
    fig, axes = plt.subplots(plots_per_page, 1, figsize=(8, 4 * plots_per_page))
    for i in range(plots_per_page):
        idx = page * plots_per_page + i
        if idx < total_plots:
            axes[i].plot(x, y * (idx + 1))
            axes[i].set_title(f"Plot {idx + 1}")
    fig.suptitle(f"Page {page + 1}")
    plt.draw()

# Initial plot
fig = plt.figure()
plot_page(current_page)

# Function to change page
def on_key(event):
    global current_page
    if event.key == "right" and (current_page + 1) * plots_per_page < total_plots:
        current_page += 1
    elif event.key == "left" and current_page > 0:
        current_page -= 1
    plot_page(current_page)

# Connect to key press event
fig.canvas.mpl_connect("key_press_event", on_key)
plt.show()
