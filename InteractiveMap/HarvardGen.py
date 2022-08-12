import requests
import pandas as pd
from bs4 import BeautifulSoup

import sys
sys.path.append(r"c:\users\jcpat\appdata\local\programs\python\python39\lib\site-packages")

import gender_guesser.detector as gender

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from HelperMethods import *

# Note that this one might take a while -- I had to implement a pause so that the
# driver would wait to pull data until the entire page loaded
class HarvardGen:

    def buildSheet(self):

        chromeOptions = Options()

        chromeOptions.add_argument("--headless")

        driver = Chrome(executable_path = r"C:\Users\jcpat\Downloads\chromedriver_win32\chromedriver", options = chromeOptions)

        driver.get("https://economics.harvard.edu/faculty")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
        'node-title')))

        namesFirstPage = driver.find_elements(By.CLASS_NAME, "node-title")

        firstList = [name.text.replace('\n', '') for name in namesFirstPage if name.text != '']

        driver.get("https://economics.harvard.edu/faculty?sv_list_box_delta=1592918309&pager_id=0&destination=node/1314266&page=1")

        WebDriverWait(driver, 20)

        namesSecondPage = driver.find_elements(By.CLASS_NAME, 'node-title')

        secondList = [name.text.replace('\n', '') for name in namesSecondPage if name.text != '']

        df = pd.DataFrame()

        df['Name'] = firstList + secondList
        df['firstName'] = [name.split()[0] for name in df['Name']]

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        # Don't need to get granular here, they separate tenure track faculty on
        # the website
        df['Title'] = 'Faculty'


        addToWb("Harvard University", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)



if __name__ == "__main__":

    harvard = HarvardGen()
    harvard.buildSheet()
