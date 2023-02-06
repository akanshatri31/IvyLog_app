from flask import Flask, request
from datetime import date, time, datetime
import mysql.connector
from mysql import connector
from credentials import DBcredential

app = Flask(__name__)

DBcredential['username'] 
row_search = ''

try:
    db = mysql.connector.connect(host="localhost",  
                    user=DBcredential['username'] ,    
                    passwd=DBcredential['password'] , 
                    db="db_ivy_app")        # name of the data base
    
    if (db.is_connected()):
        cursor = db.cursor()
        print("Connected to MySQL Server version",db.get_server_info())
except Exception as e1:
    print(" Error while connecting to DB", e1)
##
## END POINT TO GET LOGS FOR THE CLIENT 
## USING PAGE NO. (OTPIONAL), EVENT_TYPE(OTIOPNAL), SEARCH_TEXT(OPTIONAL)

@app.route('/get_logs')
def get_logs():
    input_page_num = request.args.get('page')
    input_event_type = request.args.get('event')
    input_search_text = request.args.get('search')

    if input_page_num == None:
        input_page_num = 1
    page_index = 20 * (int(input_page_num) - 1)  #paging to fetch pages as per page number i.e. 20 per pages.

#When search text is used to find the logs and event is blank
    if input_search_text != None and input_event_type == None:
       search_query = f'select a.log_id, a.timestamp, a.log_description, b.device_icon, b.device_name, c.event_name from device_table b right join log_table a on a.device_id = b.device_id right join event_table c on a.event_type_id = c.event_id where b.device_name = "{input_search_text}" limit {page_index}, 20;'

#When event is used to find the logs and search text is blank
    if input_event_type != None and input_search_text == None:
        search_query = f'select a.log_id, a.timestamp, a.log_description, b.device_icon, b.device_name, c.event_name from log_table a join device_table b on a.device_id = b.device_id right join event_table c on a.event_type_id = c.event_id where c.event_name  = "{input_event_type}"  order by a.timestamp desc  limit {page_index}, 20;'

#When event and search text both are used
    if input_search_text and input_event_type != None:
        search_query = f'select a.log_id, a.timestamp, a.log_description, b.device_icon, b.device_name, c.event_name from log_table a left join device_table b on a.device_id = b.device_id left join event_table c on a.event_type_id = c.event_id where c.event_name = "{input_event_type}" and b.device_name = "{input_search_text}"  order by a.timestamp desc limit {page_index}, 20;'

#When only page no is used for logs
    if input_event_type == None and input_search_text == None and input_page_num != None:
        search_query = f"select a.log_id, a.timestamp, a.log_description, b.device_icon, b.device_name, c.event_name from log_table a join device_table b on a.device_id = b.device_id join event_table c on a.event_type_id = c.event_id order by a.timestamp desc limit {page_index}, 20 ;"
 
    return execute_sql(search_query)

def execute_sql(search_query):
    
    try:
        cursor.execute(search_query)
        row_search = cursor.fetchall()
        ret_dict = dict()
        if cursor.rowcount != 0:
            for key in row_search:
                idx_datetime = key[1].strftime('%Y-%m-%d')
                temp_dict = {}
                temp_dict["log_desc"] = key[2]
                temp_dict["device_name"] = key[4]
                temp_dict["device_icon"] = key[3]
                temp_dict["event_name"] = key[5]
                temp_dict["timestamp"] = key[1].strftime('%Y-%m-%d %H:%M:%S')
                if ret_dict.get(idx_datetime) != None:
                    ret_dict[idx_datetime].append(temp_dict)
                else:
                    ret_dict[idx_datetime] = []
                    ret_dict[idx_datetime].append(temp_dict)
   
            return ret_dict
        else:
          return('No more result found or End of the logs')
    except Exception as E1:
        print(str(E1))
    return('Problem with DB query, try again!')
