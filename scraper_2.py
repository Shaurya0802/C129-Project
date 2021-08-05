from bs4 import BeautifulSoup
import pandas as pd
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars#verify=False"

page = requests.get(start_url)

soup = BeautifulSoup(page.text, "html.parser")
table = soup.find("table")

temp_list = []

tr_tags = table.find_all("tr")

for tr_tag in tr_tags:
    td_tags = tr_tag.find_all("td")
    row = [i.text.rstrip() for i in td_tags]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns=["name", "distance", "mass", "radius"])
df.to_csv("bright_stars.csv")