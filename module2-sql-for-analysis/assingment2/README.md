Setup virtual environment

'''sh
pipenv --python3.7
pipenv install python-dotenv psycopg2-binary
pipenv shell
'''

Setup env vars in a ".env" file (using creds from ElephantSQL):

'''sh
DB_NAME = '______________'
DB_USER = '_____'
DB_PASSWORD = '___'
DB_HOST = '____________'
'''

Run:

'''sh
python app/pg_queries.py
'''

