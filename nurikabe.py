from graph import has_no_neighbor_to_the_right, has_no_neighbor_to_the_left, has_no_neighbor_below, \
    has_no_neighbor_above


def print_nurikabe_instance(nurikabe_grid, dim):
    border_horiz = "+" + ("-" * dim) + "+\n"
    string = border_horiz
    for y in range(dim - 1, -1, -1):
        string += "|"
        for x in range(dim):
            string += nurikabe_grid[(x, y)]
        string += "|\n"

    string += border_horiz
    print(string)


def corresponding_vertex(v):
    x, y = v
    return 4 * (x + 1), 4 * (y + 1)


def insert_corresponding_vertex(nurikabe_grid, v):
    vp = corresponding_vertex(v)
    nurikabe_grid[vp] = "X"


def insert_s_label(nurikabe_grid, s):
    sp = corresponding_vertex(s)
    nurikabe_grid[sp] = "s"


def insert_t_label(nurikabe_grid, t):
    tp = corresponding_vertex(t)
    nurikabe_grid[tp] = "t"


def insert_left_blockade(nurikabe_grid, v):
    x, y = corresponding_vertex(v)
    nurikabe_grid[(x - 2, y)] = "1"


def insert_right_blockade(nurikabe_grid, v):
    x, y = corresponding_vertex(v)
    nurikabe_grid[(x + 2, y)] = "1"


def insert_bottom_blockade(nurikabe_grid, v):
    x, y = corresponding_vertex(v)
    nurikabe_grid[(x, y - 2)] = "1"


def insert_top_blockade(nurikabe_grid, v):
    x, y = corresponding_vertex(v)
    nurikabe_grid[(x, y + 2)] = "1"


def insert_horizontal_bridge(nurikabe_grid, e):
    x, y, _, b = e
    if b == y + 1:
        v = (x, y)
    else:
        v = (x, b)

    xp, yp = corresponding_vertex(v)
    nurikabe_grid[(xp - 2, yp + 2)] = "1"
    nurikabe_grid[(xp + 2, yp + 2)] = "1"


def insert_vertical_bridge(nurikabe_grid, e):
    x, y, a, _ = e
    if x == a + 1:
        v = (a, y)
    else:
        v = (x, y)

    xp, yp = corresponding_vertex(v)
    nurikabe_grid[(xp + 2, yp - 2)] = "1"
    nurikabe_grid[(xp + 2, yp + 2)] = "1"


def insert_corresponding_edge(nurikabe_grid, e):
    x, y, x2, y2 = e
    if x == x2:
        if y == y2 + 1:
            v = (x, y2)
        else:
            v = (x, y)
        xp, yp = corresponding_vertex(v)
        nurikabe_grid[(xp, yp + 1)] = "|"
        nurikabe_grid[(xp, yp + 2)] = "|"
        nurikabe_grid[(xp, yp + 3)] = "|"
    else:
        if x == x2 + 1:
            v = (x2, y)
        else:
            v = (x, y)
        xp, yp = corresponding_vertex(v)
        nurikabe_grid[(xp + 1, yp)] = "-"
        nurikabe_grid[(xp + 2, yp)] = "-"
        nurikabe_grid[(xp + 3, yp)] = "-"


def create_nurikabe_instance(grid_vertices, grid_edges, s, t,
                             draw_corresponding_vertices=False, draw_corresponding_edges=False,
                             draw_blocked_cells=False):
    xmax = max(grid_vertices, key=lambda x: x[0])[0]
    ymax = max(grid_vertices, key=lambda x: x[1])[1]
    dim = (max((xmax, ymax)) + 1) * 4 + 8

    nurikabe_grid = {(x, y): " " for x in range(dim) for y in range(dim)}
    for v in grid_vertices:
        if draw_corresponding_vertices:
            insert_corresponding_vertex(nurikabe_grid, v)

        if has_no_neighbor_to_the_right(v, grid_edges):
            insert_right_blockade(nurikabe_grid, v)

        if has_no_neighbor_to_the_left(v, grid_edges):
            insert_left_blockade(nurikabe_grid, v)

        if has_no_neighbor_above(v, grid_edges):
            insert_top_blockade(nurikabe_grid, v)

        if has_no_neighbor_below(v, grid_edges):
            insert_bottom_blockade(nurikabe_grid, v)

    for e in grid_edges:
        x, y, x2, y2 = e
        if draw_corresponding_edges:
            insert_corresponding_edge(nurikabe_grid, e)

        if x == x2:
            insert_horizontal_bridge(nurikabe_grid, e)
            pass

        else:
            insert_vertical_bridge(nurikabe_grid, e)

    if draw_blocked_cells:
        for x in range(dim):
            for y in range(dim):
                if nurikabe_grid[(x, y)] == "1":
                    nurikabe_grid[(x + 1, y)] = "."
                    nurikabe_grid[(x - 1, y)] = "."
                    nurikabe_grid[(x, y + 1)] = "."
                    nurikabe_grid[(x, y - 1)] = "."

    insert_s_label(nurikabe_grid, s)
    insert_t_label(nurikabe_grid, t)
    return nurikabe_grid, dim
