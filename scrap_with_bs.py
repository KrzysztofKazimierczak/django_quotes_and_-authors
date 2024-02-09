import requests
from bs4 import BeautifulSoup


def find_data(url, data_to_scrap):
    data_list = []
    data_to_scrap = data_to_scrap.lower()
    start_url = url

   
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(url)
    
        for div_to_scrap in soup.find_all('div', class_='record'):
            scrapped_data = div_to_scrap.find_all('span', class_=data_to_scrap)
            if scrapped_data:
                for data in scrapped_data:
                    scrapped_data_text = data.get_text(strip=True)
                    record = {data_to_scrap: scrapped_data_text}
                    if record not in data_list:
                        data_list.append(record)

        next_page = soup.find('a', class_='next')

        if next_page:
            url = start_url + next_page['href']
            print(url)
        else:
            url = None        

    return data_list



if __name__ == "__main__":
    url="http://localhost:8000/"
    print(find_data(url,"author"))
    