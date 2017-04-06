from unipath import Path
import sys
import os

PROJECT_DIR = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(PROJECT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airbnbNewUserPredictions.settings')

import django
django.setup()


import threading
from airbnbNewUserPredictions.core.models import Product
from airbnbNewUserPredictions.sniffer.crawler import AirbnbNewUserPredictions


class Howl(threading.Thread):

    def __init__(self):
        super(Howl, self).__init__()
        self.crawler = AirbnbNewUserPredictions()

    def run(self):
        while True:
            products = Product.objects.all().order_by('visited_at')
            for product in products:
                self.crawler.howl(product)

def main():
    crawling = Howl()
    crawling.start()

if __name__ == '__main__':
    main()
