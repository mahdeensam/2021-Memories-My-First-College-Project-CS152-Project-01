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
	return y
#print (t, ",", y)

#Here, we will be using loop which is our extension 08.
#That's how we can write out 1000 points instead of 100. If we code smart, we don't need to write more. We can just loop it down

def trajectory10(pi, v, a, ti):
	'''10 calls to computeAndOutput in time intervals of 0.1 seconds '''
	fp = open(f"data.csv", 'a' )
	
	for N in range (10):
		y = computeAndOutput(pi, v, a, ti+N*0.1)
		fp.write( str(ti+N*0.1) + "," + str(y) + "\n" )
		print(ti+N*0.1, ",", y)
	fp.close()

trajectory10(1, 11, -10, 0.0)
trajectory10(1, 11, -10, 1.0)

