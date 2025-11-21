import requests
from bs4 import BeautifulSoup

url = "https://www.chittorgarh.com/report/ipo-in-india-list-main-board-sme/82/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

tables = soup.find_all("table")
print(f"Found {len(tables)} tables.")

for i, table in enumerate(tables):
    print(f"Table {i}:")
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    print(f"Headers: {headers}")
    rows = table.find_all("tr")
    if len(rows) > 1:
        first_row = [td.get_text(strip=True) for td in rows[1].find_all("td")]
        print(f"First row data: {first_row}")
    print("-" * 20)
