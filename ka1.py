#def enumerate_1(n):
#    a = []
#    for i in range(1,7):
#        for j in range(1,7):
#	         dice = (i,j)
#	         a.append(dice)
#    return a

def enumerate_1(n):
	dice = range(1,7)
	result_set = [x for x in range(1,7)]
	if n > 1: result_set = enumerate_1a(n - 1, result_set)
	return result_set

def enumerate_1a(n, l):
	dice = range(1,7)
	result_set = [[x, y] for x in dice for y in l]
	#for x,y in dice, l: y.append(x)
	if n > 1: result_set = enumerate_1a(n - 1, result_set)
	return result_set

		
		

