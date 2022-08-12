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

# Standard function for adding a DataFrame to our Excel sheet. This should work
# in all or nearly all cases.
def addToWb(sheetName, filePath, dataFrame):

        workbook = load_workbook(filePath)
        writer = pd.ExcelWriter(filePath, engine = 'openpyxl')
        writer.book = workbook

        dataFrame.to_excel(writer, sheet_name = sheetName)
        writer.save()
        writer.close()

# Function that makes it super straightforward to build the DataFrame we're looking
# for if a website is formatted in a standard way. Works occcasionally.
def buildStaticDF(url, nameTag, nameAt1, nameAt2, titleTag, titleAt1, titleAt2):

        web_page = requests.get(url)

        soup = BeautifulSoup(web_page.text, 'html.parser')

        names = soup.find_all(nameTag, attrs = {nameAt1 : nameAt2})
        titles = soup.find_all(titleTag, attrs = {titleAt1 : titleAt2})

        df = pd.DataFrame()

        df['Name'] = [name.text.strip() for name in names]
        df['firstName'] = [name.split()[0] for name in df['Name']]
        df['Title'] = [title.text.strip() for title in titles]

        d = gender.Detector()
        df['Gender'] = [d.get_gender(name) for name in df['firstName']]

        return df

def tenureFilter(df):

    df['isProfessor'] = [(title.lower().__contains__('professor')
                        and not title.lower().__contains__('emeritus')) for title in df['Title']]

    df.drop(df.index[df['isProfessor'] == False], inplace = True)
    df.drop('isProfessor', inplace = True, axis = 1)

    df['isTenured'] = [not((title.lower().__contains__('assistant')
                       or title.lower().__contains__('associate')
                       or title.lower().__contains__('teaching')
                       or title.lower().__contains__('visiting'))
                       and not title.lower().__contains__('chair')
                       and not title.lower().__contains__('dean'))
                       for title in df['Title']]

    return df
