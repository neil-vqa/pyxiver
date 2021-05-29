"""
This module contains tests for the pyxiver core_requests
"""

from pyxiver import send_to_arxiv


class TestRequest:
    def test_success_response_from_arxiv(self):
        request_url = 'http://export.arxiv.org/api/query?search_query=ti:"black hole"&max_results=1'
        response = send_to_arxiv(request_url)
        assert response['status'] == 'success'

    def test_fail_response_because_of_broken_url(self):
        # if there are changes to arxiv API endpoint (eg. 'v2' now part of URL)
        request_url = 'http://export.arxiv.org/api/v2/query?search_query=ti:"black hole"&max_results=1'
        response = send_to_arxiv(request_url)
        assert response['status'] == 'fail'

