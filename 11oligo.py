# Function for melting temperature of Oligos


def temp_oligo(a, t, g, c):											# naming the fun and variables
	if a+t+g+c <= 13: print('Melting temp is', (a+t)*2 + (g+c)*4)   # if oligo is smaller or equal than 13 nt
	else: print('Melting temp is', 64.9 + 41*(g+c-16.4)/(a+c+t+g))  # if biggir than 13

temp_oligo(211,322,222,333) 										# calling the function
temp_oligo(2,3,4,1)
temp_oligo(2,3,3,3)
temp_oligo(12,23,14,11)