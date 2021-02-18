from flask import Flask,request
from flask.wrappers import Request
from Database import database 
from Department import department
from Doctor import doctor
from Patient import patient
from Hospital import hospital

app=Flask(__name__)

@app.route('/add_new_account',methods=['POST'])    #{"hospital_name": "hospital1"}
def add_new_account():
    req=request.get_json()
    hospital_name=req["hospital_name"]
    hospital_obj=hospital.hospital(hospital_name)
    res=database.database.database_existance_check_and_create_database(hospital_obj)
    return res



@app.route('/add_department',methods=['POST'])   #{"department_name": "department1"}
def add_department():
    req=request.get_json()
    department_name_to_add=req["department_name"]
    res=department.department.add_department(department_name_to_add)
    return res

@app.route('/remove_department',methods=['POST'])   #{"department_id": "department_id_2"}  
def remove_department():
    req=request.get_json()
    department_id_to_remove=req["department_id"]
    res=department.department.remove_department(department_id_to_remove)
    return res

@app.route('/edit_department',methods=['POST'])  #{"value_indicator":{"department_id": "department_id_1"},"values_to_update":{"department_name": "department_2.1"}}
def edit_department():
    req=request.get_json()
    value_indicator_to_edit=req["value_indicator"]
    values_to_update=req["values_to_update"]
    res=department.department.edit_department(value_indicator_to_edit,values_to_update)
    return res

@app.route('/search_department_id',methods=['POST'])  #{"department_id":"department_id_2"}
def search_department_id():
    req=request.get_json()
    department_id_to_search=req["department_id"]
    res=department.department.search_department_id(department_id_to_search)
    return res

@app.route('/search_department_name',methods=['POST'])  #{"department_name": "department_1"}
def search_department_name():
    req=request.get_json()
    department_name_to_search=req["department_name"]
    res=department.department.search_department_name(department_name_to_search)
    return res


@app.route('/search_all_departments',methods=['POST'])
def search_all_departments():
    res=department.department.search_all_department()
    return res
    


 #doctor

@app.route('/add_doctor',methods=['POST'])  #{"department_name":"department1","doctor_name":"doctor1"}
def add_doctor():
    req=request.get_json()
    doctor_name_to_add=req["doctor_name"]
    department_name_to_add=req["department_name"]
    res=doctor.doctor.add_doctor(doctor_name_to_add,department_name_to_add)
    return res

@app.route('/remove_doctor',methods=['POST']) #{"doctor_id": "doctor_id_1"}
def remove_doctor():
    req=request.get_json()
    doctor_id_to_remove=req["doctor_id"]
    res=doctor.doctor.remove_doctor(doctor_id_to_remove)
    return res

@app.route('/edit_doctor',methods=['POST'])  #{"value_indicator":{"doctor_id": "doctor_id_1"},"values_to_update":{"doctor_name": "doctor_name_edited",deprtment_id:"department_id_edited"}}
def edit_doctor():
    req=request.get_json()
    value_indicator_to_edit=req["value_indicator"]
    values_to_update=req["values_to_update"]
    res=doctor.doctor.edit_doctor(value_indicator_to_edit,values_to_update)
    return res

@app.route('/search_doctor_id',methods=['POST'])   #{"doctor_id": "doctor_id_1"}
def search_doctor_id():
    req=request.get_json()
    doctor_id_to_search=req["doctor_id"]
    res=doctor.doctor.search_doctor_id(doctor_id_to_search)
    return res   


@app.route('/search_doctor_name',methods=['POST'])   #{"doctor_name": "doctor_1"}
def search_doctor_name():
    req=request.get_json()
    doctor_name_to_search=req["doctor_name"]
    res=doctor.doctor.search_doctor(doctor_name_to_search)
    return res
 

@app.route('/search_all_doctors',methods=['POST'])
def search_all_doctors():
    res=doctor.doctor.search_all_doctor()
    return res

@app.route('/search_all_doctors_department_id',methods=['POST'])
def search_all_doctors_department_id():
    req=request.get_json()
    department_id=req["department_id"]
    res=doctor.doctor.search_all_doctors_department_id(department_id)
    return res

@app.route('/search_all_doctors_department_name',methods=['POST'])
def search_all_doctors_department_name():
    req=request.get_json()
    department_name=req["department_name"]
    res=doctor.doctor.search_all_doctors_department_name(department_name)
    return res

#patient

@app.route('/add_patient',methods=['POST'])  #{"patient_name":"aneesh","patient_age":21,"patient_gender":"male","doctor_name":"doctor_1","department_name":"department_1"}
def add_patient():
    req=request.get_json()
    patient_name_to_add=req["patient_name"]
    doctor_name_to_add=req["doctor_name"]
    department_name_to_add=req["department_name"]
    patient_age_to_add=req["patient_age"]
    patient_gender_to_add=req["patient_gender"]
    res=patient.patient.add_patient(patient_name_to_add,patient_age_to_add,patient_gender_to_add,doctor_name_to_add,department_name_to_add)
    return res

@app.route('/remove_patient',methods=['POST'])  #{"patient_id":"patient_id_1"}
def remove_patient():
    req=request.get_json()
    patient_id_to_add=req["patient_id"]
    res=patient.patient.remove_patient(patient_id_to_add)
    return res

@app.route('/edit_patient',methods=['POST'])  #{"value_indicator":{"patient_id": "patient_id_1"},"values_to_update":{"patient_name":"aneesh_edited","patient_age":21,"patient_gender":"male","doctor_name":"doctor_1","department_name":"department_1"}}
def edit_patient():
    req=request.get_json()
    value_indicator_to_edit=req["value_indicator"]
    values_to_update=req["values_to_update"]
    res=patient.patient.edit_patient(value_indicator_to_edit,values_to_update)
    return res

@app.route('/search_patient_id',methods=['POST'])  #{"patient_id":"patient_id_1"}
def search_patient_id():
    req=request.get_json()
    patient_id_to_search=req["patient_id"]
    res=patient.patient.search_patient_id(patient_id_to_search)
    return res

@app.route('/search_patient_name',methods=['POST'])  #{"patient_name": "aneesh_edited"}
def search_patient_name():
    req=request.get_json()
    patient_name_to_search=req["patient_name"]
    res=patient.patient.search_patient_name(patient_name_to_search)
    return res


@app.route('/search_all_patients',methods=['POST'])  #{"patient_id":"patient_id_1"}
def search_all_patients():
    res=patient.patient.search_all_patients()
    return res


@app.route('/search_patient_department_name',methods=['POST'])  #{"department_name": "department_1"}
def search_patient_department_name():
    req=request.get_json()
    department_name_to_search=req["department_name"]
    res=patient.patient.search_patient_department_name(department_name_to_search)
    return res

@app.route('/search_patient_doctor_name',methods=['POST'])  #{"doctor_name": "doctor_1"}
def search_patient_doctor_name():
    req=request.get_json()
    doctor_name_to_search=req["doctor_name"]
    res=patient.patient.search_patient_doctor_name(doctor_name_to_search)
    return res

@app.route('/search_patient_department_name_doctor_name',methods=['POST'])  #{"doctor_name": "doctor_1","department_name": "department_1"}
def search_patient_department_name_doctor_name():
    req=request.get_json()
    department_name_to_search=req["department_name"]
    doctor_name_to_search=req["doctor_name"]
    res=patient.patient.search_patient_department_name_doctor_name(department_name_to_search,doctor_name_to_search)
    return res


  


if __name__=="__main__":
    app.run(debug=True)