import pytest

from grade_calc import calc_percentage

def test_calc_percentage__grade_string_max_int():
    # Arrange
    grade = "A"
    max_grade = 100

    # Act
    # Assert
    with pytest.raises(TypeError, match="Grade and total must be integers"):
        calc_percentage(grade, max_grade)

def test_calc_percentage__grade_int_max_string():
    # Arrange
    grade = "A"
    max_grade = 100

    # Act
    # Assert
    with pytest.raises(TypeError, match="Grade and total must be integers"):
        calc_percentage(grade, max_grade)

def test_calc_percentage__negative_grade_and_max():
    # Arrange
    grade = -1
    max_grade = -1

    # Act
    # Assert
    with pytest.raises(ValueError, match="Grade and total must be positive values"):
        calc_percentage(grade, max_grade)

def test_calc_percentage__positive_grade_negative_max():
    # Arrange
    grade = 1
    max_grade = -1

    # Act
    # Assert
    with pytest.raises(ValueError, match="Grade and total must be positive values"):
        calc_percentage(grade, max_grade)

def test_calc_percentage__negative_grade_positive_max():
    # Arrange
    grade = -1
    max_grade = 1

    # Act
    # Assert
    with pytest.raises(ValueError, match="Grade and total must be positive values"):
        calc_percentage(grade, max_grade)

def test_calc_percentage__zero_grade_and_max():
    # Arrange
    grade = 0
    max_grade = 0

    # Act
    result = calc_percentage(grade, max_grade)

    # Assert
    assert result == 0

def test_calc_percentage__zero_grade_valid_max():
    # Arrange
    grade = 0
    max_grade = 100

    # Act
    result = calc_percentage(grade, max_grade)

    # Assert
    assert result == 0

def test_calc_percentage__grade_one_lower_than_max():
    # Arrange
    grade = 99
    max_grade = 100

    # Act
    result = calc_percentage(grade, max_grade)

    # Assert
    assert result == 99

def test_calc_percentage__equal_input():
    # Arrange
    grade = 100
    max_grade = 100

    # Act
    result = calc_percentage(grade, max_grade)

    # Assert
    assert result == 100

def test_calc_percentage__grade_one_greater_than_max():
    # Arrange
    grade = 101
    max_grade = 100

    # Act
    # Assert
    with pytest.raises(ValueError, match="Grade cannot be higher than max_grade"):
        calc_percentage(grade, max_grade)