import sys
import math
E=1 #CANTIDAD DE ESPECIALIDADES

tentative_engagements=[]
free_students=[]

def hospitalsAmount(f,n):
	for i in range(n):
		f.readline()
	return int(f.readline())

def saveInList(str_to_parse):

 s=str_to_parse.split(" ")
 return s

def tableCreator(finput,qlines):
	table=[]
	for i in range(qlines):
		s=saveInList(finput.readline())
		for j in range(len(s)):
			s[j]=int(s[j])
		table.append(s)
	return 	table

def beginMatching(student,prefered_by_students,prefered_by_hospitals):

	for hospital in prefered_by_students[student-1]:

		taken_match=[couple for couple in tentative_engagements if hospital == couple[1]]

		if (len(taken_match)==0):
			tentative_engagements.append([student, hospital])
			free_students.remove(student)
			break
		else:
			current_student=prefered_by_hospitals[hospital-1].index(taken_match[0][0])
			potential_student=prefered_by_hospitals[hospital-1].index(student)

			if(current_student < potential_student):
				free_students.remove(student)
				free_students.append(taken_match[0][0])
				taken_match[0][0]=student
				break

def initFreeStudents(stu_list):
	for student in range(len(stu_list)):
		free_students.append(student+1)

def stableMatching(prefered_by_students,prefered_by_hospitals):
	while(free_students):
		beginMatching(free_students[0],prefered_by_students,prefered_by_hospitals)

file_name=input("Ingrese el nombre del archivo: ")
with open(file_name + ".txt","r") as f:
	n=int(f.readline())
	PREFERED_BY_HOSPITALS=tableCreator(f,n)
	m=int(f.readline())
	PREFERED_BY_STUDENTS=tableCreator(f,m)
	initFreeStudents(PREFERED_BY_STUDENTS)
	stableMatching(PREFERED_BY_STUDENTS,PREFERED_BY_HOSPITALS)
	print("tentative_engagements")
	print(tentative_engagements)
