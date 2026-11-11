import pandas as pd
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

# Project Parameters
n_users = 10000

# 1. Create User IDs and randomly assign to groups (50/50 split)
user_ids = range(1, n_users + 1)
groups = np.random.choice(['Control', 'Treatment'], size=n_users, p=[0.5, 0.5])

# 2. Simulate Conversions based on assigned group
# Control = 12% conversion rate | Treatment = 14.5% conversion rate
conversions = []
for group in groups:
    if group == 'Control':
        converted = np.random.choice([0, 1], p=[0.88, 0.12])
    else:
        converted = np.random.choice([0, 1], p=[0.855, 0.145])
    conversions.append(converted)

# 3. Simulate Revenue for converted users (Average Order Value)
# Treatment reduces friction, slightly increasing the AOV
revenue = []
for i in range(n_users):
    if conversions[i] == 1:
        if groups[i] == 'Control':
            rev = round(np.random.normal(50.0, 15.0), 2) # Mean $50
        else:
            rev = round(np.random.normal(55.0, 15.0), 2) # Mean $55
        
        revenue.append(max(rev, 5.0)) # Ensure no negative revenue
    else:
        revenue.append(0.0)

# 4. Compile into a DataFrame and export to CSV
df = pd.DataFrame({
    'user_id': user_ids,
    'test_group': groups,
    'converted': conversions,
    'revenue': revenue
})

df.to_csv('ab_test_data.csv', index=False)
print(f"Dataset generated successfully with {n_users} records!")
print(df.head())