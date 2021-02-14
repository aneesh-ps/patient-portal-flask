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
            if os.path.exists("D:\\feather soft\\patient_portal_flask_project\\patient-portal-flask\\Database\\Database.txt") == True:
                return {"success":messages.success_message.success("database creation")}
            else:
                return {"error":messages.error_message.error("database creation")}
        else:
            return {"error":"database already exists"}

    
    def database_read(self):
        f=open("D:\\feather soft\\patient_portal_flask_project\\patient-portal-flask\\Database\\Database.txt", "r")
        value=eval(f.read())
        f.close()
        return value

    
    def database_write(self,database_value_all):
        f=open("D:\\feather soft\\patient_portal_flask_project\\patient-portal-flask\\Database\\Database.txt", "w")
        f.write(json.dumps(database_value_all))
        f.close()
        return messages.success_message.success("database write")


    def add(**values):
        success_message=""
        error_message=""
        return_values=""
        database_value_all=database.database_read(database)
        table_name=values["table_name"]
        del values["table_name"]
        database_value_all[table_name].append(values)
        database.database_write(database,database_value_all) 
        if len(database_value_all)==len(database.database_read(database)):
            success_message=messages.success_message.success("add")
            return_values=values
        else:
            error_message=messages.error_message.error("add")

        return ({"success":success_message,"error":error_message,"values":return_values})



    def remove(**values):
        success_message=""
        error_message=""
        return_value=""
        database_value_all=database.database_read(database)
        table_name=values["table_name"]
        del values["table_name"]
        success_message=messages.success_message.success("remove")
        try:
            database_value_all[table_name].remove(values)
        except:
            error_message=messages.error_message.error("remove")
            success_message=""
        
        database.database_write(database,database_value_all)
        return_value=values
        return ({"success":success_message,"error":error_message,"value":return_value})


    
    

    def search(**values):
        success_message=""
        error_message=""
        return_value=""
        database_value_all=database.database_read(database)
        table_name=values["table_name"]
        del values["table_name"]
        for item in database_value_all[table_name]:
            if all((k in values and values[k]==v) for k,v in item.items()):
                success_message=messages.success_message.success("search")
                return_value=item
                return {"error":error_message,"success":success_message,"value":return_value}
        error_message=messages.error_message.error("search")
        return {"error":error_message,"success":success_message,"value":return_value}



        
        

    
       
