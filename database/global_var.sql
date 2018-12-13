DROP TABLE IF EXISTS `global_var`;
CREATE TABLE `global_var` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `name` char(30) NOT NULL,
  `value` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;


INSERT INTO `global_var` (`id`, `name`, `value`) VALUES ('1', X'7374726174656779', '9'),
('2', X'73706563696573', '20'),
('3', X'6f7267616e697a6174696f6e', '38'),
('4', X'706172746e6572', '153'),
('5', X'70726f6a656374', '72'),
('6', X'757364', '8260275'),
('7', X'636164', '220000'),
('8', X'62726c', '100305');
