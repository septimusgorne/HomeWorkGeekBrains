CREATE DATABASE hw3;
USE hw3;
CREATE TABLE IF NOT EXISTS `personal`
(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`first_name` VARCHAR(45),
`last_name` VARCHAR(45),
`post` VARCHAR(45),
`seniority` INT,
`salary` INT,
`age` INT

);

INSERT `personal` (`first_name`, `last_name`, `post`, `seniority`, `salary`, `age`) 
VALUES
('Равиль', 'Исааков', 'Ген.Директор', 40, 200000, 60),
('Антон', 'Савельев', 'Комм.директор', 8, 75000, 30),
('Алиса', 'Долина', 'Инженер', 2, 54000, 25),
('Антон', 'Городецкий', 'Инженер', 12, 52400, 35),
('Стас', 'Гацкий', 'Дизайнер', 40, 34500, 59),
('Александр', 'меньшиков', 'Охранник', 20, 51200, 60),
('Сергей', 'Немчинский', 'Продюссер', 10, 25000, 35),
('Савелий', 'Савельев', 'Разнорабочий', 8, 20000, 28),
('Хамат', 'Чулпан', 'Рабочий', 5, 15400, 25),
('Рада', 'Гаал', 'Тех.консультант', 2, 14000, 19),
('Петр', 'Иванонв', 'Рабочий', 3, 12500, 24),
('Светлана', 'Городецкая', 'Консультант по оборудованию', 10, 14000, 49);

SELECT * FROM `personal`;

-- Отсортируйте данные по полю заработная плата (salary) в порядке возрастания;
SELECT *
FROM personal
ORDER BY salary;

-- Отсортируйте данные по полю заработная плата (salary) в порядке убывания;
SELECT *
FROM personal
ORDER BY salary DESC;

-- Выведите 5 максимальных заработных плат (salary);
SELECT * FROM personal
ORDER BY salary DESC
LIMIT 5;

-- Посчитайте суммарную зарплату (salary) по каждой специальности (роst);
SELECT 
post,
SUM(salary) AS "Total salary"
FROM personal
GROUP BY post;

/* 
Найдите кол-во сотрудников с специальностью (post) «Рабочий» в 
возрасте от 24 до 49 лет включительно;
*/ 
SELECT COUNT(*) Number_of_Employees 
FROM personal 
WHERE post = 'Рабочий' AND age BETWEEN 24 AND 49;

-- Найдите количество специальностей;
SELECT COUNT(*) Total_post 
FROM(SELECT DISTINCT post 
FROM personal) t;

-- Выведите специальности, у которых средний возраст сотрудников меньше 40 лет;  
SELECT post, AVG(age) as average_age
FROM personal
GROUP BY post
HAVING AVG(age) < 40;

