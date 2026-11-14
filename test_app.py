# test_app.py
import pytest
from app import add_numbers, divide_numbers

def test_add():
    assert add_numbers(2, 2) == 4

def test_divide():
    assert divide_numbers(10, 2) == 5

def test_divide_by_zero():
    # This test WILL FAIL because app.py doesn't handle zero division.
    # This is exactly what we want! It will trigger our AI!
    assert divide_numbers(10, 0) == 0 