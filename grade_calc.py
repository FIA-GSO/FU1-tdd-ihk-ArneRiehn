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