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

class MichiganStGen:

    def buildSheet(self):

        web_page = requests.get('http://econ.msu.edu/people/faculty.php')

        soup = BeautifulSoup(web_page.text, 'html.parser')

        names = soup.find_all('td')

        df = pd.DataFrame()

        df['Name'] = [name.text.strip() for name in names]
        df = df[df.index % 5 == 0]
        df['firstName'] = [name.partition(',')[2].strip().split()[0] for name in df['Name']]

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        df['Title'] = 'Faculty'

        addToWb("Michigan State University", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)

if __name__ == "__main__":

    MichiganSt = MichiganStGen()
    MichiganSt.buildSheet()
