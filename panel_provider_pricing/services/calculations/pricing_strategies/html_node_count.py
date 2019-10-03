from lxml import html
import requests

from panel_provider_pricing.services.crawlers import FetchHTTPResponse


class HTMLNodeCount():
    """
    Counts HTML nodes at <target_url>
    """
    def __init__(self, target_url="https://time.com/", divisor=100.0):
        self.target_url = target_url
        self.divisor = divisor


    def execute(self):
        crawler = FetchHTTPResponse(self.target_url)
        response = crawler.execute()

        if crawler.last_response_ok:
            html_node_count = html.fromstring(response.content).xpath(
                "count(//*)")

            return html_node_count / float(self.divisor)
