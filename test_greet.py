# test_greet.py
from greet import greet

def test_greet():
    result = greet()
    assert "GitHub API status" in result
