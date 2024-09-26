def calc_percentage(grade, max_grade):
    if type(grade) != int or type(max_grade) != int:
        raise TypeError("Grade and total must be integers")
    elif grade < 0 or max_grade < 0:
        raise ValueError("Grade and total must be positive values")
    elif grade > max_grade:
        raise ValueError("Grade cannot be higher than max_grade")
    elif max_grade == 0:
        return 0
    else:
        return (grade / max_grade) * 100