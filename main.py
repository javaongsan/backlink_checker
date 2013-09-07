from google_url_scrapper import google_url_scrapper
from rank_provider import RankProvider, AlexaTrafficRank, GooglePageRank
import os, re

def Test():
    keyword = raw_input('Prompt :')
    G=google_url_scrapper()
    urls=G.scrape(keyword)
    for purl in urls:
        url=purl[0]
        Title = purl[1]
        results = G.MajesticSEO_API(url)
        print("Traffic stats for: %s" % (url))
        print("Title: %s" % (Title))
        print("ACRank: %s" % (results['ACRank']))
        print("ExtBackLinks: %s" % (results['ExtBackLinks']))
        providers = (AlexaTrafficRank(), GooglePageRank(),)
        for p in providers:
            print("%s: %s" % (p.__class__.__name__, p.get_rank(url)))
        print('')

if __name__ == "__main__":		
    Test()