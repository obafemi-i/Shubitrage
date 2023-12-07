import scrapy

from ..items import ShubitrageItem
class NikeSpider(scrapy.Spider):
    name = "Nike"
    allowed_domains = ["Nike.com", "stockx.com"]

    sku = input('Enter SKU - ')

    start_urls = [f"https://www.nike.com/w?q={sku}"]

    def parse(self, response):
        shoe_name = response.css('div.product-card__title::text').get()
        shoe_category = response.css('div.product-card__subtitle::text').get()
        selling_price = response.css('div.is--current-price::text').get()

        try:
            original_price = response.css('div.is--striked-out::text').get()
        except AttributeError:
            original_price = None

        try:
            best_seller = response.css('div.product-card__messaging.accent--color::text').get()
        except AttributeError:
            best_seller = None

        items = ShubitrageItem()
        
        items['sku'] = NikeSpider.sku
        items['Nike_category'] = shoe_category
        items['Nike_name'] = shoe_name
        items['Nike_selling_price'] = selling_price
        items['Nike_original_price'] = original_price
        items['Nike_status'] = best_seller

        stockx_url = f'https://stockx.com/search?s={NikeSpider.sku}'

        yield scrapy.Request(stockx_url, callback=self.parse_stockx, cb_kwargs={'items':items})

    def parse_stockx(self, response, items):
        main = response.css('div.css-xzkzsa')
        for search in main:
            stockx_name = search.css('p.chakra-text.css-3lpefb::text').extract()
            stockx_status = search.css('p.chakra-text.css-jsq4f::text').extract()
            stockx_price = search.css('p.chakra-text.css-nsvdd9::text').extract()

            items['stockx_price'] = stockx_price
            items['stockx_name'] = stockx_name
            items['stockx_status'] = stockx_status
        
        yield items
