from pytest import raises 
from triangle import Triangle

def test_valid_init():
    triangle = Triangle(base = 5, height = 2)
    assert triangle.base == 5 and triangle.height == 2


def test_negative_base_fail(): 
    with raises(ValueError): 
        Triangle(base = -1, height = 2)


def test_negative_heigh_fail(): 
    with raises(ValueError): 
        Triangle(base =1, height = -2)

def test_invalid_type_str_fail(): 
    with raises(TypeError): 
        Triangle(base ="1", height= 1)

def test_invalid_type_bool_fail(): 
    with raises(TypeError): 
        Triangle(base =1, height= True)

def test_zero_base_fail(): 
    with raises(ValueError): 
        Triangle(base = 0 , height= 1)

def test_zero_height_fail(): 
    with raises(ValueError): 
        Triangle(base = 1 , height= 0)

def test_area_valid():
    t1 = Triangle(2,2)
    assert t1.area == 2

def test_eq_fail():
    t1 = Triangle(1,2)
    t2 = Triangle(3,4)

    assert t1.area != t2.area
    


