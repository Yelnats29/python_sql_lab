# For Future Reference
# def setup_database():
#     conn = sqlite3.connect('crm.db')
#     cursor = conn.cursor()

#     # Create companies table
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS companies (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         address TEXT
#     )
#     ''')

#     # Create employees table
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS employees (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         position TEXT,
#         company_id INTEGER,
#         FOREIGN KEY (company_id) REFERENCES companies (id)
#     )
#     ''')

#     conn.commit()
#     conn.close()

# setup_database()

import psycopg2
connection = psycopg2.connect(database='crm_db')

cursor = connection.cursor()


# Company CRUD Functions
def create_company(name, city):
    cursor.execute('INSERT INTO companies (name, city) VALUES (%s, %s)', (name, city) )
    connection.commit()

def read_companies():
    cursor.execute('SELECT * FROM companies')
    print(cursor.fetchall())

def update_companies(name, city, company_id):
    cursor.execute('UPDATE companies SET name = %s, city = %s WHERE id = %s', (name, city, company_id))
    connection.commit()

def delete_companies(company_id):
    cursor.execute('DELETE FROM companies WHERE id = %s', (company_id))
    connection.commit()



# Employee CRUD Functions
def create_employee(name, company_id):
    cursor.execute('INSERT INTO employees (name, company_id) VALUES (%s, %s)', (name, company_id) )
    connection.commit()

def read_employees():
    cursor.execute('SELECT * FROM employees')
    print(cursor.fetchall())

def update_employees(name, employee_id, company_id):
    cursor.execute('UPDATE employees SET name = %s, company_id = %s WHERE id = %s', (name, company_id, employee_id))
    connection.commit()

def delete_employees(employee_id):
    cursor.execute('DELETE FROM employees WHERE id = %s', (employee_id))
    connection.commit()



# Terminal
def terminal_menu():
    while True:
        print('1. Manage Companies')
        print('2. Manage Employess')
        print('3. Exit')
        choice = input('Enter the number of your choice: ')

        if choice == '1':
            manage_companies()
        elif choice == '2':
            manage_employees()
        elif choice == '3':
            break
        else:
            print('Enter a valid option. ')

def manage_companies():
    while True:
        print('1. Create company')
        print('2. Read companies')
        print('3. Update companies')
        print('4. Delete companies')
        print('5. Go Back')
        choice = input('Select your option: ')

        if choice == '1':
            name = input('Enter the name of the company: ')
            city = input('Enter the city the company is located in: ')
            create_company(name, city)
        elif choice == '2':
            companies = read_companies()
            for company in companies:
                print(company)
        elif choice == '3':
            company_id = INT(input('Enter the new company Id number: '))
            name = input('Enter the new company name: ')
            city = input('Enter the compnay city name: ')
            update_companies(company_id, name, city)
        elif choice == '4':
            company_id = INT(input('Enter the company Id number you wish to delete: '))
            delete_companies(company_id)
        elif choice == '5':
            break
        else:
            print('Invalid option choice. Please make another selection: ')























cursor.close()
create_company('Google', 'New York')
connection.close()