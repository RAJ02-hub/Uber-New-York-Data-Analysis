import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objs as po
import plotly.express as px
from plotly.offline import download_plotlyjs,plot,iplot,init_notebook_mode
import os
import folium
from folium.plugins import HeatMap


uber_15 = pd.read_csv(r'C:\Data Science\Projects\Uber New York\uber-pickups-in-new-york-city\uber-raw-data-janjune-15.csv')
# print(uber_15.head())                     # .head(x) returns x rows from the top of the dataset and .tail(x) returns x rows from the bottom of the dataset
# print(uber_15.shape)                      # .shape() returns the rows and columns of the selected data
print(uber_15.duplicated().sum())           # Returns total number of duplicate values
(uber_15.drop_duplicates(inplace=True))     # Removes all the duplicates values from the dataset
# print(uber_15.shape)



# 1. Which Month have Maximum Uber pickups in the NEW YORK CITY

print(uber_15.dtypes)                       # Returns data types of dataset
# We have to change the data type of Pickup_date to Datetime object through pandas
pd.to_datetime(uber_15['Pickup_date'],format='%Y-%m-%d %H:%M:%S')
uber_15['Pickup_date'] = pd.to_datetime(uber_15['Pickup_date'],format='%Y-%m-%d %H:%M:%S')      # Updating the Pickup_date datatype
print(uber_15.dtypes)

# Extracting Month from Pickup_date
uber_15['Month'] = uber_15['Pickup_date'].dt.month
counts = uber_15['Month'].value_counts()
plt.plot(counts)            # Can set any type of graph depending on the requirements
plt.show()



# 2. Finding out Total trips for each month & each weekday

uber_15['Weekday'] = uber_15['Pickup_date'].dt.day_name()
uber_15['Day'] = uber_15['Pickup_date'].dt.day
uber_15['hour'] = uber_15['Pickup_date'].dt.hour
uber_15['month'] = uber_15['Pickup_date'].dt.month
uber_15['Minutes'] = uber_15['Pickup_date'].dt.minute


print(uber_15.groupby(['month','Weekday'],as_index=False).size())
temp = uber_15.groupby(['month','Weekday'],as_index=False).size()
print(temp.head())

print(temp['month'].unique())

# Defining a dictionary to map the months according the cardinal number (i.e. 1--> jan)

dict_month = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'}
temp['month'] = temp['month'].map(dict_month)
print(temp)
sns.barplot(x='month',y='size',hue='Weekday',data=temp)
plt.show()



# 3. Finding out hourly rush in NYC

uber_15.groupby(['Weekday','hour']).size()
summary = uber_15.groupby(['Weekday','hour'],as_index=False).size()
print(summary)

# Here pointplot is a good option for analysis
sns.pointplot(x='hour',y='size',hue='Weekday',data=summary)
plt.show()



# 4. Analysing most active Uber Base-number

uber_foil = pd.read_csv(r'C:\Data Science\Projects\Uber New York\uber-pickups-in-new-york-city\Uber-Jan-Feb-FOIL.csv')

# Using the plotly lib

init_notebook_mode(connected=True)

px.box(x='dispatching_base_number',y='active_vehicles',data_frame=uber_foil)
plt.show()



# 5. Collect the entire data & make it ready for data analysis :
# a). Here we have to clean the data and prepare it for analysis.
# b). It includes recognizing duplicate rows, missing values and checking whether the datatype is correct or not.

# import os

files = os.listdir(r'C:\Data Science\Projects\Uber New York\uber-pickups-in-new-york-city')[-7:]       # We want data from APRIL to SEPTEMBER,
# so we are using negative index to get them and then storing it in files variable
files.remove('uber-raw-data-janjune-15.csv')        # Removing this file as it was not required
# print(files)
path = r'C:\Data Science\Projects\Uber New York\uber-pickups-in-new-york-city'

final = pd.DataFrame()

for file in files:
    current_df = pd.read_csv(path+'/'+file,encoding='utf-8')
    final = pd.concat([current_df,final])

# Dropping the duplicate values
final.duplicated()     # Adding .sum() at the end gives count of the total duplicate rows in the dataset
final.drop_duplicates(inplace=True)



# 6. Finding out the locations in New York where Rush is high (Use of heat map is considered specifically Geographical Heat map)
# Heat map is usually used when we have to find the areas of High,low,Average intensity
# Here, in this longitude and latitudes are required to compute the count by using groupby functionality
# Folium lib is used to get World map for plotting a heat map i.e. folium.Map

rush_uber = final.groupby(['Lat','Lon'],as_index=False).size()
print(rush_uber)

basemap = folium.Map()
HeatMap(rush_uber).add_to(basemap)      # Here, data is rush_uber which is mapped upon the world map through basemap
print(basemap)
plt.show()

# Figuring out rush on various days ( i.e. pair-wise analysis)
# Examining rush on particular hour and weekdays
# Concept : converting a dataframe into a pivot table

final['Date/Time'] = pd.to_datetime(final['Date/Time'],format='%m/%d/%Y %H:%M:%S')
# Now, we need the day & hour
final['weekday'] = final['Date/Time'].dt.day
final['hour'] = final['Date/Time'].dt.hour

pivot = final.groupby(['weekday','hour']).size().unstack()          # Changing the data type from series to pivot
print(pivot)

pivot.style.background_gradient()
print(pivot.style.background_gradient())



# 7. How to Automate your analysis
# In the previous section we used DAY AND HOUR as our attributes to find the rush.
# We can instead create a function through which we can use any attributes based upon our requirement
# Basically, automating your code is the most important thing to develop an efficient code

def gen_pivot_table(df,col1,col2):
    pivot1 = df.groupby([col1,col2]).size().unstack()
    return print(pivot.style.background_gradient())

# Simply calling this function will do the work
