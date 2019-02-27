#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return Editorials

class Editorials(BaseFeedBook):
    title                 = 'Editorials'
    description           = 'Editorials from various sources -national and international - on various topics'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 5
    oldest_article        = 1
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('The Hindu', 'https://www.thehindu.com/opinion/editorial/feeder/default.rss'),
        ('The Indian Express', 'https://indianexpress.com/section/opinion/editorials/feed/'),
        ('Dainik Jagran', 'http://rss.jagran.com/rss/editorial/nazariya.xml'),
        ('Inc42', 'https://inc42.com/features/feed'),
        ('YourStory', 'https://yourstory.com/category/ys-in-depth/feed'),
        ]
    
