import time
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver


def get_details_from_amazon(book_url, headers, booklist):
    driver = webdriver.Chrome()
    try:
        current_price = 0.0
        old_price = 0.0
        discount = 0.0
        author = 'n/a'
        rating = 0.0
        title = 'not found'
        formats = []
        driver.get(book_url)
        try:
            titleItem = driver.find_element_by_id('ebooksProductTitle').text
        except:
            titleItem = driver.find_element_by_id('productTitle').text

        try:
            author = driver.find_element_by_class_name('contributorNameID').text
        except:
            author = 'n/a'

        try:
            rating_item = driver.find_element_by_id('acrPopover')
            rated = rating_item.get_attribute('title')
            rating = rated.split()
            rating = float(rating[0])
        except:
            rating = 0.0

        try:
            review_item = driver.find_element_by_id('acrCustomerReviewText')
            reviews = review_item.text
            review_count = int(reviews.split()[0])
        except:
            review_count = 0

        try:
            selling_item = driver.find_element_by_css_selector(
                '#unqualifiedBuyBox > div > div.a-text-center.a-spacing-mini > span')
            # todo
        except:
            try:
                selling_item = driver.find_element_by_css_selector(
                    '#buybox > div > table > tbody > tr.kindle-price > td.a-color-price')
                selling_text = selling_item.text
                sale = selling_text.split()
                try:
                    current_price = float(sale[0])
                    old_price = float(sale[2])
                    discount = sale[3]
                    discount = float(discount[1:-2])
                except:
                    current_price = float(sale[0])
            except:
                pass

        try:
            sliderLink = driver.find_element_by_id('showMoreFormatsPrompt')
            sliderLink.click()
            time.sleep(1)
            title_row_item = driver.find_elements_by_class_name('dp-title-col')
            price_row_item = driver.find_elements_by_class_name('dp-price-col')
            newprice_row_item = driver.find_elements_by_class_name('dp-new-col')
            count = 0
            formats = []
            for title_item, price_item, newprice_item in zip(title_row_item, price_row_item, newprice_row_item):
                if count == 0:
                    count += 1
                    continue
                formats.append(dict(format=title_item.text,
                                    baseprice=price_item.text,
                                    newprice=newprice_item.text))

        except:
            formats = 'n/a'

        booklist.append(dict(
            title=title,
            author=author,
            review_count=review_count,
            rating=rating,
            current_price=current_price,
            old_price=old_price,
            discount=discount,
            formats=formats
        ))
    except Exception as e:
        print(e)
    finally:
        driver.close()

    return booklist


def get_details_from_snapdeal(book_url, headers, booklist):
    try:
        pass
    except Exception as e:
        print(e)
