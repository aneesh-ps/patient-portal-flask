import os
import json
from Hospital import hospital
from Message import messages

class database():
    def database_existance_check_and_create_database(hospital_obj):
        if os.path.exists("D:\\feather soft\\patient_portal_flask_project\\patient-portal-flask\\Database\\Database.txt") ==False:
            hospital_name=hospital_obj.hospital_name
            hospital_name='"'+hospital_name+'"'
            f = open("D:\\feather soft\\patient_portal_flask_project\\patient-portal-flask\\Database\\Database.txt", "w")
            f.write("{'Hospital_name':"+hospital_name+" ,'Departments':[],'Doctors':[],'Patients':[]}")
            f.close()
            if os.path.exists("D:\\feather soft\\patient_portal_flask_project2\\patient-portal-flask\\Database\\Database.txt") == True:
                return messages.success_message.success("database creation")
            else:
                return messages.error_message.error("database creation")
        else:
            return {"status":"database already exists"}

    
    def database_read(self):
        f=open("D:\\feather soft\\patient_portal_flask_project\\patient-portal-flask\\Database\\Database.txt", "r")
        return eval(f.read())

    def add(**values):
        database_value_all=database.database_read(database)
        table_name=values["table_name"]
        del values["table_name"]
        database_value_all[table_name].append(values) 
        return (database_value_all)

        
        

    
       
