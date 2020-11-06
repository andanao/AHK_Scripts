import pandas as pd
import numpy as np
import seaborn as sns

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
    # print(cost)
    cost_np = np.asarray(cost)
    return cost_np

def plan_costs(df, costs):
    '''
    Just assumes everything is in plan ¯\_(ツ)_/¯ should be good enough
    '''
    cost_plan_temp = plans_df.iloc[0,df.columns.get_level_values(1)=='val']*26
    cost_plan = cost_plan_temp.to_list()
    cost_yearly = np.asarray([0,0])
    pcp_cost = 100
    spc_cost = 400 #unused, figured it would be part of the ER, but also shake out roughly the same
    cost_yearly = cost_yearly + line_cost(plans_df,'in_visit_pcp',pcp_cost)
    
    cost_yearly = cost_yearly + line_cost(plans_df,'in_visit_er',costs[0])
    
    cost_yearly = cost_yearly + line_cost(plans_df,'in_visit_uc',costs[1])
    cost_yearly = cost_yearly + line_cost(plans_df,'in_visit_hosp_in',costs[2])
    cost_yearly = cost_yearly + line_cost(plans_df,'in_visit_hosp_out',costs[3])

    above_deduct = line_cost(df,'in_Deductible',0) - cost_yearly

    #eh i guess i've just given up and want this done
    for i in range(2):
        if above_deduct[i] < 0:
            cost_yearly[i] = cost_yearly[i] -.1*above_deduct[i]
            

    # print(above_deduct)
    cost_total = cost_yearly+cost_plan
    return cost_total
    


    
plans_df = pd.read_excel('health_plans.xlsx',header=[0,1],index_col=0)

# line_cost(plans_df,'out_visit_er',100000)

# 
sim_runs = 100


#        ER     UC      in_op   out_op
probs = np.matrix([.5,     .2,      .05,   .25])
costs = np.matrix([1000,  100,    10000,  5000])

#allright gonna be lazy about this for loops it is

for i in range(sim_runs):
    rand = np.random.normal(loc = 1)
    events = np.multiply(probs,rand).round(0)
    iter_costs = np.multiply(events,costs).tolist()[0]
    #print(iter_costs)
    final_result = plan_costs(plans_df,iter_costs)
    print(str(final_result.argmin()+1))
    # print(iter_costs.sum())



