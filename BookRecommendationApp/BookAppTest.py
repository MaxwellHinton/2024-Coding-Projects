from bs4 import BeautifulSoup
import requests
import sys
import pandas as pd

# Added this line to help when coming across non-ASCII characters, E.g. The Arabic language.
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once'
page = requests.get(url) # Returns <response [200]> indicating everything is good.
soup = BeautifulSoup(page.text, 'html.parser')

# Categories for dataframe.
df_column_titles = ['Title', 'Author', 'Average Rating']
ranks = []
book_titles = []
authors = []
avg_ratings = []

# Ranking i.e. 1-> 100 on every page
table = (soup.find('table', class_="tableList js-dataTooltip")).encode('utf-8')
table_rankings = soup.find_all('td', class_="number")
ranks = [rank.text.strip() for rank in table_rankings]

# Book information includes the title, author, and rating. Maybe add the genre.
book_info_elements = soup.find_all('td', width='100%')
book_data = []


for book_element in book_info_elements:
    title_span = book_element.find('span', itemprop='name')
    author_span = book_element.find('a', class_='authorName').find('span', itemprop='name')
    rating_span = book_element.find('span', class_='minirating')

    if title_span and author_span and rating_span:
        title = title_span.text.strip()
        author = author_span.text.strip()
        rating = rating_span.text.strip()

        book_data.append({'Title': title, 'Author': author, 'Average Rating': rating})

# Constructing the data frame.
df = pd.DataFrame(book_data, columns = df_column_titles)
df.insert(0, 'Rank', ranks)

df.to_csv(r"C:\Users\maxhi\OneDrive\Desktop\2024 Coding Projects\BookRecommendationApp\Output Folder\GoodReadsData.csv", index=False)