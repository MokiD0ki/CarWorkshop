import sqlite3
import sqlite3

conn = sqlite3.connect('employees.db')

c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        employee_id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        salary REAL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS tickets(
        ticket_id INTEGER PRIMARY KEY,
        ticket_status TEXT,
        car_brand TEXT,
        car_model TEXT,
        car_registration_id TEXT,
        ticket_description TEXT,
        time_slot TEXT,
        employee_id INTEGER,
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
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

# c.execute('''INSERT INTO tickets 
#         VALUES(NULL, 'Created', 'Toyota', 'Corolla', 'ABC123', 'Engine failure', '31-04-2024-12:00-16:00', NULL),
#         (NULL, 'Created', 'Toyota', 'Prius', 'KFC123', 'Engine failure', '30-04-2024-12:00-16:00', NULL),
#         (NULL, 'Created', 'Mazda', 'Corolla', 'GFD777', 'Engine failure', '29-04-2024-12:00-16:00', NULL)
# ''')


c.execute('''SELECT * FROM employees''')
c.execute('''SELECT * FROM tickets''')

print(c.fetchall())

# c.execute('''
#     DELETE FROM employees
# ''')

# Step 4: Commit the transaction
conn.commit()

# Step 5: Close the connection
conn.close()