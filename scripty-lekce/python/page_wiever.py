import requests
import time
from bs4 import BeautifulSoup
import urllib.parse

base = "https://elsnoxx.github.io"
    


def is_valid_url(url):
        try:
            test = requests.head(url)
            return test.status_code
        except requests.exceptions.RequestException:
            return test.status_code


def links_check(links):
    cnt = 0
    for link in links:
        # Získejte URL z atributu 'href' odkazu
        link_url = link.get('href')
        if link_url and link_url.startswith('/'):
            if is_valid_url(base+link_url) == 200:
                cnt+=1
            else:
                print(link_url)

        elif link_url == '':
            print("mising link")
        else:
            if is_valid_url(link_url) == 200:
                cnt+=1
            else:
                print(link_url)

        if link_url and link_url.startswith("http"):
            response = requests.get(link_url)
            next_page_soup = BeautifulSoup(response.text, 'html.parser')

    print("url test {}/{}".format(cnt,len(links)))


url = "https://elsnoxx.github.io"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')



for link in links:
    link_url = link.get('href')
    if link_url and link_url.startswith('/'):
        response = requests.get(base+link_url)
        print(base+link_url)
        if (base+link_url != "https://elsnoxx.github.io/bugs.html"):
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            links_check(links)
            print("\n")








