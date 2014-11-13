#coding: utf-8

import HTMLParser
import urllib2
import urllib
import re

class MyParser(HTMLParser.HTMLParser):

    def __init__(self):
        self.start = False
        self.img = []
        self.weight = 0

        HTMLParser.HTMLParser.__init__(self)   

        
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for name,value in attrs:
                if name == 'src' and value.startswith("http://img12"):
                    self.img.append(value)

        attrs = dict(attrs)
        if tag == 'ul' and attrs.get('class', '') == "detail-list":
            self.start = True

    def handle_endtag(self, tag):
        if self.start and tag == 'ul':
            self.start = False

    def handle_data(self, data):
        if self.start:
            d =  data.decode("gb2312")
            if d.startswith(u"商品毛重"):
                self.weight = d.encode("utf-8")

def download(url, name):
    image = urllib.URLopener()
    image.retrieve(url, name+".jpg")
    print "download: ", name+".jpg"

def fetch(code):
    responed = urllib2.urlopen("http://search.jd.com/Search?keyword=%s&enc=utf-8" % code)
    data = responed.read();

    pattern = re.compile("http://item.jd.com/.*.html")
    a =  pattern.findall(data)
    itemurl = a[0]

    responed = urllib2.urlopen(itemurl)
    data = responed.read()

    my = MyParser()
    my.feed(data)

    # print my.img, my.weight

    download(my.img[0], code + "  " + str(my.weight))



if __name__ == '__main__':
    fetch("09029")


    
    # my = MyParser()
    # # 传入要分析的数据，是html的。
    # my.feed(data)
