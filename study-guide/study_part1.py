import sqlite3


conn = sqlite3.connect('study_part1.sqlite3')
curs = conn.cursor()


query = """
DROP TABLE IF EXISTS example;
CREATE TABLE example (
    student VARCHAR(10),
    studied VARCHAR(5),
    grade INTEGER,
    age INTEGER,
    sex VARCHAR(6)
);
INSERT INTO example (
    student,
    studied,
    grade,
    age,
    sex
)
VALUES
('Lion-O', 'True', 85, 24, 'Male'),
('Cheetara', 'True', 95, 22, 'Female'),
('Mumm-Ra', 'False', 65, 153, 'Male'),
('Snarf', 'False', 70, 15, 'Male'),
('Panthro', 'True', 80, 30, 'Male');
"""


if __name__ == "__main__":
    curs.executescript(query)
    conn.commit()
    conn.close()
