import pytest
from source import shapes

# Creation of the fixtures using files

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(5, 6)
