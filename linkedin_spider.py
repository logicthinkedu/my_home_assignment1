import urllib
from bs4 import BeautifulSoup

def crawler(url):
    try:
        text = urllib.request.urlopen(url)
        soup = BeautifulSoup(text, 'html.parser')

        f = open('data/' + soup['title'], mode="w", encoding="utf-8")
        f.write(soup['content'])
        f.close()

    except:
        print('Error')

if __name__ == "__main__":
    crawler('https://www.baidu.com/')