# Solar Weather data analysis
import warnings
from gbc_pearson_product_moment import pearson_correlation as ppmcc
import json
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from scipy.stats import norm
from scipy import interpolate
import time


# Bring in some space data
# NOAA K-index
url = "https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json"
response = requests.get(url)
# Load the data into a JSON
data = json.loads(response.text)
print(data[0]) #Inspect Columns
col = data[0]
data.pop(0)

df = pd.DataFrame(data, columns=col)
# Make a copy as this will get normalized
df_2 = df

try:
    # Get The data into the right types
    df = df.astype({'time_tag':'string', 'speed':'float', 'density':'float', 'temperature':'float', 'bx':'float', 'by':'float', 'bz':'float', 'bt':'float', 'vx':'float', 'vy':'float', 'vz':'float', 'propagated_time_tag':'string'})
    # Set the time_tag to a datetime format
    df['time_tag'] = pd.to_datetime(df['time_tag'])
    # Normailize that data
    df['speed']=(df['speed']-df['speed'].min())/(df['speed'].max()-df['speed'].min())
    df['density']=(df['density']-df['density'].min())/(df['density'].max()-df['density'].min())
    df['temperature']=(df['temperature']-df['temperature'].min())/(df['temperature'].max()-df['temperature'].min())
except Exception as e:
    print(f'Error:\n{e}')
    
    
fig, ax = plt.subplots(1, 1)
plt.xlabel('Sample')
plt.ylabel({'Speed','Temperature', 'Denstity'})
plt.title(f'Plot of Solar wind Speed, Temperature, and Density (Normalized)' )
plt.xticks(rotation=90)
fig.set_size_inches(18.5, 10.5)
fig.savefig('test2png.png', dpi=100)
df.plot(x='time_tag', y='speed', ax=ax)
df.plot(x='time_tag', y='density', ax=ax)
df.plot(x='time_tag', y='temperature', ax=ax)
plt.show()