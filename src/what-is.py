#!/usr/bin/python

import sys
import pyttsx
import json
import scrapy
from scrapy.crawler import CrawlerProcess
from get_meaning import GetMeaningSpider as Meaning

# crawler process
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
if len(sys.argv) > 1:
    process.crawl(Meaning, word=sys.argv[1])
else:
    process.crawl(Meaning)

process.start()  # start the crawler

# text to speech engine
engine = pyttsx.init()

try:
    # open output file from crawling
    with open("temp.json") as json_result:
        result = json.load(json_result)
        print result["word"]
        engine.say(result["word"])  # say the word
        print result["meaning"]
        engine.say(result["meaning"])  # say the meaning
except:
    engine.say("Sorry! Didn't find any thing")
engine.runAndWait()
