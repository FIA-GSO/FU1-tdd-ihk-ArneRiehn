def calc_percentage(points, max_points):
    if type(points) != int or type(max_points) != int:
        raise TypeError("Points and total must be integers")
    elif points < 0 or max_points < 0:
        raise ValueError("Points and total must be positive values")
    elif points > max_points:
        raise ValueError("Points cannot be higher than max points")
    elif max_points == 0:
        return 0
    else:
        return (points / max_points) * 100

def get_grade(points):
    if type(points) != int:
        raise TypeError("Points must be an integer")

    if points < 0 or points > 100:
        raise ValueError("Points must be between 0 and 100")
    elif points >= 92:
        return "Sehr gut"
    elif points >= 81:
        return "Gut"
    elif points >= 67:
        return "Befriedigend"
    elif points >= 50:
        return "Ausreichend"
    elif points >= 30:
        return "Mangelhaft"
    else:
        return "Ungenügend"
