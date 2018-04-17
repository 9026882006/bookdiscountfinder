from bs4 import BeautifulSoup as bs
import requests

BASE_URL = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=books'


def get_details_for_book(book_url,headers):
    try:
        page_data = requests.get(book_url,headers)
        print(page_data.status_code)
        page_html = page_data.text
        page_bs = bs(page_html, "lxml")
        containers = page_bs.find_all("div", {"class": "a-container"})
        print(len(containers))
        return containers
    except Exception as e:
        print(e)
