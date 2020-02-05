#!/usr/bin/env python3
# coding:utf8
""" 
https://pybay.com/site_media/slides/raymond2017-keynote/threading.html#david-baron-at-mozillas-san-francisco-office 
"""

import urllib.request
from multiprocessing.pool import ThreadPool as Pool
# from multiprocessing.pool import Pool

sites = [
    'https://www.yahoo.com/',
    'http://www.cnn.com',
    'http://www.python.org',
    # 'http://www.jython.org',
    # 'http://www.pypy.org',
    # 'http://www.perl.org',
    # 'http://www.cisco.com',
    # 'http://www.facebook.com',
    # 'http://www.twitter.com',
    # 'http://www.macrumors.com/',
    # 'http://arstechnica.com/',
    # 'http://www.reuters.com/',
    # 'http://abcnews.go.com/',
    'http://www.cnbc.com/',
    'http://www.drooten.com/',
]


def sitesize(url):
    ''' Determine the size of a website '''

    try:

        with urllib.request.urlopen(url) as u:
            page = u.read()
            return url, len(page)

    except HTTPError as e:
        return url, -99

    except URLError as e:
        return url, -99

    else:
        return url, len(page)


# 95% baby making; 5% processes
# speed now = time to make 1 baby
pool = Pool(10)
for result in pool.imap_unordered(sitesize, sites):
    print(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()