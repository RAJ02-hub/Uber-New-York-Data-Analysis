#Uber Data Analysis in New York City
This project focuses on analyzing Uber pickups in New York City using Python and various data analysis libraries such as NumPy, Pandas, Seaborn, Matplotlib, Plotly, and Folium.

#Project Overview
The project aims to explore and analyze the Uber pickups dataset to gain insights into the following aspects:

Month with Maximum Uber Pickups in New York City
Total Trips for Each Month and Each Weekday
Hourly Rush in New York City
Most Active Uber Base-number
Cleaning and Preparing the Data for Analysis
Locations in New York with High Rush (Geographical Heat Map)
Automation of Analysis
#Prerequisites
To run the code and replicate the analysis, you need to have the following libraries installed:

NumPy
Pandas
Seaborn
Matplotlib
Plotly
Folium
#Data
The project utilizes Uber pickups data in New York City. The initial dataset used is uber-raw-data-janjune-15.csv. Additionally, data from other files in the same directory is collected and combined for further analysis.

#Project Details
#Month with Maximum Uber Pickups in New York City

The code reads the Uber pickups dataset and extracts the month from the pickup date. It then counts the number of pickups for each month and visualizes the result using a line plot.

#Total Trips for Each Month and Each Weekday

The code calculates the total trips for each month and each weekday by grouping the data based on the month and weekday attributes. It generates a bar plot to show the distribution of Trips across different months and weekdays.

#Hourly Rush in New York City

The code analyzes the hourly rush in New York City by grouping the data based on the weekday and hour attributes. It creates a point plot to visualize the rush hour trends for each weekday.

#Most Active Uber Base-number

The code reads the Uber FOIL dataset (Uber-Jan-Feb-FOIL.csv) and uses Plotly library to create a box plot showing the distribution of active vehicles for each dispatching base number.

#Cleaning and Preparing the Data for Analysis

The code collects and combines data from multiple files in the specified directory. It drops duplicate rows from the final dataset, ensuring data cleanliness and consistency.

#Locations in New York with High Rush (Geographical Heat Map)

The code calculates the count of Uber pickups at different latitude and longitude coordinates. It visualizes the high rush areas using a heat map generated with the help of the Folium library.

#Automation of Analysis

The code defines a function (gen_pivot_table) that allows users to generate pivot tables for different attributes based on their requirements. This function automates the analysis process and enhances code efficiency.

#How to Use
To run the code and reproduce the analysis:

Install the required libraries mentioned in the "Prerequisites" section.
Download the Uber pickups dataset (uber-raw-data-janjune-15.csv) and save it in the specified file path.
Run the code using a Python environment or IDE.
Each section of the code is labeled with a corresponding description. Uncomment the desired sections to execute specific analyses or uncomment the print statements to view intermediate results.
The code will generate visualizations and output analysis results accordingly.
Feel free to explore the code, modify it, and adapt it to suit your specific requirements for Uber data analysis in New York City. Enjoy analyzing the Uber dataset and gaining insights into the trends and patterns of pickups in the city!
