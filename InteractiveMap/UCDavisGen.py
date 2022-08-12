import sys
sys.path.append(r"c:\users\jcpat\appdata\local\programs\python\python39\lib\site-packages")

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pandas as pd

import gender_guesser.detector as gender

from HelperMethods import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class UCDavisGen:

    def buildSheet(self):

        chromeOptions = Options()

        chromeOptions.add_argument("--headless")

        driver = Chrome(executable_path = r"C:\Users\jcpat\Downloads\chromedriver_win32\chromedriver", options = chromeOptions)

        driver.get("https://economics.ucdavis.edu/directory-of-people/econ-faculty#c4=all&b_start=0")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
        'personName')))

        elements = driver.find_elements(By.CLASS_NAME, "personName")
        fieldNames = driver.find_elements(By.CLASS_NAME, "job")

        df = pd.DataFrame()

        df['Name'] = [element.text for element in elements if element.text != '']
        df['firstName'] = [name.split()[0] for name in df['Name']]
        df['Title'] = [title.text for title in fieldNames if title.text != '']

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        addToWb("UC Davis", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)


if __name__ == "__main__":

    UCDavis = UCDavisGen()
    UCDavis.buildSheet()
