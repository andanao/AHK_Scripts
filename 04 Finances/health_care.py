import pandas as pd
import numpy as np
import seaborn as sns

plans_df = pd.read_excel('health_plans.xlsx',header=[0,1],index_col=0)

# 
sim_runs = 1

#        ER     UC      in_op   out_op
probs = np.matrix([.5,     .2,      .05,   .25])
costs = np.matrix([1000,  100,    10000,  5000])

#allright gonna be lazy about this for loops it is

for i in range(sim_runs):
    rand = np.random.normal(loc = 1)
    np.multiply(probs,stat).round(0)



