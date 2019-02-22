"""
----------------------------------------------------------------
             SQL lite Tutorial
----------------------------------------------------------------
"""
import sqlite3


def conx_sqlite(db_filename):
    conn = sqlite3.connect(db_filename)
    return conn


def create_tables(c, conn):
    # ___ Create table ____________________________________________
    create_script = '''
    CREATE TABLE Physician (
    EmployeeID INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Position TEXT NOT NULL,
    SSN INTEGER NOT NULL
    ); 
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Department (
    DepartmentID INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Head INTEGER NOT NULL
        CONSTRAINT fk_Physician_EmployeeID REFERENCES Physician(EmployeeID)
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Affiliated_With (
    Physician INTEGER NOT NULL
        CONSTRAINT fk_Physician_EmployeeID REFERENCES Physician(EmployeeID),
    Department INTEGER NOT NULL
        CONSTRAINT fk_Department_DepartmentID REFERENCES Department(DepartmentID),
    PrimaryAffiliation BOOLEAN NOT NULL,
    PRIMARY KEY(Physician, Department)
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Procedure (
    Code INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Cost REAL NOT NULL
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Trained_In (
    Physician INTEGER NOT NULL
        CONSTRAINT fk_Physician_EmployeeID REFERENCES Physician(EmployeeID),
    Treatment INTEGER NOT NULL
        CONSTRAINT fk_Procedure_Code REFERENCES Procedure(Code),
    CertificationDate DATETIME NOT NULL,
    CertificationExpires DATETIME NOT NULL,
    PRIMARY KEY(Physician, Treatment)
    );
    '''

    c.execute(create_script)

    create_script = '''
    CREATE TABLE Patient (
    SSN INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Address TEXT NOT NULL,
    Phone TEXT NOT NULL,
    InsuranceID INTEGER NOT NULL,
    PCP INTEGER NOT NULL
        CONSTRAINT fk_Physician_EmployeeID REFERENCES Physician(EmployeeID)
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Nurse (
    EmployeeID INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Position TEXT NOT NULL,
    Registered BOOLEAN NOT NULL,
    SSN INTEGER NOT NULL
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Appointment (
    AppointmentID INTEGER PRIMARY KEY NOT NULL,
    Patient INTEGER NOT NULL
        CONSTRAINT fk_Patient_SSN REFERENCES Patient(SSN),
    PrepNurse INTEGER
        CONSTRAINT fk_Nurse_EmployeeID REFERENCES Nurse(EmployeeID),
    Physician INTEGER NOT NULL
        CONSTRAINT fk_Physician_EmployeeID REFERENCES Physician(EmployeeID),
    Start DATETIME NOT NULL,
    End DATETIME NOT NULL,
    ExaminationRoom TEXT NOT NULL
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Medication (
    Code INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Brand TEXT NOT NULL,
    Description TEXT NOT NULL
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Prescribes (
    Physician INTEGER NOT NULL
        CONSTRAINT fk_Physician_EmployeeID REFERENCES Physician(EmployeeID),
    Patient INTEGER NOT NULL
        CONSTRAINT fk_Patient_SSN REFERENCES Patient(SSN),
    Medication INTEGER NOT NULL
        CONSTRAINT fk_Medication_Code REFERENCES Medication(Code),
    Date DATETIME NOT NULL,
    Appointment INTEGER
        CONSTRAINT fk_Appointment_AppointmentID REFERENCES Appointment(AppointmentID),
    Dose TEXT NOT NULL,
    PRIMARY KEY(Physician, Patient, Medication, Date)
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Block (
    Floor INTEGER NOT NULL,
    Code INTEGER NOT NULL,
    PRIMARY KEY(Floor, Code)
    ); 
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Room (
    Number INTEGER PRIMARY KEY NOT NULL,
    Type TEXT NOT NULL,
    BlockFloor INTEGER NOT NULL
        CONSTRAINT fk_Block_Floor REFERENCES Block(Floor),
    BlockCode INTEGER NOT NULL
        CONSTRAINT fk_Block_Code REFERENCES Block(Code),
    Unavailable BOOLEAN NOT NULL
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE On_Call (
    Nurse INTEGER NOT NULL
        CONSTRAINT fk_Nurse_EmployeeID REFERENCES Nurse(EmployeeID),
    BlockFloor INTEGER NOT NULL
        CONSTRAINT fk_Block_Floor REFERENCES Block(Floor),
    BlockCode INTEGER NOT NULL
        CONSTRAINT fk_Block_Code REFERENCES Block(Code),
    Start DATETIME NOT NULL,
    End DATETIME NOT NULL,
    PRIMARY KEY(Nurse, BlockFloor, BlockCode, Start, End)
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Stay (
    StayID INTEGER PRIMARY KEY NOT NULL,
    Patient INTEGER NOT NULL
        CONSTRAINT fk_Patient_SSN REFERENCES Patient(SSN),
    Room INTEGER NOT NULL
        CONSTRAINT fk_Room_Number REFERENCES Room(Number),
    Start DATETIME NOT NULL,
    End DATETIME NOT NULL
    );
    '''
    c.execute(create_script)

    create_script = '''
    CREATE TABLE Undergoes (
    Patient INTEGER NOT NULL
        CONSTRAINT fk_Patient_SSN REFERENCES Patient(SSN),
    Procedure INTEGER NOT NULL
        CONSTRAINT fk_Procedure_Code REFERENCES Procedure(Code),
    Stay INTEGER NOT NULL
        CONSTRAINT fk_Stay_StayID REFERENCES Stay(StayID),
    Date DATETIME NOT NULL,
    Physician INTEGER NOT NULL
        CONSTRAINT fk_Physician_EmployeeID REFERENCES Physician(EmployeeID),
    AssistingNurse INTEGER
        CONSTRAINT fk_Nurse_EmployeeID REFERENCES Nurse(EmployeeID),
    PRIMARY KEY(Patient, Procedure, Stay, Date)
    );
    '''
    c.execute(create_script)
    conn.commit()  #  save the changes


def insert_data(c, conn):
    # ___ Insert data ______________________________________
    file = open('insert_data.sql', 'r')
    for line in file:
        line = line.replace('\n', '')
        ins_scr = line
        c.execute(ins_scr)
    conn.commit()
    return


def verify_output(cur):
    # ___ Print out a List __________________________________________
    for row in cur.execute('SELECT * FROM Physician'):
        print(row[1])
    return


def main():
    # ____ connect to db ____
    conn = conx_sqlite('hospital.db')
    cur = conn.cursor()  

    # _____  Process ______
    # create_tables(cur, conn)
    # insert_data(cur, conn)
    verify_output(cur)

    # ___end main ________
    cur.close()
    conn.close()   
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
