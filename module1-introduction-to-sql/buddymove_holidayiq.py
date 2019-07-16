import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
df = pd.read_csv('buddymove_holidayiq.csv')
df.to_sql(name='review',con=engine)

engine.execute('SELECT count(Sports) FROM review').fetchall()
engine.execute('''SELECT count(Sports)
FROM review as r
WHERE (r.Nature >= 100) AND (r.Shopping > 100)
''').fetchall()

print(engine.execute('''SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic)
FROM review as r
''').fetchall())