# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def der_T(m,Cp,UA,T_inf,T):
	der_T = (UA/(m*Cp))*(T_inf - T)
	return der_T
	
def tau(k1,mu):
	tau = k1*mu
	return tau


