import requests
import pandas as pd
from bs4 import BeautifulSoup

import sys
sys.path.append(r"c:\users\jcpat\appdata\local\programs\python\python39\lib\site-packages")

import gender_guesser.detector as gender

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from openpyxl import load_workbook

from HelperMethods import *

class UChicagoGen:

    def buildSheet(self):

        web_page = requests.get('https://economics.uchicago.edu/directories/full/faculty')

        soup = BeautifulSoup(web_page.text, 'html.parser')

        names = soup.find_all('h2')
        titles = soup.find_all('p', attrs = {'class' : 'title'})

        df = pd.DataFrame()

        df['Name'] = [name.text.strip() for name in names]

        lastIndex = df[df['Name'] == 'Instructional Professors'].index[0]
        df = df[ : lastIndex]

        df['firstName'] = [name.split()[0] for name in df['Name']]

        df['Title'] = [title.text.strip() for title in titles[ : lastIndex]]

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        addToWb("University of Chicago", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)

if __name__ == "__main__":

    UChicago = UChicagoGen()
    UChicago.buildSheet()