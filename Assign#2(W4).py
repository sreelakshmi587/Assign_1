import sqlite3
def db_connect():
    con = sqlite3.connect('employee_folder.db')
    return con

def employee_table():
    con=db_connect()
    cur=con.cursor()
    employee_sql = """
      CREATE TABLE Employee(
      Name TEXT NOT NULL ,
      ID INTEGER NOT NULL PRIMARY KEY,
      Salary INTEGER NOT NULL,
      Department_id INTEGER NOT NULL, 
      FOREIGN KEY (Department_id)
      REFERENCES Departments(Department_id))"""
    cur.execute(employee_sql)
    add_column = """
      ALTER TABLE Employee ADD COLUMN City TEXT NOT NULL DEFAULT 1"""
    cur.execute(add_column)
    con.commit()
    con.close()

def employee_details():
    con = db_connect()
    cur = con.cursor()
    employeedetail = [('Sree', 1, 35000, 1213, 'TRIVANDRUM'), ('Raj', 2, 32000, 1214, 'Kollam'),
                      ('Helen', 3, 30000, 1215, 'TRIVANDRUM'), ('Ella', 4, 32000, 1216, 'Idukki'),
                      ('Dazzle', 5, 28000, 1217,'Kochi')]
    con.executemany("INSERT INTO Employee(Name,ID,Salary,Department_id,City) VALUES(?,?,?,?,?)", employeedetail)
    con.commit()
    con.close()

con = db_connect()
cur = con.cursor()
cur.execute(("DROP TABLE IF EXISTS Employee"))
employee_table()
employee_details()
cur.execute("SELECT DISTINCT Name,ID,Salary FROM Employee")
Name,ID,Salary,Department_id,City='Name','ID','Salary','Department_id','City'
format=[f"{Name:<20}{ID:<20}{Salary:<20}" for Name,ID,Salary in cur.fetchall()]
print('\n'.join([f"{Name:<20}{ID:<20}{Salary:<20}"]+format))
con.commit()
print('\n','Identifying Employees with their first letter...')
letter= input('Enter the character to find a name that starts with it: ')
cur.execute(f"SELECT DISTINCT * FROM Employee WHERE Name LIKE '{letter}%'")
let=cur.fetchall()
for l in let:
    print(f"The details of the employee whose name begins with {letter} are as follows:\nName:{l[0]}\nID:{l[1]}\nSalary:{l[2]}\nDepartment_id:{l[3]}\nCity:{l[4]}")
print('\n','Accessing Employee details with the user given ID')
id=int(input('Enter the ID to access employee detail: '))
cur.execute(f"SELECT DISTINCT Name,Salary,Department_id,City FROM Employee WHERE ID={id}")
emp=cur.fetchall()
for e in emp:
    print(f"Name:{e[0]}\nSalary:{e[1]}\nDepartment_id:{e[2]}\nCity:{e[3]} ")
print('\n','Changing name of the employee whose ID is provided...')
swap=int(input('Enter the ID to change the employee name with the same: '))
new_name=input('Enter a new name: ')
cur.execute(f"UPDATE Employee SET Name='{new_name}' WHERE ID='{swap}' ")
con.commit()
cur = con.cursor()
cur.execute(f"SELECT DISTINCT * FROM Employee WHERE ID='{swap}' ")
up=cur.fetchall()
for u in up:
    print(f"The updated Employee details are:\nName:{u[0]}\nID:{u[1]}\nSalary:{u[2]}\nDepartment_id:{u[3]}\nCity:{u[4]}")
con.commit()
con.close()
print('\n','Adding another table...')

def dept_table():
    con=db_connect()
    cur=con.cursor()
    dept_in="""
       CREATE TABLE Departments(
       Department_id INTEGER NOT NULL PRIMARY KEY,
       Department_name TEXT NOT NULL)"""
    cur.execute(dept_in)
    con.commit()
    con.close()

def dept_detail():
    con = db_connect()
    cur = con.cursor()
    depdetail=[(1213,'Technical'),(1214,'HR'),(1215,'QA'),(1216,'Marketing'),(1217,'Finance')]
    cur.executemany("INSERT INTO Departments(Department_id,Department_name) VALUES(?,?)",depdetail)
    con.commit()
    con.close()

con = db_connect()
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Departments")
dept_table()
dept_detail()
cur.execute("SELECT DISTINCT * FROM Departments")
Department_id,Department_name='Department_id','Department_name'
format_d=[f"{Department_id:<20}{Department_name:<20}" for Department_id,Department_name in cur.fetchall()]
print('\n'.join([f"{Department_id:<20}{Department_name:<20}"]+format_d))
dep_id=int(input('Enter the Department_id (1213-1217) to access employee details: '))
cur.execute(f"SELECT * FROM Employee INNER JOIN Departments where Employee.Department_id='{dep_id}' and Departments.Department_id=Employee.Department_id")
d=cur.fetchall()
for i in d:
    print(f"'\nThe details are as follows...'\nName:{i[0]}\nID:{i[1]}\nSalary:{i[2]}\nDepartment_id:{i[3]}\nCity:{i[4]}\nDepartment:{i[5]} ")
con.commit()
con.close()


