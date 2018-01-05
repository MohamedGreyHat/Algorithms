# Interlude : nombres parfaits et nombres chanceux
from math import sqrt

def div_propre(n):
	if n<1:
		raise ValueError('Invalid Value')
	list=[]
	if n==1 : 
		list.append(1)
	for i in range(1,n):
		if n%i==0:
			list.append(i)
	return list
	
def som_div(n):
	return sum(div_propre(n))
	
def is_perfect(n):
	return n==som_div(n) 

def is_prime(n):
	div=2
	while div<=(n/2):
		if n % div==0:
			return False
		div+=1
	return True
"""	
def est_chanceux(n,a):
	l=filter(is_prime,)	
"""

def solutionEquationTrinome(a,b,c):
	delta=b*b -(4*a*c)
	if delta<0:
		return (0)
		
	elif delta==0:
		x=-b/(2.0*a)
		return (1,x)
	else:
		x1=(-b-sqrt(delta))/(2*a)
		x2=(-b+sqrt(delta))/(2*a)
		return (2,x1,x2)

#print solutionEquationTrinome(1,2,-3)


		
