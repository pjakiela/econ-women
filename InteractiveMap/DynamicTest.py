import sys
sys.path.append(r"c:\users\jcpat\appdata\local\programs\python\python39\lib\site-packages")

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

class DynamicTest:
    def printer(self):
        print("please")

if __name__ == "__main__":

    chromeOptions = Options()

    chromeOptions.add_argument("--headless")

    driver = Chrome(executable_path = r"C:\Users\jcpat\Downloads\chromedriver_win32\chromedriver", options = chromeOptions)

    driver.get("https://lsa.umich.edu/econ/people/faculty.html")

    elements = driver.find_elements(By.CLASS_NAME, "name")
    fieldNames = driver.find_elements(By.CLASS_NAME, "fields")

    for element in elements:
        print(element.text)

    for name in fieldNames:
        print(name.text)

#myOptions = webdriver.ChromeOptions()
#myOptions.add_argument('--ignore-certificate-errors')
#myOptions.add_argument('--incognito')
#myOptions.add_argument('--headless')
#driver = webdriver.Chrome(r"C:\Users\jcpat\Documents\chromedriver_win32\chromedriver", options=myOptions)

#print("test")

#import time
