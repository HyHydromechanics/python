import requests

url = 'https://hikarifield.co.jp/maitetsu_lastrun/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 '
                  'Safari/537.36'}
if __name__ == "__main__":
    print(getHTMLText(url))
