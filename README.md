<h2>Create a file called <em>private.py</em> and write this inside it </h2>

```py
import hashlib

sql_host = "localhost"
sql_username = "username"
sql_password = "password"
sql_dbname = "dbName"
sql_tablename = "tableName"
sql_columnname = "columnName" #The ip-column needs to be VarChar(255)

#Ofcourse you will use another method to hide the ip
#Maybe encrypt it or do something better to make it more secure

def hideIP(ipaddr): 
    return hashlib.md5(ipaddr.encode('UTF-8').hexdigest())
 ```
 <h4>To install the modules (make sure python is installed)</h4>
 
 ```
pip -r requirements.txt
 ```
 
 <h4>To run the app</h4>
 
 ```
 python init.py
 ```
 
