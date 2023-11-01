import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data Visualization in Python with `Matplotlib` and `Seaborn`

"""
**Data visualization** is the process of searching, interpreting, contrasting and 
    comparing data that allows in-depth and detailed knowledge of the data in such
    a way that they become comprehensible information. There are several packages 
    in Python for data visualization, among which are: 
    
- `Matplotlib`: It is the most used library for plotting in the Python community,
    despite having more than a decade of development. Because matplotlib was the 
    first Python data visualization library, many other libraries are built on top of it.
    Some libraries like `pandas` and `Seaborn` are wrappers over `matplotlib`.
- `Seaborn`: leverages matplotlib's ability to create aesthetic graphics in a few lines
    of code. The most palpable difference is Seaborn's default styles and color palettes,
    which are designed to be more aesthetically pleasing and modern.
- `Pandas` plotting: allows data visualization through adaptations of the `matplotlib` 
    library, facilitating the data aggregation and manipulation in a few lines of code.
- `Plotly`: allows the data viusalization by interactive plots, offering additional chart
    configurations as contour plots, dendograms, and 3D charts.
- `ggplot`: is based on *ggplot2* from R plotting system. `ggplot` operates differently
    than `matplotlib` and `seaborn`, making layers fromo its components to create a 
    complete plot.
- `Bokeh`: creates interactive, web-ready plots, which can be easily output as JSON 
    objects, HTML documents, or interactive web applications, supporting streaming and
    real-time data.
- `AstroPy`: is a collection of software packages written in the Python, and designed for
    use in astronomy.
- `Gleam`: is inspired by R's Shiny package. It allows to turn analysis into interactive
    web applications using only Python scripts, avoiding the use of other languages like 
    HTML, CSS, or JavaScript.
- `Geoplotlib`: is a toolbox for creating maps and plotting geographical data by creating
    a variety of map-types, like choropleths, heatmaps, and dot density maps.
- `Missingno`: allows to quickly gauge the completeness of a dataset with a visual summary,
    instead of trudging through a table.

In this notebook we will be reviewing the data visualization process through `matplotlib`
and `seaborn` packages, which are considerably malleable and very flexible, allowing a
better understanding of the behavior of the plotted variables.
"""

# I - Matplotlib

"""
`Matplotlib` is a comprehensive library for creating static, animated, and interactive
visualizations in Python. It is useful for those working with `Python` and `NumPy`.

`Matplotlib`'s charts are made up of two main components:
1. **The axes:** the lines that delimit the area of the chart
2. **The figure:** where we draw the axes, titles and elements that come out of the area 
    of the axes.
"""

# 1 - load the dataset 

x = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv") 

# or 
x = pd.read_csv('./datasets/Standard_Metropolitan_Areas_Data-data.csv')

# 2 - check what all variables/fields are there in the dataset
print(x.head())

"""
   land_area  percent_city  percent_senior  physicians  ...  work_force  income  region  crime_rate
0       1384          78.1            12.3       25627  ...      4083.9   72100       1       75.55
1       3719          43.9             9.4       13326  ...      3305.9   54542       2       56.03
2       3553          37.4            10.7        9724  ...      2066.3   33216       1       41.32
3       3916          29.9             8.8        6402  ...      1966.7   32906       2       67.38
4       2480          31.5            10.5        8502  ...      1514.5   26573       4       80.19

[5 rows x 10 columns]
"""

print(x.columns)
"""
Index(['land_area', 'percent_city', 'percent_senior', 'physicians',
       'hospital_beds', 'graduates', 'work_force', 'income', 'region',
       'crime_rate'],
      dtype='object')
"""
# 3 - Scatter Plot using `Matplotlib`

"""
- A scatter plot (aka scatter chart, scatter graph) uses dots to represent values for
    two different numeric variables. 
- The position of each dot on the horizontal and vertical axis indicates values for an
    individual data point. 
- Scatter plots are used to observe relationships between variables.

To create a scatter plot in `Matplotlib` we can use the `.scatter()` method:
"""

# 3-1 Create a scatter plot between crime rate and percent senior variables
plt.scatter(x.crime_rate, x.percent_senior) # Plotting the scatter plot
plt.title('Plotting the scatter plot between crime rate and percent senior variables') 
plt.show() # Showing the figure

"""
       Applications of Scatter Plot:

A scatter plot can also be useful for identifying other patterns in data. 
- We can divide data points into groups based on how closely sets of points cluster 
    together. 
- Scatter plots can also show if there are any unexpected gaps in the data and if there
    are any outlier points.(Look at the 2 points away from rest of the data in the scatter plot. Those are outliers.)

This can be useful if we want to segment the data into different parts, like categorising
    users into different groups.
    
"""

# 3-2 Adding titles and labels

plt.scatter(x.percent_senior, x.crime_rate)

plt.title('Plot of Crime Rate vs Percent Senior') # Adding a title to the plot
plt.xlabel("Percent Senior") # Adding the label for the horizontal axis
plt.ylabel("Crime Rate") # Adding the label for the vertical axis
plt.show()

# 4 - Line Chart using `Matplotlib`

"""
A line chart is used to represent data over a continuous time span. It is generally used
    to show trend of a measure (or a variable) over time. Data values are plotted as 
    points that are connected using line segments.

In Matplotlib we can create a line chart by calling the plot method.

plot() is a versatile command, and will take an arbitrary number of arguments.


     Applications of Line Chart:

Using a line chart one can see the pattern of any dependent variable over time like share
price, weather recordings (like temperature, precipitation or humidity), etc.

"""

plt.plot(x.work_force, x.income) # 2 arguments: X and Y points
plt.title('Plot a line chart')
plt.xlabel("Work Force") # Adding the label for the horizontal axis
plt.ylabel("Income")
plt.show()

"""
Because it is a line chart, `matplotlib` automatically draws a line to connect each
pair of consecutive points that represent Cartesian coordinates on the graph. We can
also make a graph with a single input argument
"""
plt.plot(x.work_force) # 1 argument
plt.title('Line chart workforce variable')
plt.show()

# 4-1  Changing the size of the plot

"""
The size of the figure that contains the graph can be varied with the `figsize` 
argument as follows:

```
plt.figure(figsize=(new_width_pixels, new_height_pixels))
"""

plt.figure(figsize=(12,5)) # 12x5 plot

plt.plot(x.work_force, x.income) 
plt.xlabel("Work Force") 
plt.ylabel("Income")
plt.show()

# 4-2  Formatting the style of your plot

# Specify the keyword args linestyle and/or marker in your call to plot.
# For example, using a dashed line and red circle markers:

plt.plot(x.work_force, x.income, linestyle='--', marker='o', color='r')
plt.xlabel("Work Force") 
plt.ylabel("Income")
plt.show()
