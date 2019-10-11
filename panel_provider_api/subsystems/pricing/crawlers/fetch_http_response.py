import requests


class FetchHTTPResponse():

    def __init__(self, target_url):
        """
        Params:
            target_url : string
        """

        self.target_url = target_url
        self.last_response = None
        self.last_response_ok = False


    def execute(self):
        """
        Returns:
            HTTP response object from <target_url>

        Side effects:
            1. Connects to target URL over HTTP
            2. Overwrites <self.last_response>
        """

        response = requests.get(self.target_url)

        self.last_response = response
        self.last_response_ok = response.status_code == requests.codes.ok

        return self.last_response
