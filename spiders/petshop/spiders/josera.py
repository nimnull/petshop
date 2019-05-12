# -*- coding: utf-8 -*-
import scrapy


class JoseraSpider(scrapy.Spider):
    name = 'josera'
    allowed_domains = ['www.josera-dog.com']
    start_urls = ['http://www.josera-dog.com/']

    def parse(self, response):
        for subcategory in response.xpath("//*[@id='navilang']//li//@href"):
            yield response.follow(subcategory, self.parse_subcategory)

    def parse_subcategory(self, response):
        for product_page in response.xpath("//*[@id='produkt_inhalt']//p//@href"):
            yield response.follow(product_page, self.parse_product)

    def parse_product(self, response):
        yield {
            'source': response.url,
            'title': response.xpath("//*[@id='produktbeschreibung']//h1/text()").get(),
            'composition': response.xpath("//*[@id='produkttabs']//p[contains(.,'Composition')]/text()").get()
        }
        # yield response

