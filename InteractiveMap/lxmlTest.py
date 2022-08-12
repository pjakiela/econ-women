import requests
from lxml import html

url = "https://lsa.umich.edu/econ/people/faculty.html"

path = '/html/body/div[6]/div[1]/div[3]/div[3]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div/h3/a[2]'

response = requests.get(url)

byte_string = response.content

source_code = html.fromstring(byte_string)

tree = source_code.xpath(path)

print(tree)
