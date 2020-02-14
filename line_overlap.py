def line_overlap(x1, x2, x3, x4):
    """Checks if two lines (x1,x2) and (x3,x4) overlap."""

    if x1 > x2:
        return line_overlap(x2, x1, x3, x4)
    if x3 > x4:
        return line_overlap(x1, x2, x4, x3)
        
    return ((x3 >= x1 and x3 < x2) or
            (x1 >= x3 and x1 < x4))