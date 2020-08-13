import pandas as pd
from sqlalchemy import creat_engine

engine = create_engine(
    "postgres://ajkuvccu:FBOFpSpFdAFrxYUG-DBqN39wDQ0Mjc4V@isilo.db.elephantsql.com:5432/ajkuvccu"
)

df = pd.read_csv("titanic.csv")

df.to_sql("titanic_postgres", con=engine)
