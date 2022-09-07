import bs4
import requests
from fake_headers import Headers

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)

keywords = ['дизайн', 'фото', 'web', 'python']
base_url = 'https://habr.com'
url = base_url + '/ru/all/'
responce = requests.get(url, headers=header.generate())
text = responce.text
soup = bs4.BeautifulSoup(text, 'html.parser')
articles = soup.find_all('article')


for article in articles:
    search_article = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    search_article = [search.text.strip() for search in search_article]
    for article_search in search_article:
        for key in keywords:
            if key in article_search:
                title = article.find('h2').find('span').text
                href = article.find(class_="tm-article-snippet__title-link").attrs['href']
                link = base_url + href
                date = article.find('time').attrs['title'].split(',')[0]
                print(date, title, link)

print()
print('Дополнительное (необязательное) задание:')
for article in articles:
    search_article = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    search_article = [search.text.strip() for search in search_article]
    for article_search in search_article:
                href = article.find(class_="tm-article-snippet__title-link").attrs['href']
                link = base_url + href
                responce = requests.get(link, headers=header.generate())
                text = responce.text
                soup = bs4.BeautifulSoup(text, 'html.parser')
                articles = soup.find_all('article')
                for article in articles:
                    search_article = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
                    search_article = [search.text.strip() for search in search_article]
                    for article_search in search_article:
                        for key in keywords:
                            if key in article_search:
                                search_article_full = article.find_all(class_="tm-article-snippet__title tm-article-snippet__title_h1")
                                search_article_full = [search.text.strip() for search in search_article_full]
                                date = article.find('time').attrs['title'].split(',')[0]
                                print(date, *search_article_full, link)





