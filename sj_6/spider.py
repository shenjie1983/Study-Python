import requests
import re
from urllib import request


# 断点调试
class Spider():
    url = 'https://www.douyu.com/g_LOL'
    root_pattern = '<div class="DyListCover-info">[\s\S]*?</div>'
    res = requests.get(url)
    print(res.encoding)
    a = 1
    
    def __fetch_content(self):
        # urlopen接受url地址
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = htmls.decode('utf-8', errors='replace')
        a = 1
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        a = 1

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()

