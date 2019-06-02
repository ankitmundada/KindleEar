#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return TheEconomicTimes

class TheEconomicTimes(BaseFeedBook):
    title                 = 'The Economic Times'
    description           = 'The economic times'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 3
    coverfile             = "cv_economic_times.jpg"
    oldest_article        = 1
    deliver_days          = ['Sunday']
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('Magazine','https://rss.app/feeds/3SNhRqw5oUEe8ZWb.xml'),
        ('Opinion','https://economictimes.indiatimes.com/opinion/rssfeeds/897228639.cms'),
        ]
    
