import pandas as pd
import random

# Define some sample data for generating demo company asset info
asset_types = ['Laptop', 'Desktop', 'Monitor', 'Printer', 'Router', 'Switch', 'Projector', 'Tablet', 'Smartphone', 'Server']
departments = ['IT', 'HR', 'Finance', 'Marketing', 'Sales', 'Operations', 'Admin']
conditions = ['New', 'Good', 'Fair', 'Needs Repair']
locations = ['New York', 'San Francisco', 'Chicago', 'Austin', 'Seattle']

# Generate 50 sample asset entries
num_assets = 50
data = []

for i in range(1, num_assets + 1):
    asset = {
        'Asset ID': f'A{i:04}',
        'Asset Type': random.choice(asset_types),
        'Department': random.choice(departments),
        'Condition': random.choice(conditions),
        'Location': random.choice(locations),
        'Purchase Date': pd.to_datetime(f'202{random.randint(0,3)}-{random.randint(1,12):02}-{random.randint(1,28):02}'),
        'Value ($)': round(random.uniform(200, 5000), 2)
    }
    data.append(asset)

# Create DataFrame
df_assets = pd.DataFrame(data)

# Save to CSV
df_assets.to_csv("company_assets_demo.csv", index=False)
