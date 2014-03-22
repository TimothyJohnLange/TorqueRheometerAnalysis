# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Differential equations describing the temperature behaviour
# of the system

def der_T(m, Cp, UA, T_inf, T):
	der_T = (UA/(m*Cp))*(T_inf - T)
	return der_T
	
def der_Tm(k2, T, Tm):
	der_Tm = k2*(T - Tm)
	return der_Tm



	

