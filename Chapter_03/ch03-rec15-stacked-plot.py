import pandas as pd
import matplotlib.pyplot as plt

# We load the data with pandas.
df = pd.read_csv('ch03-energy-production.csv')

# We give names for the columns that we want to load. Different types of energy have been ordrered by total production values).
columns = ['Coal', 'Natural Gas (Dry)', 'Crude Oil', 'Nuclear Electric Power',
 'Biomass Energy', 'Hydroelectric Power', 'Natural Gas Plant Liquids',
 'Wind Energy', 'Geothermal Energy', 'Solar/PV Energy']

# We define some specific colors to plot each type of energy produced.
colors = ['darkslategray', 'powderblue', 'darkmagenta', 'lightgreen', 'sienna',
'royalblue', 'mistyrose', 'lavender', 'tomato', 'gold']

# Let's create the figure.
plt.figure(figsize = (12,8))
polys = plt.stackplot(df['Year'], df[columns].values.T, colors = colors)

# The legend is not yet supported with stackplot. We will add it manually.
rectangles= []
for poly in polys:
    rectangles.append(plt.Rectangle((0, 0), 1, 1, fc=poly.get_facecolor()[0]))
legend = plt.legend(rectangles, columns, loc = 3)
frame = legend.get_frame()
frame.set_color('white')

# We add some information to the plot.
plt.title('Primary Energy Production by Source', fontsize = 16)
plt.xlabel('Year', fontsize = 16)
plt.ylabel('Production (Quad BTU)', fontsize = 16)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.xlim(1973,2014)

# Finally we show the figure.
plt.show()
