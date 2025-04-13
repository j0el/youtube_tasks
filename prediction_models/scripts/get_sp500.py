import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_sp500_data():
    """
    Scrapes S&P 500 company data from Wikipedia and returns a list of dictionaries.
    Each dictionary represents a company with the specified columns.
    """
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the main table containing S&P 500 data
    table = soup.find('table', {'id': 'constituents'})
    rows = table.find_all('tr')[1:]  # Skip header row
    
    companies = []
    for row in rows:
        cols = row.find_all('td')
        
        # Extract data from each column
        symbol = cols[0].text.strip()
        security = cols[1].text.strip()
        sector = cols[3].text.strip()
        sub_industry = cols[4].text.strip()
        hq_location = cols[5].text.strip()
        date_added = cols[6].text.strip()
        cik = cols[7].text.strip()
        founded = cols[8].text.strip() if len(cols) > 8 else 'N/A'
        
        # Clean up date format if available
        try:
            date_obj = datetime.strptime(date_added, '%Y-%m-%d')
            date_added = date_obj.strftime('%Y-%m-%d')
        except ValueError:
            pass
        
        company_data = {
            'Symbol': symbol,
            'Security': security,
            'GICS Sector': sector,
            'GICS Sub-Industry': sub_industry,
            'Headquarters Location': hq_location,
            'Date added': date_added,
            'CIK': cik,
            'Founded': founded
        }
        companies.append(company_data)
    
    return companies

def save_to_csv(data, filename='sp500_companies.csv'):
    """
    Saves the S&P 500 data to a CSV file with the specified columns.
    """
    fieldnames = ['Symbol', 'Security', 'GICS Sector', 'GICS Sub-Industry', 
                  'Headquarters Location', 'Date added', 'CIK', 'Founded']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Successfully saved S&P 500 data to {filename}")

if __name__ == "__main__":
    # Scrape the data
    sp500_data = scrape_sp500_data()
    
    # Save to CSV
    save_to_csv(sp500_data)