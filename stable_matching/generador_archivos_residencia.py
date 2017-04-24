import sys
import math
import random

L=1 #CANTIDAD DE ESPECIALIDADES
MIN_V=20 #CANTIDAD MINIMA DE VACANTES
MAX_V=50 #CANTIDAD MAXIMA DE VACANTES
random.seed()

def orderedPreferenceMaker(m,l):
	q_ordered=[]

	for i in range(int(m)):
		q_ordered.append(str(i+1))
	return q_ordered
	
def arrayDisordering(a):
	i=len(a)
	while i>1 :
		i=i-1
		j=random.randrange(i)
		a[j],a[i] = a[i], a[j]
	return
	
def preferenceDisordering(q):
		arrayDisordering(q)
		return q
		
def preferenceCreator(m,l):
		s=""
		Q = orderedPreferenceMaker(m,l)
		preferenceDisordering(Q)
		for	i in range(int(m)):
			s=s+" "+str(Q[i])	
		return s

def meritCreator(n):
	H=[]
	s=""
	for i in range(int(n)):
		H.append(i+1)
	arrayDisordering(H)
	for i in range(int(n)):
		s=s+" "+str(H[i])
	return s

def _vacantCreator(i,j,m):
	q=[]
	s=""
	for k in range(int(m)):
	 	q.append(random.randint(i,j))
	 	s=s+" "+str(q[k])
	return s	

def vacantCreator(m):
	return _vacantCreator(MIN_V,MAX_V,m)

def randomPreferencePrinter(m,n,f): #IMPRIME m PREFERENCIAS DE HOSPITALES Y ESPECIALIDADES PARA n ALUMNOS
	for i in range(int(n)):
		f.write(str(preferenceCreator(m,L))+'\n') # N RENGLONES CON LAS PREFERENCIAS DE LOS ESTUDIANTES SEPARADAS POR ESPACIOS

def randomMeritPrinter(n,m,f):
	for j in range(int(m)):
		for k in range(L):
			f.write(str(meritCreator(n))+'\n')# M RENGLONES CON EL ORDEN DE MERITO DE CADA HOSP SEPARADO CON ESPACIOS


file_name = sys.argv[1]   #input("Ingrese el nombre del archivo de salida: ")
N = sys.argv[2] #input("Ingrese la cantidad de estudiantes: ")
M = sys.argv[3] #input("Ingrese la cantidad de hospitales: ")
int(N)
int(M)
										
with open(file_name + ".txt","w") as f:

	f.write(N+'\n')
	
	randomPreferencePrinter(M,N,f)
	
	f.write(M+'\n')

	randomMeritPrinter(N,M,f)
	
	f.write(str(vacantCreator(M))) #CANTIDAD DE VACANTES DE CADA HOSP SEPARADAS POR ESPACIOS

