import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Target live tabular data page
url = "https://scrapethissite.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 2. Isolate tabular row blocks
table_rows = soup.find_all("tr", class_="team")

team_names = []
years = []
wins = []

# 3. Harvest structured data fields
for row in table_rows:
    team_names.append(row.find("td", class_="name").get_text(strip=True))
    years.append(row.find("td", class_="year").get_text(strip=True))
    wins.append(row.find("td", class_="wins").get_text(strip=True))

# 4. Consolidate and type cast clean variables
df_scraped_table = pd.DataFrame({"Team_Name": team_names, "Season_Year": years, "Total_Wins": wins})
df_scraped_table["Total_Wins"] = df_scraped_table["Total_Wins"].astype(int)

print("--- Production Tabular Scraper Executed Successfully ---")
print(df_scraped_table.head())
