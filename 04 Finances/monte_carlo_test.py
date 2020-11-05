import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style('whitegrid')

avg = 1
strd_dev = .1
num_reps = 500
num_simulations = 1000

pct_to_target = np.random.normal(avg,strd_dev, num_reps).round(2)
# print(pct_to_target)

sales_target_values = [75_000, 100_000, 200_000, 300_000, 400_000, 500_000]
sales_target_prob = [.3, .3, .2, .1, .05, .05]
sales_target = np.random.choice(sales_target_values, num_reps, p=sales_target_prob)

df = pd.DataFrame(index=range(num_reps), data={'Pct_To_Target': pct_to_target,
                                               'Sales_Target': sales_target})

df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']