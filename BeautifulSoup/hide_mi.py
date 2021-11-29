from bs4 import BeautifulSoup
import requests
import random

user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36'
]
proxy_list = {
    'https': 'http://127.0.0.1:8118'
}

def get_location(url):
    user_agent = random.choice(user_agent_list)
    #proxies = random.choice(proxy_list)
    headers = {'User agent': user_agent}
    try:
        responses = requests.get(url=url, headers=headers, proxies=proxy_list)
        soup = BeautifulSoup(responses.text, "lxml")
        ip_ = soup.find("div", class_="ip").text.strip()
        locate_ =  soup.find("div", class_="value value-country").text.strip()
        print(f"IP: {ip_} \nLocation: {locate_}")
    except:
        raise ValueError("We have error")

def main():
    get_location(url = "https://2ip.ru/")

if __name__ == '__main__':
    main()


