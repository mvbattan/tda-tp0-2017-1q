import sys
import time
from comunidades import main as comunidades
from fallas import main as fallas
from asignaciones import main as asignaciones

USAGE = '''
Instrucciones de uso:
        -ar <n>     Ejecuta el problema de Asignación de Residencias con n estudiantes y hospitales
        -pf <n>     Ejecuta el problema de Puntos de Falla utilizando el archivo g<n>.txt provisto por el curso
                    0 < n < 7
        -cr <n>     Ejecuta el problema de Comunidades en Redes utilizando el archivo g<n>.txt provisto por el curso
                    0 < n < 7
        '''


def main(argc, argv):
    print("-------TDA TP1-------")
    if argc <= 2:
        print(USAGE)
        return

    ej, n = argv[1], int(argv[2])

    if ej == "-ar":
        print("Asignación de Residencias")
        return measure_time(asignaciones.main, n)

    if not 0 < n < 7:
        print("n debe ser un número entre 1 y 6 inclusive")
        return

    if ej == "-pf":
        print("Puntos de Falla")
        return measure_time(fallas.main,n)

    if ej == "-cr":
        print("Comunidades en Redes")
        return measure_time(comunidades.main,n)

def measure_time(f,n):
    start = time.perf_counter()
    f(n)
    end = time.perf_counter()
    print("Tiempo de ejecución:     {:.5f} segundos".format(end - start))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
