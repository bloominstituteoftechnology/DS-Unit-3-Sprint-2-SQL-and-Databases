"""# function to get first 5 preview of the data and also prints the table info

def preview_info(table, db="northwind_small.sqlite3"):
    data_preview = SELECT * FROM @table limit 5;
    table_info = PRAGMA table_info @table ;
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    preview = curs.execute(data_preview).fetchall()
    info = curs.execute(table_info).fetchall()
    curs.close()
    conn.commit()
    
    return preview, info"""