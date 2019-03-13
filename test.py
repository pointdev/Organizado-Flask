from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

#configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def index():
    return redirect('/crearEscuela')

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
        print('Here is what pueblo had')
        print(pueblo)

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



#CODIGO PARTICIPACION===============================================
@app.route('/codigoParticipacion')
def codigoParticipacion():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM codigoParticipacion")
    if resultValue > 0:
        codigoDetails = cur.fetchall()
        return render_template('codigoParticipacion.html',codigoDetails=codigoDetails)




if __name__ == '__main__':
    app.run(debug=True)
