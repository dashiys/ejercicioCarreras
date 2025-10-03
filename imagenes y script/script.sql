CREATE DATABASE  IF NOT EXISTS `carreras` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `carreras`;
DROP TABLE IF EXISTS `carreras`;
CREATE TABLE `carreras` (
  `idcarreras` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `duracion` int DEFAULT NULL,
  `institucion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcarreras`)
)

