import pandas as pd
import numpy as np
import seaborn as sns

plans_df = pd.read_excel('health_plans.xlsx',header=[0,1],index_col=0)

def plan_costs(df, costs):
    '''
    Just assumes everything is in plan ¯\_(ツ)_/¯ should be good enough
    '''
    cost_plan = plans_df.iloc[0,df.columns.get_level_values(1)=='val']*26

    pcp_cost = 100
    spc_cost = 400

    
def line_cost(df,index_str,cost_in):
    cost = [0, 0]
    line = df.loc[index_str]
    if line[1] == 'd':
        cost[0] = line[0]
    else:
        cost[0] = line[0]*cost_in
    if line[3] == 'd':  
        cost[1] = line[2]
    else:
        cost[1] = line[2]*cost_in
    print(cost)

line_cost(plans_df,'out_visit_er',100000)
# 
sim_runs = 10

#        ER     UC      in_op   out_op
probs = np.matrix([.5,     .2,      .05,   .25])
costs = np.matrix([1000,  100,    10000,  5000])

#allright gonna be lazy about this for loops it is

for i in range(sim_runs):
    rand = np.random.normal(loc = 1)
    events = np.multiply(probs,rand).round(0)
    iter_costs = np.multiply(events,costs)
    # print(iter_costs.sum())


