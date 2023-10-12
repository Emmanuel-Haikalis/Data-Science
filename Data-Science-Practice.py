# %%
# Import required libraries
from matplotlib import pyplot as plt
import numpy as np

N = 10000 # Quantity of random points
Z = 100 #Scale of random points

# Generate random data for x, y, and scale (10000 points)
x, y, scale = np.random.randn(3, N)

# Create scatter plot for x vs y, color-coded by scale
fig, ax = plt.subplots()
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*Z)
ax.set(title="Random Data")

# Plot x-axis frequency histogram (1000 bins, blue color, slightly transparent)
plt.figure()
plt.hist(x, bins=100, color='blue', alpha=0.5, label='X-Axis Frequency')
plt.title('X Histogram')
plt.ylabel('Frequency')

# Plot y-axis frequency histogram (1000 bins, green color, slightly transparent)
plt.figure()
plt.hist(y, bins=100, color='green', alpha=0.5, label='Y-Axis Frequency')
plt.title('Y Histogram')
plt.ylabel('Frequency')

# Plot the scale size frequency histogram (100 bins, red color, slightly transparent)
plt.figure()
plt.hist(scale, bins=100, color='red', alpha=0.5, label='Y-Axis Frequency')
plt.title('Scale Histogram')
plt.ylabel('Frequency')

# Plot all graphs together on a frequency histogram (100 bins, red color, slightly transparent)
plt.figure()
plt.hist(x, bins=100, color='blue', alpha=0.5, label='X-Axis Frequency')
plt.hist(y, bins=100, color='green', alpha=0.5, label='Y-Axis Frequency')
plt.hist(scale, bins=100, color='red', alpha=0.5, label='Y-Axis Frequency')
plt.ylabel('Frequency')
plt.legend()

plt.show()


# %%
# Import required libraries
from matplotlib import pyplot as plt
import numpy as np

N = 10000 # Quantity of random points
Z = 100 #Scale of random points

# Generate random data for x, y, and scale (10000 points)
x, y, scale = np.random.randn(3, N)


# Create subplots for the scatter plot and histograms
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Scatter plot on the first subplot
axes[0, 0].scatter(x=x, y=y, c=scale, s=np.abs(scale) * Z)
axes[0, 0].set(title="Random Data")

# X-axis frequency histogram on the second subplot
axes[0, 1].hist(x, bins=100, color='blue', alpha=0.5)
axes[0, 1].set(title='X Histogram')
axes[0, 1].set_ylabel('Frequency')

# Y-axis frequency histogram on the third subplot
axes[1, 0].hist(y, bins=100, color='green', alpha=0.5)
axes[1, 0].set(title='Y Histogram')
axes[1, 0].set_ylabel('Frequency')

# Scale size frequency histogram on the fourth subplot
axes[1, 1].hist(scale, bins=100, color='red', alpha=0.5)
axes[1, 1].set(title='Scale Histogram')
axes[1, 1].set_ylabel('Frequency')

# Adjust layout for better spacing
plt.tight_layout()

# Plot all graphs together on a frequency histogram (100 bins, red color, slightly transparent)
plt.figure()
plt.hist(x, bins=100, color='blue', alpha=0.5, label='X-Axis Frequency')
plt.hist(y, bins=100, color='green', alpha=0.5, label='Y-Axis Frequency')
plt.hist(scale, bins=100, color='red', alpha=0.5, label='Y-Axis Frequency')
plt.ylabel('Frequency')
plt.legend()

# Display the plots
plt.show()


# %%
# Import required libraries
from matplotlib import pyplot as plt
import numpy as np

N = 10000  # Quantity of random points
Z = 10     # Scale of random points

# Generate random data for x, y, and scale (10000 points)
data = np.random.randn(3, N)

# Create subplots for the scatter plot and histograms
fig, axes = plt.subplots(2, 2)

# Plot scatter plot and histograms for x, y, and scale
titles = ["Random Data", 'X Histogram', 'Y Histogram', 'Scale Histogram']
colors = ['blue', 'green', 'red']
for i, ax in enumerate(axes.flat):
    if i == 0:
        ax.scatter(x=data[0], y=data[1], c=data[2], s=np.abs(data[2]) * Z)
    else:
        ax.hist(data[i - 1], bins=100, color=colors[i - 1], alpha=0.5)
        ax.set_ylabel('Frequency')
    ax.set(title=titles[i])

# Adjust layout for better spacing
plt.tight_layout()

# Display the plots
plt.show()


# %%
# Import required libraries
from matplotlib import pyplot as plt
import numpy as np

N = 10000  # Quantity of random points
Z = 10     # Scale of random points

# Generate random data for x, y, and scale (10000 points)
data = np.random.randn(3, N)

# Create subplots for the scatter plot and histograms
fig, axes = plt.subplots(2, 2)

# Plot scatter plot and histograms for x, y, and scale
titles = ["Random Data", 'X Histogram', 'Y Histogram', 'Scale Histogram']
colors = ['blue', 'green', 'red']

# Scatter plot for Random Data
axes[0, 0].scatter(x=data[0], y=data[1], c=data[2], s=np.abs(data[2]) * Z)

# Histograms for X, Y, and Scale
for i in range(1, 4):
    axes[i // 2, i % 2].hist(data[i - 1], bins=100, color=colors[i - 1], alpha=0.5)
    axes[i // 2, i % 2].set(title=titles[i])
    axes[i // 2, i % 2].set_ylabel('Frequency')

# Adjust layout for better spacing
plt.tight_layout()

# Display the plots
plt.show()


# %%
import urllib

tb_deaths_url_csv = 'https://docs.google.com/spreadsheets/d/12uWVH_IlmzJX_75bJ3IH5E-Gqx6-zfbDKNvZqYjUuso/pub?gid=0&output=CSV'
tb_existing_url_csv = 'https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv'
tb_new_url_csv = 'https://docs.google.com/spreadsheets/d/1Pl51PcEGlO9Hp4Uh0x2_QM0xVb53p2UDBMPwcnSjFTk/pub?gid=0&output=csv'

local_tb_deaths_file = 'tb_deaths_100.csv'
local_tb_existing_file = 'tb_existing_100.csv'
local_tb_new_file = 'tb_new_100.csv'

deaths_f = urllib.request.urlretrieve(tb_deaths_url_csv, local_tb_deaths_file)
existing_f = urllib.request.urlretrieve(tb_existing_url_csv, local_tb_existing_file)
new_f = urllib.request.urlretrieve(tb_new_url_csv, local_tb_new_file)

import pandas as pd

deaths_df = pd.read_csv(local_tb_deaths_file, index_col = 0, thousands  = ',').T
existing_df = pd.read_csv(local_tb_existing_file, index_col = 0, thousands  = ',').T
new_df = pd.read_csv(local_tb_new_file, index_col = 0, thousands  = ',').T

existing_df.head()

# %%



