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
    department_name=req["department_name"]
    res=department.department.add_department(department_name)
    return res

@app.route('/remove_department',methods=['POST'])   #{"department_id": "department_id_2"}  
def remove_department():
    req=request.get_json()
    department_id=req["department_id"]
    res=department.department.remove_department(department_id)
    return res

@app.route('/edit_department',methods=['POST'])  #{"value_indicator":{"department_id": "department_id_2.1"},"values_to_update":{"department_name": "department_2.1"}}
def edit_department():
    req=request.get_json()
    value_indicator=req["value_indicator"]
    values_to_update=req["values_to_update"]
    res=department.department.edit_department(value_indicator,values_to_update)
    return res

@app.route('/search_department',methods=['POST'])  #{"department_id":"department_id_2"}
def search_department():
    req=request.get_json()
    department_id=req["department_id"]
    res=department.department.search_department(department_id)
    return res
    


 #doctor

@app.route('/add_doctor',methods=['POST'])  #{"department_name":"department1","doctor_name":"doctor1"}
def add_doctor():
    req=request.get_json()
    doctor_name=req["doctor_name"]
    department_name=req["department_name"]
    res=doctor.doctor.add_doctor(doctor_name,department_name)
    return res

@app.route('/remove_doctor',methods=['POST']) #{"doctor_id": "doctor_id_1"}
def remove_doctor():
    req=request.get_json()
    doctor_id=req["doctor_id"]
    res=doctor.doctor.remove_doctor(doctor_id)
    return res

@app.route('/edit_doctor',methods=['POST'])  #{"value_indicator":{"doctor_id": "doctor_id_1"},"values_to_update":{"doctor_name": "doctor_name_edited"}}
def edit_doctor():
    req=request.get_json()
    value_indicator=req["value_indicator"]
    values_to_update=req["values_to_update"]
    res=doctor.doctor.edit_doctor(value_indicator,values_to_update)
    return res

@app.route('/search_doctor',methods=['POST'])   #{"doctor_id": "doctor_id_1"}
def search_doctor():
    req=request.get_json()
    doctor_id=req["doctor_id"]
    res=doctor.doctor.search_doctor(doctor_id)
    return res   

#patient

@app.route('/add_patient',methods=['POST'])  
def add_patient():
    # req=request.get_json()
    res=patient.patient.add_patient()
    return res

@app.route('/remove_patient',methods=['POST'])  
def remove_patient():
    # req=request.get_json()
    res=patient.patient.remove_patient()
    return res

@app.route('/edit_patient',methods=['POST'])  
def edit_patient():
    # req=request.get_json()
    res=patient.patient.edit_patient()
    return res

@app.route('/search_patient',methods=['POST'])  
def search_patient():
    # req=request.get_json()
    res=patient.patient.search_patient()
    return res

  


if __name__=="__main__":
    app.run(debug=True)