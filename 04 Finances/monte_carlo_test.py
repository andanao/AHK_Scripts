import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style('whitegrid')

def calc_commission_rate(x):
    """ Return the commission rate based on the table:
    0-90% = 2%
    91-99% = 3%
    >= 100 = 4%
    """
    if x <= .90:
        return .02
    if x <= .99:
        return .03
    else:
        return .04

avg = 1
strd_dev = .1
num_reps = 500
num_simulations = 1000

pct_to_target = np.random.normal(avg,strd_dev, size = (num_reps,num_simulations))
# print(pct_to_target)

sales_target_values = [75_000, 100_000, 200_000, 300_000, 400_000, 500_000]
sales_target_prob = [.3, .3, .2, .1, .05, .05]

sales_target = np.random.choice(sales_target_values, num_reps, p=sales_target_prob, size = (num_reps,num_simulations))

df = pd.DataFrame(index=range(num_reps), data={'Pct_To_Target': pct_to_target,
                                               'Sales_Target': sales_target})

df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']


commission_percentages = np.take(
    np.array([0.02, 0.03, 0.04]),
    np.digitize(pct_to_target, bins=[.9, .99, 10])
)

total_commissions = (commission_percentages * sales_target).sum(axis=0)

df = pd.DataFrame(data = {'Total_commisions':total_commisions})
df.plot(kind='hist', title='Commissions Distribution')
