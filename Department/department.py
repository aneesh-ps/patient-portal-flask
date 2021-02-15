from Database import database

class department():
    def department_id_create():
        department_id_create_status=database.database.create_id(table_name="departments")
        return department_id_create_status

    def add_department(department_name):
        department_id=department.department_id_create()
        department_add_status=database.database.add(table_name ='departments',department_id=department_id,department_name =department_name)
        return department_add_status

    def remove_department(department_id_to_remove):
        department_remove_status=database.database.remove(table_name='departments',department_id=department_id_to_remove)
        return department_remove_status

    def edit_department(value_indicators,new_values):
        department_edit_status=database.database.edit(table_name='departments',value_indicators=value_indicators,values_to_update=new_values)
        return department_edit_status

    def search_department(department_id_to_search):
        department_search_status=database.database.search(table_name='departments',department_id=department_id_to_search)
        return department_search_status


