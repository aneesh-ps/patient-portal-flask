from Database import database

class department():
    def __init__(self,department_name):
        self.department_name=department_name

    def add_department(self):
        status=database.database.add(table_name ='Departments',name =self.department_name)
        return status

    def remove_department(self):
        status=database.database.remove(table_name='Departments',name=self.department_name)
        return status

    def edit_department():
        status={"status":"Department edited successfully"}
        return status

    def search_department(self):
        status=database.database.search(table_name='Departments',name=self.department_name)
        return status


