DROP TABLE IF EXISTS `strategy`;
CREATE TABLE `strategy` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `name` char(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;


INSERT INTO `strategy` (`id`, `name`) VALUES ('1', X'50726f7465637420486162697461742028436f6d6d65726369616c20616e64205265736964656e7469616c20446576656c6f706d656e7429'),
('2', X'50726f7465637420486162697461742028436f617374616c20456e67696e656572696e6729'),
('3', X'50726f7465637420486162697461742028496e766173697665205370656369657329'),
('4', X'50726f7465637420486162697461742028496e636f6d70617469626c65204d616e6167656d656e7429'),
('5', X'52656475636520507265646174696f6e'),
('6', X'5265647563652048756d616e2044697374757262616e6365'),
('7', X'5265647563652048756e74696e67'),
('8', X'436c696d617465204368616e6765'),
('9', X'46696c6c204b6e6f776c656467652047617073');
