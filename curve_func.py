# stoichiometric matrix

def stoyk():
    from numpy import array
    #reaction kinetics parameters
    n = 10.
    return array([[-n, -1., 0., 0., 0., 0., 0.],
                  [1., 0., -1., 1., 0., 0., 0.],
				  [1., 0., -1., 1., 0., 0., 0.],
				  [0., 0., 0., -1., -1., 0., 0.],
				  [0., 0., 0., -1., 0., 1., 0.],
				  [0., 0., 0., -2., 0., 0., 1.]])

# Function accepting parameters to give the modelled curves

def model_curves(time, k1, k2, k3, k4, k5, k6, k7, k8, x_k9, k10, k11, UA, mu_0, E, q, prim_stab_0):
    from numpy import linspace, array, append, squeeze, zeros
    from scipy.integrate import odeint
    
    # Limiting parameters using logistic function
    from logistic import sigmoid
    k9 = sigmoid(x_k9, 0., 5.)
    
    # temperature curve parameters
    R = 8.314
    	
    # initial concentrations
    HCl_0 = 0.
    LDH_0 = 0.3
    poly_act_0 = 5.
    #prim_stab_0 = 0.5
    
    # initial temperatures
    T_0 = 125.
    Tm_0 = 200.
    
    from rxn_rates import r1, r2, r3, r4, r5, r6
    from visc_torque_eq import mu, torque
    from temp_der import dTdt, dTmdt
    
    # differential equations
    def dXdt(A, time):
        HCl, LDH, poly_act, radical, prim_stab, deg_poly, x_link, T, Tm = A
        
        r = array([r1(k3, HCl, LDH), 
                   r2(k4, HCl, poly_act),
				   r3(k5, poly_act),
				   r4(k6, radical, prim_stab),
				   r5(k7, radical), 
				   r6(k8, radical)])
        return append(squeeze(stoyk().T.dot(r)),
                      [dTdt(T, mu_0, E, UA, k9, deg_poly, k10, x_link, q, k11),
                       dTmdt(T, Tm, k2)]
                      )

    A_0 = array([HCl_0, LDH_0, poly_act_0, 0., prim_stab_0, 0., 0., T_0, Tm_0])
    
    soln = odeint(dXdt, A_0, time)

    HCl = soln[:, 0]
    LDH = soln[:, 1]
    poly_act = soln[:, 2]
    radical = soln[:, 3]
    prim_stab = soln[:, 4]
    deg_poly = soln[:, 5]
    x_link = soln[:, 6]
    T = soln[:, 7]
    Tm = soln[:, 8]

    mu_V = zeros(len(time))
    torque_V = zeros(len(time))

    for i in range(0,len(time)):
        mu_V[i] = mu(mu_0, E, R, T[i], k9, deg_poly[i], k10, x_link[i], q)
        torque_V[i] = torque(k1, mu_V[i])

    return HCl, LDH, poly_act, radical, prim_stab, deg_poly, x_link, T, Tm, mu_V, torque_V

# Function only returning torque curve

def torque_curve(time, k1, k2, k3, k4, k5, k6, k7, k8, x_k9, k10, k11, UA, mu_0, E, q, prim_stab_0):
    curves = model_curves(time, k1, k2, k3, k4, k5, k6, k7, k8, x_k9, k10, k11, UA, mu_0, E, q, prim_stab_0)
    return curves[10]
	
def temp_curve(time, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, UA, mu_0, E, q, prim_stab_0):
    curves = model_curves(time, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, UA, mu_0, E, q, prim_stab_0)
    return curves[8]