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



class UCSDGen:

    def buildSheet(self):

        web_page = requests.get('https://economics.ucsd.edu/faculty-and-research/faculty-profiles/index.html')

        soup = BeautifulSoup(web_page.text, 'html.parser')

        names = soup.find_all('h3')


    #    print(elements[27].text.split('\n')) # 2 is the index

        #for element in elements:
        #    print(element.text)

#        tempdf = pd.DataFrame()
#        tempdf['contents'] = [element.text for element in elements]
#
        # should be the name of the last non-emeritus professor
#        firstIndex = tempdf[tempdf['contents'] == 'Titan Alon'].index[0]
#        tempdf = tempdf[firstIndex : ]

#        print(tempdf)

        df = pd.DataFrame()


        df['Name'] = [name.text.strip() for name in names]
        df['firstName'] = [name.split()[0] for name in df['Name']]
        df['Title'] = 'Faculty'

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        addToWb("UC San Diego", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)

if __name__ == "__main__":

    UCSD = UCSDGen()
    UCSD.buildSheet()
