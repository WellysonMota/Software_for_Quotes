-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: QuotesDatabase
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `QuoteSent`
--

DROP TABLE IF EXISTS `QuoteSent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `QuoteSent` (
  `idQuoteSent` int NOT NULL AUTO_INCREMENT,
  `Origin` varchar(45) NOT NULL,
  `Currency` varchar(45) NOT NULL,
  `Date` date NOT NULL,
  `AccountManager` varchar(45) NOT NULL,
  `CompanyName` varchar(45) NOT NULL,
  `ContactName` varchar(45) NOT NULL,
  `CompanyType` varchar(45) NOT NULL,
  `CompanyCountry` varchar(45) NOT NULL,
  `CompanyState` varchar(45) NOT NULL,
  `CompanyCity` varchar(45) NOT NULL,
  `PaymentTerm` varchar(45) NOT NULL,
  `Freight` varchar(45) NOT NULL,
  `TotalAmount` float NOT NULL,
  PRIMARY KEY (`idQuoteSent`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `QuoteSent`
--

LOCK TABLES `QuoteSent` WRITE;
/*!40000 ALTER TABLE `QuoteSent` DISABLE KEYS */;
INSERT INTO `QuoteSent` VALUES (6,'EPS Americana','BRL','2024-03-25','Wellyson','Compwire','Murilo Rupp','System Integrator','Brasil','Santa Catarina','Florianapolis','NET30','Sedex',17800),(7,'EPS Americana','BRL','2024-03-25','Wellyson','Compwire','Murilo Rupp','System Integrator','Brasil','Santa Catarina','Florianapolis','NET30','Sedex',17800),(8,'EPS Americana','BRL','2024-03-25','Wellyson','Compwire','Murilo Rupp','System Integrator','Brasil','Santa Catarina','Florianapolis','NET30','Sedex',17800),(9,'EPS Americana','BRL','2024-03-25','Wellyson','Compwire','Murilo Rupp','System Integrator','Brasil','Santa Catarina','Florianapolis','NET30','Sedex',17800);
/*!40000 ALTER TABLE `QuoteSent` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-25 23:23:34
