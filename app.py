from flask import Flask, render_template, request, redirect, url_for, flash, session, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
#from data import Articles


app = Flask(__name__)
app.secret_key='secret123'
app.config['MYSQL_HOST'] = 'fnx6frzmhxw45qcb.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'ophmvxggd70qi4hx'
app.config['MYSQL_PASSWORD'] = 'lxv5byb85vydqsnu'
app.config['MYSQL_DB'] = 's80s1c8qqx6rqp2o'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

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
            flash('Falta Informacion, favor volver a intentar.', 'success')
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

# WILL BECOME EDITAR ESCUELA
@app.route('/editarEscuela/<string:id>' , methods=['GET', 'POST'])
def editarEscuela(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM escuela WHERE nombre=%s", [id])
        entry = cur.fetchone()
   
        escuelaDetails = request.form
        if request.method == 'POST':
                
                nombre = escuelaDetails['nombre']
                disciplina = escuelaDetails['disciplina']
                instructorPrincipal = escuelaDetails['instructorPrincipal']
                pueblo = escuelaDetails['pueblo']
                
                

                if (nombre == '') or (disciplina == '') or (instructorPrincipal == '') or (pueblo == ''):
                   flash('Falta Informacion, favor volver a intentar.', 'success')
                   return redirect ('/editarEscuela')

                else:
                     #   cur = mysql.connection.cursor()
                        cur.execute("UPDATE escuela SET nombre=%s, disciplina=%s, instructorPrincipal=%s, pueblo=%s WHERE nombre=%s",(nombre,disciplina, instructorPrincipal, pueblo, nombre))
                        # ("INSERT INTO estudiante(nombre, apellido1, apellido2, cinta, edad, escuela, codigoParticipacion) VALUES(%s, %s, %s, %s, %s, %s, %s)",(nombre,apellido1, apellido2, cinta, edad, escuela, codigoParticipacion))
                        mysql.connection.commit()
                        cur.close()
                        return redirect('/escuelas')
        return render_template('editarEscuela.html', escuelaDetails=escuelaDetails, entry=entry)


@app.route('/queryDeleteAllEscuela')
def eliminarTodasEscuelas():
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM escuela")
        mysql.connection.commit()
        cur.close()
        return redirect('/home')


@app.route('/queryDeleteEscuela/<string:id>', methods=['POST'])
def deleteEscuela(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM escuela WHERE nombre = %s", [id])
        mysql.connection.commit()
        cur.close()
        return redirect ('/escuelas')





#ESTUDIANTE ==================================================================
@app.route('/crearEstudiante', methods=['GET', 'POST'])
def crearEstudiante():
    cur = mysql.connection.cursor()
    cur2 = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM codigoParticipacion")
    resultValue2 = cur2.execute("SELECT * FROM escuela")
    if resultValue > 0  or resultValue2 > 0:
        escuelaDetails = cur2.fetchall()
        codigoDetails = cur.fetchall()

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
            flash('Falta Informacion, favor volver a intentar.', 'success')
            return redirect ('/crearEstudiante')
        else:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO estudiante(nombre, apellido1, apellido2, cinta, edad, escuela, codigoParticipacion) VALUES(%s, %s, %s, %s, %s, %s, %s)",(nombre,apellido1, apellido2, cinta, edad, escuela, codigoParticipacion))
            mysql.connection.commit()
            cur.close()
            return redirect('/estudiantes')
    return render_template('crearEstudiante.html', codigoDetails=codigoDetails, escuelaDetails=escuelaDetails)



@app.route('/queryDeleteEstudiante/<string:id>', methods=['POST'])
def deleteEstudiante(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM estudiante WHERE id = %s", [id])
        mysql.connection.commit()
        cur.close()
        return redirect ('/estudiantes')

@app.route('/queryDeleteAllEstudiante')
def eliminarTodosEstudiantes():
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM estudiante")
        mysql.connection.commit()
        cur.close()
        return redirect('/home')


@app.route('/editarEstudiante/<string:id>' , methods=['GET', 'POST'])
def editarEstudiante(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM estudiante WHERE id=%s", [id])
        entry = cur.fetchone()
        
        cur2 = mysql.connection.cursor()
        cur3 = mysql.connection.cursor()
        resultValue2 = cur2.execute("SELECT * FROM codigoParticipacion")
        resultValue3 = cur3.execute("SELECT * FROM escuela")
        if resultValue2 > 0  or resultValue3 > 0:
                codigoDetails = cur2.fetchall()
                escuelaDetails = cur3.fetchall()

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
                   flash('Falta Informacion, favor volver a intentar.', 'success')
                   return redirect ('/editarEstudiante')

                else:
                        cur.execute("UPDATE estudiante SET nombre=%s, apellido1=%s, apellido2=%s, cinta=%s, edad=%s, escuela=%s, codigoParticipacion=%s WHERE id=%s",(nombre,apellido1, apellido2, cinta, edad, escuela, codigoParticipacion, id))
                        mysql.connection.commit()
                        cur.close()
                        return redirect('/estudiantes')
        return render_template('editarEstudiante.html', codigoDetails=codigoDetails, escuelaDetails=escuelaDetails, entry=entry)

@app.route('/estudiantes')
def estudiantes():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM estudiante")
    if resultValue > 0:
        estudianteDetails = cur.fetchall()
        return render_template('estudiantes.html',estudianteDetails=estudianteDetails)



#CODIGO PARTICIPACION===============================================================
@app.route('/codigoParticipacion')
def codigoParticipacion():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM codigoParticipacion")
    if resultValue > 0:
        codigoDetails = cur.fetchall()
        return render_template('codigoParticipacion.html',codigoDetails=codigoDetails)

#==================================================================================
@app.route('/about')
def about():
        return render_template('about.html')


@app.route('/home')
def home():
        return render_template('home.html')

# RENDER ERROR PAGES =========================================================

app.config['TRAP_HTTP_EXCEPTIONS']=True

@app.errorhandler(404)
def page_not_found(e):
        # note that we set the 404 status explicitly
        return render_template('errors/404.html'), 404
        

@app.errorhandler(500)
def internal_server_error(e):
        # note that we set the 404 status explicitly
        return render_template('errors/500.html'), 500


@app.errorhandler(403)
def prohibited(e):
        # note that we set the 404 status explicitly
        return render_template('errors/403.html'), 403


@app.errorhandler(410)
def gone(e):
        # note that we set the 404 status explicitly
        return render_template('errors/410.html'), 410

@app.errorhandler(400)
def bad_request(e):
        # note that we set the 404 status explicitly
        return render_template('errors/400.html'), 400



#FORMS FOR LOGGING IN AND REGISTERING ============================================================================

class RegisterForm(Form):
        name = StringField ('Name', [validators.Length(min=1, max=50)])
        username = StringField('Username',  [validators.Length(min=4, max=25)])
        email = StringField('Email', [validators.Length(min=6, max=50)])
        password = PasswordField('Password', 
                [validators.DataRequired(),
                validators.equal_to('confirm', message= "Passwords do not match")
                ])
        confirm = PasswordField('Confirm Password')

#REGISTER
@app.route('/registrar', methods = ['GET', 'POST'])
def registrar():
        form = RegisterForm(request.form)
        if request.method == 'POST' and form.validate():
                name= form.name.data
                email = form.email.data
                username = form.username.data
                password = sha256_crypt.encrypt(str(form.password.data))

                #Create cursor
                cur = mysql.connection.cursor()
                cur.execute("INSERT into users(name, email, username, password) VALUES (%s,%s,%s,%s)",(name, email, username, password))
                
                mysql.connection.commit()
                cur.close()
                flash('Ahora estas registrado.', 'success')
                redirect('/index')

        return render_template('registrar.html', form = form)

#LOGIN
@app.route('/login', methods = ['GET', 'POST'])
def login():
        if request.method == 'POST':
                username = request.form['username']
                password_candidate = request.form['password']

                cur = mysql.connection.cursor()
                result = cur.execute("SELECT * FROM users WHERE username = %s",[username])

                if result > 0:
                        data = cur.fetchone()
                        password = data['password']

                        if sha256_crypt.verify(password_candidate, password):
                                app.logger.info('PASSWORD MATCHED')
                        else
                                error = 'Login inválido'
                                return render_template('login.html', error)
                else:
                        error = 'Usuario no encontrado'
                        return render_template('login.html', error)

        return render_template('login.html')

#=============================================================================
if __name__ == '__main__':
        app.run(debug=True)