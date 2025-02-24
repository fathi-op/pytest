import pytest
from api import get_post_by_id, get_posts_by_user_id,get_post_by_id_with_validation

from requests.exceptions import HTTPError


def test_get_post_by_id_1(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'id': 1, 'title': 'Test Post 1'}
    mocker.patch('api.http_get', return_value=mock_response)
    assert get_post_by_id(1) == {'id': 1, 'title': 'Test Post 1'}


def test_get_post_by_id_2(mocker):
    mocker.patch('api.http_get', side_effect=HTTPError('HTTP Error'))
    assert get_post_by_id(1) is None


def test_get_posts_by_user_id(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = [{'id': 1, 'userId': 1, 'title': 'User 1 Post 1'}]
    mocker.patch('api.http_get', return_value=mock_response)
    assert get_posts_by_user_id(1) == [{'id': 1, 'userId': 1, 'title': 'User 1 Post 1'}]


def test_get_posts_by_user_id_http(mocker):
    mocker.patch('api.http_get', side_effect=HTTPError('HTTP Error'))
    assert get_posts_by_user_id(1) is None


def test_get_post_by_id_with_validation_1(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'id': 1, 'title': 'Valid Post'}
    mocker.patch('api.http_get', return_value=mock_response)
    assert get_post_by_id_with_validation(1) == {'id': 1, 'title': 'Valid Post'}


def test_get_post_by_id_with_validation_no_connect(mocker):
    mocker.patch('api.http_get', side_effect=HTTPError('HTTP Error'))
    assert get_post_by_id_with_validation(1) is None


def test_get_post_by_id_with_validation_invalid_post_id():
    with pytest.raises(ValueError, match='post_id must be greater than 0'):
        get_post_by_id_with_validation(-1)