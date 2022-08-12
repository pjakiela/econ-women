import sys
sys.path.append(r"c:\users\jcpat\appdata\local\programs\python\python39\lib\site-packages")

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

if __name__ == "__main__":

    driver = Chrome(executable_path = r"C:\Users\jcpat\Downloads\chromedriver_win32\chromedriver")

    driver.get("https://economics.brown.edu/people/faculty")

    elements = driver.find_elements(By.CLASS_NAME, "people_item_name")
    fieldNames = driver.find_elements(By.CLASS_NAME, "people_item_title")

    for element in elements:
        print(element.text)

    for name in fieldNames:
        print(name.text)
