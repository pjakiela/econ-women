import requests
import pandas as pd
from bs4 import BeautifulSoup

import sys
sys.path.append(r"c:\users\jcpat\appdata\local\programs\python\python39\lib\site-packages")

import gender_guesser.detector as gender
import matplotlib.pyplot as plt
import plotly.express as px

from DynamicTest import *

b = DynamicTest()
b.printer()

d = gender.Detector()

web_page = requests.get('https://economics.brown.edu/people/faculty')
wellesley = requests.get('https://www.wellesley.edu/economics/faculty')

soup = BeautifulSoup(web_page.text, 'html.parser')
wellSoup = BeautifulSoup(wellesley.text, 'html.parser')

results = soup.find_all('h3', attrs = {'class':'people_item_name'})
wellRes = wellSoup.find_all('div', attrs = {'class' : 'field-content profile-name'})


df = pd.DataFrame()
wellDf = pd.DataFrame()

df['firstName'] = [result.find('a').text.replace('\n', '').split()[0] for result in results]
df['GenderHat'] = [d.get_gender(name) for name in df['firstName']]


wellDf['firstName'] = [result.find('h4').text.replace('\n', '').split()[0] for result in wellRes]
wellDf['GenderHat'] = [d.get_gender(name) for name in wellDf['firstName']]

totalProfsWellesley = len(wellDf)

wellesley_female = ((wellDf['GenderHat'] == 'male').sum() + (wellDf['GenderHat'] == 'mostly_male').sum()) / totalProfsWellesley
wellesley_male = ((wellDf['GenderHat'] == 'female').sum() + (wellDf['GenderHat'] == 'mostly_female').sum()) / totalProfsWellesley
wellesley_unknown = ((wellDf['GenderHat'] == 'unknown').sum() + (wellDf['GenderHat'] == 'andy').sum()) / totalProfsWellesley
wellesley = pd.DataFrame({'School Name' : ["Wellesley College"], 'Female' : [wellesley_female], 'Male' : [wellesley_male], 'Unknown' : [wellesley_unknown], 'lat' : [42.2936], 'lon' : [-71.3059]})

totalProfsBrown = len(df)

maleCount = ((df['GenderHat'] == 'male').sum() + (df['GenderHat'] == 'mostly_male').sum()) / totalProfsBrown
femaleCount = ((df['GenderHat'] == 'female').sum() + (df['GenderHat'] == 'mostly_female').sum()) / totalProfsBrown
unknownCount = ((df['GenderHat'] == 'unknown').sum() + (df['GenderHat'] == 'andy').sum()) / totalProfsBrown


# plotDf = pd.DataFrame({'Counts' : [femaleCount, unknownCount, maleCount]}, index = ["Female", "Unknown", "Male"])

mapDf = pd.DataFrame({'School Name' : ["Brown University"], 'Female' : [femaleCount], 'Male' : [maleCount], 'Unknown' : [unknownCount], 'lat' : [41.8268], 'lon' : [-71.4025]})
mapDf.append(wellesley)


fig = px.scatter_mapbox(mapDf, lat="lat", lon="lon", hover_name="School Name", hover_data=["Female", "Male", "Unknown"],
                        color_continuous_scale= "bluered", color = "Female", zoom=3, height=300)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_layout(
    height=800)
fig.show()



# plot = plotDf.plot.pie(y='Counts', figsize=(5, 5))

# plt.show()
