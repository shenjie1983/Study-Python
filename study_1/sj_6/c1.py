import requests
import re
from urllib import request
import gzip


# 断点调试
class Spider():
    url = 'https://www.douyu.com/g_LOL'
    # root_pattern = '<span class="DyListCover-hot">([\s\S]*?)</span>'
    root_pattern = '<div class="DyListCover-info"><span class="DyListCover-hot is-template">([\s\S]*?)</div>'
    number_pattern = '</svg>([\s\S]*?)</span><h2'
    name_pattern = '<use xlink:href="#icon-user_05fb112"></use></svg>([\s\S]*?)</h2>'
    
    a = 1
    
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = gzip.decompress(htmls).decode('utf-8')
        # print(htmls)
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        # print(root_html[2])
        # a = 1
        anchors = [] 
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name':name, 'number':number}
            # 把匹配的字典放到列表anchors中
            anchors.append(anchor)
        # print(anchors)
        # a = 1
        return anchors
    
    def __refine(self, anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
            }
        return map(l, anchors)

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        print(anchors)

spider = Spider()
spider.go()

