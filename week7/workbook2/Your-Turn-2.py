## Your Turn 2
# load data from datasets/salesdata.db

import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))
sql = 'SELECT * from scores'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df