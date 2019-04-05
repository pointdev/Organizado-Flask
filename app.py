from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
#from flask_heroku import Heroku
#heroku = Heroku(app)

#import yaml

app = Flask(__name__)

#configure db
#db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = 'fnx6frzmhxw45qcb.cbetxkdyhwsb.us-east-1.rds.amazonaws.comhost'
app.config['MYSQL_USER'] = 'ophmvxggd70qi4hx'
app.config['MYSQL_PASSWORD'] = 'lxv5byb85vydqsnu'
app.config['MYSQL_DB'] = 's80s1c8qqx6rqp2o'

mysql = MySQL(app)

@app.route('/')
def index():
    return redirect('/home')

#@app.route('/', methods=['GET', 'POST'])
#def index():
#
#    if request.method == 'POST':
#        #Fetch form data
#        userDetails = request.form
#        name = userDetails['name']
#        email = userDetails['email']
#        cur = mysql.connection.cursor()
#        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
#        mysql.connection.commit()
#        cur.close()
#        return redirect('/users')
#    return render_template('index.html')

#@app.route('/users')
#def users():
#    cur = mysql.connection.cursor()
#    resultValue = cur.execute("SELECT * FROM users")
#    if resultValue > 0:
#        userDetails = cur.fetchall()
#        return render_template('users.html',userDetails=userDetails)

#ESCUELA==============================================================
@app.route('/crearEscuela', methods=['GET', 'POST'])
def crearEscuela():

    if request.method == 'POST':
        #Fetch form data
        escuelaDetails = request.form
        nombre = escuelaDetails['nombre']
        disciplina = escuelaDetails['disciplina']
        instructorPrincipal = escuelaDetails['instructorPrincipal']
        pueblo = escuelaDetails['pueblo']

        if (pueblo == '') or (instructorPrincipal == '') or (disciplina == '') or (nombre == ''):
            return redirect ('/crearEscuelas')
        else:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO escuela(nombre,disciplina, instructorPrincipal, pueblo) VALUES(%s, %s,%s, %s)",(nombre,disciplina, instructorPrincipal, pueblo))
            mysql.connection.commit()
            cur.close()
            return redirect('/escuelas')
    return render_template('crearEscuela.html')

@app.route('/escuelas')
def escuelas():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM escuela")
    if resultValue > 0:
        escuelaDetails = cur.fetchall()
        return render_template('escuelas.html',escuelaDetails=escuelaDetails)



#ESTUDIANTE ==================================================================
@app.route('/crearEstudiante', methods=['GET', 'POST'])
def crearEstudiante():

    if request.method == 'POST':
        #Fetch form data
        estudianteDetails = request.form
        nombre = estudianteDetails['nombre']
        apellido1 = estudianteDetails['apellido1']
        apellido2 = estudianteDetails['apellido2']
        cinta = estudianteDetails['cinta']
        edad = estudianteDetails['edad']
        escuela = estudianteDetails['escuela']
        codigoParticipacion = estudianteDetails['codigoParticipacion']

        if (nombre == '') or (cinta == '') or (codigoParticipacion == '') or (edad == ''):
            return redirect ('/crearEstudiante')
        else:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO estudiante(nombre, apellido1, apellido2, cinta, edad, escuela, codigoParticipacion) VALUES(%s, %s, %s, %s, %s, %s, %s)",(nombre,apellido1, apellido2, cinta, edad, escuela, codigoParticipacion))
            mysql.connection.commit()
            cur.close()
            return redirect('/estudiantes')
    return render_template('crearEstudiante.html')

@app.route('/estudiantes')
def estudiantes():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM estudiante")
    if resultValue > 0:
        estudianteDetails = cur.fetchall()
        return render_template('estudiantes.html',estudianteDetails=estudianteDetails)



#CODIGO PARTICIPACION===============================================
@app.route('/codigoParticipacion')
def codigoParticipacion():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM codigoParticipacion")
    if resultValue > 0:
        codigoDetails = cur.fetchall()
        return render_template('codigoParticipacion.html',codigoDetails=codigoDetails)

#======================================================
@app.route('/about')
def about():
        return render_template('about.html')


@app.route('/home')
def home():
        return render_template('home.html')

#=============================================================================
if __name__ == '__main__':
    app.run(debug=True)
