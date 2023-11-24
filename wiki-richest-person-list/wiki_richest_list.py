import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'
page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find_all("table",{"class":"wikitable"})
    
    table = tables[1]

    rich_list = []
    rows = table.find_all("tr")
    for row in rows[1:]:
        values = row.find_all("td")

        row_value = []
        for value in values:
            row_value.append(value.text.strip())       

        
        rich_list.append(row_value)    

    header = table.find_all("th")
    
    titles = []
    for column_title in header:
        titles.append(column_title.text.strip())

    df = pd.DataFrame(rich_list, columns=titles, index=None)
    print(df)

    df.to_csv("richest.csv", index=False)