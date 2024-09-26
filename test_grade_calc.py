import pytest

from grade_calc import calc_percentage, get_grade


def test_calc_percentage__points_not_int_max_int():
    # Arrange
    points = "A"
    max_points = 100

    # Act
    with pytest.raises(TypeError, match="Points and total must be integers"):
        calc_percentage(points, max_points)

def test_calc_percentage__points_int_max_not_int():
    # Arrange
    points = "A"
    max_points = 100

    # Act
    with pytest.raises(TypeError, match="Points and total must be integers"):
        calc_percentage(points, max_points)

def test_calc_percentage__negative_points_and_max():
    # Arrange
    points = -1
    max_points = -1

    # Act
    with pytest.raises(ValueError, match="Points and total must be positive values"):
        calc_percentage(points, max_points)

def test_calc_percentage__positive_points_negative_max():
    # Arrange
    points = 1
    max_points = -1

    # Act
    # Assert
    with pytest.raises(ValueError, match="Points and total must be positive values"):
        calc_percentage(points, max_points)

def test_calc_percentage__negative_points_positive_max():
    # Arrange
    points = -1
    max_points = 1

    # Act
    with pytest.raises(ValueError, match="Points and total must be positive values"):
        calc_percentage(points, max_points)

def test_calc_percentage__zero_points_and_max():
    # Arrange
    points = 0
    max_points = 0

    # Act
    result = calc_percentage(points, max_points)

    # Assert
    assert result == 0.0

def test_calc_percentage__zero_points_valid_max():
    # Arrange
    points = 0
    max_points = 100

    # Act
    result = calc_percentage(points, max_points)

    # Assert
    assert result == 0.0

def test_calc_percentage__points_one_lower_than_max():
    # Arrange
    points = 99
    max_points = 100

    # Act
    result = calc_percentage(points, max_points)

    # Assert
    assert result == 99.0

def test_calc_percentage__equal_input():
    # Arrange
    points = 100
    max_points = 100

    # Act
    result = calc_percentage(points, max_points)

    # Assert
    assert result == 100.0

def test_calc_percentage__points_one_greater_than_max():
    # Arrange
    points = 101
    max_points = 100

    # Act
    with pytest.raises(ValueError, match="Points cannot be higher than max points"):
        calc_percentage(points, max_points)


""" 
get_grade Tests 
"""
def test_get_grade__too_many_points():
    # Arrange
    points = 101

    # Act
    with pytest.raises(ValueError, match="Points must be between 0 and 100"):
        get_grade(points)


def test_get_grade__sehr_gut_upper():
    # Arrange
    points = 100

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Sehr gut"

def test_get_grade__sehr_gut_lower():
    # Arrange
    points = 92

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Sehr gut"


def test_get_grade__gut_upper():
    # Arrange
    points = 91

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Gut"


def test_get_grade__gut_lower():
    # Arrange
    points = 81

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Gut"

def test_get_grade__befriedigend_upper():
    # Arrange
    points = 80

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Befriedigend"


def test_get_grade__befriedigend_lower():
    # Arrange
    points = 67

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Befriedigend"

def test_get_grade__ausreichend_upper():
    # Arrange
    points = 66

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Ausreichend"


def test_get_grade__ausreichend_lower():
    # Arrange
    points = 50

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Ausreichend"

def test_get_grade__mangelhaft_upper():
    # Arrange
    points = 49

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Mangelhaft"


def test_get_grade__mangelhaft_lower():
    # Arrange
    points = 30

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Mangelhaft"

def test_get_grade__ungenügend_upper():
    # Arrange
    points = 29

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Ungenügend"


def test_get_grade__ungenügend_lower():
    # Arrange
    points = 0

    # Act
    result = get_grade(points)

    # Assert
    assert result == "Ungenügend"

def test_get_grade__negative_points():
    # Arrange
    points = -1

    # Act
    with pytest.raises(ValueError, match="Points must be between 0 and 100"):
        get_grade(points)

def test_get_grade__points_not_int():
    # Arrange
    points = "A"

    # Act
    with pytest.raises(TypeError, match="Points must be an integer"):
        get_grade(points)