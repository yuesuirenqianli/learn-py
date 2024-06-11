"""
    11.7
    加载主页；
    保存该页的漫画图片；
    转入前一张漫画的链接；
    重复直到第一张漫画。
    这意味着代码需要做下列事情：
    利用 requests 模块下载页面。
    利用 Beautiful Soup 找到页面中漫画图像的 URL。
    利用 iter_content()下载漫画图像，并保存到硬盘。
    找到前一张漫画的链接 URL，然后重复
"""


import requests
import os
import bs4
from abc import ABC, abstractmethod


class PageDownloader(ABC):
    @abstractmethod
    def download_page(self, url: str) -> str:
        pass


class SimplePageDownloader(PageDownloader):
    def download_page(self, url: str) -> str:
        res = requests.get(url)
        res.raise_for_status()
        return res.text


class ComicImageExtractor(ABC):
    @abstractmethod
    def extract_image_url(self, page_content: str) -> str:
        pass


class XKCDComicImageExtractor(ComicImageExtractor):
    def extract_image_url(self, page_content: str) -> str:
        soup = bs4.BeautifulSoup(page_content, "html.parser")
        comic_elem = soup.select("#comic img")
        if not comic_elem:
            raise ValueError('Could not find comic image.')
        return f'http:{comic_elem[0].get('src')}'


class ImageDownloader(ABC):
    @abstractmethod
    def download_image(self, image_url: str, save_path: str) -> None:
        pass


class SimpleImageDownloader(ImageDownloader):
    def download_image(self, image_url: str, save_path: str) -> None:
        res = requests.get(image_url)
        res.raise_for_status()
        with open(save_path, 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)


class XKCDComicScraper:
    def __init__(self, downloader: PageDownloader, extractor: ComicImageExtractor, image_downloader: ImageDownloader) -> None:
        self.downloader = downloader
        self.extractor = extractor
        self.image_downloader = image_downloader

    def scrape_comics(self, start_url: str, save_dir: str) -> None:
        os.makedirs(save_dir, exist_ok=True)
        url = start_url
        while not url.endswith('#'):
            print('Downloading page %s...' % url)
            page_content = self.downloader.download_page(url)
            try:
                comic_url = self.extractor.extract_image_url(page_content)
                save_path = os.path.join(save_dir, os.path.basename(comic_url))
                print(f'Downloading image {comic_url}...')
                self.image_downloader.download_image(comic_url, save_path)
            except Exception as e:
                print(e)

            soup = bs4.BeautifulSoup(page_content, 'html.parser')
            prev_link = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prev_link.get('href')


def main():
    downloader = SimplePageDownloader()
    extractor = XKCDComicImageExtractor()
    image_downloader = SimpleImageDownloader()
    scraper = XKCDComicScraper(downloader, extractor, image_downloader)
    scraper.scrape_comics('https://xkcd.com', 'xkcd')


if __name__ == '__main__':
    main()
