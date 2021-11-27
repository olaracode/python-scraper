from bs4 import BeautifulSoup
import requests

# Finding elements inside the html "tree"

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody  # .tbody returns the table body
trs = tbody.contents  # with this you can see all the tags that are in the table

# print(list(trs[0].next_siblings))

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    processed_name = name.p.string
    processed_price = price.span.string

    prices[processed_name] = processed_price

print(prices)
