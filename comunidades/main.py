import os
from common.graph import create_graph_from_file
from comunidades.KosarajuSCC import KosarajuSCC

def main(n):
    g = create_graph_from_file(os.getcwd()+"/comunidades/entradas/d{}.txt".format(n))
    SCC = KosarajuSCC(g)

    print(SCC)
    print("Hay {} Componentes Fuertemente Conexas".format(SCC.count()))

if __name__ == "__main__":
    main(2)
