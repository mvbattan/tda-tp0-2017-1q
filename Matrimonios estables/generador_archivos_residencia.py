import random
from random import sample

MIN_V = 20  # CANTIDAD MINIMA DE VACANTES
MAX_V = 50  # CANTIDAD MAXIMA DE VACANTES
random.seed()


def vacantCreator(m_hospitals):
    return " ".join(str(random.randint(MIN_V, MAX_V + 1)) for x in range(m_hospitals))


def write_random_matrix(rows, columns, max, f):
    for i in range(rows):
        f.write(" ".join(str(x) for x in sample(range(1, max + 1), columns)))
        f.write("\n")


def randomPreferencePrinter(m_hospitals, n_students, f):
    write_random_matrix(n_students, m_hospitals, m_hospitals, f)


def randomMeritPrinter(m_hospitals, n_students, f):
    write_random_matrix(m_hospitals, n_students, n_students, f)


file_name = input("Ingrese el nombre del archivo de salida: ")
n_students = input("Ingrese la cantidad de estudiantes: ")
m_hospitals = input("Ingrese la cantidad de hospitales: ")

# file_name = "p2"
# n_students = "20"
# m_hospitals = "90"


with open(file_name + ".txt", "w") as f:
    f.write(n_students + '\n')

    randomPreferencePrinter(int(m_hospitals), int(n_students), f)

    f.write(m_hospitals + '\n')

    randomMeritPrinter(int(m_hospitals), int(n_students), f)

    f.write(str(vacantCreator(int(m_hospitals))))  # CANTIDAD DE VACANTES DE CADA HOSP SEPARADAS POR ESPACIOS
