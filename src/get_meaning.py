# -*- coding: utf-8 -*-
import scrapy
import json

class GetMeaningSpider(scrapy.Spider):
    name = "get_meaning"

    def start_requests(self):
        url = "http://www.urbandictionary.com/define.php"
        word = getattr(self,'word',None)

        if word is not None:
            url = url+"?term="+word
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # extracted data
        data = {
                "word": response.css("a.word::text").extract_first(),
                "meaning": response.css("div.meaning::text").extract_first()
                }     
        
        # write output to a file
        output_file = open("temp.json","w")
        json.dump(data, output_file)
        output_file.close()
        
        yield data
            
