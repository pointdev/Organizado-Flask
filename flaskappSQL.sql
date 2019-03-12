CREATE DATABASE flaskapp;

USE flaskapp;

CREATE TABLE users(
name varchar(20) ,
email varchar(40)
);

CREATE TABLE codigoParticipacion(
codigo_participacion varchar(4),
kumite varchar(3),
kata varchar(3),
armas varchar(3),
rompimiento varchar(3)
);

#SELECT * FROM users;

insert  into codigoParticipacion(codigo_participacion, kumite, kata, armas, rompimiento) values

(0001, 'no' , 'no', 'no' , 'yes' );

#ESCUELA====================================================

#Escuela(nombre,disciplina, instructor_principal, pueblo)

CREATE TABLE escuela(
nombre varchar(40) NOT NULL,
disciplina varchar(40),
instructorPrincipal varchar(40),
pueblo varchar(40)
);