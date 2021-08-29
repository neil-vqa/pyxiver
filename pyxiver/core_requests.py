"""
This module contains the requests to arxiv and handle responses
"""


import requests
from typing import Dict, Union
from requests.models import Response


def send_to_arxiv(request_url: str) -> Dict[str, Union[str, int, Response]]:
    response = requests.get(request_url)
    if response.status_code != 200:
        return {
            "status": "fail",
            "content": "Cannot fetch articles.",
            "status_code": response.status_code,
            "status_fail_reason": response.reason,
        }
    else:
        return {"status": "success", "content": response}


"""
TODO: Handling of network errors
"""
