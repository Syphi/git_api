import pytest

from ..app.app_flask import app, db
from ..view.view import ITEMS_PER_PAGE


@pytest.yield_fixture(scope="module")
def test_client_app():
    app.testing = True
    test_app = app.test_client()
    yield test_app
    db.session.rollback()


def simple_check_answer(response):
    response_fields = {"id", "full_name", "html_url", "description", "stargazers_count", "language"}

    resp_data = response.json
    assert response.status_code == 200
    assert {"count", "result"}.issubset(resp_data.keys())
    assert isinstance(resp_data["count"], int)
    assert isinstance(resp_data["result"], list)

    if len(resp_data["result"]) != 0:
        for data in resp_data["result"]:
            assert isinstance(data, dict)
            assert response_fields.issubset(data.keys())

    return resp_data


def test_simple(test_client_app):
    response = test_client_app.get('/')
    simple_check_answer(response)


def test_sort_order(test_client_app):
    response_asc = simple_check_answer(test_client_app.get('/?sort_order=asc'))
    response_desc = simple_check_answer(test_client_app.get('/?sort_order=desc'))

    assert response_desc['count'] == response_asc['count']
    assert len(response_desc['result']) == len(response_desc['result'])

    if response_desc['count'] > 1:
        assert response_asc['result'] != response_desc['result']
        assert response_asc['result'][0]['stargazers_count'] \
               < response_asc['result'][-1]['stargazers_count']
        assert response_desc['result'][-1]['stargazers_count'] \
               < response_desc['result'][0]['stargazers_count']

    response_fail = test_client_app.get('/?sort_order=asc_desc')
    assert response_fail.status_code == 400


def test_pagination(test_client_app):
    page_limit = 24
    response_page_limit = simple_check_answer(test_client_app.get(f'/?page_limit={page_limit}'))

    if response_page_limit['count'] >= page_limit:
        assert len(response_page_limit['result']) == page_limit

    response_page_limit_fail = test_client_app.get('/?page_limit=fail')
    assert response_page_limit_fail.status_code == 400

    page_number = 1
    response_page_number = simple_check_answer(test_client_app.get(f'/?page={page_number}'))

    if response_page_number['count'] >= ITEMS_PER_PAGE:
        assert len(response_page_number['result']) == ITEMS_PER_PAGE

    response_page_number_fail = test_client_app.get('/?page=fail')
    assert response_page_number_fail.status_code == 400
