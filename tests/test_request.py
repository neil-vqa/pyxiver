"""
This module contains tests for the pyxiver core_requests
"""

from pyxiver import send_to_arxiv, get_all, Papers, get_one, OnePaper


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


class TestAPI:
    def test_success_get_all(self):
        result = get_all('black hole', search_field="ti", max_results=2)
        assert isinstance(result, Papers)

    def test_success_get_one(self):
        result = get_one('http://arxiv.org/abs/2106.05901v1')
        assert isinstance(result, OnePaper)
