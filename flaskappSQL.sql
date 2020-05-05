CREATE DATABASE flaskapp;

USE flaskapp;
USE s80s1c8qqx6rqp2o;
#Estudiante(numero, nombre, apellido1, apellido2, cinta, edad, escuela, codigo_participacion)
CREATE TABLE estudiante(
ID int auto_increment NOT NULL ,
nombre varchar(40) NOT NULL,
apellido1 varchar(40),
apellido2 varchar(40),
cinta varchar(40) NOT NULL,
edad int NOT NULL,
escuela varchar(40),
codigoParticipacion varchar(5) NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (escuela) REFERENCES `escuela` (nombre),
    FOREIGN KEY (codigoParticipacion) REFERENCES `codigoParticipacion` (codigo_participacion)
);


# CODIGO PARTICIPACION====================================================
CREATE TABLE codigoParticipacion(
codigo_participacion varchar(5) NOT NULL,
kumite varchar(3) NOT NULL,
kata varchar(3) NOT NULL,
armas varchar(3) NOT NULL,
rompimiento varchar(3) NOT NULL,
  PRIMARY KEY (codigo_participacion)
);

SELECT * FROM codigoParticipacion;

insert  into codigoParticipacion(codigo_participacion, kumite, kata, armas, rompimiento) values
(20000, 'no' , 'no', 'no' , 'no' ),
(20001, 'no' , 'no', 'no' , 'yes' ),
(20010, 'no' , 'no', 'yes' , 'no' ),
(20011, 'no' , 'no', 'yes' , 'yes' ),
(20100, 'no' , 'yes', 'no' , 'no' ),
(20101, 'no' , 'yes', 'no' , 'yes' ),
(20110, 'no' , 'yes', 'yes' , 'no' ),
(20111, 'no' , 'yes', 'yes' , 'yes' ),
(21000, 'yes' , 'no', 'no' , 'no' ),
(21001, 'yes' , 'no', 'no' , 'yes' ),
(21010, 'yes' , 'no', 'yes' , 'no' ),
(21011, 'yes' , 'no', 'yes' , 'yes' ),
(21100, 'yes' , 'yes', 'no' , 'no' ),
(21101, 'yes' , 'yes', 'no' , 'yes' ),
(21110, 'yes' , 'yes', 'yes' , 'no' ),
(21111, 'yes' , 'yes', 'yes' , 'yes' )
;



#ESCUELA====================================================

SELECT * FROM escuela;

#Escuela(nombre,disciplina, instructor_principal, pueblo)
CREATE TABLE escuela(
nombre varchar(40) NOT NULL,
disciplina varchar(40) NOT NULL,
instructorPrincipal varchar(40) NOT NULL,
pueblo varchar(40) NOT NULL,
  PRIMARY KEY (nombre)
);

#USERS
CREATE TABLE users(
id INT (11)AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
email VARCHAR (100),
username VARCHAR(50),
password VARCHAR(100),
register_name TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);
SELECT * FROM users;