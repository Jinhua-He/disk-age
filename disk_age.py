#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides the function Age(alpha) to calculate evolutionary age of a protoplanetary disk from its infrared (IR) SED slope alpha, according to the work of Liu et al. (2024). 

N.B.: You need to install scipy first.

Please use it in python by 
    import * from disk_age
    
Input: 
    alpha: float or array of float, the IR SED slope alpha; defaults to 0.0. It must be in the range: -2.0 ~ 4.8. Otherwise, the edge value of this range that is closest to the input value will be forced and a warning will be issued.

Output: 
    Age: float or a list of float, the corresponding disk ages (unit: Myr).
"""

from scipy.interpolate import splrep,splint
def Age(alpha=0.0):
    # the best observed histogram of IR SED slope alpha from that paper:
    histo_alpha = [-3.028380897,-2.946254679,-2.864128461,-2.782002244,-2.699876026,-2.617749808,-2.53562359,-2.453497372,-2.371371154,-2.289244937,-2.207118719,-2.124992501,-2.042866283,-1.960740065,-1.878613848,-1.79648763,-1.714361412,-1.632235194,-1.550108976,-1.467982758,-1.385856541,-1.303730323,-1.221604105,-1.139477887,-1.057351669,-0.975225452,-0.893099234,-0.810973016,-0.728846798,-0.64672058,-0.564594362,-0.482468145,-0.400341927,-0.318215709,-0.236089491,-0.153963273,-0.071837056,0.010289162,0.09241538,0.174541598,0.256667816,0.338794034,0.420920251,0.503046469,0.585172687,0.667298905,0.749425123,0.831551341,0.913677558,0.995803776,1.077929994,1.160056212,1.24218243,1.324308647,1.406434865,1.488561083,1.570687301,1.652813519,1.734939737,1.817065954,1.899192172,1.98131839,2.063444608,2.145570826,2.227697043,2.309823261,2.391949479,2.474075697,2.556201915,2.638328133,2.72045435,2.802580568,2.884706786,2.966833004,3.048959222,3.131085439,3.213211657,3.295337875,3.377464093,3.459590311,3.541716529,3.623842746,3.705968964,3.788095182,3.8702214,3.952347618,4.034473836,4.116600053,4.198726271,4.280852489,4.362978707,4.445104925,4.527231142,4.60935736,4.691483578,4.773609796]
    histo_value = [0.002449976,0.004899952,0.015442271,0.100419626,0.030194253,0.06643178,0.079866664,0.08716341,0.067915637,0.056719817,0.082373265,0.089398067,0.053945029,0.060853461,0.044014358,0.06509256,0.16317058,0.101891253,0.125773205,0.219043265,0.432833895,0.449567946,0.544663194,0.886259852,0.989236206,0.862846181,0.783440641,0.583325985,0.538039262,0.555406536,0.344999831,0.262820176,0.260577964,0.19849541,0.168269814,0.165631222,0.201100745,0.192358644,0.186583574,0.141933609,0.161162725,0.08387892,0.117124554,0.126359873,0.147117747,0.098773219,0.137713416,0.111048893,0.125858942,0.057581656,0.067554811,0.078102251,0.075011976,0.043499395,0.048333773,0.054341961,0.036089777,0.072085757,0.080411503,0.019417482,0.030378068,0.025724051,0.018948669,0.02000099,0.000978612,0.037802944,0.003579561,0.004455848,0.003073425,0.019818801,0.001011327,0.0,0.002615764,0.0,0.001073755,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    
    # fit it with a smoothed cubic spline function:
    tck_36 = splrep(histo_alpha,histo_value,k=3,s=0.08) #This is the interpolation function on alpha histogram.
    alpha_max = 4.814672904812319 #The value is the max alpha in alpha histogram.
    
    # evaluate the disk age(s):
    if type(alpha) in [int, float]:
        if alpha<-2: print(f'\n\033[31mWarning! Too small input alpha value ({alpha}) is forced to the allowed lower limit of -2.\033[0m\n')
        elif alpha>4.8: print(f'\n\033[31mWarning! Too large input alpha value ({alpha}) is forced to the allowed upper limit of 4.8.\033[0m\n')
        alpha=min(max(alpha,-2),4.8)
        Age = splint(alpha_max,alpha,tck_36)*2/splint(-0.3,-1.6,tck_36) #
    else:
        Age = []
        for i in alpha:
            if i<-2: print(f'\n\033[31mWarning! Too small input alpha value ({i}) is forced to the allowed lower limit of -2.\033[0m\n')
            elif i>4.8: print(f'\n\033[31mWarning! Too large input alpha value ({i}) is forced to the allowed upper limit of 4.8.\033[0m\n')
            a=min(max(i,-2),4.8)
            Age.append( splint(alpha_max,a,tck_36)*2/splint(-0.3,-1.6,tck_36) )
    return Age
