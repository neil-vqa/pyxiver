"""
This module implements the pyXiver API
"""


from .models import RequestPapers, RequestOnePaper, Papers, OnePaper, ApiError
from .core_requests import send_to_arxiv


def get_all(query, search_field="all", max_results=10, sort_by='relevance', sort_order='descending'):
    """
    Fetches articles in all fields that can be searched (https://arxiv.org/help/api/user-manual#query_details)
    :param query: Query string for the arXiv search_query param
    :param search_field: Search fields available (ti: title), (au: author), (all: all fields - default)
    :param max_results: Count of articles to be returned
    :param sort_by: Sort by "relevance", "lastUpdatedDate", "submittedDate"
    :param sort_order: Order by "ascending" or "descending"
    :return: Dictionary constructed by Papers class or an error message
    """

    request = RequestPapers(query, search_field, max_results, sort_by, sort_order)
    request_url = request.construct_url()
    response = send_to_arxiv(request_url)
    if response['status'] == 'fail':
        result = ApiError(response)
        return result
    else:
        result = Papers(response)
        return result


def get_one(paper_url):
    """
    Fetches a single article using arXiv id_list param
    :param paper_url: url that is designated as "id" in the get_all() response
    :return: Dictionary constructed by OnePaper class or an error message
    """

    arxiv_id = arxiv_id_parser(paper_url)
    request = RequestOnePaper(arxiv_id)
    request_url = request.construct_url_for_id()
    response = send_to_arxiv(request_url)
    if response['status'] == 'fail':
        result = ApiError(response)
        return result
    else:
        result = OnePaper(response)
        return result


def arxiv_id_parser(paper_url):
    id_split = paper_url.split("/")
    id = id_split[-1]
    return id
