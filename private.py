import hashlib

sql_host = "localhost"
sql_username = "squar3wiki"
sql_password = "1l1k3myw1k1"
sql_dbname = "wiki"
sql_tablename = "wiki"
sql_columnname = "viewer"

def hideIP(ipaddr):
    return hashlib.sha512((hashlib.md5(str(ipaddr).encode('UTF-8')).hexdigest()).encode('UTF-8')).hexdigest()