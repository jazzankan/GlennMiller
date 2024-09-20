from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.glennmillercafe.se/konserter")
glenn_page = response.text
soup = BeautifulSoup(glenn_page, "html.parser")

#comment


