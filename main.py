import argparse
from parsing import parse_from_graph_str
from nurikabe import create_nurikabe_instance, print_nurikabe_instance


def run(filename, draw_corresponding_vertices, draw_corresponding_edges, draw_blocked_cells):
    vertices, edges, s, t = parse_from_graph_str(filename)
    I, dim = create_nurikabe_instance(vertices, edges, s, t, draw_corresponding_vertices, draw_corresponding_edges,
                                      draw_blocked_cells)
    print_nurikabe_instance(I, dim)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-fname", help="Grid graph text file", required=True)
    parser.add_argument("-v", "--vertices", help="Draw corresponding vertices", default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("-e", "--edges", help="Draw corresponding vertices", default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("-b", "--blocked", help="Draw blocked cells", default=False,
                        action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    fname = args.fname
    v = args.vertices
    e = args.edges
    b = args.blocked
    run(fname, v, e, b)
