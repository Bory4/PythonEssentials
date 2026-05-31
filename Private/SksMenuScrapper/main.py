#!/bin/python

import requests
from bs4 import BeautifulSoup

url = "https://sks.pwr.edu.pl/menu/"
soup = BeautifulSoup(requests.get(url).text, "html.parser")
categories = soup.find_all("div", {"class": "category"})

for category in categories:
    print(f"Category: {category.find('h2').contents[0]}\n")
    for position in category.find_all("li"):
        content = position.contents
        print(f"\t* {" ".join(str(content[0]).strip().split(' ')[:-1])}; Serving: {str(content[0]).strip().split(' ')[-1]}; Price:{content[1].text} pln")
    print()