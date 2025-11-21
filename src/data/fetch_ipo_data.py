import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def get_upcoming_ipos(url="https://www.chittorgarh.com/report/ipo-in-india-list-main-board-sme/82/"):
    """
    Fetches upcoming IPO data from Chittorgarh.com.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table - usually the first table or one with specific class
        # Based on inspection, we'll look for the table with IPO data
        tables = soup.find_all("table")
        
        if not tables:
            raise Exception("No tables found on the page")
            
        # Assuming the first table is the main IPO list
        table = tables[0]
        
        ipo_list = []
        
        # Skip header row
        rows = table.find_all("tr")[1:]
        
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 6:
                # Extract data based on typical column structure
                # Note: This is brittle and depends on the exact column order
                # Issuer Company, Open, Close, Lot Size, Issue Price, Issue Size
                
                try:
                    name = cols[0].get_text(strip=True)
                    open_date = cols[1].get_text(strip=True)
                    close_date = cols[2].get_text(strip=True)
                    lot_size = cols[3].get_text(strip=True)
                    issue_price = cols[4].get_text(strip=True)
                    issue_size = cols[5].get_text(strip=True)
                    
                    ipo_data = {
                        "name": name,
                        "open_date": open_date,
                        "close_date": close_date,
                        "lot_size": lot_size,
                        "issue_price": issue_price,
                        "issue_size": issue_size
                    }
                    ipo_list.append(ipo_data)
                except IndexError:
                    continue
                    
        return ipo_list

    except Exception as e:
        print(f"Error fetching IPO data: {e}")
        return []