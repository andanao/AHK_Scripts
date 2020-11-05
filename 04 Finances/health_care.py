import pandas as pd
import numpy as numpy
import seaborn as sns

plans_df = pd.read_excel('health_plans.xlsx',header=[0,1],index_col=0)

# 
sim_runs = 1000

prob_er = .5
prob_uc = .2
prob_i_surg = .2
prob_o_surg= .1

cost_er = 1000
cost_uc = 100
cost_i_surg = 10000
cost_o_surg = 5000

# 