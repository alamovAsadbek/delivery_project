from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Manage:
    @log_decorator
    def create_company_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS company (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(255) NOT NULL,
        CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        # kament olishdan maqsad programma ishlagan payt har safar malumot qushaveradi databasega
        # self.insert_company_table()
        return True

    @log_decorator
    def insert_company_table(self):
        query = '''
                    INSERT INTO Company (name) VALUES
                    ('Tech Innovators Inc.'),
                    ('Global Financial Services Ltd.'),
                    ('Wellness Solutions LLC'),
                    ('SuperMart'),
                    ('EduTech Systems'),
                    ('Fast Transport Co.'),
                    ('Prime Properties'),
                    ('Green Energy Solutions'),
                    ('Precision Manufacturing Corp.'),
                    ('Creative Media Group');
                    '''
        execute_query(query)
        return True

    @log_decorator
    def create_department_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS department (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(255) NOT NULL,
        COMPANY_ID BIGINT NOT NULL REFERENCES company(ID),
        CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        # kament olishdan maqsad programma ishlagan payt har safar malumot qushaveradi databasega
        # self.insert_department_table()
        return True

    @log_decorator
    def insert_department_table(self):
        query = '''
        INSERT INTO Department (name, company_id) VALUES
        ('Human Resources', 1),
        ('Finance', 1),
        ('Engineering', 2),
        ('Marketing', 2),
        ('Sales', 3),
        ('Customer Support', 3),
        ('Research and Development', 4),
        ('IT', 4),
        ('Legal', 5),
        ('Logistics', 5)
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_employee_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS employee (
        ID BIGSERIAL PRIMARY KEY,
        FULL_NAME VARCHAR(255) NOT NULL,
        DEPARTMENT_ID BIGINT REFERENCES department(ID),
        CREATED_AT TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        # kament olishdan maqsad programma ishlagan payt har safar malumot qushaveradi databasega
        # self.insert_employee_table()
        return True

    @log_decorator
    def insert_employee_table(self):
        query = '''
        INSERT INTO Employee (full_name, department_id) VALUES
        ('Alice Johnson', 1),
        ('Bob Smith', 2),
        ('Charlie Brown', 3),
        ('David Wilson', NULL), 
        ('Emily Davis', 4),
        ('Frank Miller', NULL),  
        ('Grace Lee', 5),
        ('Henry Moore', 1),
        ('Ivy Clark', 2),
        ('Jack Taylor', NULL),  
        ('Kathy Anderson', 3),
        ('Louis Thomas', NULL),  
        ('Mia Harris', 4),
        ('Noah Martin', 5),
        ('Olivia White', 1);
        '''
        execute_query(query)
        return True


@log_decorator
def run_query():
    manager = Manage()
    manager.create_company_table()
    manager.create_department_table()
    manager.create_employee_table()
    return True
