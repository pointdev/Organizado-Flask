# Organizador-de-Torneos-de-Karate

Team/App Name and Concept - Select a Project Manager (PM):
Team Name: **DevPoint Inc**
Project Manager: **Annamary Cartagena**
App name: **Organizador de Torneos de Karate**
Concept:
	A web app used to record entries in a karate tournament. This web app will save the names of the competitors and be able to sort for when the tournament start, all the appropriate informacion of the competitors can be searched easily.


### Selected Development Frameworks:
+ Client-Side framework: Not yet identified
+ Application Server Framework: Play Framework with Java
+ DBMS Technologies: MySQL

### Complete ER Diagram

<img src = ERDiagram.png title = 'ERDiagram' />


+ Estudiante(numero, nombre, apellido1, apellido2, cinta, edad,  escuela, codigo_participacion)
+ Escuela(nombre,disciplina, instructor_principal, pueblo, cantidad_estudiantes)
+ Participacion(codigo_participacion, kumite, kata, armas, rompimiento)
+ Cantidad_estudiantes(numero, nombre_estudiante)

//numero in Estudiente will be the primary key
//nombre and disciplina will be the primary key to Escuela
//codigo_participacion will be the the primary key to Paticipacion
//numero is the primary key to cantidad_estudiante and well as the foreign key for estudiante
//cantidad_estudiante is being called to Escuela to register the amount of students per school
//Participacion is being used to store the different ways a student can participate in a tournament 

### Requirements Definition Document - Description of each operation supported by the app
+ The application will be mainly used to store information and display information. The application was created to easily obtain information from the participating student and school, and use it to score properly according to size. The most important tables on information is Estudiante and Escuela. 
+ Estudiante will store information of each competitor. It must be connected to Escuela for further analysis at the end of the tournament. Since every student can opt in and out of specific competitions, the table for Participacion was created to less inflate the table Estudiante. It is necessary to know which student is participating in what of the tournament to tally up scores once the tournament is finished. It is also important to know how many student are per school so that when the score is tallies up, can be divided by the amount of student to know the average grade per school.
#### Requirements inside the application:
+ 2 Entries, Escuela and Estudiante
+ Participation keys must already exist before registering any competitor
+ If registering school, must enter NAME, STYLE, PRIMARY INSTRUCTOR, and CITY
+ later, a table must be created to store how many students are per school
+ If registering student, must enter NAME, LASTNAMES, BELT, AGE, and SCHOOL
+ The student must then say what he/she in going to participate, and assigned a participation code that will be later used for assignment
+ At end of registering, every table can be searched through keys
+ Call Estudiante, shows all competitors
+ Call Escuela, show all schools
+ Call Participacion, show all the participation codes
+ Estudiante and Cantidad_escuela must be updateable, should a more students come or drop out tournaments.



## Master Project Development Plan
Sprint 1
* [X]  Generic, empty Tables have been made
* [X]  Connect Database MySQL
* [X] Functions for create, edit, and delete information
* [X]  Web App must show the registration form
May not be operational
#### Comments
+ Only Escuela db table has been created
+ Registration form is currently ussing hashsets instead of db tables
+ Functions work with hashsets instead of db tables

Sprint 2
* [ ] Create remaining tables
* [ ] Activar servidor/tener applicacion en algun servidor
* [ ] Modelo diagrama a tabla
* [ ] Mockup webpage/ creation interface
* [ ]  Participacion table has been finished with participation_codes created
* [ ]  Generic registration form for Estudiante slightly Operational
* [ ]  Generic registration form for Escuela slightly Operational

Sprint 3
* [ ]  Participation table connected to Estudiante Table
* [ ] Improve interface

## Notes

Folders Containing Documentation:
https://drive.google.com/open?id=1YdCnQzFtT31UswCvwbg2D5RJDb6oEL16

Feb 15 2019:
Early Start Up of the proyect. Using Play Framework and Java language
Difficult first start, and hello world would not work. No easy documentation for tutorial on Java. Managed to get it to work eventually.
Most of the time used on how to compile hello world.
Used Eclipse and IntelliJ, Java JDK x64 8, SBT, Play Framework ver 2.7
//---------------------------------
