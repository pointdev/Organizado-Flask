#CREATE DATABASE flaskapp;

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
(0001, 'no' , 'no', 'no' , 'yes' ),
(0010, 'no' , 'no', 'yes' , 'no' ),
(0011, 'no' , 'no', 'yes' , 'yes' ),
(0100, 'no' , 'yes', 'no' , 'no' ),
(0101, 'no' , 'yes', 'no' , 'yes' ),
(0110, 'no' , 'yes', 'yes' , 'no' ),
(0111, 'no' , 'yes', 'yes' , 'yes' ),
(1000, 'yes' , 'no', 'no' , 'no' ),
(1001, 'yes' , 'no', 'no' , 'yes' ),
(1010, 'yes' , 'no', 'yes' , 'no' ),
(1011, 'yes' , 'no', 'yes' , 'yes' ),
(1100, 'yes' , 'yes', 'no' , 'no' ),
(1101, 'yes' , 'yes', 'no' , 'yes' ),
(1110, 'yes' , 'yes', 'yes' , 'no' ),
(1111, 'yes' , 'yes', 'yes' , 'yes' )
;

#ESCUELA====================================================

#Escuela(nombre,disciplina, instructor_principal, pueblo)

CREATE TABLE escuela(
nombre varchar(40) NOT NULL,
disciplina varchar(40) NOT NULL,
instructorPrincipal varchar(40) NOT NULL,
pueblo varchar(40) NOT NULL,
  PRIMARY KEY (nombre)
);