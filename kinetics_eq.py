# Differential equations describing the kinetics of PVC thermal degradation with primary
# and secondary stabilisers 

def der_HCl(n, k3, HCl, LDH, k4, polymer_active_sites):
	der_HCl = -n*k3*(HCl)*LDH + k4*HCl*polymer_active_sites
	return der_HCl

def der_LDH(n, k3, HCl, LDH):
	der_LDH = -k3*(HCl)*LDH
	return der_LDH

def der_polymer_active_sites(k4, HCl, polymer_active_sites):
	der_polymer_active_sites = -k4*HCl*polymer_active_sites
	return der_polymer_active_sites

def der_radical(k4, HCl, polymer_active_sites, k5, radical, primary_stabiliser, k6):
	der_radical = k4*HCl*polymer_active_sites - k5*radical*primary_stabiliser - k6*radical
	return der_radical

def der_primary_stabiliser(k5, radical, primary_stabiliser):
	der_primary_stabiliser = -k5*radical*primary_stabiliser
	return der_primary_stabiliser

def der_degraded_polymer(k6, radical):
	der_degraded_polymer = k6*radical
	return der_degraded_polymer