-- MySQL dump 10.13  Distrib 8.0.16, for Linux (x86_64)
--
-- Host: localhost    Database: compliance
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `compliance_run_result`
--

DROP TABLE IF EXISTS `compliance_run_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `compliance_run_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `rule_id` int(11) NOT NULL,
  `provider` varchar(31) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `region` varchar(31) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `entity` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `result` varchar(31) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `message` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rule_id` (`rule_id`),
  CONSTRAINT `compliance_run_result_ibfk_1` FOREIGN KEY (`rule_id`) REFERENCES `rules` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compliance_run_result`
--

LOCK TABLES `compliance_run_result` WRITE;
/*!40000 ALTER TABLE `compliance_run_result` DISABLE KEYS */;
INSERT INTO `compliance_run_result` VALUES (33,'2019-07-18 08:36:40',1,'AWS','us-east-1','DUMMY','FAIL','User anant.mahajan has Password enabled but MFA disabled'),(34,'2019-07-18 08:36:40',1,'AWS','us-east-1','DUMMY','FAIL','User sakshi.kathuria has Password enabled but MFA disabled'),(35,'2019-07-18 08:36:40',2,'AWS','us-east-1','DUMMY','FAIL','User \"anandh.ravindran\" has not logged in during the last 90 days '),(36,'2019-07-18 08:36:40',2,'AWS','us-east-1','DUMMY','PASS','User \"anant.mahajan\" found with credentials used in the last 90 days'),(37,'2019-07-18 08:36:40',2,'AWS','us-east-1','DUMMY','PASS','User \"arijit.banerjee\" found with credentials used in the last 90 days'),(38,'2019-07-18 08:36:40',2,'AWS','us-east-1','DUMMY','PASS','User \"arvind.batra\" found with credentials used in the last 90 days'),(39,'2019-07-18 08:36:40',2,'AWS','us-east-1','DUMMY','FAIL','User \"ben.southward\" has not logged in during the last 90 days ');
/*!40000 ALTER TABLE `compliance_run_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rules`
--

DROP TABLE IF EXISTS `rules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `rules` (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `severity` varchar(31) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `rgroup` varchar(1023) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `entity_type` varchar(31) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `provider` varchar(31) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rules`
--

LOCK TABLES `rules` WRITE;
/*!40000 ALTER TABLE `rules` DISABLE KEYS */;
INSERT INTO `rules` VALUES (0,'check11',' Avoid the use of the root account (Scored)','Level 1','Identity and Access Management,CIS Level 1,CIS Level 2','DUMMY_TYPE','AWS'),(1,'check12',' Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password (Scored)','Level 1','Identity and Access Management,CIS Level 1,GDPR Readiness,HIPAA Compliance,CIS Level 2','DUMMY_TYPE','AWS'),(2,'check13',' Ensure credentials unused for 90 days or greater are disabled (Scored)','Level 1','Identity and Access Management,CIS Level 1,CIS Level 2','DUMMY_TYPE','AWS');
/*!40000 ALTER TABLE `rules` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-18  8:40:35
