from bs4 import BeautifulSoup

# Parse a local html file
with open("dummy.html", "r") as f:  # Asign the document in read mode to the variable f(f for file)
    doc = BeautifulSoup(f, "html.parser")

# Print the html file. Use prettify to have the cmd show indentation
print(doc.prettify())

# Using the doc.html_tag will return ONLY the first item which includes your selected tag.
tag = doc.title  # You can access specific html tags by using doc.html_tag
# Using ".string" allows you to access only the text inside the tag
print(tag.string)

tag.string = "hello"  # using the .string method you can modify the element

# You can also search for a tag using do.find("a")
finding = doc.find("p")  # Will return only the FIRST

# If you want to get all the elements that use the tag you are looking for use .find.all
finding_all = doc.find_all("h2")

# accessing nested tags(The basic way)
tags = doc.find_all("div")[0]  # find_all always returns a list(?)
nested_tags = tags.find_all("p")
print(nested_tags)
