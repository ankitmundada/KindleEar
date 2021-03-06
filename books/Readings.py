#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return DailyReadings

class DailyReadings(BaseFeedBook):
    title                 = 'The Daily Journal'
    description           = 'Editorials from various sources on various topics'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 15
    coverfile             = "cv_the_daily_journal.jpg"
    oldest_article        = 1
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('News', 'https://www.thehindu.com/opinion/cartoon/feeder/default.rss', 1),
        ('News', 'https://www.thehindu.com/opinion/editorial/feeder/default.rss', 1),
        #('News', 'https://www.thehindu.com/opinion/lead/feeder/default.rss', 1),
        ('News', 'https://www.thehindu.com/opinion/interview/feeder/default.rss', 1),
        ('News', 'https://www.tribuneindia.com/rss/feed.aspx?cat_id=187&mid=70', True, 1),
        ('News', 'https://www.tribuneindia.com/rss/feed.aspx?cat_id=34&mid=70', True, 1),
        ('Biz', 'https://yourstory.com/category/ys-startup/feed'),
        ('Biz', 'https://yourstory.com/category/daily-capsule/feed'),
        #('Biz', 'http://feeds.feedburner.com/hbrLatest', 3), # HBR
        ('Biz', 'http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fhbr.org%2F&in_id_or_class=&url_contains=&item=ul+.hero-featured-items+li'), # HBR
        ('AI', 'https://towardsdatascience.com/feed/tagged/deep-learning', 1),
        ('AI', 'https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml'),
        ('Short-Story', 'https://americanliterature.com/feed/shortstoryfeed.xml'),
        ('Bookmarked', 'https://www.instapaper.com/rss/6974367/jcrQql6U6UgcuGZVa6uXVs2OVYU'),
        # ('Biz', 'https://inc42.com/features/feed'),
        # ('Biz', 'https://inc42.com/startups/feed'),
        # ('Biz', 'https://yourstory.com/category/funding-investments/feed'), # infrequent
        # ('AI', 'https://blog.bigml.com/feed/'), # Not DL Focused
        # ('AI', 'https://blogs.nvidia.com/blog/category/deep-learning/feed/'), # Mostly Promotional
        # ('AI', 'http://aiweekly.co/issues.rss'), # AI Weekly (Doesn't work as expected)
        # ('AI', 'https://chatbotslife.com/feed'),
        # ('AI', 'https://eng.uber.com/tag/machine-learning/feed/'),
        # ('Editorials', 'https://indianexpress.com/section/opinion/editorials/feed/'), # Okayish
        # ('Editorials', 'https://www.orfonline.org/content-type/commentary/feed/'), # Too long
        # ('Editorials', 'http://rss.jagran.com/rss/editorial/nazariya.xml'), # Dianik Jagaran (Not so good)
        # ('Editorials', 'https://navbharattimes.indiatimes.com/opinions/rssfeedsection/2279782.cms'),
        ]
    
