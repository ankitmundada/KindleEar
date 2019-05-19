#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return ReadingsWeekly

class ReadingsWeekly(BaseFeedBook):
    title                 = 'The Weekly Journal'
    description           = 'Editorials from various sources on various topics'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 3
    coverfile             = "cv_weekly_news.jpg"
    oldest_article        = 7
    deliver_days          = ['Friday']
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('ThoughtProvoking', 'http://nautil.us/rss/all'),
        ('AI', 'http://feeds.feedburner.com/blogspot/gJZg', True), # Google AI
        ('AI', 'https://deepmind.com/blog/feed/basic/'),
        ('AI', 'https://blog.openai.com/rss/'),
        ('AI', 'https://distill.pub/rss.xml'),
        ('Biz', 'https://yourstory.com/category/ys-in-depth/feed'),
        ('Instapaper-D', 'https://www.instapaper.com/rss/7044488/et9bBlTZ56Mj5c23OdfoefH34cw'),
        ]
    
