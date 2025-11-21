import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from data.fetch_ipo_data import get_upcoming_ipos

def test_fetch():
    print("Fetching IPO data...")
    data = get_upcoming_ipos()
    print(f"Fetched {len(data)} IPOs.")
    
    if data:
        print("First IPO sample:")
        print(data[0])
        
        # Basic validation
        required_keys = ['name', 'issue_price', 'open_date']
        first_item = data[0]
        if all(key in first_item for key in required_keys):
            print("SUCCESS: Data structure looks correct.")
        else:
            print("FAILURE: Missing keys in data.")
    else:
        print("WARNING: No data fetched. Check connection or selector logic.")

if __name__ == "__main__":
    test_fetch()
