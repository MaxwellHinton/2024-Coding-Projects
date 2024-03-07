from bs4 import BeautifulSoup
import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once'
page = requests.get(url) # Returns <response [200]>

soup = BeautifulSoup(page.text, 'html.parser')

# Number i.e. 1-> 100 on every page
table = (soup.find('table', class_="tableList js-dataTooltip")).encode('utf-8')
table_rankings = soup.find_all('td', class_="number")

for rank in table_rankings:
    number = rank.text.strip()

# Book information includes the title, author, and rating. Maybe add the genre.
book_info_elements = soup.find_all('td', width='100%')
print("Book Titles: \n")

for book_element in book_info_elements:
    title_span = book_element.find('span', itemprop='name')
    author_span = book_element.find('a', class_='authorName').find('span', itemprop='name')
    rating_span = book_element.find('span', class_='minirating')

    if title_span and author_span and rating_span:
        title = title_span.text.strip()
        author = author_span.text.strip()
        rating = rating_span.text.strip()
        # print(title)
        # print(author)
        # print(rating)


