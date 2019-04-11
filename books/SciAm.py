#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return SciAm

class SciAm(BaseFeedBook):
    title                 = 'Scientific American'
    description           = 'Global advances in Science'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    coverfile             = "cv_sciam.jpg"
    deliver_days          = ['Friday']
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('Technology', 'http://rss.sciam.com/sciam/technology'),
        ('Science', 'http://rss.sciam.com/basic-science'),
        ('Latest', 'http://rss.sciam.com/ScientificAmerican-Global'),
        ('Mind', 'http://rss.sciam.com/sciam/mind-and-brain'),
        ('Health', 'http://rss.sciam.com/sciam/health-and-medicine'),
        ('Sustainability', 'http://feeds.feedburner.com/energy-and-sustainability'),
        ]
    
