import pandas
from matplotlib import pyplot as plt

# Obtain the raw data from https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases
df = pandas.read_csv('time_series_covid19_confirmed_global.csv')
df = df.groupby('Country/Region').sum().drop(columns=['Lat', 'Long']).transpose()

# Select which countries to plot
countries = ['Japan', 'Korea, South', 'Italy', 'US', 'Spain', 'France', 'Germany', 'Portugal', 'United Kingdom', 'Australia']

# Skip the first 25 days
skip = 25

# Customize the range of the plot
min_cases = 50
max_cases = 1e5

# Customize the line styles
styles = ['o-', 'v-.', '^:', 's--', 'd-', 'h-.', '>:', '<--', 'X-', 'p-.']

# Customize the grid lines
ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(7))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.grid(which='minor', ls='--', alpha=0.3)

ax.set_title('Confirmed Cases (John Hopkins University Data)')
df[countries].iloc[skip:].plot(ax=ax, logy=True, figsize=(20,15), style=styles, grid=True, ylim=(min_cases, max_cases))

# Optional: save the figure to a file
# Comment out the next line if you do not want this script to create a file
plt.savefig('cases.png', bbox_inches='tight')
