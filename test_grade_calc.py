import pytest

from grade_calc import calc_percentage

def test_calc_percentage__points_not_int_max_int():
    # Arrange
    points = "A"
    max_points = 100

    # Act
    # Assert
    with pytest.raises(TypeError, match="Points and total must be integers"):
        calc_percentage(points, max_points)

def test_calc_percentage__points_int_max_not_int():
    # Arrange
    points = "A"
    max_points = 100

    # Act
    # Assert
    with pytest.raises(TypeError, match="Points and total must be integers"):
        calc_percentage(points, max_points)

def test_calc_percentage__negative_points_and_max():
    # Arrange
    points = -1
    max_points = -1

    # Act
    # Assert
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
    # Assert
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
    # Assert
    with pytest.raises(ValueError, match="Points cannot be higher than max points"):
        calc_percentage(points, max_points)