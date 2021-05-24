"""
This module contains the primary classes for
building the search query for the arXiv request, and
providing client methods for the arXiv response
"""


import xmltodict
import json


class RequestPapers(object):
    """
    build the search query and send
    """

    BASE_URL = 'http://export.arxiv.org/api/query?'

    def __init__(self, query, max_results, sort_by, sort_order):
        self.query = query
        self.max_results = max_results
        self.sort_by = sort_by
        self.sort_order = sort_order

    def __repr__(self):
        return f'{self.query}'

    def construct_url(self):
        sorting = f'sortBy={self.sort_by}&sortOrder={self.sort_order}'
        query_params = f'search_query=all:{self.query}&max_results={self.max_results}&{sorting}'
        request_url = f'{self.BASE_URL}{query_params}'
        return request_url


class Papers(object):
    """
    parse response and provide interface for client
    """

    def __init__(self, response):
        self.response = response

    @property
    def content(self):
        xml_response = self.response.text
        articles_feed = json.loads(json.dumps(xmltodict.parse(xml_response)))
        articles = articles_feed['feed']['entry']
        return articles


class ApiError(object):
    def __init__(self, response):
        self.error = response

    @property
    def content(self):
        return self.error
