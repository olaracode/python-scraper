from os import write
from bs4 import BeautifulSoup
import requests
import re
import csv

search_term = input("What product do you want to search for? ")
filename = input("How do you wish to save this search? ")
url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

pagination_text = doc.find(class_="list-tool-pagination-text").strong
pagination = int(str(pagination_text).split("/")[-2].split(">")[-1][:-1])

items_found = []

for page in range(1, pagination + 1):
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page?{page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(
        class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search_term))

    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue

        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        price = next_parent.find(class_="price-current").strong.string
        items_found.append({"Name": item, "Price": int(
            price.replace(",", "")), "Link": link})

for item in items_found:
    print(item)
with open(f"./{filename}.csv", 'w', encoding="UTF8") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Price", "Link"])
    writer.writerows(items_found)
# for item in items_found:
#    writer.writerows(item)
#    print(item)
