"""
This module implements the pyXiver API
"""


from .models import RequestPapers, RequestOnePaper, Papers, OnePaper, ApiError
from .core_requests import send_to_arxiv
from typing import Union


def get_all(
    query: str,
    search_field: str = "all",
    max_results: int = 10,
    sort_by: str = "relevance",
    sort_order: str = "descending",
) -> Union[Papers, ApiError]:

    request = RequestPapers(query, search_field, max_results, sort_by, sort_order)
    request_url = request.construct_url()
    response = send_to_arxiv(request_url)
    if response["status"] == "fail":
        fail_result = ApiError(response)
        return fail_result
    else:
        success_result = Papers(response)
        return success_result


def get_one(paper_url: str) -> Union[OnePaper, ApiError]:
    arxiv_id = arxiv_id_parser(paper_url)
    request = RequestOnePaper(arxiv_id)
    request_url = request.construct_url_for_id()
    response = send_to_arxiv(request_url)
    if response["status"] == "fail":
        fail_result = ApiError(response)
        return fail_result
    else:
        success_result = OnePaper(response)
        return success_result


def arxiv_id_parser(paper_url: str) -> str:
    id_split = paper_url.split("/")
    id = id_split[-1]
    return id
