from Database import database
class doctor():
    def doctor_id_create():
        doctor_id_create_status=database.database.create_id(table_name="doctors")
        return doctor_id_create_status

    def add_doctor(doctor_name,department_name):
        department_search_status=database.database.search(table_name='departments',department_name=department_name)
        if len(department_search_status["error"])!=0:
            return department_search_status
        else:
            doctor_id_to_add=doctor.doctor_id_create()
            department_id_to_add=department_search_status["value"][0]["department_id"]
            doctor_add_status=database.database.add(table_name='doctors',doctor_name=doctor_name,department_id=department_id_to_add,doctor_id=doctor_id_to_add)
            return doctor_add_status

    def remove_doctor(doctor_id_to_remove):
        doctor_remove_status=database.database.remove(table_name='doctors',doctor_id=doctor_id_to_remove)
        return doctor_remove_status

    def edit_doctor(value_indicators,new_values):
        department_search_status=database.database.search(table_name='departments',department_id=new_values["deprtment_id"])
        if len(department_search_status["error"])!=0:
            return department_search_status
        else:
            doctor_edit_status=database.database.edit(table_name='doctors',value_indicators=value_indicators,values_to_update=new_values)
            return doctor_edit_status

    def search_doctor_id(doctor_id_to_search):
        doctor_search_status=database.database.search(table_name='doctors',doctor_id=doctor_id_to_search)
        return doctor_search_status

    def search_doctor_name(doctor_name_to_search):
        doctor_search_status=database.database.search(table_name='doctors',doctor_name=doctor_name_to_search)
        return doctor_search_status

    def search_all_doctor():
        doctor_search_all_status=database.database.search(table_name='doctors')
        return doctor_search_all_status
    
    def search_all_doctors_department_id(department_id_to_search):
        doctor_search_all_department_id_status=database.database.search(table_name='doctors',department_id=department_id_to_search)
        return doctor_search_all_department_id_status

    def search_all_doctors_department_name(department_name_to_search):
        department_name_search_status=database.database.search(table_name='departments',department_name=department_name_to_search)
        if (department_name_search_status["error"])==0:
            return department_name_search_status
        else:
            doctor_search_all_department_name_status=database.database.search(table_name='doctors',department_id=department_name_search_status["value"][0]["department_id"])
            return doctor_search_all_department_name_status


