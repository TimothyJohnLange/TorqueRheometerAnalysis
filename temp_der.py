# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def der_T(m,Cp,UA,T_inf,T):
	der_T = (UA/(m*Cp))*(T_inf - T)
	return der_T
	
def der_Tm(k2,T,Tm):
	der_Tm = k2*(T - Tm)
	return der_Tm

def mu(mu0,E,R,T):
	from math import exp
	mu = mu0*exp(E/(R*T))
	return mu
	
def torque(k1,mu):
	torque = k1*mu
	return torque

	

