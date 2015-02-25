# -*- coding: utf-8 -*
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

import scrapy
from cricketdata.items import CricketrecurItem
l=[]
for i in range(0,len(r.lrange("url:l:1:day:c",0,-1))):
    result =r.lpop("url:l:1:day:c")
    l.append(result)
    r.rpush("url:l:1:day:c",result)
class PakSpider(scrapy.Spider):
    name = "cri"
    start_urls = l
    def parse(self, response):
        
        item = CricketrecurItem()
        item["url"]=response.url
        item['matchid']=response.xpath('//*[@id="full-scorecard"]/div[1]/div[2]/div[1]/a[1]/text()').extract()
        item['toss']= response.xpath('//*[@id="full-scorecard"]/div[3]/div/div/div[1]/span[1]/text()').extract()
        item['daynight']=  response.xpath('//*[@id="full-scorecard"]/div[1]/div[2]/div[3]/text()').extract()
        item['ground']=response.xpath('//*[@id="full-scorecard"]/div[1]/div[1]/div[1]/a/text()').extract()


        item['team1']=response.xpath('//*[@id="full-scorecard"]/div[1]/div[1]/div[2]/a[1]/text()').extract()
        item['team2']=response.xpath('//*[@id="full-scorecard"]/div[1]/div[1]/div[2]/a[2]/text()').extract()
        
        item['winner_margin']=response.xpath('//*[@id="full-scorecard"]/div[1]/div[1]/div[3]/text()').extract()
        item['matchdate']=response.xpath('//*[@id="full-scorecard"]/div[1]/div[2]/div[3]/text()').extract()
        item['series']=response.xpath('//*[@id="full-scorecard"]/div[1]/div[1]/div[1]/a/text()').extract()
        item['inning1']=response.xpath('//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[1]/th[2]/text()').extract()
        item['inning2']=response.xpath('//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[1]/th[2]/text()').extract()
        
        

        r.rpush("data:one:day:match",item)
        yield item