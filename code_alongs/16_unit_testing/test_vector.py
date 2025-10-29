from pytest import raises
from vector import Vector

def test_valid_init():
    v = Vector(1, 2, 3)
    assert v.numbers == (1, 2, 3)


def test_invalid_init():
    with raises(TypeError):
        Vector(1, 2, "3")

    with raises(ValueError):
        Vector()

def test_negative_valid_int(): 
    v = Vector(-1,-2)
    assert v.numbers == (-1,-2)

def test_str_value_fails(): 
    with raises(TypeError):
        Vector(1,"3")



def test_addition():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    result = v1 + v2
    assert result.numbers == (5, 7, 9)

    with raises(TypeError):
        v1 + "not a vector"

def test_subtraction():
    v1 = Vector(4, 5, 6)
    v2 = Vector(1, 2, 3)
    result = v1 - v2
    assert result.numbers == (3, 3, 3)

    with raises(TypeError):
        v1 - "not a vector"

def test_multiplication():
    v = Vector(1, 2, 3)
    result = v * 2
    assert result.numbers == (2, 4, 6)

    with raises(TypeError):
        v * "not a number"

    # Test commutative property
    result_rmul = 2 * v
    assert result_rmul.numbers == (2, 4, 6)

def test_length():
    v = Vector(1, 2, 3)
    assert len(v) == 3

def test_abs():
    v = Vector(3, 4)
    assert abs(v) == 5.0  # Euclidean norm: sqrt(3^2 + 4^2) = 5

def test_validate_vectors():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert v1.validate_vectors(v2) is True

    v3 = Vector(1, 2, 3)
    with raises(TypeError):
        v1.validate_vectors(v3)

    with raises(TypeError):
        v1.validate_vectors("not a vector")

    
def test_getitem():
    v = Vector(1, 2, 3)
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3

    with raises(IndexError):
        _ = v[3]  # Out of bounds access

def test_plot():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = Vector(5, 6)

    # This test is more about ensuring no exceptions are raised
    # since we cannot visually verify the plot in a unit test.
    v1.plot(v2, v3)

    # If you want to check if the method runs without error:
    assert True  # Placeholder for successful execution


## TODO: for reader - add more tests


