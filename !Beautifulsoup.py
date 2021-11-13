# Beautifulsoup
from bs4 import BeautifulSoup

with open("files/1.html", encoding="utf8") as file:
    src = file.read()

# print(src)

soup = BeautifulSoup(src, 'lxml')
title = soup.title
print(title.text)
# print(title.string)

# .find() find_all()
# page_h1 = soup.findAll("meta")
# for entry in page_h1:
#    print(entry)

# news = soup.find_all("li", class_ = "even")
# for entry in news:
#     print(entry.text.strip())

# news = soup.find_all("div", {"itemList", "itemListSecondary","catItemTitle", "catItemIntroText" })
news = soup.find_all("div", class_="catItemIntroText")
for entry in news:
    print(entry.text.strip())
