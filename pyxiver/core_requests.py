"""
This module contains the requests to arxiv and handle responses
"""


import requests


def send_to_arxiv(request_url):
    response = requests.get(request_url)
    if response.status_code != 200:
        return {
                'status': 'fail',
                'content': 'Cannot fetch articles.',
                'status_code': response.status_code,
                'status_fail_reason': response.reason
                }
    else:
        return {
                'status': 'success',
                'content': response
                }


"""
TODO: Handling of network errors
"""