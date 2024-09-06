from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator
from main_files.manage.manage import run_query


class Statistic:
    def __init__(self):
        run_query()

    @log_decorator
    def number_of_employees(self):
        query = '''
        SELECT c.name as NAME, COUNT(c.ID) as All_EMPLOYEES
        FROM company c
        LEFT JOIN department d ON d.COMPANY_ID = c.ID
        LEFT JOIN employee e ON e.DEPARTMENT_ID = d.id
        GROUP BY c.name;
        '''
        result_exc = execute_query(query, fetch='all')
        pagination = Pagination(table_name='users', table_keys=[0, 1], display_keys=['Name', 'Count'],
                                data=result_exc)
        pagination.page_tab()
        return True

    @log_decorator
    def number_of_departments(self):
        query = '''
        SELECT c.name as NAME, COUNT(c.ID) as All_DEPARTMENTS
        FROM company c
        LEFT JOIN department d ON d.COMPANY_ID = c.ID
        GROUP BY c.name;
        '''
        result_exc = execute_query(query, fetch='all')
        pagination = Pagination(table_name='users', table_keys=[0, 1], display_keys=['Company name', 'Count'],
                                data=result_exc)
        pagination.page_tab()
        return True

    @log_decorator
    def number_of_employees_in_departments(self):
        query = '''
        SELECT c.name, d.name, COUNT(e.id)
        FROM department d
            LEFT JOIN employee e on d.ID = e.DEPARTMENT_ID
            LEFT JOIN company c on d.company_id=c.ID
        group by c.name, d.name ORDER BY count(*) desc ;
        '''
        result_exc = execute_query(query, fetch='all')
        pagination = Pagination(table_name='users', table_keys=[0, 1, 2],
                                display_keys=['Company name', 'Department name', 'Employees'], data=result_exc)
        pagination.page_tab()
        return True

    @log_decorator
    def departments_without_staff(self):
        query = '''
        SELECT c.name, d.name
        FROM department d
                 LEFT JOIN employee e on e.DEPARTMENT_ID = d.ID
                 LEFT JOIN company c on d.company_id = c.ID
        WHERE e.ID is NULL
        group by c.name, d.name;
        '''
        result_exc = execute_query(query, fetch='all')
        pagination = Pagination(table_name='users', table_keys=[0, 1], display_keys=['Company name', 'Department name'],
                                data=result_exc)
        pagination.page_tab()
        return True

    @log_decorator
    def employee_information(self):
        query = '''
        SELECT c.name, d.name, e.full_name
        FROM employee e
        INNER JOIN department d on e.DEPARTMENT_ID = d.ID
        INNER JOIN company c on c.ID = d.COMPANY_ID;
        '''
        result_exc = execute_query(query, fetch='all')
        pagination = Pagination(table_name='users', table_keys=[0, 1, 2],
                                display_keys=['Company name', 'Department name', 'Employees'],
                                data=result_exc)
        pagination.page_tab()
        return True
