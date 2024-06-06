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


def main():
    url = 'https://xkcd.com'
    os.makedirs('xkcd', exist_ok=True)
    while not url.endswith('#'):
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comicElem = soup.select('#comic img')
        if not comicElem:
            print('Could not find comic image.')
        else:
            comicUrl = f'http:{comicElem[0].get('src')}'
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')


if __name__ == '__main__':
    main()
