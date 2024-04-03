import sqlite3

# Step 1: Create a connection object
conn = sqlite3.connect('employees.db')

# Step 2: Create a cursor object
c = conn.cursor()

# Step 3: Execute a SQL command
c.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        salary REAL
    )
''')

# c.execute('''
#     INSERT INTO employees 
#         VALUES(NULL, 'Jane', 'Doe', 30), 
#         (NULL, 'Mike', 'Smith', 40), 
#         (NULL, 'Anna', 'Frank', 50),
#         (NULL, 'Tom', 'Hanks', 60),
#         (NULL, 'Brad', 'Pitt', 70),
#         (NULL, 'Angelina', 'Jolie', 80),
#         (NULL, 'Jeniffer', 'Aniston', 90),
#         (NULL, 'Tom', 'Cruise', 100),
#         (NULL, 'Nicole', 'Kidman', 110),
#         (NULL, 'Julia', 'Roberts', 120),
#         (NULL, 'George', 'Clooney', 130),
#         (NULL, 'Scarlett', 'Johansson', 140),
#         (NULL, 'Robert', 'Downey Jr.', 150),
#         (NULL, 'Chris', 'Evans', 160),
#         (NULL, 'Chris', 'Hemsworth', 170),
#         (NULL, 'Chris', 'Pratt', 180),
#         (NULL, 'Chris', 'Pine', 190),
#         (NULL, 'Chris', 'Rock', 200),
#         (NULL, 'Chris', 'Tucker', 210),
#         (NULL, 'Chris', 'Brown', 220),
#         (NULL, 'Chris', 'Martin', 230),
#         (NULL, 'Chris', 'Martin', 240),
#         (NULL, 'Chris', 'Johnson', 250),
#         (NULL, 'Chris', 'Davis', 260),
#         (NULL, 'Chris', 'Thompson', 270)
# ''')

c.execute('''SELECT * FROM employees''')

print(c.fetchall())

# c.execute('''
#     DELETE FROM employees
# ''')

# Step 4: Commit the transaction
conn.commit()

# Step 5: Close the connection
conn.close()