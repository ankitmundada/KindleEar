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
        ('Nautilus', 'http://nautil.us/rss/all'),
        ('Google AI Blog', 'http://feeds.feedburner.com/blogspot/gJZg', True), # Google AI
        ('DeepMind AI Blog', 'https://deepmind.com/blog/feed/basic/'),
        ('Open AI Blog', 'https://blog.openai.com/rss/'),
        ]
    
