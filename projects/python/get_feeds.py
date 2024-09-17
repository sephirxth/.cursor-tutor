import feedparser
 
from http import HTTPStatus
 

def parse_feeds(feeds):
    all_entries = []
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        all_entries.extend(feed.entries)
    return all_entries