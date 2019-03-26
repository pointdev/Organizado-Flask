-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Escuela`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Escuela` (
  `Nombre` VARCHAR(45) NOT NULL,
  `Disciplina` VARCHAR(45) NULL,
  `Instructor_Principal` VARCHAR(45) NULL,
  `Pueblo` VARCHAR(45) NULL,
  `Cantidad_Estudiantes` INT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Nombre`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Participacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Participacion` (
  `idParticipacion` VARCHAR(4) NOT NULL,
  `Kumite` TINYINT(1) NOT NULL,
  `Kata` TINYINT(1) NOT NULL,
  `Armas` TINYINT(1) NOT NULL,
  `Rompimiento` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idParticipacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Estudiante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Estudiante` (
  `numeroID` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido1` VARCHAR(45) NOT NULL,
  `Apellido2` VARCHAR(45) NOT NULL,
  `cinta` VARCHAR(45) NOT NULL,
  `Edad` INT NOT NULL,
  `Escuela` VARCHAR(4) NOT NULL,
  `Escuela_Nombre` VARCHAR(45) NOT NULL,
  `CodigoIDparticipacion` VARCHAR(4) NOT NULL,
  PRIMARY KEY (`numeroID`, `Escuela_Nombre`, `CodigoIDparticipacion`),
  INDEX `fk_Estudiante_Escuela_idx` (`Escuela_Nombre` ASC) VISIBLE,
  INDEX `fk_Estudiante_Participacion1_idx` (`CodigoIDparticipacion` ASC) VISIBLE,
  CONSTRAINT `fk_Estudiante_Escuela`
    FOREIGN KEY (`Escuela_Nombre`)
    REFERENCES `mydb`.`Escuela` (`Nombre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Estudiante_Participacion1`
    FOREIGN KEY (`CodigoIDparticipacion`)
    REFERENCES `mydb`.`Participacion` (`idParticipacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
