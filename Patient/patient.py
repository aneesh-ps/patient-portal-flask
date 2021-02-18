from Database import database

class patient():
    def patient_id_create():
        patient_id_create_status=database.database.create_id(table_name="patients")
        return patient_id_create_status

    def add_patient(patient_name,patient_age,patient_gender,doctor_name,department_name):
        department_search_status=database.database.search(table_name='departments',department_name=department_name)
        if len(department_search_status["error"])!=0:
            return department_search_status
        else:
            department_name_to_add=department_search_status["value"][0]["department_name"]
            department_id_to_add=department_search_status["value"][0]["department_id"]
        
        doctor_search_status=database.database.search(table_name='doctors',doctor_name=doctor_name,department_id=department_id_to_add)
        if len(doctor_search_status["error"])!=0:
            return doctor_search_status
        else:
            doctor_name_to_add=doctor_search_status["value"][0]["doctor_name"]
            patient_id_to_add=patient.patient_id_create()
        patient_add_status=database.database.add(table_name="patients",patient_id=patient_id_to_add,patient_name=patient_name,department_name=department_name_to_add,doctor_name=doctor_name_to_add,age=patient_age,gender=patient_gender)
        return patient_add_status

    def remove_patient(patient_id_to_remove):
        patient_remove_status=database.database.remove(table_name='patients',patient_id=patient_id_to_remove)
        return patient_remove_status

    def edit_patient(value_indicators,new_values):

        department_search_status=database.database.search(table_name='departments',department_name=new_values["department_name"])
        if len(department_search_status["error"])!=0:
            return department_search_status
        else:
            new_values["department_name"]=department_search_status["value"][0]["department_name"]
            department_id_to_add=department_search_status["value"][0]["department_id"]
        
        doctor_search_status=database.database.search(table_name='doctors',doctor_name=new_values["doctor_name"],department_id=department_id_to_add)
        if len(doctor_search_status["error"])!=0:
            return doctor_search_status
        else:
            new_values["doctor_name"]=doctor_search_status["value"][0]["doctor_name"]


        patient_edit_status=database.database.edit(table_name='patients',value_indicators=value_indicators,values_to_update=new_values)
        return patient_edit_status

    def search_patient_id(patient_id_to_search):
        patient_search_status=database.database.search(table_name='patients',patient_id=patient_id_to_search)
        return patient_search_status

    def search_patient_name(patient_name_to_search):
        patient_search_status=database.database.search(table_name='patients',patient_name=patient_name_to_search)
        return patient_search_status

    def search_all_patients():
        patients_search_all_status=database.database.search(table_name='patients')
        return patients_search_all_status

    def search_patient_department_name(department_name_to_search):
        department_search_status=database.database.search(table_name="departments",department_name=department_name_to_search)
        if len(department_search_status["error"])!=0:
            return department_search_status
        else:
            patient_search_department_name=database.database.search(table_name="patients",department_name=department_name_to_search)
            return patient_search_department_name


    def search_patient_doctor_name(doctor_name_to_search):
        doctor_search_status=database.database.search(table_name="doctors",doctor_name=doctor_name_to_search)
        if len(doctor_search_status["error"])!=0:
            return doctor_search_status
        else:
            patient_search_doctor_name=database.database.search(table_name="patients",doctor_name=doctor_name_to_search)
            return patient_search_doctor_name

    def search_patient_department_name_doctor_name(department_name_to_search,doctor_name_to_search):
        doctor_search_status=database.database.search(table_name="doctors",doctor_name=doctor_name_to_search)
        department_search_status=database.database.search(table_name="departments",department_name=department_name_to_search)
        if len(doctor_search_status["error"])!=0:
            return doctor_search_status
        
        if len(department_search_status["error"])!=0:
            return department_search_status
        
        patient_search_doctor_name_status=database.database.search(table_name="patients",doctor_name=doctor_name_to_search,department_name=department_name_to_search)

        return patient_search_doctor_name_status