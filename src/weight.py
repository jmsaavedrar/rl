import numpy as np
from model import LinearModel

def random_weights():
    return np.random.randn(LinearModel.weight_count)
    


def get_initial_weight_bipedal_walker():
    return [ -7.53555448e+00,   1.12665018e+01,   1.02132295e+01,
         2.01851307e+01,  -1.75228618e+01,  -7.63807957e+00,
         3.92799667e+00,  -2.13922201e+01,  -3.24077449e+01,
         2.49865507e+00,  -8.00052626e+00,  -1.30263419e+01,
         8.97544727e+00,   8.12124823e-01,   4.02617428e+01,
         2.18272490e+01,  -3.10250696e+01,  -2.36980956e+01,
         1.59445374e+01,   1.40231452e+01,  -1.01619744e+01,
        -5.56062605e+00,   3.51423210e+00,  -5.05401967e+00,
        -1.52653087e+01,   1.15900243e+01,   2.58716870e+00,
        -3.90423170e+00,  -2.62043921e+01,  -2.79795380e+01,
         6.07657840e+00,  -2.22918722e+01,   2.23834771e+00,
        -3.23746919e+00,  -3.40615142e+00,   2.45160741e+00,
         2.99851912e+01,   2.92969193e+01,   1.00960230e+01,
         7.81068099e+00,   2.19554827e-02,   2.41775283e+01,
        -2.43659477e+01,  -9.86638924e+00,  -1.82891284e+01,
         1.69419411e+01,   8.82756732e+00,  -2.39985595e+01,
        -4.51291898e+00,  -1.06533716e+01,   1.56936617e+01,
         5.73176993e+00,  -2.25493508e+01,  -5.44979696e+00,
        -4.78941099e+00,   1.65753052e+01,  -2.57973878e+01,
        -5.74931969e+00,   2.93202102e+01,  -1.74553426e+01,
        -1.26168770e+00,  -3.28448740e+01,   1.62268837e+00,
        -3.34297630e+01,  -3.61000704e+00,   1.19686128e+00,
        -3.20871605e+00,   1.34448752e+01,  -3.17132098e+01,
        -7.88108080e+00,   3.93066650e-01,  -8.40320104e+00,
        -7.51023304e+00,   1.35364293e+01,   5.20546459e+00,
         8.25565185e+00,  -6.99188854e-01,  -6.72523616e+00,
         2.11499904e+01,  -1.88279572e-01,   5.95471379e-01,
        -1.34398208e+01,  -1.68789918e+00,   6.66088076e+00,
        -3.79824329e+00,  -1.88025667e-01,   4.84622691e+00,
         2.48113830e+01,  -2.30331893e+01,   1.91964360e+01,
        -4.66880745e+01,  -1.81685226e+01,   1.50823040e+01,
        -2.27193072e+01,  -6.71517334e+00,  -1.39391214e+00,
        -4.88247402e+00,  -2.98327298e+00,   1.97465342e+01,
         4.55896208e+00]


def get_initial_weight():
    return [-16.01697523,  -1.08307523, -15.29844101,  19.5883391 ,
       -21.5550496 , -28.0553868 ,  35.85251644,   1.92230766,
       -24.62705508,   9.85558755,  -5.71038571, -33.75433172,
       -11.19962733,  16.51205223,  42.59097054,  87.28642746,
       -68.22244598,  -4.40434657,  10.99683589,  -5.86847309,
         6.65082591,  20.27418002,   0.46200577, -22.28701771,
       -21.28566069,   3.25690878,  -8.92102808,  -0.35484093,
        -9.61005293, -27.00208564,  20.40144561, -30.40392842,
        -6.65985217,  -6.85763339,  16.00902161,   4.31835639,
        49.53507994,  42.56183212,  28.58591706,  16.48757846,
       -19.64664985,  37.82346241, -26.17649735, -20.1355877 ,
        -6.50620398,  -5.82601518,  34.88585528, -59.79373428,
        -7.70184524, -14.07151806,  41.00299724,  -2.58735129,
       -58.25441384,  31.42951712,  29.57192882,  21.26459307,
       -38.09906247, -24.11814499,  41.45505917, -22.4704558 ,
         6.66033829, -42.6819133 ,  14.00916683, -37.07466871,
       -11.08570633,  13.83253283,  13.4959958 ,   8.69275944,
       -45.34743051,  -6.53281861,  10.27798671,  34.68254426,
       -17.04923337,  32.91769105, -21.35641477,  10.68887266,
        35.30229488,  30.46743723,  32.74410396,  -7.23384475,
         6.12722787, -19.21488421,  18.21758793,  24.55085118,
         4.49303348,  -8.9069708 ,   2.78651566,  18.19236021,
       -31.07191225,  53.29675652, -62.69597668, -13.92135457,
       -15.69005756, -57.54608527, -19.87531126,  -1.28340889,
        37.72990527, -14.03815287,   2.24029417,  -7.47029071]