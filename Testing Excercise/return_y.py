def return_y(points, x_coord):
    p1 = points[0]
    p2 = points[1]
    # m = (y2 - y1)/(x2 - x1)
    slope = (p2[1] - p1[1])/(p2[0]-p1[0])
    # (y - y1) = m*(x - x1)
    y_coord = slope*(x_coord - p1[0]) + p1[1]

    return y_coord
