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

class UCLAGen:

    def buildSheet(self):

        web_page = requests.get('https://economics.ucla.edu/faculty/ladder')

        soup = BeautifulSoup(web_page.text, 'html.parser')

        names = soup.find_all('h3')[:-3]
        titles = soup.find_all('h4')

        df = pd.DataFrame()

        df['Name'] = [name.text.strip() for name in names]
        df['firstName'] = [name.split()[0] for name in df['Name']]
        df['Title'] = [title.text for title in titles]

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        addToWb("UCLA", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)

if __name__ == "__main__":

    UCLA = UCLAGen()
    UCLA.buildSheet()
