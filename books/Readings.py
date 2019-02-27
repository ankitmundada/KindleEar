#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return Readings

class Readings(BaseFeedBook):
    title                 = 'The Daily Journal'
    description           = 'Editorials from various sources on various topics'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 5
    coverfile             = "cv_the_daily_journal.jpg"
    oldest_article        = 1
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('Editorials', 'https://www.thehindu.com/opinion/editorial/feeder/default.rss'),
        ('Editorials', 'https://indianexpress.com/section/opinion/editorials/feed/'),
        ('Editorials', 'http://rss.jagran.com/rss/editorial/nazariya.xml'),
        ('Startups', 'https://inc42.com/features/feed'),
        ('Startups', 'https://yourstory.com/category/ys-in-depth/feed'),
        ('AI', 'https://blog.openai.com/rss/'),
        ('AI', 'http://aiweekly.co/issues.rss'),
        ('AI', 'https://distill.pub/rss.xml'),
        ('AI', 'https://www.aitrends.com/category/features/feed/'),
        ('AI', 'https://blogs.nvidia.com/blog/category/deep-learning/feed/'),
        ]
    
