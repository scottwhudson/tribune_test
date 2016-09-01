import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup
import csv


def fetch_tribune_data():
    articles_list = []

    for x in range(1,4):
        url = ("https://www.texastribune.org/all/?page=%(x)s." % locals())

        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        articles = soup.find_all('article', {"class": " "})

        for article in articles:
            title = article.contents[1].h1.text
            url = article.contents[1].a.get('href')
            author = article.contents[1].find('li', {"class": "byline"}).a.text
            img_url = article.contents[3].find('img').get('src')
            date = article.contents[1].find('time').get('datetime')

            articles_list.append([url, date, author, title, img_url])

    return articles_list

def transform_data(data):
    for article in data:

        article[1] = convert_to_utc(article[1])

        if 'https' not in article[0]:
            article[0] = prepend_baseurl('article', article[0])

        if 'https' not in article[4]:
            article[4] = prepend_baseurl('image', article[4])

    return data


def convert_to_utc(date_string):
    return parse(date_string).strftime("%Y-%m-%d")


def prepend_baseurl(url_type, url):
    if url_type == 'article':
        return 'https://www.texastribune.org' + url
    elif url_type == 'image':
        return 'https:' + url
    else:
        return None


def prepare_csv(data):
    # Sort By Date Column Asc
    data = sorted(data,key=lambda col:col[1])

    # Insert CSV Header
    data.insert(0, ['Article URL', 'Date', 'Author', 'Headline', 'Image URL'])

    return data


def generate_csv(data):
    with open('articles.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(data)

    print("CSV generated!")    


data = fetch_tribune_data()
data = transform_data(data)
data = prepare_csv(data)
generate_csv(data)
