CREATE DATABASE flaskapp;

USE flaskapp;

CREATE TABLE users(
name varchar(20) ,
email varchar(40)
);

CREATE TABLE codigoParticipacion(
codigo_participacion varchar(4) NOT NULL,
kumite varchar(3) NOT NULL,
kata varchar(3) NOT NULL,
armas varchar(3) NOT NULL,
rompimiento varchar(3) NOT NULL,
  PRIMARY KEY (codigo_participacion)
);

#SELECT * FROM users;

insert  into codigoParticipacion(codigo_participacion, kumite, kata, armas, rompimiento) values

(0001, 'no' , 'no', 'no' , 'yes' );

#ESCUELA====================================================

#Escuela(nombre,disciplina, instructor_principal, pueblo)

CREATE TABLE escuela(
nombre varchar(40) NOT NULL,
disciplina varchar(40) NOT NULL,
instructorPrincipal varchar(40) NOT NULL,
pueblo varchar(40) NOT NULL,
  PRIMARY KEY (nombre)
);