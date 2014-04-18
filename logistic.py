# limiting parameters using logistic function with lower and upper limits
def sigmoid(x, lower, upper):
    from math import exp
    return lower + (upper - lower)/(1 + exp(-x))
	
# reverse logistic function to find x given y

def rev_sigmoid(y, lower, upper):
    from math import log
    from math import e
    return log(1/((upper - lower)/(y - lower) - 1))	