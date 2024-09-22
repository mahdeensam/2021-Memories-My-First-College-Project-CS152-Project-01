'''Mahdeen Ahmed Khan Sameer 
02/14/2022
CS 152 A'''

pi = 1
vi=11
t=0.5
a=-10
pf = pi+(vi*t)+(0.5*a*t**2)
'''Final position, P_f of a thrown object given values of pi, vi, t, and a'''

#print(pf )

def ballistic1(t):
	'''Final position, P_f of a thrown object when given time, t'''
	pf = pi+(vi*t)+(0.5*a*t**2)
	#print(pf )


ballistic1(0.5)
ballistic1(1)

def ballistic1(t):
	'''Final position, P_f of a thrown object when given time, t'''
	pf = pi+(vi*t)+(0.5*a*t**2)
	return pf
y = ballistic1(0.5)
#print("f(0.5) is", y)
y2 = ballistic1(1)
#print("f(1) is", y2)


def ballistic2(pi, v1, a, t):
	'''Final position, P_f of a thrown object when given time, t'''
	pf = pi+(v1*t)+(0.5*a*t**2)
	return pf
ballistic2(1, 11, -10, 0.5)

ballistic2(2, 11, -10, 0.5)

def computeAndOutput(pi, v1, a, t):
	y = ballistic2(pi, v1, a, t)
	fp = open( 'data2.csv', 'a' )
	fp.write( str(t) + "," + str(y) + "\n" )
	fp.close()
	return y
#print (t, ",", y)

def trajectory10(pi, v, a, ti):
	'''10 calls to computeAndOutput in time intervals of 0.1 seconds '''
	for N in range (10):
		y = computeAndOutput(pi, v, a, ti+N*0.1)
		print(ti+N*0.1, ",", y)
				
trajectory10(1, 11, -10, 0.0)
trajectory10(1, 11, -10, 1.0)

def trajectory100(pi, v, a, ti):
	'''10 calls to trajectory10 in increasing time of 1 second'''
	for N in range (10):
		y = trajectory10(pi, v, a, ti+N)

trajectory100(1, 50, -10, 0)

def trajectory1000(pi, v, a, ti):
	'''10 calls to trajectory10 in increasing time of 1 second'''
	for N in range (10):
		y = trajectory100(pi, v, a, ti+N*10)

trajectory1000(1, 50, -10, 0)
