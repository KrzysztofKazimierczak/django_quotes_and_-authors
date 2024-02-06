import requests
from bs4 import BeautifulSoup
import json


def find_data(url, data_to_scrap):
    data_list = []
    data_to_scrap = data_to_scrap.lower()
   
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    
        for div_to_scrap in soup.find_all('div', class_='record'):
            scrapped_data = div_to_scrap.find_all('span', class_=data_to_scrap)
            if scrapped_data:
                scrapped_data_text = ','.join(tag.get_text(strip=True) for tag in scrapped_data)
                data_list.append({data_to_scrap: scrapped_data_text})
        break
                           
    return data_list



if __name__ == "__main__":
    url="http://localhost:8000/"
    print(find_data(url,"author"))
    