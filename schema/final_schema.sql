 SET character_set_client = utf8mb4 ;
CREATE TABLE `rules` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(25) COLLATE utf8_bin DEFAULT NULL,
  `description` varchar(25) COLLATE utf8_bin DEFAULT NULL,
  `severity` varchar(25) COLLATE utf8_bin NOT NULL,
  `group` varchar(25) COLLATE utf8_bin NOT NULL,
  `entity_type` varchar(25) COLLATE utf8_bin NOT NULL,
  `provider` varchar(25) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
