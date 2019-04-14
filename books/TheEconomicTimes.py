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
    deliver_days          = ['Friday']
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('ET Home', 'https://economictimes.indiatimes.com/rssfeedsdefault.cms'),
        ('Top Stories', 'https://economictimes.indiatimes.com/rssfeedstopstories.cms', True),
        ('Markets', 'https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms'),
        ('News', 'https://economictimes.indiatimes.com/news/rssfeeds/1715249553.cms'),
        ('Industry', 'https://economictimes.indiatimes.com/industry/rssfeeds/13352306.cms'),
        ('Small Biz','https://economictimes.indiatimes.com/small-biz/rssfeeds/5575607.cms'),
        ('Wealth','https://economictimes.indiatimes.com/wealth/rssfeeds/837555174.cms'),
        ('Tech','https://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms'),
        ('Opinion','https://economictimes.indiatimes.com/opinion/rssfeeds/897228639.cms'),
        ('Magazine','https://economictimes.indiatimes.com/magazines/rssfeeds/1466318837.cms'),
        ]
    
