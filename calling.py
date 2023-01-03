import requests
import time
from urllib.parse import urlparse

def get_hostname(url):
    try:
        parsed_uri = urlparse(url)
        hostname = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        return hostname
    except e:
        return None

with open("url_list.csv", 'r') as url_list_file:
    url_postfix = "/front/php/ghost_mall/makeNaverCheckoutPrdXml.php"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    }
    for url in url_list_file.readlines():
        print("url", url.strip())
        url = url.strip()
        url = url + "/" if not url.endswith("/") else url
        hostname = get_hostname(url)
        print("hostname", hostname)
        if not hostname.endswith('/'):
            hostname += '/'
        req_url = hostname + url_postfix
        print("req_url", req_url)
        res = requests.get(req_url, headers=header)
        print(res.history)
        print(res.status_code)
        print(res.text)
        print()
    