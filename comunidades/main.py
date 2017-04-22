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
    #assert str(SCC) == "{1: [6, 11, 14, 20, 27, 31, 33, 38, 40, 44, 59, 60, 64, 66, 70, 73, 79, 86, 95], 2: [12, 28, 30, 52, 53, 54, 76, 78, 80, 81, 97], 3: [2, 7, 23, 47, 51, 62, 67, 72, 91], 4: [0, 9, 18, 29, 32, 37, 43, 45, 50, 55, 57, 58, 61, 69, 75, 90, 96], 5: [10, 26, 35, 39, 46, 68, 84, 93], 6: [1, 8, 16, 17, 19, 21, 48, 71, 82, 83, 87, 88, 94], 7: [3, 13, 15, 25, 34, 36, 41, 42, 49, 56, 63, 65, 89, 99], 8: [4, 5, 22, 24, 74, 77, 85, 92, 98]}"

if __name__ == "__main__":
    # execute only if run as a script
    main()