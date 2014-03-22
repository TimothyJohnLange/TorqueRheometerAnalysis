def mu(mu0, E, R, T, k7, deg_poly):
	from math import exp
	mu = mu0*exp(E/(R*T)) + k7*deg_poly
	return mu
	
def torque(k1, mu):
	torque = k1*mu
	return torque