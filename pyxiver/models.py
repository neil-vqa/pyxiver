"""
This module contains the primary classes for
building the search query for the arXiv request, and
providing client methods for the arXiv response
"""


import xmltodict
import json


class RequestPapers(object):
    """
    build the search query for multiple papers
    """

    BASE_URL = 'http://export.arxiv.org/api/query?'

    def __init__(self, query, search_field, max_results, sort_by, sort_order):
        self.query = query
        self.max_results = max_results
        self.search_field = search_field
        self.sort_by = sort_by
        self.sort_order = sort_order

    def __repr__(self):
        return f'{self.query}'

    def construct_url(self):
        sorting = f'sortBy={self.sort_by}&sortOrder={self.sort_order}'
        query_params = f'search_query={self.search_field}:{self.query}&max_results={self.max_results}&{sorting}'
        request_url = f'{self.BASE_URL}{query_params}'
        return request_url


class RequestOnePaper(object):
    """
    build query for a single paper
    """

    BASE_URL = 'http://export.arxiv.org/api/query?'

    def __init__(self, arxiv_id):
        self.arxiv_id = arxiv_id

    def construct_url_for_id(self):
        query_params = f'id_list={self.arxiv_id}'
        request_url = f'{self.BASE_URL}{query_params}'
        return request_url


class Papers(object):
    """
    parse response and provide interface for client
    """

    def __init__(self, response):
        self.response = response['content']

    @property
    def verbose(self):
        articles_list = self.__list_parser()
        return articles_list

    @property
    def minimal(self):
        articles_list = self.__list_parser()
        minimal_list = [{'title': article['title'],
                         'summary': article['summary'],
                         'id': article['id'],
                         'category': article['arxiv:primary_category']['@term']} for article in articles_list]
        return minimal_list

    def __list_parser(self):
        xml_response = self.response.text
        articles_feed = json.loads(json.dumps(xmltodict.parse(xml_response)))
        articles = articles_feed['feed']['entry']
        return articles


class OnePaper(object):
    """
    parse response and provide interface for client
    """

    def __init__(self, response):
        self.response = response['content']

    @property
    def verbose(self):
        article = self.__content_parser()
        return article

    @property
    def minimal(self):
        full_article = self.__content_parser()
        minimal = {
            'title': full_article['title'],
            'author': full_article['author'],
            'published': full_article['published'],
            'summary': full_article['summary']
        }
        return minimal

    def __content_parser(self):
        xml_response = self.response.text
        article_dict = json.loads(json.dumps(xmltodict.parse(xml_response)))
        article = article_dict['feed']['entry']
        return article


class ApiError(object):
    def __init__(self, response):
        self.error = response

    @property
    def verbose(self):
        return self.error

    @property
    def minimal(self):
        return {
            'status': 'fail',
            'status_code': self.error['status_code'],
        }
