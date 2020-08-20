# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    province_name=scrapy.Field()
    city_name=scrapy.Field()
    city_url=scrapy.Field()
    flag=scrapy.Field()

class Fang1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    flag=scrapy.Field()
    province_name=scrapy.Field()
    city_name=scrapy.Field()
    area_name=scrapy.Field()
    area_url=scrapy.Field()


class Fang2Item(scrapy.Item):
    house_image=scrapy.Field()
    house_detail=scrapy.Field()
    house_name=scrapy.Field()
    house_descript=scrapy.Field()
    house_size=scrapy.Field()
    house_address=scrapy.Field()
    house_phone=scrapy.Field()
    flag=scrapy.Field()
    city_name=scrapy.Field()
    area_name=scrapy.Field()
    house_price=scrapy.Field()
    house_label=scrapy.Field()
