# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field


class CricketrecurItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    matchid=scrapy.Field()
    toss =scrapy.Field()
    daynight=scrapy.Field()
    ground=scrapy.Field()
    crawled=scrapy.Field()
    spider=scrapy.Field()
    team1=scrapy.Field()
    team2=scrapy.Field()
    winner_margin=scrapy.Field()
    matchdate=scrapy.Field()
    series=scrapy.Field()
    inning1=scrapy.Field()
    inning2=scrapy.Field()