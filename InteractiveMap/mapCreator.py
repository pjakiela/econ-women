import requests
import pandas as pd
from bs4 import BeautifulSoup

import sys
sys.path.append(r"c:\users\jcpat\appdata\local\programs\python\python39\lib\site-packages")

import gender_guesser.detector as gender
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from openpyxl import load_workbook

from HelperMethods import *

def buildRow(bookName, collegeName, lati, long):

    wb = load_workbook(bookName)

    ws = wb[collegeName]

    data = ws.values
    columns = next(data)[0:]

    df = pd.DataFrame(data, columns = columns)

    totalProfs = len(df)
    male = ((df['Gender'] == 'male').sum() + (df['Gender'] == 'mostly_male').sum()) / totalProfs
    female = ((df['Gender'] == 'female').sum() + (df['Gender'] == 'mostly_female').sum()) / totalProfs
    unknown = ((df['Gender'] == 'unknown').sum() + (df['Gender'] == 'andy').sum()) / totalProfs

    if female >= 0.25:
        category = 'Proportion Female > 0.25'
    elif female >= 0.175:
        category = '0.25 > Proportion Female > 0.175'
    elif female >= 0.125:
        category = '0.175 > Proportion Female > 0.125'
    else:
        category = 'Proportion Female < 0.125'


    return pd.DataFrame({'School Name' : [collegeName], 'Proportion Female' : [female], 'Male' : [male], 'Unknown' : [unknown], 'lat' : [lati], 'lon' : [long], 'Legend' : [category], 'Total Faculty' : [totalProfs]})


if __name__ == "__main__":

    file = 'EconomicsFaculty.xlsx'

    mapDf = pd.DataFrame()
    mapDf = mapDf.append(buildRow(file, "Princeton University", 40.3431, -74.6551))
    mapDf = mapDf.append(buildRow(file, "University of Michigan", 42.2780, -83.7382))
    mapDf = mapDf.append(buildRow(file, "Stanford University", 37.4275, -122.1697))
    mapDf = mapDf.append(buildRow(file, "Columbia University", 40.8075, -73.9626))
    mapDf = mapDf.append(buildRow(file, "Williams College", 42.7129, -73.2031))
    mapDf = mapDf.append(buildRow(file, "Boston University", 42.3505, -71.1054))
    mapDf = mapDf.append(buildRow(file, "Dartmouth College", 43.7044, -72.2887))
    mapDf = mapDf.append(buildRow(file, "University of Pennsylvania", 39.9522, -75.1932))
    mapDf = mapDf.append(buildRow(file, "Northwestern University", 42.0565, -87.6753))
    mapDf = mapDf.append(buildRow(file, "UCLA", 34.0689, -118.4452))
    mapDf = mapDf.append(buildRow(file, "University of Wisconsin-Madison", 43.0766, -89.4125))
    mapDf = mapDf.append(buildRow(file, "Michigan State University", 42.7018, -84.4822))
    mapDf = mapDf.append(buildRow(file, "Duke University", 36.0014, -78.9382))
    mapDf = mapDf.append(buildRow(file, "University of Chicago", 41.7886, -87.5987))
    mapDf = mapDf.append(buildRow(file, "UC Berkeley", 37.8719, -122.2585))
    mapDf = mapDf.append(buildRow(file, "New York University", 40.7295, -73.9965))
    mapDf = mapDf.append(buildRow(file, "Boston College", 42.3355, -71.1685))
    mapDf = mapDf.append(buildRow(file, "Cornell University", 42.4534, -76.4735))
    mapDf = mapDf.append(buildRow(file, "Brown University", 41.8268, -71.4025))
    mapDf = mapDf.append(buildRow(file, "Yale University", 41.3163, -72.9223))
    mapDf = mapDf.append(buildRow(file, "USC", 34.0224, -118.2851))
    mapDf = mapDf.append(buildRow(file, "UC Davis", 38.5382, -121.7617))
    mapDf = mapDf.append(buildRow(file, "UC San Diego", 32.8801, -117.2340))
    mapDf = mapDf.append(buildRow(file, "Harvard University", 42.3770, -71.1167))
    mapDf = mapDf.append(buildRow(file, "MIT", 42.3601, -71.0942))
    mapDf = mapDf.append(buildRow(file, "Johns Hopkins University", 39.3299, -76.6205))
    mapDf = mapDf.append(buildRow(file, "University of Virginia", 38.0336, -78.5080))
    mapDf = mapDf.append(buildRow(file, "Ohio State University", 40.0067, -83.0305))
    mapDf = mapDf.append(buildRow(file, "Notre Dame", 41.7056, -86.2353))

    fig = px.scatter_mapbox(mapDf, lat="lat", lon="lon", hover_name="School Name", hover_data={ "Total Faculty" : True, "Proportion Female" : True, "lat" : False, "Legend" : False, "lon" : False},
                            color_discrete_sequence = ["#ff0303", "#ff037d", "#7d03ff", "#0307ff"],
                            category_orders = {'Legend' : ['Proportion Female > 0.25', '0.25 > Proportion Female > 0.175', '0.175 > Proportion Female > 0.125', 'Proportion Female < 0.125']},
                            color = "Legend", zoom = 3, height = 800)

    fig.update_layout(mapbox_style="carto-darkmatter")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(
        margin={"t":100},
        title = "Female Representation in Major Economics Departments")
    fig.update_traces(marker = dict(size = 8))

    fig.write_html("InteractiveMap_Professors.html")
