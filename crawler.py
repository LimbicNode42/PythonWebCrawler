from urllib.request import urlopen
from findlinks import LinkFinder
from general import *

class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    not_crawled = ''
    crawled = ''
    queue = set()
    done = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.not_crawled = Spider.project_name + '/uncrawled.txt'
        Spider.crawled = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First crawl', Spider.base_url)

    @staticmethod
    def boot():
        create_project(Spider.project_name)
        create_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.not_crawled)
        Spider.done = file_to_set(Spider.crawled)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + '   now crawling    ' + page_url)
            print('Queue    ' + str(len(Spider.queue)) + '  |   Done    ' + str(len(Spider.done)))
            Spider.add_links(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.done.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: can not crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.done:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.not_crawled)
        set_to_file(Spider.done, Spider.crawled)