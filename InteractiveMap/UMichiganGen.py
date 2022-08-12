import sys
sys.path.append(r"c:\users\jcpat\appdata\local\programs\python\python39\lib\site-packages")

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

import gender_guesser.detector as gender

from HelperMethods import *

class UMichiganGen:

    def buildSheet(self):

        chromeOptions = Options()

        chromeOptions.add_argument("--headless")

        driver = Chrome(executable_path = r"C:\Users\jcpat\Downloads\chromedriver_win32\chromedriver", options = chromeOptions)

        driver.get("https://lsa.umich.edu/econ/people/faculty.html")

        WebDriverWait(driver, 20)

        elements = driver.find_elements(By.CLASS_NAME, "name")
        fieldNames = driver.find_elements(By.CLASS_NAME, "fields")

        df = pd.DataFrame()

        df['Name'] = [element.text for element in elements]
        df['firstName'] = [name.split()[0] for name in df['Name']]
        df['Title'] = [title.text for title in fieldNames]

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        df = tenureFilter(df)

        addToWb("University of Michigan", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)


if __name__ == "__main__":

    Michigan = UMichiganGen()
    Michigan.buildSheet()
