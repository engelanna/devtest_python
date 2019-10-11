import requests

from .fetch_http_response import FetchHTTPResponse

class FetchJSONResponse(FetchHTTPResponse):
    def execute(self):
        """
        Expose the HTTP response fetched from <target_url> as JSON

        Returns:
            JSON made from HTTP response object

        Side effects:
            Connects to target URL over HTTP
        """

        response = super().execute()
        self.last_response = response.json()

        return self.last_response
