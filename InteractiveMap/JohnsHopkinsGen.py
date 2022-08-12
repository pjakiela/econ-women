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

class JohnsHopkinsGen:

    def buildSheet(self):

        web_page = requests.get('https://econ.jhu.edu/people/faculty/')

        soup = BeautifulSoup(web_page.text, 'html.parser')

        names = soup.find_all('h3')

        titles = soup.find_all('h4')

        df = pd.DataFrame()

#        for name in names:
#            print(name.text)
#
#        for title in titles:
#            print(title.text)

        df['Name'] = [name.text.strip() for name in names]

        # For some reason, this guy doesn't have a title
        df = df[df['Name'].str.contains('Barclay Knapp') == False]
        df['firstName'] = [name.split()[0] for name in df['Name']]
        df['Title'] = [title.text.strip() for title in titles]


        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]


        addToWb("Johns Hopkins University", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)

if __name__ == "__main__":

    JHU = JohnsHopkinsGen()
    JHU.buildSheet()
