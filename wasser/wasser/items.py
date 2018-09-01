# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WaterSystem(scrapy.Item):
    water_system_no = scrapy.Field()
    water_system_name = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    pricipal_country_served = scrapy.Field()
    primary_source_water_type = scrapy.Field()
