import os
from common.graph import create_graph_from_file
from comunidades.KosarajuSCC import KosarajuSCC

def main():
    g = create_graph_from_file(os.getcwd()+"/comunidades/entradas/d4.txt")
    print(g)
    print(g.adj_list(6))

    SCC = KosarajuSCC(g)
    print(SCC)
    print(SCC.count())

if __name__ == "__main__":
    main()
