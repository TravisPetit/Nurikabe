import argparse
from parsing import parse_from_graph_str
from nurikabe import create_nurikabe_instance, print_nurikabe_instance, create_t_graph, create_t_prime_graph


def run(filename, draw_corresponding_vertices, draw_corresponding_edges, draw_blocked_cells, draw_t_graph, draw_t_prime_grah):
    vertices, edges, s, t = parse_from_graph_str(filename)
    I, dim = create_nurikabe_instance(vertices, edges, s, t, draw_corresponding_vertices, draw_corresponding_edges,
            draw_blocked_cells)
    t_graph, dim = create_t_graph(vertices, edges, s, t)
    t_prime_graph = create_t_prime_graph(t_graph, s, t, dim)
    print("Nurikabe instance:")
    print_nurikabe_instance(I, dim)
    if draw_t_graph: 
        print("T graph:")
        print_nurikabe_instance(t_graph, dim)
    if draw_t_prime_grah:
        print("T prime graph:")
        print_nurikabe_instance(t_prime_graph, dim)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-fname", help="Grid graph text file", required=True)
    parser.add_argument("-v", "--vertices", help="Draw corresponding vertices", default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("-e", "--edges", help="Draw corresponding vertices", default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("-b", "--blocked", help="Draw blocked cells", default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("-T", "--tgraph", help="Draw T graph", default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("-Tp", "--tprimegraph", help="Draw T prime graph", default=False,
                        action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    fname = args.fname
    v = args.vertices
    e = args.edges
    b = args.blocked
    tg = args.tgraph
    tpg = args.tprimegraph
    run(fname, v, e, b, tg, tpg)
