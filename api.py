from typing import Any
from requests import get as http_get
from requests.exceptions import HTTPError

BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

def get_post_by_id(post_id: int) -> dict[str, Any]:
    try:
        response = http_get(f'{BASE_URL}/{post_id}')
        print(response)
        response.raise_for_status()
        return response.json()
    except HTTPError:
        return None


def get_posts_by_user_id(user_id: int) -> dict[str, Any] | None:
    try:
        response = http_get(f'{BASE_URL}?userId={user_id}')
        response.raise_for_status()
        return response.json()
    except HTTPError:
        return None


def get_post_by_id_with_validation(post_id: int) -> dict[str, Any] | None:
    if post_id <= 0:
        raise ValueError('post_id must be greater than 0')
    try:
        response = http_get(f'{BASE_URL}/{post_id}')
        # print(response)
        # print(response.json()[1]['userId'])
        response.raise_for_status()
        return response.json()
    except HTTPError:
        # print(response.json()[1]['userId'])
        return None
    
    
# get_post_by_id()
# get_posts_by_user_id(None)
# get_posts_by_user_id(-1)

# get_post_by_id_with_validation(-1)

# get_post_by_id_with_validation(0)
