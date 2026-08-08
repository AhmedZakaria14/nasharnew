import os
from bs4 import BeautifulSoup

html_path = "/home/ubuntu/nasharnew/index.html"
if not os.path.exists(html_path):
    print("index.html not found!")
    exit(1)

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# Ensure all stylesheet and font links point correctly to relative local paths
for link in soup.find_all("link", rel="stylesheet"):
    href = link.get("href", "")
    if "https://adselams.com/" in href:
        link["href"] = href.replace("https://adselams.com/", "./")
    elif "http://adselams.com/" in href:
        link["href"] = href.replace("http://adselams.com/", "./")

for script in soup.find_all("script"):
    src = script.get("src", "")
    if "https://adselams.com/" in src:
        script["src"] = src.replace("https://adselams.com/", "./")
    elif "http://adselams.com/" in src:
        script["src"] = src.replace("http://adselams.com/", "./")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Fonts and layout paths successfully fixed.")
