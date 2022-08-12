import sys
sys.path.append(r"c:\users\jcpat\appdata\local\programs\python\python39\lib\site-packages")

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pandas as pd

import gender_guesser.detector as gender

from HelperMethods import *

class BostonCollegeGen:

    def buildSheet(self):

        chromeOptions = Options()

        chromeOptions.add_argument("--headless")

        driver = Chrome(executable_path = r"C:\Users\jcpat\Downloads\chromedriver_win32\chromedriver", options = chromeOptions)

        driver.get("https://www.bc.edu/bc-web/schools/mcas/departments/economics/people.html")

        elements = driver.find_elements(By.TAG_NAME, "h3")
        fieldNames = driver.find_elements(By.CLASS_NAME, "position")

        df = pd.DataFrame()

        df['Name'] = [element.text for element in elements if element.text != '']
        df['firstName'] = [name.split()[0] for name in df['Name']]
        df['Title'] = [title.text for title in fieldNames if title.text != '']

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        addToWb("Boston College", r"C:\Users\jcpat\SummerResearch2022\InteractiveMap\EconomicsFaculty.xlsx", df)


if __name__ == "__main__":

    BC = BostonCollegeGen()
    BC.buildSheet()
