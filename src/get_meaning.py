# -*- coding: utf-8 -*-
import scrapy
import json
from bs4 import BeautifulSoup

class GetMeaningSpider(scrapy.Spider):
    name = "get_meaning"

    def start_requests(self):
        url = "http://www.urbandictionary.com/define.php"
        word = getattr(self,'word',None)
        word = word.replace("+","%2B")

        if word is not None:
            url = url+"?term="+word
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # extracted data
        data = {
                "word": response.css("a.word::text").extract_first(),
                "meaning": BeautifulSoup(response.css("div.meaning").extract_first()).text
                }     
        
        # write output to a file
        output_file = open("temp.json","w")
        json.dump(data, output_file)
        output_file.close()
        
        yield data
            
