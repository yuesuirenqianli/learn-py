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


def main():
    print('Googling...')

    url = ''
    headers = {
        'User-Agent': '',
        'Cookie': ''
    }
    res = requests.get(url=url, headers=headers)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    links = soup.select('.item a')
    numOpen = min(5, len(links))
    for i in range(numOpen):
        webbrowser.open(links[i].get('href'))


if __name__ == '__main__':
    main()
