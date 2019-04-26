from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'fnx6frzmhxw45qcb.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'ophmvxggd70qi4hx'
app.config['MYSQL_PASSWORD'] = 'lxv5byb85vydqsnu'
app.config['MYSQL_DB'] = 's80s1c8qqx6rqp2o'

mysql = MySQL(app)

@app.route('/')
def index():
    return redirect('/home')


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

@app.route('/escuelas',  methods=['GET', 'POST'])
def escuelas():
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM escuela")
        if resultValue > 0:
                escuelaDetails = cur.fetchall()
                return render_template('escuelas.html',escuelaDetails=escuelaDetails)


@app.route('/queryDeleteAllEscuela')
def eliminarTodasEscuelas():
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM escuela")
        mysql.connection.commit()
        cur.close()
        return redirect('/home')



@app.route('/queryDeleteAllEstudiante')
def eliminarTodosEstudiantes():
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM estudiante")
        mysql.connection.commit()
        cur.close()
        return redirect('/home')


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

# RENDER ERROR PAGES =========================================================

app.config['TRAP_HTTP_EXCEPTIONS']=True

@app.errorhandler(404)
def page_not_found(e):
        # note that we set the 404 status explicitly
        return render_template('404.html'), 404
        

@app.errorhandler(500)
def internal_server_error(e):
        # note that we set the 404 status explicitly
        return render_template('500.html'), 500