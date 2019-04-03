# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = [
        
        # 'http://web/'
        'https://news.qq.com/a/20190402/008953.htm',
        'https://www.aqistudy.cn/historydata/monthdata.php?city=%E5%8C%97%E4%BA%AC'
        #测试
        # 'file:///C:/Users/zhengyimiing/OneDrive/%E6%A1%8C%E9%9D%A2/%E5%A4%B4%E7%89%8C%E7%8B%AC%E5%AE%B6%20_%20AI%E6%8D%A2%E8%84%B8%E8%B5%B7%E6%AD%BB%E5%9B%9E%E7%94%9F%EF%BC%8C%E9%BB%91%E7%A7%91%E6%8A%80%E6%96%B0%E8%BF%9B%E5%B1%95%E8%AF%A5%E5%96%9C%E8%AF%A5%E5%BF%A7%EF%BC%9F_%E6%96%B0%E9%97%BB_%E8%85%BE%E8%AE%AF%E7%BD%91.html'
                  ]

    def parse(self, response):
        #标题
        self.log("title: %s"%response.xpath(
            '/html/head/title'
        ).extract())

        self.log("content: %s" % response.xpath(
            '/html/body/div[3]/div[1]/div[1]/table/tbody/tr[7]/td[8]'
        ).extract())   #因为是动态的，所以是提取不到这个东西的。破解js的话，scrapy需要怎么操作。

        #正文
        


        pass
