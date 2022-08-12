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

class OSUGen:

    def buildSheet(self):

        df = buildStaticDF('https://economics.osu.edu/people', 'a',
                            'class', 'views-field-field-first-name', 'div', 'class',
                            'views-field views-field-field-your-title')

        df = tenureFilter(df)


        addToWb("Ohio State University", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)

if __name__ == "__main__":

    OSU = OSUGen()
    OSU.buildSheet()
