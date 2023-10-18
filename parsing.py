def parse_from_graph_str(filename):
    with open(filename, "r") as f:
        l = list(map(lambda line: line.rstrip(), f.readlines()))

    vertices = set()
    edges = set()
    s = None
    t = None
    for line_number, line in enumerate(reversed(l)):
        for character_number, character in enumerate(line):
            x, y = character_number // 2, line_number // 2
            match character:
                case "X":
                    vertices.add((x, y))
                case "s":
                    vertices.add((x, y))
                    s = (x, y)
                case "t":
                    vertices.add((x, y))
                    t = (x, y)
                case "-":
                    edges.add((x, y, x + 1, y))
                case "|":
                    edges.add((x, y, x, y + 1))
                case " ":
                    continue
                case _:
                    raise Exception
    return vertices, edges, s, t


def print_parsed_graph(vertices, edges, s, t):
    xmax = max(vertices, key=lambda x: x[0])[0] * 2
    ymax = max(vertices, key=lambda x: x[1])[1] * 2

    grid_str = {(x, y): " " for x in range(xmax + 1) for y in range(ymax + 1)}

    for (x, y) in vertices:
        grid_str[(x * 2, y * 2)] = "X"
    grid_str[(s[0] * 2, s[1] * 2)] = "s"
    grid_str[(t[0] * 2, t[1] * 2)] = "t"

    for (x, y, x2, y2) in edges:
        if x == x2:
            grid_str[2 * x, 2 * y + 1] = "|"
        else:
            grid_str[2 * x + 1, 2 * y] = "-"

    string = ""
    for y in range(ymax, -1, -1):
        for x in range(xmax + 1):
            string += grid_str[(x, y)]
        string += "\n"
    print(string)
