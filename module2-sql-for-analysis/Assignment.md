>>> import psycopg2 as pg
>>> import sqlite3
>>> pg.connect
<function connect at 0x101091d08>
>>> pg
<module 'psycopg2' from '/Users/danielleromanoff/anaconda3/lib/python3.6/site-packages/psycopg2/__init__.py'>
>>> dbname = 'lypxyiou'
>>> user = 'lypxyiou'
>>> password = 'aTBkmr6shusePq6YSAT5R_h5Nf891q2W'
>>> host = 'stampy.db.elephantsql.com'
>>> conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
>>> dir(conn)
['DataError', 'DatabaseError', 'Error', 'IntegrityError', 'InterfaceError', 'InternalError', 'NotSupportedError', 'OperationalError', 'ProgrammingError', 'Warning', '__class__', '__delattr__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'async', 'async_', 'autocommit', 'binary_types', 'cancel', 'close', 'closed', 'commit', 'cursor', 'cursor_factory', 'deferrable', 'dsn', 'encoding', 'fileno', 'get_backend_pid', 'get_dsn_parameters', 'get_parameter_status', 'get_transaction_status', 'isexecuting', 'isolation_level', 'lobject', 'notices', 'notifies', 'poll', 'protocol_version', 'readonly', 'reset', 'rollback', 'server_version', 'set_client_encoding', 'set_isolation_level', 'set_session', 'status', 'string_types', 'tpc_begin', 'tpc_commit', 'tpc_prepare', 'tpc_recover', 'tpc_rollback', 'xid']
>>> cur = conn.cursor()
>>> cur.execute('SELECT * from test_table;')
>>> cur.fetchall()
[(1, 'A row name', None), (2, 'Row with JSON', {'x': [1, 2, 3], 'age': 30, 'name': 'John'})]
>>> pass
>>> import pandas as pd
>>> cur.fetchall()
[]
>>> cur.execute('SELECT * from test_table;')
>>> results = cur.fetchall()
>>> results
[(1, 'A row name', None), (2, 'Row with JSON', {'x': [1, 2, 3], 'age': 30, 'name': 'John'})]
