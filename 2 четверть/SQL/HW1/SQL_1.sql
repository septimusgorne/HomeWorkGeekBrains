1. Создать таблицу и ввести данные

CREATE TABLE`mob_db` . `mobile_phones` (
  `id_mobile_phones` INT NOT NULL AUTO_INCREMENT,
  `made_phones` VARCHAR(25) NOT NULL,
  `models_phone` VARCHAR(25) NOT NULL,
  `q-ty_mobile_phones` INT NOT NULL,
  `price_mobile_phones` DECIMAL NOT NULL,
  PRIMARY KEY (`id_mobile_phones`),
  UNIQUE INDEX `id_mobile_phones_UNIQUE` (`id_mobile_phones` DESC) VISIBLE);

INSERT INTO `mob_db`.`mobile_phones` 
(`made_phones`, `models_phones`, `q-ty_mobile_phones`, `price_mobile_phones`) VALUES ('Motorolla', 'e398', '2', '10000');
INSERT INTO `mob_db`.`mobile_phones` 
(`made_phones`, `models_phones`, `q-ty_mobile_phones`, `price_mobile_phones`) VALUES ('Apple', 'Iphone 14', '8', '140000');
INSERT INTO `mob_db`.`mobile_phones` 
(`made_phones`, `models_phones`, `q-ty_mobile_phones`, `price_mobile_phones`) VALUES ('Samsung', 's20ultra', '4', '60000');
INSERT INTO `mob_db`.`mobile_phones` 
(`made_phones`, `models_phones`, `q-ty_mobile_phones`, `price_mobile_phones`) VALUES ('Xiaomi ', 'Note10pro', '20', '11000');
INSERT INTO `mob_db`.`mobile_phones` 
(`made_phones`, `models_phones`, `qty_mobile_phones`, `price_mobile_phones`) VALUES ('Nokia', '3310', '13', '3000');
INSERT INTO `mob_db`.`mobile_phones` 
(`made_phones`, `models_phones`, `q-ty_mobile_phones`, `price_mobile_phones`) VALUES ('Samsung', 'S21', '10', '28100');

SELECT * FROM mobile_phones;

2. Выведите название, производителя и цену для товаров, количество которых превышает 2

SELECT models_phones, made_phones, price_mobile_phones  FROM mob_db.mobile_phones
where qty_mobile_phones >2;

3. Выведите весь ассортимент товаров марки “Samsung”

SELECT * FROM mob_db.mobile_phones
WHERE made_phones = 'Samsung';