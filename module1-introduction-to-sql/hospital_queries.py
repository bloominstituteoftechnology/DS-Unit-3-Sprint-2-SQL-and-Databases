import sqlite3


def conx_sqlite(db_filename):
    conn = sqlite3.connect(db_filename)
    return conn


def run_queries(cur):
    qr1 = '''
    SELECT pt.name AS "Patient",
        p.name AS "Primary Physician",
        n.name AS "Nurse"
    FROM appointment a
    JOIN patient pt ON a.patient=pt.ssn
    JOIN nurse n ON a.prepnurse=n.employeeid
    JOIN physician p ON pt.pcp=p.employeeid
    WHERE a.patient IN
        (SELECT patient
        FROM appointment a
        GROUP BY a.patient
        HAVING count(*)>=2)
    AND n.registered=1
    ORDER BY pt.name;
    '''

    for row in cur.execute(qr1):
        print(row)

    qr2 = '''
    SELECT patient
    FROM appointment a
    GROUP BY a.patient
    HAVING count(*) >= 2
    '''
    for row in cur.execute(qr2):
        print(row)
    return


def main():
    conn = conx_sqlite('hospital.db')
    cur = conn.cursor()  # create cursor

    run_queries(cur)

    cur.close()
    conn.close()   # Close the connection
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
