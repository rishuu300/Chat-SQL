import sqlite3

# Connect to sqlite
connection = sqlite3.connect('student.db')

# Create a cursor object to insert record, create table
cursor = connection.cursor()

# Create the table
table_info = """
create table STUDENT(NAME VARCHAR(25), 
                    CLASS VARCHAR(25),
                    SECTION VARCHAR(25),
                    MARKS INT
)
"""

cursor.execute(table_info)

# Insert some more records
cursor.execute('''Insert Into STUDENT values ('Krish', 'Data Science', 'A',90) ''')
cursor.execute('''Insert Into STUDENT values ('John', 'Data Science', 'B',100) ''')
cursor.execute('''Insert Into STUDENT values('Mukesh', 'Data Science', 'A', 86)''')
cursor.execute('''Insert Into STUDENT values ('Jacob', 'DEVOPS', 'A',50)''')
cursor.execute('''Insert Into STUDENT values ('Dipesh', 'DEVOPS', 'A',35)''')

# Display all the records
print('The inserted records are')
data = cursor.execute('''Select * from Student''')

for row in data:
    print(row)
    
    
# Commit your changes in the databases
connection.commit()
connection.close()