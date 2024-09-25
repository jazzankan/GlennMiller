from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.glennmillercafe.se/konserter")
glenn_page = response.text
months = ['januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti', 'september', 'oktober', 'november', 'december']
found_months = []
month_index = []
for m in months:
    try:
        month_index.append(glenn_page.index(m))
        found_months.append(m)
    except(ValueError):
        pass

print(f"Senaste månaden är { found_months[-1] }:")
glenn_page = glenn_page[month_index[-1]:]
soup = BeautifulSoup(glenn_page, "html.parser")
#soup = soup.find_all("div", class_="konsert-container")
artist_clean = []
date_clean = []
artists = soup.find_all("p", class_="artist")
for a in artists:
    artist_text = a.get_text()
    artist_clean.append(artist_text)
    print(artist_text)

dates = soup.find_all("p", class_="date")
for d in dates:
    date_text = d.get_text()
    date_clean.append(date_text)

if len(artist_clean) != len(date_clean):
    print("\nDiskrepans mellan artister och datum!")
else:
    user_input = input("Vill du mata in posterna? j/n:\n")
    if user_input == "j":
        print("Jasså du")





