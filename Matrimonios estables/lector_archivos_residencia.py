import sys
import math
E=1 #CANTIDAD DE ESPECIALIDADES

def hospitalsAmount(f,n):	
	for i in range(n):
		f.readline()
	return int(f.readline())

def saveInList(str_to_parse):
	
 s=str_to_parse.split(" ")
 s.pop(0)
 return s

def tableCreator(finput,qlines):
	table=[]
	for i in range(qlines):
		s=saveInList(finput.readline())
		for j in range(len(s)):
			s[j]=int(s[j])
		table.append(s)
	return 	table

def dictionaryCreator(n):
	dic={i+1: None for i in range(n)}
	#for i in range(n):
	#	dic=dic+dict(i)
	return dic


def stableMatching(N,M,matching):
	#while(None in matching.values()):
		for i in range(len(N)):
			for j in range(len(N[i])):

				if N[i][j] not in matching.values():
					matching[i+1]=N[i][j]
				
				elif M[N[i][j]].index((list(matching.values())).index(N[i][j])+1)>M[N[i][j]].index(i+1):
					matching[i]=None
					print(list(matching.values()))
					matching[[M[N[i][j]].index((list(matching.values())).index(N[i][j])+1)]]=N[i][j]
				else:
					continue
				
					
				
		"""
		si h esta libre
			(n,h) se comprometen
		si no
			existe algun (n',h)
		si h prefiere a n sobre n'
			n' se libera
						(n,h) se comprometen		
		si no:
			(n',h) siguen comprometidos"""

s=""
file_name=input("Ingrese el nombre del archivo: ")
with open(file_name + ".txt","r") as f:
	n=int(f.readline())
	HOSPITALS_TAB=tableCreator(f,n)
	m=int(f.readline())
	STUDENTS_TAB=tableCreator(f,m)  
	dict_matching=dictionaryCreator(n)

	stableMatching(STUDENTS_TAB,HOSPITALS_TAB,dict_matching)

	print(dict_matching)
	print(STUDENTS_TAB)
	print(HOSPITALS_TAB)
