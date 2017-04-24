import sys
import math

E = 1  # CANTIDAD DE ESPECIALIDADES

tentative_engagements = []
free_students = []


def hospitalsAmount(f, n):
    for i in range(n):
        f.readline()
    return int(f.readline())

def tableCreator(finput, qlines):
    table = []
    for i in range(qlines):
        s = finput.readline().split(" ")
        for j in range(len(s)):
            s[j] = int(s[j])
        table.append(s)
    return table


def dictionaryCreator(n):
    dic = {i + 1: None for i in range(n)}
    return dic


def beginMatching(student, prefered_by_students, prefered_by_hospitals):
    for hospital in prefered_by_students[student - 1]:

        print("for")
        taken_match = [couple for couple in tentative_engagements if hospital in couple]
        if (len(taken_match) == 0):
            print("primer if")
            tentative_engagements.append([student, hospital])
            free_students.remove(student)
            break
        elif (len(taken_match) > 0):
            print("elif")

            current_student = prefered_by_hospitals[hospital - 1].index(taken_match[0][0])
            potential_student = prefered_by_hospitals[hospital - 1].index(student)

            if (current_student > potential_student):
                print("if del elif")
                print(free_students)
                free_students.remove(student)
                print(free_students)
                free_students.append(taken_match[0][0])
                print(free_students)
                taken_match[0][0] = student
                break


def initFreeStudents(stu_list):
    for student in range(len(stu_list)):
        free_students.append(student + 1)


def stableMatching(prefered_by_students, prefered_by_hospitals, matching):
    while (len(free_students) > 0):
        print("while")

        for student in free_students:
            beginMatching(student, prefered_by_students, prefered_by_hospitals)


# file_name = input("Ingrese el nombre del archivo: ")
with open("p2.txt", "r") as f:
    n = int(f.readline())
    PREFERED_BY_HOSPITALS = tableCreator(f, n)
    m = int(f.readline())
    PREFERED_BY_STUDENTS = tableCreator(f, m)
    dict_matching = dictionaryCreator(n)
    initFreeStudents(PREFERED_BY_STUDENTS)
    stableMatching(PREFERED_BY_STUDENTS, PREFERED_BY_HOSPITALS, dict_matching)
    print("tentative_engagements")
    print(tentative_engagements)
    print(PREFERED_BY_STUDENTS)
    print(PREFERED_BY_HOSPITALS)
