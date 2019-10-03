import requests

from panel_provider_pricing.services.crawlers import FetchHTTPResponse


class CharacterCount():
    """
    Counts the occurences of <character> in the text of <target_url>
    """

    def __init__(
        self,
        character_to_count = "a",
        target_url="https://time.com/",
        divisor=100.0
     ):
        self.character_to_count = character_to_count
        self.target_url = target_url
        self.divisor = divisor


    def execute(self):
        crawler = FetchHTTPResponse(self.target_url)
        crawler.execute()

        if crawler.last_response_ok:
          return crawler.last_response.text.count(self.character_to_count) / float(self.divisor)
