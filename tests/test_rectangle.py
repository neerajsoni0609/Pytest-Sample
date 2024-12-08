import pytest
from source import shapes

# Implementation of pytest fixtures

# my_rectangle value fetched from conftest
def test_area(my_rectangle):
    
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    
    assert my_rectangle.perimeter() == (10 + 20) * 2

def test_not_equal(my_rectangle, other_rectangle):
    
    assert my_rectangle != other_rectangle