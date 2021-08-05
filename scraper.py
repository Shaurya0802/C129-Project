from bs4 import BeautifulSoup
import requests
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(start_url)

soup = BeautifulSoup(page.text, "html.parser")
tables = soup.find_all("table")

temp_list = []

tr_tags = tables[3].find_all("tr")

for tr_tag in tr_tags:
    td_tags = tr_tag.find_all("td")
    row = [i.text.rstrip() for i in td_tags]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(name, distance, mass, radius)), columns=['name','distance','mass','radius'])
print(df2)

df2.to_csv('dwarf_stars.csv')