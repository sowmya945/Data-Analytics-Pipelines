import requests
import pandas as pd

# Dynamic API Data Extraction Pipeline
api_url = "https://coingecko.com"
response = requests.get(api_url)
df_crypto = pd.DataFrame(response.json())
df_dashboard = df_crypto[['name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']]

print("--- Automated Pipeline Executed Safely ---")
print(df_dashboard.head())
