import sqlite3
con=sqlite3.connect('hospital_directory.db')
cur=con.cursor()
# hospital_sql="""
#     CREATE TABLE Hospital(
#         Hospital_Id INTEGER NOT NULL PRIMARY KEY,
#         Hospital_Name TEXT NOT NULL,
#         Bed_Count INTEGER NOT NULL)"""
# cur.execute(hospital_sql)
# doctor_sql="""
#   CREATE TABLE Doctor(
#     Doctor_Id INTEGER NOT NULL PRIMARY KEY,
#     Doctor_Name TEXT NOT NULL,
#     Hospital_Id INTEGER NOT NULL,
#     Joining_Date TEXT NOT NULL,
#     Speciality TEXT NOT NULL,
#     Salary INTEGER NOT NULL,
#     Experience INTEGER,
#     FOREIGN KEY (Hospital_Id)
#     REFERENCES hospital_sql(Hospital_Id))"""
# cur.execute(doctor_sql)

hospital_sql="INSERT INTO Hospital(Hospital_Id,Hospital_Name,Bed_Count) VALUES(?,?,?)"
cur.execute(hospital_sql,(1,'Mayo Clinic',200))
cur.execute(hospital_sql,(2,'Cleveland',400))
cur.execute(hospital_sql,(3,'Johns Hopkins',1000))
cur.execute(hospital_sql,(4,'UCLA Medical Center',1500))
cur.execute("SELECT * FROM Hospital")
format_h=[f"{Hospital_Id:<20}{Hospital_Name:<30}{Bed_Count:<25}" for Hospital_Id,Hospital_Name,Bed_Count in cur.fetchall()]
Hospital_Id,Hospital_Name,Bed_Count='Hospital_Id','Hospital_Name','Bed_Count'
print('\n'.join([f"{Hospital_Id:<20}{Hospital_Name:<30}{Bed_Count:<50}"]+format_h))
print('\n'*2)

doctor_sql="INSERT INTO Doctor(Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) VALUES(?,?,?,?,?,?,?)"
cur.execute(doctor_sql,('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', 'NULL'))
cur.execute(doctor_sql,('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', 'NULL'))
cur.execute(doctor_sql,('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', 'NULL'))
cur.execute(doctor_sql,('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', 'NULL'))
cur.execute(doctor_sql,('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', 'NULL'))
cur.execute(doctor_sql,('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', 'NULL'))
cur.execute(doctor_sql,('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', 'NULL'))
cur.execute(doctor_sql,('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', 'NULL'))
cur.execute("SELECT * FROM Doctor")
Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience='Doctor_Id','Doctor_Name','Hospital_Id','Joining_Date','Speciality','Salary','Experience'
format_d=[f"{Doctor_Id:<20}{Doctor_Name:<20}{Hospital_Id:<20}{Joining_Date:<20}{Speciality:<20}{Salary:<20}{Experience:<20}" for Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience in cur.fetchall()]
print('\n'.join([f"{Doctor_Id:<20}{Doctor_Name:<20}{Hospital_Id:<20}{Joining_Date:<20}{Speciality:<20}{Salary:<20}{Experience:<20}"]+format_d))


def hsptl_detail(hsptl_id):
    con=sqlite3.connect('hospital_directory.db')
    cur=con.cursor()
    get_hsptl = "SELECT Hospital_Name from Hospital where Hospital_Id=?"
    cur.execute(get_hsptl,(hsptl_id,))
    result=cur.fetchone()
    return result
def dr_detail(hsptl_id):
    con = sqlite3.connect('hospital_directory.db')
    cur = con.cursor()
    hsptl_name=hsptl_detail(hsptl_id)
    get_doctor = "SELECT * from Doctor where Hospital_Id=?"
    cur.execute(get_doctor,(hsptl_id,))
    records=cur.fetchall()
    return records
    print('Doctors from',hsptl_name,'includes: ')
    for row in records:
        print(row[1])
        print(hsptl_name)
def dr_list(speciality,salary):
    con = sqlite3.connect('hospital_directory.db')
    cur = con.cursor()
    list="SELECT * FROM Doctor where speciality=? and salary>?"
    cur.execute(list,(speciality,salary))
    records=cur.fetchall()
    for row in records:
        print(row[1])

print('\n')
speciality=input('Enter the speciality to check the doctors from the same: ')
salary=int(input("Enter the salary to find the doctor: "))
print(dr_list(speciality,salary))
hsptl_id=int(input('Enter the hospital id to access details: '))
print(dr_detail(hsptl_id))

