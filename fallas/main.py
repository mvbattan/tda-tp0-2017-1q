import os
from common.graph import create_graph_from_file
from fallas.TarjanAP import TarjanAP

def main():
    g = create_graph_from_file(os.getcwd() + "/fallas/entradas/g4.txt", is_directed = False)
    print(g)

    AP = TarjanAP(g).getArticulationPoints()

    print(AP)
    print(len(AP))

if __name__ == '__main__':
    main()
