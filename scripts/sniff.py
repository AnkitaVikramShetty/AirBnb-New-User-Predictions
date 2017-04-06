from unipath import Path
import sys
import os

PROJECT_DIR = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(PROJECT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airbnbNewUserPredictions.settings')

import django
django.setup()


import threading
from airbnbNewUserPredictions.sniffer.crawler import AirbnbNewUserPredictions


class Sniff(threading.Thread):

    def __init__(self):
        super(Sniff, self).__init__()
        self.crawler = AirbnbNewUserPredictions()
        self.crawler.feed('http://www.verkkokauppa.com/')

    def run(self):
        self.crawler.sniff()


def main():
    crawling = Sniff()
    crawling.start()

if __name__ == '__main__':
    main()
