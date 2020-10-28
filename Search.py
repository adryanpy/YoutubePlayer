import urllib3
import re

class Search(object):
    """
    docstring
    """
    def __init__(self, keyword=""):
        self.keyword = keyword.replace(" ","+")
        self.base_url = "https://www.youtube.com/"
        self.query_search = "results?search_query="
        self.query_watch = "watch?v="
        self.response_regex = r"watch\?v=(\S{11})"
        self.http_client = urllib3.PoolManager()

    def find(self, keyword=""):

        if keyword == "":
            keyword = self.keyword

        html = self.http_client.request("GET", str(self.base_url+self.query_search+keyword.replace(" ","+")))
        print(html)
        video_ids = re.findall(self.response_regex, html.data.decode())
        urls_return = []

        for id in video_ids:
            urls_return.append(str(self.base_url+self.query_watch)+str(id))

        return urls_return