import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# 1. Load the generated CSV
df = pd.read_csv('ab_test_data.csv')

# 2. URL-encode the password to safely handle the '@' symbol
password = urllib.parse.quote_plus("Reddy@9441")

# 3. Connect to MySQL using the safely formatted password string
engine = create_engine(f'mysql+pymysql://root:{password}@localhost:3306/ab_testing')

# 4. Push the dataframe to a new SQL table called 'raw_ab_test'
df.to_sql(name='raw_ab_test', con=engine, if_exists='replace', index=False)

print("Success! 10,000 rows loaded into the 'raw_ab_test' table in MySQL.")