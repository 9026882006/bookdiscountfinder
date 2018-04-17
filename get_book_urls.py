from bs4 import BeautifulSoup as bs
import requests


def fetch(base_url,headers):
    webPage = requests.get(base_url,headers)
    if webPage.status_code == 200:
        webPageText = webPage.text
        soup = bs(webPageText, 'lxml')
        results = soup.find('ul', {'class': 's-result-list'})
        next = soup.find('a', {'id': 'pagnNextLink'})['href']
        books = results.find_all('div', {'class': 's-item-container'})
        all_book_links = set()
        for book in books:
            book_link = book.find('a', {'class': 's-access-detail-page'})['href']
            all_book_links.add(book_link)
            # print(book_link)
        return (all_book_links)
    else:
        return 'error {}'.format(webPage.status_code)


if __name__ == '__main__':
    data = fetch("https://www.amazon.com/b/ref=gbpp_itr_m-3_0168_Arts&Pho?node=1&ie=UTF8")
    print(data)