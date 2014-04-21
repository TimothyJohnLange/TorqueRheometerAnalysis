def parameters():
    from scipy.optimize.lmfit import Parameters
    p = Parameters()
    #          (         Name, Value, Vary,  Min,  Max)    
    p.add_many((         'k1',   2.0, True,  0.0, None),
               (         'k2',   5.0, True,  0.0, None),
               (         'k3',  0.35, True,  0.0, None),
               (         'k4',   0.3, True,  0.0, None),
               (         'k5', 0.001, True,  0.0, None),
               (         'k6',   1.0, True,  0.0, None),
               (         'k7',   0.1, True,  0.0, None),
               (         'k8',  0.05, True,  0.0, None),
               (         'k9',   2.0, True,  0.0, None),
               (        'k10',   2.0, True,  0.0, None),
               (        'k11',   1.0, True,  0.0, None),
               (         'UA', 340.0, True,  0.0, None),
               (       'mu_0',  0.03, True,  0.0, None),
               (          'E',6500.0, True,  0.0, None),
               (          'q',   2.5, True,  0.0, None),
               ('prim_stab_0',   0.7, True,  0.0, None))
    return p

def unpack_parameters(p):
    #unpack parameter values from parameter structure
    k1 = p['k1'].value
    k2 = p['k2'].value
    k3 = p['k3'].value
    k4 = p['k4'].value
    k5 = p['k5'].value
    k6 = p['k6'].value
    k7 = p['k7'].value
    k8 = p['k8'].value
    k9 = p['k9'].value
    k10 = p['k10'].value
    k11 = p['k11'].value
    UA = p['UA'].value
    mu_0 = p['mu_0'].value
    E = p['E'].value
    q = p['q'].value
    prim_stab_0 = p['prim_stab_0'].value
    return k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, UA, mu_0, E, q, prim_stab_0