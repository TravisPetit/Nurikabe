def has_no_neighbor_to_the_right(v, edges):
    x, y = v
    cond1 = (x, y, x + 1, y) in edges
    cond2 = (x + 1, y, x, y) in edges
    return not (cond1 or cond2)


def has_no_neighbor_to_the_left(v, edges):
    x, y = v
    cond1 = (x, y, x - 1, y) in edges
    cond2 = (x - 1, y, x, y) in edges
    return not (cond1 or cond2)


def has_no_neighbor_above(v, edges):
    x, y = v
    cond1 = (x, y + 1, x, y) in edges
    cond2 = (x, y, x, y + 1) in edges
    return not (cond1 or cond2)


def has_no_neighbor_below(v, edges):
    x, y = v
    cond1 = (x, y - 1, x, y) in edges
    cond2 = (x, y, x, y - 1) in edges
    return not (cond1 or cond2)
