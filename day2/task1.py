import mysql.connector

try:

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='test_py',
    port=3308
    )
    # print(mydb)
except Exception as e:
    print(e)





cur = mydb.cursor()



class Employee:
    employees=[]
    id=0
    def __init__(self,First_name,Last_name,Age,Department,Salary):
        self.First_name=First_name
        self.Last_name=Last_name
        self.Age=Age
        self.Department=Department
        self.Salary=Salary
        Employee.id+=1
        self.id=Employee.id
        cur.execute(f"INSERT INTO employees (FirstName, LastName, Age, department, salary) VALUES ('{First_name}', '{Last_name}', {Age}, '{Department}', {Salary})")
        mydb.commit()
        Employee.employees.append(self)

    def transfer(self,department):
        self.department=department
        cur.execute(f"Update employees set department='{department}' where FirstName='{self.First_name}' and LastName='{self.Last_name}'")
        mydb.commit()
    
    def fire(self):
        Employee.employees.remove(self)
        cur.execute(f"delete from employees  where FirstName='{self.First_name}' and LastName='{self.Last_name}' ")
        mydb.commit()
    
    def show(self):
        cur.execute(f"select * from employees where FirstName='{self.First_name}' and LastName='{self.Last_name}'")
        rows = cur.fetchone()
        print(rows[0], rows[1], rows[2],rows[3],rows[4])
        mydb.commit()
    
    @classmethod
    def List_employees(cls):
        cur.execute(f"select * from employees")
        rows = cur.fetchall()
        for row in rows:
            print(row[0], row[1], row[2],row[3],row[4])
        mydb.commit() 

# e=Employee("Ali","adel",25,"cs",15000)
# e.transfer("SE")
# e.fire()
# e.show()
# Employee.List_employees()

while True:
    action= input(""" welcome to our company
            to add employee type 'add'
            to show all employees 'show_all'
            to exit press Q
            """)
    if action=='add':
        manager=input("If you are manager press “m” || if you are employee press ‘e’")
        if manager=="m":
            first_name=input('please enter the first name: ')
            last_name=input('please enter the last name: ')
            age=int(input('please enter the age: '))
            department=input('please enter the department: ')
            salary=int(input('please enter the salary: '))
            e=Employee(first_name,last_name,age,department,salary)
        else:
            print("you can not add employee")

            
    if action=='show_all':
        Employee.List_employees()
    
    if action=='q':
        break
