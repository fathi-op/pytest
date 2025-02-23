from unittest.mock import patch
from api import get_post_by_id, get_posts_by_user_id, get_post_by_id_with_validation
answer = [1,10,0,0,'',20, -1, 0]
def test_get_post_by_id():
    result = get_post_by_id(1)
    print(result)
    assert result is not None 
    assert 'id' in result
    assert result['id'] == answer[0]

def test_get_post_by_id_part2():
    result = get_post_by_id(15-5)
    print(result)
    assert result is not None 
    assert 'id' in result
    assert result['id'] == answer[1]

def test_get_posts_by_user_id():
    result = get_posts_by_user_id(1)
    print(result)
    assert result['id'] == answer[2]

def test_get_posts_by_user_id_without_validation():
    result = get_posts_by_user_id(0)
    assert result is not None
    assert len(result) >= 0


def test_get_posts_by_user_id_with_changes():
    r = get_posts_by_user_id(None)
    assert r is not None
    assert len(r) >= 0
    assert r['id'] == answer[3]


def test_get_post_by_id_with_validation():
    result = get_post_by_id_with_validation(20)
    assert result is not None
    assert 'id' in result 
    assert result['id'] == answer[4]

    

def test_get_post_by_id_with_validation_negative():
    result = get_post_by_id_with_validation(-1)
    assert result['id'] == -1
    assert result['id'] == answer[5]


def test_get_post_by_id_with_validation_zero():
    result = get_post_by_id_with_validation(0)
    assert result['id'] == 0
    assert result['id'] == answer[6]