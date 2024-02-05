import requests
from bs4 import BeautifulSoup
import json


def find_data(url, data_to_scrap):
    data_list = []
    data_to_scrap = data_to_scrap.lower()
   
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    
        for span_to_scrap in soup.find_all('div', class_='record'):
            scrapped_data = span_to_scrap.find('span', class_=data_to_scrap).get_text(strip=True)
            print(scrapped_data)

            if not any(item[data_to_scrap] == scrapped_data for item in data_list):
                data_list.append(
                    {
                        data_to_scrap: scrapped_data
                    })
                           
        break
    return data_list



if __name__ == "__main__":
    url="http://localhost:8000/"
    print(find_data(url,"author"))
    