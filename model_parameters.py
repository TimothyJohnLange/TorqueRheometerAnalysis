def parameters():
    from lmfit import Parameters
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
               ('prim_stab_0',   0.7, True,  0.0,  1.0))
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

def parameter_vectors(all_ps):
    from numpy import append
    k1_all = []
    k2_all = []
    k3_all = []
    k4_all = []
    k5_all = []
    k6_all = []
    k7_all = []
    k8_all = []
    k9_all = []
    k10_all = []
    k11_all = []
    UA_all = []
    mu_0_all = []
    q_all = []
    prim_stab_0_all = []
    
    for j in range(len(all_ps)):
        para = unpack_parameters(all_ps[j])
        k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, UA, mu_0, E, q, prim_stab_0 = para
    
        k1_all = append(k1_all, k1)
        k2_all = append(k2_all, k2)
        k3_all = append(k3_all, k3)
        k4_all = append(k4_all, k4)
        k5_all = append(k5_all, k5)
        k6_all = append(k6_all, k6)
        k7_all = append(k7_all, k7)
        k8_all = append(k8_all, k8)
        k9_all = append(k9_all, k9)
        k10_all = append(k10_all, k10)
        k11_all = append(k11_all, k11)
        UA_all = append(UA_all, UA)
        mu_0_all = append(mu_0_all, mu_0)
        q_all = append(q_all, q)
        prim_stab_0_all = append(prim_stab_0_all, prim_stab_0)

    return k1_all, k2_all, k3_all, k4_all, k5_all, k6_all, k7_all, k8_all, k9_all, k10_all, k11_all, UA_all, mu_0_all, q_all, prim_stab_0_all