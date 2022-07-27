








import requests
from fake_useragent import UserAgent
from lxml import etree
import pandas as pd


def main() -> None:
    url = 'https://ip.ihuan.me/'
    headers = {
        'User-Agent': UserAgent().random
    }

    resp = requests.get(url, headers=headers)
    e = etree.HTML(resp.text)
    tr = e.xpath("//table/tbody/tr")[0]

    ip_list  = tr.xpath("//td[1]/a/text()")
    port_list = tr.xpath("//td[2]/text()")
    is_support_https_list = tr.xpath('//td[5]/text()')
    anonymity_list = tr.xpath("//td[7]/a/text()")
    speed_list = tr.xpath('//td[8]/text()')

    with open('./proxy_ip.csv', "a", encoding='utf-8') as f:
        for tuple_str in zip(ip_list, port_list, is_support_https_list, anonymity_list, speed_list):
            # tuple_str = set(tuple_str)
            f.write(','.join(tuple_str)+'\n')








    resp.close()


def get_rid_of_repeat() -> None:
    str = ''.join(list(set(open("./proxy_ip.csv", 'r', encoding='utf-8').readlines())))
    with open('./proxy_ip.csv', 'w', encoding='utf-8') as f:
        f.write(str)


if __name__ == '__main__':
    # for i in range(10):
    #     main()
    get_rid_of_repeat()