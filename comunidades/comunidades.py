import os
from common.graph import Digraph
from common.graph import create_graph_from_file


def main():
    g = create_graph_from_file(os.getcwd()+"/comunidades/entradas/d2.txt")
    print(g)
    print(g.adj_list(6))


if __name__ == "__main__":
    # execute only if run as a script
    main()