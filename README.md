<h1>Create a file called `private.py` and set it to something like that </h1>

```

import hashlib

sql_host = "localhost"
sql_username = "username"
sql_password = "password"
sql_dbname = "dbName"
sql_tablename = "tableName"
sql_columnname = "columnName" #The ip-column needs to be VarChar(255)

#Ofcourse you will use another method to hide the ip maybe encrypt it or do something better to make it more secure I won't share my way

def hideIP(ipaddr): 
    return hashlib.md5(ipaddr.encode('UTF-8').hexdigest())
  
 ```
