import requests
import re
from urllib import request
import gzip


# 断点调试
class Spider():
    url = 'https://www.douyu.com/g_LOL'
    root_pattern = '<div class="DyListCover-info"><span class="DyListCover-hot">([\s\S]*?)</div>'
    name_pattern = '</use></svg>([\s\S]*?)</h2>'
    number_pattern = '</svg>([\s\S]*?)</span>'
    # res = requests.get(url)
    # print(res.encoding)
    # a = 1
    
    def __fetch_content(self):
        # urlopen接受url地址
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = gzip.decompress(htmls).decode('utf-8')
        # htmls = htmls.decode('utf-8', errors='replace')
        # a = 1
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        print(root_html)
        a = 1
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.name_pattern, html)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        print(anchors[3])
        # print(root_html[3])
        a = 1

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()

