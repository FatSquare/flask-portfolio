from flask import Flask,redirect,render_template,request,url_for
from colorama import Fore
import flaskpdf
port = 5000

app = Flask(__name__)
flaskpdf.init_app(app)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/certificates/')
def Certs():
    return render_template('certs.html')

@app.route('/certificates/<certname>')
def ShowCert(certname):
    if certname == "jusoor":
        return  redirect(url_for('static',filename='certs/Ayoub-Hedri-certificate.pdf'))
    return 'Invalid certificate name!'

@app.route('/contact/')
def Contact():
    return render_template('contact.html')

@app.route('/hack/')
def HackSquare():
    return render_template('hack.html')


@app.route('/flag/')
def GetFlag():
    return 'U3F1YXIze1doNHRfNF9XMzFyZDB9'


for i in (500,404,403):
    @app.errorhandler(i)
    def PageNotFound404(er):
        ercode = str(er)[0:3]
        return render_template('error.html',errorCode=ercode)

if __name__ == "__main__" and True: # Change True to False if you don't want to run the script by default
    print(Fore.YELLOW + f"Website started on port {port}\n" +Fore.WHITE)
    app.run(debug=True,port=port)
    
