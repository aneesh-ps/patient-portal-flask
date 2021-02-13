from flask import Flask,request
from Database import database 
from Department import department
from Doctor import doctor
from Patient import patient
from Hospital import hospital

app=Flask(__name__)

@app.route('/add_new_account',methods=['POST'])
def add_new_account():
    req=request.get_json()
    hospital_name=req["hospital_name"]
    hospital_obj=hospital.hospital(hospital_name)
    res=database.database.database_existance_check_and_create_database(hospital_obj)
    return res



@app.route('/add_department',methods=['POST'])  
def add_department():
    req=request.get_json()
    department_name=req["department_name"]
    department_obj=department.department(department_name)
    res=department.department.add_department(department_obj)
    return res

@app.route('/remove_department',methods=['POST'])  
def remove_department():
    # req=request.get_json()
    res=department.department.remove_department()
    return res

@app.route('/edit_department',methods=['POST'])  
def edit_department():
    # req=request.get_json()
    res=department.department.edit_department()
    return res

@app.route('/search_department',methods=['POST'])  
def search_department():
    # req=request.get_json()
    res=department.department.search_department()
    return res


 #doctor

@app.route('/add_doctor',methods=['POST'])  
def add_doctor():
    # req=request.get_json()
    res=doctor.doctor.add_doctor()
    return res

@app.route('/remove_doctor',methods=['POST'])  
def remove_doctor():
    # req=request.get_json()
    res=doctor.doctor.remove_doctor()
    return res

@app.route('/edit_doctor',methods=['POST'])  
def edit_doctor():
    # req=request.get_json()
    res=doctor.doctor.edit_doctor()
    return res

@app.route('/search_doctor',methods=['POST'])  
def search_doctor():
    # req=request.get_json()
    res=doctor.doctor.search_doctor()
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