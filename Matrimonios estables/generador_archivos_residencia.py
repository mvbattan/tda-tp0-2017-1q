import random
from random import sample

MIN_V = 20  # CANTIDAD MINIMA DE VACANTES
MAX_V = 50  # CANTIDAD MAXIMA DE VACANTES
random.seed()

def vacantCreator(m_hospitals):
    return " ".join(str(random.randint(MIN_V,MAX_V+1)) for x in range(m_hospitals))


def randomPreferencePrinter(m_hospitals, n_studentes, f):
    for i in range(n_studentes):
        f.write(" ".join(str(x) for x in sample(range(1,m_hospitals+1),m_hospitals)))
        f.write("\n") # N RENGLONES CON LAS PREFERENCIAS DE LOS ESTUDIANTES SEPARADAS POR ESPACIOS


def randomMeritPrinter(m_hospitals, n_students, f):
    for j in range(int(m_hospitals)):
        f.write(" ".join(str(x) for x in sample(range(1, n_students + 1), n_students)))
        f.write("\n")  # N RENGLONES CON LAS PREFERENCIAS DE LOS HOSPITALES SEPARADAS POR ESPACIOS

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
