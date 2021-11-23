from bs4 import BeautifulSoup
import requests

# Web scraping


url = "https://www.newegg.com/msi-geforce-gtx-1050-ti-gtx-1050-ti-gaming-x-4g/p/N82E16814137054?Item=N82E16814137054"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# Instead of searching for a specific tag we search for a specific text
prices = doc.find_all(text="$")
# Then we get the parent of the first $ sign that appears(index: 0)
parent = prices[0].parent

# After checking the parent information we know that the information that we want is inside the strong tag
strong = parent.find("strong")  # So we store that inside a variable

# Finally we display the price using .string
print(strong.string)
