# Organizador-de-Torneos-de-Karate

Team/App Name and Concept - Select a Project Manager (PM):
Team Name: **DevPoint Inc**
Project Manager: **Annamary Cartagena**
App name: **Organizador de Torneos de Karate**
Concept:
	A web app used to record entries in a karate tournament. This web app will save the names of the competitors and be able to sort for when the tournament start, all the appropriate information of the competitors can be searched easily.


### Selected Development Frameworks:
+ Client-Side framework: Not yet identified
+ Application Server Framework: Flash Framework with Python
+ DBMS Technologies: MySQL

### Complete ER Diagram

<img src = ERDiagram.png title = 'ERDiagram' />


+ Estudiante(numero, nombre, apellido1, apellido2, cinta, edad,  escuela, codigo_participacion)
+ Escuela(nombre,disciplina, instructor_principal, pueblo, cantidad_estudiantes)
+ Participacion(codigo_participacion, kumite, kata, armas, rompimiento)

//numero in Estudiente will be the primary key
//nombre and disciplina will be the primary key to Escuela
//codigo_participacion will be the the primary key to Paticipacion
//numero is the primary key to cantidad_estudiante and well as the foreign key for estudiante
//cantidad_estudiante is being called to Escuela to register the amount of students per school
//Participacion is being used to store the different ways a student can participate in a tournament 

### Requirements Definition Document - Description of each operation supported by the app
+ The application will be mainly used to store information and display information. The application was created to easily obtain information from the participating students and schools, and use it to score properly at the end of the tournament.
+ The most important tables on information is Estudiante and Escuela. 
+ Estudiante will store information of each competitor. It must be connected to Escuela for further analysis at the end of the tournament. Since every student can opt in and out of specific competitions, the table for Participacion was created to less inflate the table Estudiante. It is necessary to know which student is participating in what of the tournament to tally up scores once the tournament is finished. It is also important to know how many students are per school so that when the score is tallies up, can be divided by the amount of student to know the average grade per school.
+ Escuela will store information of the different schools participating in the tournament. Since we need to know how many students are per school, estudiantes will store the name of the school.
#### Requirements inside the application:
+ 2 Entries, Escuela and Estudiante
+ Participation keys must already exist before registering any competitor and is static.
+ If registering school, must enter NAME, STYLE, PRIMARY INSTRUCTOR, and CITY
+ later, a table must be created to store how many students are per school
+ If registering student, must enter NAME, LASTNAMES, BELT, AGE, and SCHOOL
+ The student must then say what he/she in going to participate, which will generate a code detailing what the sudent is going to aprticipate in.
	+ Example: If a student participates in katas, but not kumite, armas,  or rompimiento, the student entry will have a code 0100 (no to kumite, yes to kata, no to armas, no to rompimiento) stored with their information.
+ At end of registering, every table can be searched through keys
+ Call Estudiante, shows all competitors
+ Call Escuela, show all schools
+ Call Participacion, show all the participation codes
+ Estudiante must be updateable, should a more students come or drop out tournaments.
+ Escuela must be updateable, should a more schools come or drop out tournaments.



## Master Project Development Plan
Sprint 1
* [X]  Generic, empty Tables have been made
* [X]  Connect Database MySQL
* [X] Functions for create, edit, and delete information
* [X]  Web App must show the registration form
May not be operational
#### Comments
+ Only Escuela db table has been created
+ Registration form is currently using hashsets instead of db tables
+ Functions work with hashsets instead of db tables

Sprint 2

* [x] Model diagram to table
* [x] Mockup webpage/ creation interface
* [x]  Participacion table has been finished with participation_codes created
* [x]  Generic registration form for Escuela slightly Operational
#### Comments
+ Participation table has been created, but not all participation_codes have been implemented

Sprint 3
* [x] Activar servidor/tener applicacion en algun servidor
* [x] Create estudiante table
* [-] Start developing a pleasant interface
* [x] Generic registration form for Estudiante slightly Operational
#### Comments
+ codigo participaton table finished
+ toolbar ovverlay designed, but not implemented in all webpaged
+ Logo fot page created
+ home, about
+ registrations form for estudiantes and escuela operational

Sprint 4
* [ ]  Participation table connected to Estudiante Table
* [x] Improve interface
* [x] toolbar implemented
* [X] Heroku now works perfectly with database
* [X] Delete tables Escuela and Estudiante
* [x] Added Home and About page information

Sprint 5
* [ ] Improve interfac
* [ ] Debugging
* [ ] Error catching
* [ ] creatng default Error 404

## Notes
URL for heroku app:
https://organizador-torneos-flask.herokuapp.com/home

Folders Containing Documentation:
https://drive.google.com/open?id=1YdCnQzFtT31UswCvwbg2D5RJDb6oEL16

Feb 15 2019:
Early Start Up of the proyect. Using Play Framework and Java language
Difficult first start, and hello world would not work. No easy documentation for tutorial on Java. Managed to get it to work eventually.
Most of the time used on how to compile hello world.
Used Eclipse and IntelliJ, Java JDK x64 8, SBT, Play Framework ver 2.7
//---------------------------------
March 11 2019:
Using the Play Framework has been very difficult, so the team has decided to switch to Flask framework with Python. Results have been satisfying. Using Flask Framework version 1.0.2 with Visual Studio Code
//--------------------------------- 
