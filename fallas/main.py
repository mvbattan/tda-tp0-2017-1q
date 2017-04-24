import os
from common.graph import create_graph_from_file
from fallas.TarjanAP import TarjanAP

def main(n):
    g = create_graph_from_file(os.getcwd() + "/fallas/entradas/g{}.txt".format(n), is_directed = False)
    AP = TarjanAP(g).getArticulationPoints()

    print(AP)
    print(len(AP))

if __name__ == '__main__':
    main(2)
