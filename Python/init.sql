CREATE DATABASE docker;
use docker;

CREATE TABLE `usertable` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(20),
  `lastname` varchar(20),
  `email` varchar(50),
  `number` int,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `usertable`(`id`,`firstname`,`lastname`,`email`,`number`) values
(1,'Test1','User','test1.user@mail.com', 09835347484),
(2,'Test2','User2','test2.user@mail.com',34256780),
(3,'Test2','User3','test2.user@mail.com',34256780);



