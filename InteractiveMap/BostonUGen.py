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

class BostonUGen:

    def buildSheet(self):

        df = buildStaticDF('https://www.bu.edu/econ/people/faculty/', 'h6',
                            'class', 'profile-name profile-name-basic', 'p', 'class',
                            'profile-title profile-title-basic')

        addToWb("Boston University", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)

if __name__ == "__main__":

    BostonU = BostonUGen()
    BostonU.buildSheet()
