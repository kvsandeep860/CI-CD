import pytest
def square(n):
    return n**2

def test_square():
    assert square(2) == 4, "Test failed square of 2 should be 4"
    assert square(3) == 9, "Test failed square of 3 should be 9"
    
def test_valid_input():
    with pytest.raises(TypeError):
        square("string")
    