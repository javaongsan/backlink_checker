import  os, time, random, datetime, sys, requests
from xgoogle.search import GoogleSearch, SearchError

class google_url_scrapper:
    def __init__(self):        
        self.urls = []
        self.seo = ''

    def scrape(self, keyword, pages=2):
        try:
            gs = GoogleSearch(keyword)
            gs.results_per_page = 10
            gs.page = 0
            results = gs.get_results()
            for res in results:
                url = res.url.encode('utf8')
                Title = res.title
                self.urls.append((url, Title))
        except SearchError, e:
          print "Search failed: %s" % e
        return self.urls

    def MajesticSEO_API(self, url):
        """Get metrics for a single URL"""
        
        data = {
            'getcsv': 'Get backlink counts as .CSV',
            'SortBy': '-1',
            'items': '1',
            'Datasource': 'Fresh',
            'item0': url
        }

        request = requests.post('https://csv.majesticseo.com/getcsvdata/bulkbacklinks',
                                data=data,
                                cookies={'STOK': 'anything'})

        if 'We could not determine your user creditials' not in request.text:
             self.seo = dict(zip(request.text.splitlines()[0].split(','),
                        request.text.splitlines()[1].split(',')))
             return self.seo
        else:
            raise Exception("Couldn't authenticate without proper session variable")



