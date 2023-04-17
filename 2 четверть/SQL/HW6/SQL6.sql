-- 1. Создайте таблицу users_old, аналогичную таблице users. Создайте процедуру, с помощью которой можно переместить любого (одного) пользователя из таблицы users в таблицу users_old. (использование транзакции с выбором commit или rollback – обязательно).
CREATE TABLE users_old (
	id_old SERIAL PRIMARY KEY,
    firstname_old VARCHAR(50),
    lastname_old VARCHAR(50) COMMENT 'Фамилия',
    email_old VARCHAR(120) UNIQUE
);

START TRANSACTION;

INSERT INTO users_old
select * from users
where firstname = 'firstname_old' and lastname = 'lastname_old';

COMMIT; -- применить изменения
-- ROLLBACK; -- отменить изменения


-- 2. Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
DELIMITER //

DROP FUNCTION IF EXISTS hello//
CREATE FUNCTION hello() RETURNS TEXT DETERMINISTIC
BEGIN
  RETURN CASE
      WHEN "06:00" <= CURTIME() AND CURTIME() < "12:00" THEN "Доброе утро"
      WHEN "12:00" <= CURTIME() AND CURTIME() < "18:00" THEN "Добрый День"
      WHEN "18:00" <= CURTIME() AND CURTIME() < "00:00" THEN "Добрый вечер"
      ELSE "Доброй ночи"
    END;
END //

DELIMITER ;

-- 3. (по желанию)* Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, communities и messages в таблицу logs помещается время и дата создания записи, название таблицы, идентификатор первичного ключа.
------------------ Создам таблицу ----------------
drop table if exists `logs`;
create table `logs`(
create_at datetime DEFAULT NOW(), 
`table_name` varchar(45) NOT NULL, 
table_id INT UNSIGNED NOT NULL, 
engine=ARCHIVE;

-------------------таблица communities --------------------------------

USE `communities`;

DELIMITER $$

USE `communities`$$
DROP TRIGGER IF EXISTS `communities`.`users_AFTER_INSERT` $$
DELIMITER ;
DROP TRIGGER IF EXISTS `communities`.`creation_record _users`;

DELIMITER $$
USE `communities`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `creation_record _users` AFTER INSERT ON `users` FOR EACH ROW BEGIN
insert into communities.logs (create_at,`table_name`, table_id)
values (now(), 'communities.users', new.id);

END$$
DELIMITER ;

-----------------------таблица messages-------------------------------
DROP TRIGGER IF EXISTS `messages`.`creation_record_messages`;

DELIMITER $$
USE `messages`$$
CREATE DEFINER = CURRENT_USER TRIGGER `creation_record_messages` AFTER INSERT ON `messages` FOR EACH ROW
BEGIN
insert into messages.logs (create_at,`table_name`, table_id)
values (now(), 'messages', new.id);


END$$
DELIMITER ;