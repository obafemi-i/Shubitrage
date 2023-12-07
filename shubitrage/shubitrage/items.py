# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ShubitrageItem(scrapy.Item):
    sku = scrapy.Field()
    Nike_name = scrapy.Field()
    Nike_category = scrapy.Field()
    Nike_selling_price = scrapy.Field()
    Nike_original_price = scrapy.Field()
    Nike_status = scrapy.Field()
    stockx_price = scrapy.Field()
    stockx_status = scrapy.Field()
    stockx_name = scrapy.Field()
    
