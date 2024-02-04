import requests
from bs4 import BeautifulSoup
import json


def find_data(url, span_to_srap):
    data_list = []
    start_url = url
    
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
    
        for span_to_srap in soup.find_all('div', class_='quote'):
            scrapped_data = span_to_srap.find('span', class_=span_to_srap).text

            if not any(item["quote"] == scrapped_data for item in data_list):
                data_list.append(
                    {
                        span_to_srap: scrapped_data
                    })
                           

    return data_list
"""
    with open('quotes.json', 'w', encoding='utf-8') as quotes_file:
        json.dump(quotes_list, quotes_file, indent=2, ensure_ascii=False)

    with open('authors.json', 'w', encoding='utf-8') as authors_file:
        json.dump(authors_list, authors_file, indent=2, ensure_ascii=False)"""

if __name__ == "__main__":
    pass
