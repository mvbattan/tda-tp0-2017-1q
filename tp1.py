import sys
from comunidades import main as comunidades
from fallas import main as fallas
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

    if not 0 < n < 7:
        print("n debe ser un número entre 1 y 6 inclusive")
        return

    if ej == "-ar":
        print("Asignación de Residencias")
        return

    if ej == "-pf":
        print("Puntos de Falla")
        return fallas.main(n)

    if ej == "-cr":
        print("Comunidades en Redes")
        return comunidades.main(n)


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)