#! python3
# lucky.py - Opens several Google search results.


"""
    11.6
    从命令行参数中获取查询关键字。
    取得查询结果页面。
    为每个结果打开一个浏览器选项卡。
这意味着代码需要完成以下工作：
    用 requests 模块取得查询结果页面。
    找到每个查询结果的链接。
    调用 webbrowser.open()函数打开 Web 浏览器。
"""

import webbrowser
import requests
import bs4
from abc import ABC, abstractmethod


class FetchStrategy(ABC):
    @abstractmethod
    def fetch(self, url, headers):
        pass


class SimpleFetchStrategy(FetchStrategy):
    def fetch(self, url, headers):
        try:
            res = requests.get(url=url, headers=headers)
            res.raise_for_status()
            return res.text
        except requests.RequestException as e:
            print(f'Error fetching {url}: {e}')
            return None


class ParseStrategy(ABC):
    @abstractmethod
    def parse(self, html):
        pass


class SimpleParseStrategy(ParseStrategy):
    def parse(self, html):
        soup = bs4.BeautifulSoup(html, 'html.parser')
        links = soup.select('.item a')
        return [link.get('href') for link in links]


class ScraperFactory:
    @abstractmethod
    def create_scraper(fetch_strategy: FetchStrategy, parser_strategy: ParseStrategy):
        return Scraper(fetch_strategy, parser_strategy)


class Scraper:
    def __init__(self, fetch_strategy: FetchStrategy, parser_strategy: ParseStrategy):
        self.fetch_strategy = fetch_strategy
        self.parser_strategy = parser_strategy

    def scrape_adn_open(self, url, headers):
        html = self.fetch_strategy.fetch(url, headers)
        if html:
            links = self.parser_strategy.parse(html)
            self.open_links(links)

    @staticmethod
    def open_links(links):
        num_open = min(5, len(links))
        for i in range(num_open):
            webbrowser.open(links[i])


def main():
    print('Googling...')

    url = ''
    headers = {
        'User-Agent': '',
        'Cookie': ''
    }
    fetch_strategy = SimpleFetchStrategy()
    parser_strategy = SimpleParseStrategy()
    scraper = ScraperFactory.create_scraper(fetch_strategy, parser_strategy)
    scraper.scrape_adn_open(url, headers)


if __name__ == '__main__':
    main()
