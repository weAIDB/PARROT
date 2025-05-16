SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2025	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2019	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2009	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2014	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2022	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2024 OR YEAR = 2015	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2018 OR YEAR = 2015	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2008 OR YEAR = 2015	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2013 OR YEAR = 2015	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2021 OR YEAR = 2015	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2025	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2019	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2009	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2014	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2014 OR YEAR = 2022	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2024 OR YEAR = 2015	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2018 OR YEAR = 2015	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2008 OR YEAR = 2015	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2013 OR YEAR = 2015	concert_singer
SELECT count(*) FROM concert WHERE YEAR = 2021 OR YEAR = 2015	concert_singer
SELECT T2.name , T2.capacity FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year >= 2015 GROUP BY T2.stadium_id ORDER BY count(*) DESC LIMIT 1	concert_singer
select t2.name , t2.capacity from concert as t1 join stadium as t2 on t1.stadium_id = t2.stadium_id where t1.year > 2014 group by t2.stadium_id order by count(*) desc limit 1	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2024	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2018	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2008	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2013	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2021	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2024	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2018	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2008	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2013	concert_singer
SELECT name FROM stadium EXCEPT SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2021	concert_singer
SELECT T2.name FROM singer_in_concert AS T1 JOIN singer AS T2 ON T1.singer_id = T2.singer_id JOIN concert AS T3 ON T1.concert_id = T3.concert_id WHERE T3.year = 2015	concert_singer
SELECT T2.name FROM singer_in_concert AS T1 JOIN singer AS T2 ON T1.singer_id = T2.singer_id JOIN concert AS T3 ON T1.concert_id = T3.concert_id WHERE T3.year = 2015	concert_singer
SELECT T2.name , T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.Year = 2014 INTERSECT SELECT T2.name , T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.Year = 2014	concert_singer
SELECT T2.name , T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.Year = 2015 INTERSECT SELECT T2.name , T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.Year = 2015	concert_singer
SELECT T2.name , T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.Year = 2014 INTERSECT SELECT T2.name , T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.Year = 2014	concert_singer
SELECT T2.name , T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.Year = 2015 INTERSECT SELECT T2.name , T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.Year = 2015	concert_singer
SELECT count(*) FROM pets WHERE weight > 7	pets_1
SELECT count(*) FROM pets WHERE weight > 5	pets_1
SELECT count(*) FROM pets WHERE weight > 8	pets_1
SELECT count(*) FROM pets WHERE weight > 13	pets_1
SELECT count(*) FROM pets WHERE weight > 9	pets_1
SELECT count(*) FROM pets WHERE weight > 7	pets_1
SELECT count(*) FROM pets WHERE weight > 5	pets_1
SELECT count(*) FROM pets WHERE weight > 8	pets_1
SELECT count(*) FROM pets WHERE weight > 13	pets_1
SELECT count(*) FROM pets WHERE weight > 9	pets_1
SELECT petid , weight FROM pets WHERE pet_age > 2	pets_1
SELECT petid , weight FROM pets WHERE pet_age > 2	pets_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1974	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1979	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1977	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1976	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1978	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1974	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1979	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1977	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1976	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1978	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 3	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 5	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 10	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 6	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 13	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 3	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 5	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 10	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 6	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 13	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1984	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1978	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1968	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1973	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1981	car_1
select min(weight) from cars_data where cylinders = 17 and year = 1974	car_1
select min(weight) from cars_data where cylinders = 3 and year = 1974	car_1
select min(weight) from cars_data where cylinders = 7 and year = 1974	car_1
select min(weight) from cars_data where cylinders = 5 and year = 1974	car_1
select min(weight) from cars_data where cylinders = 9 and year = 1974	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1984	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1978	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1968	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1973	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1981	car_1
select min(weight) from cars_data where cylinders = 17 and year = 1974	car_1
select min(weight) from cars_data where cylinders = 3 and year = 1974	car_1
select min(weight) from cars_data where cylinders = 7 and year = 1974	car_1
select min(weight) from cars_data where cylinders = 5 and year = 1974	car_1
select min(weight) from cars_data where cylinders = 9 and year = 1974	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 160	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 154	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 144	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 149	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 157	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 160	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 154	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 144	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 149	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 157	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 4 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 5 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 6 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 8 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 4 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 5 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 6 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 8 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT avg(horsepower) FROM CARS_DATA WHERE YEAR < 1990	car_1
SELECT avg(horsepower) FROM CARS_DATA WHERE YEAR < 1984	car_1
SELECT avg(horsepower) FROM CARS_DATA WHERE YEAR < 1974	car_1
SELECT avg(horsepower) FROM CARS_DATA WHERE YEAR < 1979	car_1
SELECT avg(horsepower) FROM CARS_DATA WHERE YEAR < 1987	car_1
select avg(horsepower) from cars_data where year < 1990	car_1
select avg(horsepower) from cars_data where year < 1984	car_1
select avg(horsepower) from cars_data where year < 1974	car_1
select avg(horsepower) from cars_data where year < 1979	car_1
select avg(horsepower) from cars_data where year < 1987	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 3	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 5	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 6	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 7	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 1	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 3	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 5	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 6	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 7	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 1	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1974	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1977	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1976	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1978	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1975	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1974	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1977	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1976	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1978	car_1
SELECT count(*) FROM CARS_DATA WHERE YEAR = 1975	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 5	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 4	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 3	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 1	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 2	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 5	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 4	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 3	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 1	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Cylinders > 2	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 3 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 5 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 8 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 3 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 5 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 8 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.MakeId , T2.Make FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Horsepower > (SELECT min(Horsepower) FROM CARS_DATA) AND T1.Cylinders <= 4	car_1
SELECT T2.MakeId , T2.Make FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Horsepower > (SELECT min(Horsepower) FROM CARS_DATA) AND T1.Cylinders <= 5	car_1
SELECT T2.MakeId , T2.Make FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Horsepower > (SELECT min(Horsepower) FROM CARS_DATA) AND T1.Cylinders <= 10	car_1
SELECT T2.MakeId , T2.Make FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Horsepower > (SELECT min(Horsepower) FROM CARS_DATA) AND T1.Cylinders <= 6	car_1
SELECT T2.MakeId , T2.Make FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Horsepower > (SELECT min(Horsepower) FROM CARS_DATA) AND T1.Cylinders <= 13	car_1
select t2.makeid , t2.make from cars_data as t1 join car_names as t2 on t1.id = t2.makeid where t1.horsepower > (select min(horsepower) from cars_data) and t1.cylinders < 5	car_1
select t2.makeid , t2.make from cars_data as t1 join car_names as t2 on t1.id = t2.makeid where t1.horsepower > (select min(horsepower) from cars_data) and t1.cylinders < 10	car_1
select t2.makeid , t2.make from cars_data as t1 join car_names as t2 on t1.id = t2.makeid where t1.horsepower > (select min(horsepower) from cars_data) and t1.cylinders < 6	car_1
select t2.makeid , t2.make from cars_data as t1 join car_names as t2 on t1.id = t2.makeid where t1.horsepower > (select min(horsepower) from cars_data) and t1.cylinders < 13	car_1
select t2.makeid , t2.make from cars_data as t1 join car_names as t2 on t1.id = t2.makeid where t1.horsepower > (select min(horsepower) from cars_data) and t1.cylinders < 8	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3510 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3507 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3508 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3509 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3506 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3510 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3507 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3508 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3509 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3506 AND T4.FullName != 'Ford Motor Company'	car_1
SELECT city FROM employee WHERE age < 40 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT city FROM employee WHERE age < 34 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT city FROM employee WHERE age < 37 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT city FROM employee WHERE age < 38 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT city FROM employee WHERE age < 39 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT city FROM employee WHERE age < 40 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT city FROM employee WHERE age < 34 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT city FROM employee WHERE age < 37 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT city FROM employee WHERE age < 38 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT city FROM employee WHERE age < 39 GROUP BY city HAVING count(*) > 1	employee_hire_evaluation
SELECT version_number , template_type_code FROM Templates WHERE version_number > 6	cre_Doc_Template_Mgt
SELECT version_number , template_type_code FROM Templates WHERE version_number > 7	cre_Doc_Template_Mgt
SELECT version_number , template_type_code FROM Templates WHERE version_number > 4	cre_Doc_Template_Mgt
SELECT version_number , template_type_code FROM Templates WHERE version_number > 8	cre_Doc_Template_Mgt
SELECT version_number , template_type_code FROM Templates WHERE version_number > 3	cre_Doc_Template_Mgt
SELECT version_number , template_type_code FROM Templates WHERE version_number > 6	cre_Doc_Template_Mgt
SELECT version_number , template_type_code FROM Templates WHERE version_number > 7	cre_Doc_Template_Mgt
SELECT version_number , template_type_code FROM Templates WHERE version_number > 4	cre_Doc_Template_Mgt
SELECT version_number , template_type_code FROM Templates WHERE version_number > 8	cre_Doc_Template_Mgt
SELECT version_number , template_type_code FROM Templates WHERE version_number > 3	cre_Doc_Template_Mgt
SELECT Name FROM teacher WHERE Age = 42 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 36 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 26 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 31 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 39 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 43	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 37	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 27	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 32	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 40	course_teach
SELECT Name FROM teacher WHERE Age = 42 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 36 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 26 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 31 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 39 OR Age = 33	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 43	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 37	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 27	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 32	course_teach
SELECT Name FROM teacher WHERE Age = 32 OR Age = 40	course_teach
SELECT count(*) FROM visitor WHERE age < 40	museum_visit
SELECT count(*) FROM visitor WHERE age < 37	museum_visit
SELECT count(*) FROM visitor WHERE age < 27	museum_visit
SELECT count(*) FROM visitor WHERE age < 26	museum_visit
SELECT count(*) FROM visitor WHERE age < 28	museum_visit
SELECT name FROM visitor WHERE Level_of_membership > 5 ORDER BY Level_of_membership DESC	museum_visit
SELECT name FROM visitor WHERE Level_of_membership > 6 ORDER BY Level_of_membership DESC	museum_visit
SELECT name FROM visitor WHERE Level_of_membership > 7 ORDER BY Level_of_membership DESC	museum_visit
SELECT name FROM visitor WHERE Level_of_membership > 1 ORDER BY Level_of_membership DESC	museum_visit
SELECT avg(age) FROM visitor WHERE Level_of_membership <= 5	museum_visit
SELECT avg(age) FROM visitor WHERE Level_of_membership <= 10	museum_visit
SELECT avg(age) FROM visitor WHERE Level_of_membership <= 6	museum_visit
SELECT avg(age) FROM visitor WHERE Level_of_membership <= 13	museum_visit
SELECT avg(age) FROM visitor WHERE Level_of_membership <= 8	museum_visit
SELECT name , Level_of_membership FROM visitor WHERE Level_of_membership > 5 ORDER BY age DESC	museum_visit
SELECT name , Level_of_membership FROM visitor WHERE Level_of_membership > 6 ORDER BY age DESC	museum_visit
SELECT name , Level_of_membership FROM visitor WHERE Level_of_membership > 7 ORDER BY age DESC	museum_visit
SELECT name , Level_of_membership FROM visitor WHERE Level_of_membership > 1 ORDER BY age DESC	museum_visit
SELECT avg(num_of_staff) FROM museum WHERE open_year < 2019	museum_visit
SELECT avg(num_of_staff) FROM museum WHERE open_year < 2013	museum_visit
SELECT avg(num_of_staff) FROM museum WHERE open_year < 2003	museum_visit
SELECT avg(num_of_staff) FROM museum WHERE open_year < 2008	museum_visit
SELECT avg(num_of_staff) FROM museum WHERE open_year < 2016	museum_visit
SELECT name FROM museum WHERE num_of_staff > (SELECT min(num_of_staff) FROM museum WHERE open_year > 2004)	museum_visit
SELECT name FROM museum WHERE num_of_staff > (SELECT min(num_of_staff) FROM museum WHERE open_year > 2009)	museum_visit
SELECT name FROM museum WHERE num_of_staff > (SELECT min(num_of_staff) FROM museum WHERE open_year > 2007)	museum_visit
SELECT name FROM museum WHERE num_of_staff > (SELECT min(num_of_staff) FROM museum WHERE open_year > 2006)	museum_visit
SELECT name FROM museum WHERE num_of_staff > (SELECT min(num_of_staff) FROM museum WHERE open_year > 2008)	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 4	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 10	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 5	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 7	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 8	museum_visit
SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year < 2019 INTERSECT SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year > 2011	museum_visit
SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year < 2013 INTERSECT SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year > 2011	museum_visit
SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year < 2016 INTERSECT SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year > 2011	museum_visit
SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year < 2017 INTERSECT SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year > 2011	museum_visit
SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year < 2018 INTERSECT SELECT t1.name FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id JOIN museum AS t3 ON t3.Museum_ID = t2.Museum_ID WHERE t3.open_year > 2011	museum_visit
SELECT count(*) FROM visitor WHERE id NOT IN (SELECT t2.visitor_id FROM museum AS t1 JOIN visit AS t2 ON t1.Museum_ID = t2.Museum_ID WHERE t1.open_year > 2020)	museum_visit
SELECT count(*) FROM visitor WHERE id NOT IN (SELECT t2.visitor_id FROM museum AS t1 JOIN visit AS t2 ON t1.Museum_ID = t2.Museum_ID WHERE t1.open_year > 2014)	museum_visit
SELECT count(*) FROM visitor WHERE id NOT IN (SELECT t2.visitor_id FROM museum AS t1 JOIN visit AS t2 ON t1.Museum_ID = t2.Museum_ID WHERE t1.open_year > 2017)	museum_visit
SELECT count(*) FROM visitor WHERE id NOT IN (SELECT t2.visitor_id FROM museum AS t1 JOIN visit AS t2 ON t1.Museum_ID = t2.Museum_ID WHERE t1.open_year > 2018)	museum_visit
SELECT count(*) FROM visitor WHERE id NOT IN (SELECT t2.visitor_id FROM museum AS t1 JOIN visit AS t2 ON t1.Museum_ID = t2.Museum_ID WHERE t1.open_year > 2019)	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2007 OR open_year < 2008	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2010 OR open_year < 2008	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2009 OR open_year < 2008	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2011 OR open_year < 2008	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2008 OR open_year < 2008	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2013 OR open_year < 2018	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2013 OR open_year < 2012	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2013 OR open_year < 2015	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2013 OR open_year < 2016	museum_visit
SELECT count(*) FROM museum WHERE open_year > 2013 OR open_year < 2017	museum_visit
SELECT winner_name FROM matches WHERE YEAR = 2013 INTERSECT SELECT winner_name FROM matches WHERE YEAR = 2013	wta_1
SELECT winner_name FROM matches WHERE YEAR = 2013 INTERSECT SELECT winner_name FROM matches WHERE YEAR = 2017	wta_1
SELECT winner_name FROM matches WHERE YEAR = 2017 INTERSECT SELECT winner_name FROM matches WHERE YEAR = 2016	wta_1
SELECT winner_name FROM matches WHERE YEAR = 2016 INTERSECT SELECT winner_name FROM matches WHERE YEAR = 2016	wta_1
SELECT winner_name FROM matches WHERE YEAR = 2013 INTERSECT SELECT winner_name FROM matches WHERE YEAR = 2013	wta_1
SELECT winner_name FROM matches WHERE YEAR = 2013 INTERSECT SELECT winner_name FROM matches WHERE YEAR = 2017	wta_1
SELECT winner_name FROM matches WHERE YEAR = 2017 INTERSECT SELECT winner_name FROM matches WHERE YEAR = 2016	wta_1
SELECT winner_name FROM matches WHERE YEAR = 2016 INTERSECT SELECT winner_name FROM matches WHERE YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2026	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2020	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2010	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2015	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2023	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2023 OR YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2017 OR YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2007 OR YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2012 OR YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2020 OR YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2026	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2020	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2010	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2015	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2013 OR YEAR = 2023	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2023 OR YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2017 OR YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2007 OR YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2012 OR YEAR = 2016	wta_1
SELECT count(*) FROM matches WHERE YEAR = 2020 OR YEAR = 2016	wta_1
SELECT T1.id , T1.name FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle JOIN death AS T3 ON T2.id = T3.caused_by_ship_id GROUP BY T1.id HAVING sum(T3.killed) > 2	battle_death
SELECT T1.id , T1.name FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle JOIN death AS T3 ON T2.id = T3.caused_by_ship_id GROUP BY T1.id HAVING sum(T3.killed) > 1	battle_death
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 210	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 194	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 207	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 208	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 209	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 210	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 194	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 207	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 208	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 209	poker_player
SELECT Name FROM country WHERE IndepYear > 1960	world_1
SELECT Name FROM country WHERE IndepYear > 1954	world_1
SELECT Name FROM country WHERE IndepYear > 1944	world_1
SELECT Name FROM country WHERE IndepYear > 1957	world_1
SELECT Name FROM country WHERE IndepYear > 1947	world_1
SELECT Name FROM country WHERE IndepYear > 1960	world_1
SELECT Name FROM country WHERE IndepYear > 1954	world_1
SELECT Name FROM country WHERE IndepYear > 1944	world_1
SELECT Name FROM country WHERE IndepYear > 1957	world_1
SELECT Name FROM country WHERE IndepYear > 1947	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1921 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1922 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1920 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1923 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1921 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1922 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1920 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1923 AND T2.IsOfficial = "T"	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 82	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 76	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 66	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 71	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 79	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 82	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 76	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 66	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 71	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 79	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 82	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 76	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 66	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 79	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 69	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 82	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 76	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 66	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 79	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 69	world_1
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2002	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2007	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2005	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2004	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2006	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2002	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2007	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2005	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2004	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2006	orchestra
SELECT name FROM Highschooler WHERE grade = 9	network_1
SELECT name FROM Highschooler WHERE grade = 12	network_1
SELECT name FROM Highschooler WHERE grade = 11	network_1
SELECT name FROM Highschooler WHERE grade = 9	network_1
SELECT name FROM Highschooler WHERE grade = 12	network_1
SELECT name FROM Highschooler WHERE grade = 11	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 19	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 17	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 7	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 5	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 8	network_1
SELECT count(*) FROM Highschooler WHERE grade = 18 OR grade = 10	network_1
SELECT count(*) FROM Highschooler WHERE grade = 3 OR grade = 10	network_1
SELECT count(*) FROM Highschooler WHERE grade = 7 OR grade = 10	network_1
SELECT count(*) FROM Highschooler WHERE grade = 5 OR grade = 10	network_1
SELECT count(*) FROM Highschooler WHERE grade = 8 OR grade = 10	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 19	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 17	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 7	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 5	network_1
SELECT count(*) FROM Highschooler WHERE grade = 9 OR grade = 8	network_1
SELECT count(*) FROM Highschooler WHERE grade = 18 OR grade = 10	network_1
SELECT count(*) FROM Highschooler WHERE grade = 3 OR grade = 10	network_1
SELECT count(*) FROM Highschooler WHERE grade = 7 OR grade = 10	network_1
SELECT count(*) FROM Highschooler WHERE grade = 5 OR grade = 10	network_1
SELECT count(*) FROM Highschooler WHERE grade = 8 OR grade = 10	network_1
SELECT T2.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.grade > 10 GROUP BY T1.student_id HAVING count(*) >= 2	network_1
SELECT T2.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.grade > 9 GROUP BY T1.student_id HAVING count(*) >= 2	network_1
SELECT T2.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.grade > 10 GROUP BY T1.student_id HAVING count(*) >= 2	network_1
SELECT T2.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.grade > 9 GROUP BY T1.student_id HAVING count(*) >= 2	network_1
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1959	singer
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1953	singer
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1943	singer
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1948	singer
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1956	singer
SELECT Name FROM singer WHERE Birth_Year = 1958 OR Birth_Year = 1949	singer
SELECT Name FROM singer WHERE Birth_Year = 1952 OR Birth_Year = 1949	singer
SELECT Name FROM singer WHERE Birth_Year = 1942 OR Birth_Year = 1949	singer
SELECT Name FROM singer WHERE Birth_Year = 1947 OR Birth_Year = 1949	singer
SELECT Name FROM singer WHERE Birth_Year = 1955 OR Birth_Year = 1949	singer
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1959	singer
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1953	singer
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1943	singer
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1948	singer
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1956	singer
SELECT Name FROM singer WHERE Birth_Year = 1958 OR Birth_Year = 1949	singer
SELECT Name FROM singer WHERE Birth_Year = 1952 OR Birth_Year = 1949	singer
SELECT Name FROM singer WHERE Birth_Year = 1942 OR Birth_Year = 1949	singer
SELECT Name FROM singer WHERE Birth_Year = 1947 OR Birth_Year = 1949	singer
SELECT Name FROM singer WHERE Birth_Year = 1955 OR Birth_Year = 1949	singer
SELECT property_name FROM Properties WHERE property_type_code = "House" UNION SELECT property_name FROM Properties WHERE property_type_code = "Apartment" AND room_count > 4	real_estate_properties
SELECT property_name FROM Properties WHERE property_type_code = "House" UNION SELECT property_name FROM Properties WHERE property_type_code = "Apartment" AND room_count > 10	real_estate_properties
SELECT property_name FROM Properties WHERE property_type_code = "House" UNION SELECT property_name FROM Properties WHERE property_type_code = "Apartment" AND room_count > 5	real_estate_properties
SELECT property_name FROM Properties WHERE property_type_code = "House" UNION SELECT property_name FROM Properties WHERE property_type_code = "Apartment" AND room_count > 7	real_estate_properties
SELECT property_name FROM Properties WHERE property_type_code = "House" UNION SELECT property_name FROM Properties WHERE property_type_code = "Apartment" AND room_count > 8	real_estate_properties
