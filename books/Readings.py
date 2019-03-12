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
    max_articles_per_feed = 3
    coverfile             = "cv_the_daily_journal.jpg"
    oldest_article        = 1
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('Editorials', 'https://www.thehindu.com/opinion/editorial/feeder/default.rss'),
        ('Editorials', 'https://www.thehindu.com/opinion/lead/feeder/default.rss'),
        ('Editorials', 'https://www.thehindu.com/opinion/interview/feeder/default.rss'),
        ('Editorials', 'https://www.tribuneindia.com/rss/feed.aspx?cat_id=187&mid=70', True),
        ('Editorials', 'https://www.tribuneindia.com/rss/feed.aspx?cat_id=34&mid=70', True),
        ('Editorials', 'https://indianexpress.com/section/opinion/editorials/feed/'),
        ('Biz', 'https://yourstory.com/category/ys-in-depth/feed'),
        ('Biz', 'http://feeds.feedburner.com/hbr/KsRB'),
        ('AI', 'https://blog.openai.com/rss/'),
        ('AI', 'https://distill.pub/rss.xml'),
        ('AI', 'https://www.aitrends.com/category/features/feed/'),
        ('AI', 'https://blogs.nvidia.com/blog/category/deep-learning/feed/'),
        ('AI', 'http://feeds.feedburner.com/blogspot/gJZg', True),
        ('AI', 'https://deepmind.com/blog/feed/basic/'),
        ('AI', 'https://towardsdatascience.com/feed/tagged/deep-learning'),
        ('AI', 'https://blog.bigml.com/feed/'),
        ('AI', 'https://eng.uber.com/tag/machine-learning/feed/'),
        ('AI', 'https://chatbotslife.com/feed'),
        ('AI', 'https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml'),
        ('Curious?', 'http://nautil.us/rss/all'),
        ('Bookmarked', 'https://www.instapaper.com/rss/6974367/jcrQql6U6UgcuGZVa6uXVs2OVYU'),
        # ('Biz', 'https://inc42.com/features/feed'),
        # ('Biz', 'https://inc42.com/startups/feed'),
        # ('Biz', 'https://yourstory.com/category/funding-investments/feed'), # infrequent
        # ('AI', 'http://aiweekly.co/issues.rss'), # AI Weekly (Doesn't work as expected)
        # ('Editorials', 'https://www.orfonline.org/content-type/commentary/feed/'), # Too long
        # ('Editorials', 'http://rss.jagran.com/rss/editorial/nazariya.xml'), # Dianik Jagaran (Not so good)
        # ('Editorials', 'https://navbharattimes.indiatimes.com/opinions/rssfeedsection/2279782.cms'),
        ]
    
