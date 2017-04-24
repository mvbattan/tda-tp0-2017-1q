import random
from random import sample

random.seed()

MIN_V = 20
MAX_V = 50
FILE_NAME = "asign-tmp"

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

def generatePreferences(residences):
    n_students = str(residences)
    m_hospitals = str(residences)
    with open(FILE_NAME + ".txt", "w") as f:
        f.write(n_students + '\n')
        randomPreferencePrinter(int(m_hospitals), int(n_students), f)
        f.write(m_hospitals + '\n')
        randomMeritPrinter(int(m_hospitals), int(n_students), f)
        # CANTIDAD DE VACANTES DE CADA HOSP SEPARADAS POR ESPACIOS
        f.write(str(vacantCreator(int(m_hospitals))))
