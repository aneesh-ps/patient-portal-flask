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
            f.write("{'hospital_name':"+hospital_name+" ,'departments':[],'doctors':[],'patients':[]}")
            f.close()
            if os.path.exists("D:\\feather soft\\patient_portal_flask_project\\patient-portal-flask\\Database\\Database.txt") == True:
                return {"success":messages.success_message.success("database","database creation")}
            else:
                return {"error":messages.error_message.error("database","database creation")}
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
        return messages.success_message.success("database","database write")


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
            success_message=messages.success_message.success(table_name,"add")
            return_values=values
        else:
            error_message=messages.error_message.error(table_name,"add")

        return ({"success":success_message,"error":error_message,"values":return_values})



    def remove(**values):
        success_message=""
        error_message=""
        return_value=""
        database_value_all=database.database_read(database)
        table_name=values["table_name"]
        del values["table_name"]
        
        for item in database_value_all[table_name]:
            if set(values.items()).issubset(set(item.items())):
                database_value_all[table_name].remove(item)
                success_message=messages.success_message.success(table_name,"remove")
                database.database_write(database,database_value_all)
                return_value=item
                return({"error":error_message,"success":success_message,"values":return_value})
        error_message=messages.error_message.error(table_name,"remove")
        return ({"error":error_message,"success":success_message,"values":return_value})

            

    
           

    
    

    def search(**values):
        success_message=""
        error_message=""
        return_value=[]
        database_value_all=database.database_read(database)
        table_name=values["table_name"]
        del values["table_name"]
        for item in database_value_all[table_name]:
            if set(values.items()).issubset(set(item.items())):
                success_message=messages.success_message.success(table_name,"search")
                return_value.append(item)
        if len(return_value)!=0:
            return {"error":error_message,"success":success_message,"value":return_value}
        error_message=messages.error_message.error(table_name,"search")
        return {"error":error_message,"success":success_message,"value":return_value}
            

    def edit(**values):
        success_message=""
        error_message=""
        value_to_return=""
        database_value_all=database.database_read(database)
        table_name=values["table_name"]
        value_indicators=values["value_indicators"]
        values_to_update=values["values_to_update"]
        for item in database_value_all[table_name]:
            if set(value_indicators.items()).issubset(set(item.items())):
                for key_value_to_update,value_value_to_update in values_to_update.items():
                    for key_item,value_item in item.items():
                        if key_item==key_value_to_update:  
                           item[key_item]=values_to_update[key_item]
                           success_message=messages.success_message.success(table_name,"edit")
                           database.database_write(database,database_value_all)
                           value_to_return=item
                return ({"success":success_message,"error":error_message,"values":value_to_return})
        error_message=messages.error_message.error(table_name,"edit")
        return ({"success":success_message,"error":error_message,"values":value_to_return})
                

    
    def create_id(**values):
        id=""
        error_message=""
        database_value_all=database.database_read(database)
        table_name=values["table_name"]
        success_message=messages.success_message.success(table_name,"id creation")
        try:
            if len(database_value_all[table_name])==0:
                largest_id=len(database_value_all[table_name])+1
                largest_id=table_name[0:-1]+"_id_"+str(largest_id)
            else:
                item=database_value_all[table_name][-1]
                for key_item,value_item in item.items():
                    id_identifier=table_name[0:-1]+"_id_"
                    largest_id=value_item.split(id_identifier,1)[1]
                    largest_id=int(largest_id)+1
                    largest_id=table_name[0:-1]+"_id_"+str(largest_id)
                        
        except:
            success_message=""
            error_message=messages.error_message.error(table_name,"id creation")
        # return{"error":error_message,"success":success_message,table_name[:-1]+"_id ":largest}
        return str(largest_id)


        




        
        

    
       
