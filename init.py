from flask import Flask,render_template,request
#from flask_mysqldb import MySQL
#import private
from colorama import Fore

port = 5000

app = Flask(__name__)
#app.config['MYSQL_HOST'] = private.sql_host
#app.config['MYSQL_USER'] = private.sql_username
#app.config['MYSQL_PASSWORD'] = private.sql_password
#app.config['MYSQL_DB'] = private.sql_dbname

###mysql = MySQL(app)

def GetViews():
    return 0
#    query = f"select count(*) from {private.sql_tablename}"
#    cur = mysql.connection.cursor()
#    cur.execute(query)
#    mysql.connection.commit()
#    data = cur.fetchall()
#    cur.close()
#    return data[0][0]
#

def AddView(ipaddr):
    return 0
    #cur = mysql.connection.cursor()
    #try: 
    #    cur.execute(f"INSERT INTO {private.sql_tablename} ({private.sql_columnname}) VALUES(%s)",[private.hideIP(ipaddr)])
    #    mysql.connection.commit()
    #except Exception as ex:
    #    print(ex)
    #    pass
    #cur.close()
    #print(Fore.GREEN + f"Incoming connection from: {ipaddr}" +Fore.WHITE)

@app.route('/')
def Home():
    AddView(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    return render_template('index.html',views=GetViews())

@app.route('/certificates/')
def Certs():
    AddView(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    return render_template('certs.html',views=GetViews())

@app.route('/certificates/<certname>')
def ShowCert(certname):
    AddView(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    if certname == "jusoor":
        imgurl = "https://www.simplilearn.com/ice9/certificates/MIT-SCC_certificate.jpg"
        return f'<img src="{imgurl}" width=50% height=50% style="position:relative;left:25%;top:25%"/>'
    return 'Invalid certificate name!'

@app.route('/contact/')
def Contact():
    AddView(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    return render_template('contact.html',views=GetViews())

@app.route('/hack/')
def HackSquare():
    AddView(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    return render_template('hack.html',views=GetViews())


@app.route('/flag/')
def GetFlag():
    AddView(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    return 'U3F1YXIze1doNHRfNF9XMzFyZDB9'


for i in (500,404,403):
    @app.errorhandler(i)
    def PageNotFound404(er):
        ercode = str(er)[0:3]
        return render_template('error.html',errorCode=ercode)

if __name__ == "__main__" and False: # Change True to False if you don't want to run the script by default
    print(Fore.YELLOW + f"Website started on port {port}\n" +Fore.WHITE)
    app.run(debug=True,port=port)
    
