import requests


class WebClient:
    """Client to use for request to other service.
       Add different methods to handle different request"""

    @staticmethod
    def get_json_from_request(url) -> (str, int):
        response, error = WebClient.get_request(url)
        if error:
            return response, 500
        if response.status_code != requests.codes.ok:
            return None, response.status_code
        return response.json(), response.status_code


    @staticmethod
    def get_request(url: str) -> (str, str):
        """Get data from url

        The exceptions will be handled better in production app
        Log the errors and handle them appropriately
        """
        if not url:
            raise ValueError('url required for the request')

        error = None

        try:
            response = requests.get(url)
            return response, error
        except requests.exceptions.ConnectionError as econ:
            error = econ.response
        except requests.exceptions.Timeout as etout:
            error = etout.response
        except requests.exceptions.RequestException as erq:
            error = erq.response
        return None, error


