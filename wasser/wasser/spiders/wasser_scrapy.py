# from __future__ import unicode_literals

import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from wasser.items import *
# from scrapy.selector import HtmlXPathSelector
# from scrapy.http import FormRequest, Request
# from scrapy.utils.response import open_in_browser







class wasser_liste(scrapy.Spider):
    name = "spinne"

    start_urls = ['http://water.epa.state.il.us/dww/JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=null&begin_date=6/26/2016&end_date=6/26/2018&action=Search%20For%20Water%20Systems']

    # custom_settings = {
    #     # specifies exported fields and order
    #     'FEED_EXPORT_FIELDS': ["number", "name", "type", "status", "principal", "prim"],
    # }


    # THIS "PARSE" METHOD IS IMPORTANT FOR SPIDER TO SCRAPE THE URL
    def parse(self, response):

        divs = response.xpath('//td')
        for itm in divs:

            system_nos = divs.xpath('//a[@href]/text()').extract()
            systemnos = [systemno.strip() for systemno in system_nos]

            names = divs.xpath('//td[2]/text()').extract()
            names = [name.strip() for name in names]

            type = divs.xpath('//td[3]/text()').extract()
            types = [typenum.strip() for typenum in type]

            status = divs.xpath('//td[4]/text()').extract()
            statuses = [water_stat.strip() for water_stat in status]

            pri_co_ser = divs.xpath('//td[8]/text()').extract()
            principal_county = [prico.strip() for prico in pri_co_ser]

            primarysource = divs.xpath('//td[6]/text()').extract()
            primsour = [primso.strip() for primso in primarysource]

            result = zip(systemnos, names, types, statuses, principal_county, primsour)
            for number, name,  type, status, principal, prim  in result:
                items = WaterSystem()
                items['water_system_no'] = number
                items['water_system_name'] = name
                items['type'] = type
                items['status'] = status
                items['pricipal_country_served'] = principal
                items['primary_source_water_type'] = prim
                yield items









    #
    # def parse_second(self, response):
    #     divs = response.xpath('//div')
    #     for itm_two in divs:
    #         type = divs.xpath('.//td[3]/text()').extract()
    #         types = [typenum.strip() for typenum in type]
    #
    #         status = divs.xpath('.//td[4]/text()').extract()
    #         statuses = [water_stat.strip() for water_stat in status]
    #
    #         result = zip(types, statuses)
    #         for type, status in result:
    #             items_two = WaterSystem()
    #             items_two['type'] = type
    #             items_two['status'] = status
    #             yield items_two
    #
    #
    #
    #
    #
    # def parse_third(self, response):
    #     divs = response.xpath('//div')
    #     for itm_three in divs:
    #
    #         pri_co_ser = divs.xpath('.//td[8]/text()').extract()
    #         principal_county = [prico.strip() for prico in pri_co_ser]
    #
    #         primarysource = divs.xpath('.//td[6]/text()').extract()
    #         primsour = [primso.strip() for primso in primarysource]
    #
    #         result = zip(principal_county, primsour)
    #         for principal, prim  in result:
    #             items_three = WaterSystem()
    #             items_three['pricipal_country_served'] = principal
    #             items_three['primary_source_water_type'] = prim
    #             yield items_three