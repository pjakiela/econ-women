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

class USCGen:

    def buildSheet(self):

        web_page = requests.get('https://dornsife.usc.edu/cf/econ/econ_core_faculty_roster.cfm')

        soup = BeautifulSoup(web_page.text, 'html.parser')

        names = soup.find_all('font', attrs = {'color' : '#000000'})

        df = pd.DataFrame()


        df['Name'] = [name.text.strip() for name in names]

        # should be the name of the last non-emeritus professor
        lastIndex = df[df['Name'] == 'David Zeke'].index[0] + 1
        df = df[ : lastIndex]

        df['firstName'] = [name.split()[0] for name in df['Name']]
        df['Title'] = 'Faculty'

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        addToWb("USC", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)

if __name__ == "__main__":

    USC = USCGen()
    USC.buildSheet()
