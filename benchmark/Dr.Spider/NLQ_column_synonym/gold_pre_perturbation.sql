SELECT name , capacity FROM stadium ORDER BY average DESC LIMIT 1	concert_singer
SELECT name , country FROM singer WHERE song_name LIKE '%Hey%'	concert_singer
SELECT name , country FROM singer WHERE song_name LIKE '%Hey%'	concert_singer
SELECT name , country FROM singer WHERE song_name LIKE '%Hey%'	concert_singer
SELECT name , country FROM singer WHERE song_name LIKE '%Hey%'	concert_singer
SELECT T1.fname , T1.sex FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid GROUP BY T1.stuid HAVING count(*) > 1	pets_1
SELECT count(*) FROM pets WHERE weight > 10	pets_1
SELECT count(*) FROM pets WHERE weight > 10	pets_1
SELECT weight FROM pets ORDER BY pet_age LIMIT 1	pets_1
SELECT max(weight) , petType FROM pets GROUP BY petType	pets_1
SELECT count(*) FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T2.petid = T3.petid WHERE T1.sex = 'F' AND T3.pettype = 'dog'	pets_1
SELECT avg(weight) , pettype FROM pets GROUP BY pettype	pets_1
SELECT T1.fname , T1.sex FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid GROUP BY T1.stuid HAVING count(*) > 1	pets_1
SELECT T1.Accelerate FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T2.Make = 'amc hornet sportabout (sw)'	car_1
SELECT T1.Accelerate FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T2.Make = 'amc hornet sportabout (sw)'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT T1.horsepower FROM CARS_DATA AS T1 ORDER BY T1.accelerate DESC LIMIT 1	car_1
SELECT T1.horsepower FROM CARS_DATA AS T1 ORDER BY T1.accelerate DESC LIMIT 1	car_1
SELECT T1.horsepower FROM CARS_DATA AS T1 ORDER BY T1.accelerate DESC LIMIT 1	car_1
SELECT Maker , Model FROM MODEL_LIST	car_1
SELECT Maker , Model FROM MODEL_LIST	car_1
SELECT Maker , Model FROM MODEL_LIST	car_1
SELECT Maker , Model FROM MODEL_LIST	car_1
SELECT Maker , Model FROM MODEL_LIST	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 3 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 3 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 3 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 4	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 4	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model JOIN CARS_DATA AS T4 ON T3.MakeId = T4.id WHERE T4.year = '1970'	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'General Motors' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'General Motors' OR T4.weight > 3500	car_1
SELECT T2.Make , T1.Year FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Year = (SELECT min(YEAR) FROM CARS_DATA)	car_1
SELECT T2.Make , T1.Year FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Year = (SELECT min(YEAR) FROM CARS_DATA)	car_1
SELECT T2.Make , T1.Year FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Year = (SELECT min(YEAR) FROM CARS_DATA)	car_1
SELECT T2.Make , T1.Year FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Year = (SELECT min(YEAR) FROM CARS_DATA)	car_1
SELECT T2.Make , T1.Year FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Year = (SELECT min(YEAR) FROM CARS_DATA)	car_1
SELECT T2.Make , T1.Year FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Year = (SELECT min(YEAR) FROM CARS_DATA)	car_1
SELECT T2.Make , T1.Year FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Year = (SELECT min(YEAR) FROM CARS_DATA)	car_1
SELECT T2.Make , T1.Year FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Year = (SELECT min(YEAR) FROM CARS_DATA)	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 4 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Accelerate > ( SELECT Accelerate FROM CARS_DATA ORDER BY Horsepower DESC LIMIT 1 )	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Accelerate > ( SELECT Accelerate FROM CARS_DATA ORDER BY Horsepower DESC LIMIT 1 )	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Accelerate > ( SELECT Accelerate FROM CARS_DATA ORDER BY Horsepower DESC LIMIT 1 )	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.horsepower ASC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.horsepower ASC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.horsepower ASC LIMIT 1	car_1
SELECT T1.model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Weight < (SELECT avg(Weight) FROM CARS_DATA)	car_1
SELECT T1.model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Weight < (SELECT avg(Weight) FROM CARS_DATA)	car_1
SELECT T1.model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Weight < (SELECT avg(Weight) FROM CARS_DATA)	car_1
SELECT T1.model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Weight < (SELECT avg(Weight) FROM CARS_DATA)	car_1
SELECT T1.model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Weight < (SELECT avg(Weight) FROM CARS_DATA)	car_1
SELECT T2.Make , T1.Year FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Year = (SELECT min(YEAR) FROM CARS_DATA)	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1980	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1980	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.model = T2.model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.id WHERE T3.year > 1980	car_1
SELECT T1.Accelerate FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T2.Make = 'amc hornet sportabout (sw)'	car_1
SELECT T1.Accelerate FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T2.Make = 'amc hornet sportabout (sw)'	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 4	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 4	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 4	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 4	car_1
SELECT avg(mpg) FROM CARS_DATA WHERE Cylinders = 4	car_1
select min(weight) from cars_data where cylinders = 8 and year = 1974	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 150	car_1
SELECT count(*) FROM CARS_DATA WHERE horsepower > 150	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.mpg DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.mpg DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.mpg DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.mpg DESC LIMIT 1	car_1
select t1.model from car_names as t1 join cars_data as t2 on t1.makeid = t2.id order by t2.mpg desc limit 1	car_1
select t1.model from car_names as t1 join cars_data as t2 on t1.makeid = t2.id order by t2.mpg desc limit 1	car_1
SELECT avg(horsepower) FROM CARS_DATA WHERE YEAR < 1980	car_1
SELECT avg(horsepower) FROM CARS_DATA WHERE YEAR < 1980	car_1
select avg(horsepower) from cars_data where year < 1980	car_1
SELECT max(Accelerate) , Cylinders FROM CARS_DATA GROUP BY Cylinders	car_1
SELECT max(Accelerate) , Cylinders FROM CARS_DATA GROUP BY Cylinders	car_1
SELECT max(Accelerate) , Cylinders FROM CARS_DATA GROUP BY Cylinders	car_1
SELECT count(*) FROM CARS_DATA WHERE Cylinders > 4	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'General Motors' OR T4.weight > 3500	car_1
select distinct year from cars_data where weight between 3000 and 4000	car_1
select distinct year from cars_data where weight between 3000 and 4000	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 4 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 4 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 4 ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.MakeId , T2.Make FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T1.Horsepower > (SELECT min(Horsepower) FROM CARS_DATA) AND T1.Cylinders <= 3	car_1
select max(mpg) from cars_data where cylinders = 8 or year < 1980	car_1
select max(mpg) from cars_data where cylinders = 8 or year < 1980	car_1
select max(mpg) from cars_data where cylinders = 8 or year < 1980	car_1
SELECT T1.Id , T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker GROUP BY T1.Id HAVING count(*) >= 2 INTERSECT SELECT T1.Id , T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model GROUP BY T1.Id HAVING count(*) > 3	car_1
SELECT T1.Id , T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker GROUP BY T1.Id HAVING count(*) >= 2 INTERSECT SELECT T1.Id , T1.Maker FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker JOIN CAR_NAMES AS T3 ON T2.model = T3.model GROUP BY T1.Id HAVING count(*) > 3	car_1
SELECT T1.countryId , T1.CountryName FROM Countries AS T1 JOIN CAR_MAKERS AS T2 ON T1.CountryId = T2.Country GROUP BY T1.countryId HAVING count(*) > 3 UNION SELECT T1.countryId , T1.CountryName FROM Countries AS T1 JOIN CAR_MAKERS AS T2 ON T1.CountryId = T2.Country JOIN MODEL_LIST AS T3 ON T2.Id = T3.Maker WHERE T3.Model = 'fiat'	car_1
SELECT Abbreviation FROM AIRLINES WHERE Airline = "JetBlue Airways"	flight_2
SELECT Abbreviation FROM AIRLINES WHERE Airline = "JetBlue Airways"	flight_2
SELECT Abbreviation FROM AIRLINES WHERE Airline = "JetBlue Airways"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRPORTS AS T2 ON T1.SourceAirport = T2.AirportCode WHERE T2.City = "Aberdeen"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRPORTS AS T2 ON T1.SourceAirport = T2.AirportCode WHERE T2.City = "Aberdeen"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "APG" INTERSECT SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "CVO"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "APG" INTERSECT SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "CVO"	flight_2
SELECT Abbreviation FROM AIRLINES WHERE Airline = "JetBlue Airways"	flight_2
SELECT count(*) FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T2.Airline = T1.uid WHERE T1.Airline = "United Airlines" AND T2.SourceAirport = "AHD"	flight_2
SELECT count(*) FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T2.Airline = T1.uid WHERE T1.Airline = "United Airlines" AND T2.SourceAirport = "AHD"	flight_2
SELECT count(*) FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T2.Airline = T1.uid WHERE T1.Airline = "United Airlines" AND T2.SourceAirport = "AHD"	flight_2
SELECT count(*) FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T2.Airline = T1.uid WHERE T1.Airline = "United Airlines" AND T2.SourceAirport = "AHD"	flight_2
SELECT count(*) FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T2.Airline = T1.uid WHERE T1.Airline = "United Airlines" AND T2.SourceAirport = "AHD"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRPORTS AS T2 ON T1.SourceAirport = T2.AirportCode WHERE T2.City = "Aberdeen"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.DestAirport = "AHD"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.DestAirport = "AHD"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.DestAirport = "AHD"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.DestAirport = "AHD"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.DestAirport = "AHD"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.DestAirport = "AHD"	flight_2
SELECT AirportName FROM Airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM Flights UNION SELECT DestAirport FROM Flights)	flight_2
SELECT AirportName FROM Airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM Flights UNION SELECT DestAirport FROM Flights)	flight_2
SELECT AirportName FROM Airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM Flights UNION SELECT DestAirport FROM Flights)	flight_2
SELECT AirportName FROM Airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM Flights UNION SELECT DestAirport FROM Flights)	flight_2
SELECT AirportName FROM Airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM Flights UNION SELECT DestAirport FROM Flights)	flight_2
SELECT AirportName FROM Airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM Flights UNION SELECT DestAirport FROM Flights)	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "UAL"	flight_2
SELECT T1.Abbreviation , T1.Country FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline GROUP BY T1.Airline ORDER BY count(*) LIMIT 1	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "AHD"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "AHD"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.DestAirport = "AHD"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.DestAirport = "AHD"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "CVO" EXCEPT SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "APG"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "CVO" EXCEPT SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "APG"	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "CVO" EXCEPT SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline WHERE T2.SourceAirport = "APG"	flight_2
SELECT FlightNo FROM FLIGHTS WHERE SourceAirport = "APG"	flight_2
SELECT FlightNo FROM FLIGHTS WHERE SourceAirport = "APG"	flight_2
SELECT FlightNo FROM FLIGHTS WHERE DestAirport = "APG"	flight_2
SELECT count(*) , LOCATION FROM shop GROUP BY LOCATION	employee_hire_evaluation
SELECT manager_name , district FROM shop ORDER BY number_products DESC LIMIT 1	employee_hire_evaluation
SELECT min(Number_products) , max(Number_products) FROM shop	employee_hire_evaluation
SELECT min(Number_products) , max(Number_products) FROM shop	employee_hire_evaluation
SELECT name , LOCATION , district FROM shop ORDER BY number_products DESC	employee_hire_evaluation
SELECT name , LOCATION , district FROM shop ORDER BY number_products DESC	employee_hire_evaluation
SELECT name FROM shop WHERE number_products > (SELECT avg(number_products) FROM shop)	employee_hire_evaluation
SELECT name FROM shop WHERE number_products > (SELECT avg(number_products) FROM shop)	employee_hire_evaluation
SELECT name FROM shop WHERE number_products > (SELECT avg(number_products) FROM shop)	employee_hire_evaluation
SELECT template_type_code , template_type_description FROM Ref_template_types	cre_Doc_Template_Mgt
SELECT template_type_code , template_type_description FROM Ref_template_types	cre_Doc_Template_Mgt
SELECT template_type_code , template_type_description FROM Ref_template_types	cre_Doc_Template_Mgt
SELECT template_type_code , template_type_description FROM Ref_template_types	cre_Doc_Template_Mgt
SELECT template_type_code , template_type_description FROM Ref_template_types	cre_Doc_Template_Mgt
SELECT document_id , document_name , document_description FROM Documents	cre_Doc_Template_Mgt
SELECT template_type_code , count(*) FROM Templates GROUP BY template_type_code	cre_Doc_Template_Mgt
SELECT template_type_code , count(*) FROM Templates GROUP BY template_type_code	cre_Doc_Template_Mgt
SELECT template_type_code , count(*) FROM Templates GROUP BY template_type_code	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Presentation"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "Book"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "Book"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Robbin CV"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Robbin CV"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Robbin CV"	cre_Doc_Template_Mgt
SELECT template_id , version_number , template_type_code FROM Templates	cre_Doc_Template_Mgt
SELECT template_id , version_number , template_type_code FROM Templates	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "CV"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "CV"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Templates GROUP BY template_type_code ORDER BY count(*) DESC LIMIT 1	cre_Doc_Template_Mgt
SELECT min(Version_Number) , template_type_code FROM Templates	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Data base"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Data base"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Data base"	cre_Doc_Template_Mgt
SELECT T1.template_type_code , count(*) FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id GROUP BY T1.template_type_code	cre_Doc_Template_Mgt
SELECT template_type_code FROM Templates EXCEPT SELECT template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id	cre_Doc_Template_Mgt
SELECT template_type_code FROM Templates EXCEPT SELECT template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id	cre_Doc_Template_Mgt
SELECT template_type_code , template_type_description FROM Ref_template_types	cre_Doc_Template_Mgt
SELECT template_type_code , template_type_description FROM Ref_template_types	cre_Doc_Template_Mgt
SELECT template_type_description FROM Ref_template_types WHERE template_type_code = "AD"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "Book"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Presentation"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Presentation"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Presentation"	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'Summer Show'	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'Summer Show'	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'Summer Show'	cre_Doc_Template_Mgt
select other_details from paragraphs where paragraph_text like 'korea'	cre_Doc_Template_Mgt
select other_details from paragraphs where paragraph_text like 'korea'	cre_Doc_Template_Mgt
select other_details from paragraphs where paragraph_text like 'korea'	cre_Doc_Template_Mgt
select other_details from paragraphs where paragraph_text like 'korea'	cre_Doc_Template_Mgt
select other_details from paragraphs where paragraph_text like 'korea'	cre_Doc_Template_Mgt
select other_details from paragraphs where paragraph_text like 'korea'	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Customer reviews"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Customer reviews"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Customer reviews"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Customer reviews"	cre_Doc_Template_Mgt
SELECT document_id FROM Paragraphs WHERE paragraph_text = 'Brazil' INTERSECT SELECT document_id FROM Paragraphs WHERE paragraph_text = 'Ireland'	cre_Doc_Template_Mgt
SELECT document_id FROM Paragraphs WHERE paragraph_text = 'Brazil' INTERSECT SELECT document_id FROM Paragraphs WHERE paragraph_text = 'Ireland'	cre_Doc_Template_Mgt
SELECT Age , Hometown FROM teacher	course_teach
SELECT Age , Hometown FROM teacher	course_teach
SELECT Hometown , COUNT(*) FROM teacher GROUP BY Hometown	course_teach
SELECT Hometown , COUNT(*) FROM teacher GROUP BY Hometown	course_teach
SELECT T3.Name , T2.Course FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID	course_teach
SELECT T3.Name , T2.Course FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID	course_teach
SELECT T3.Name , T2.Course FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID	course_teach
select name from teacher where hometown != "little lever urban district"	course_teach
select name from teacher where hometown != "little lever urban district"	course_teach
select name from teacher where hometown != "little lever urban district"	course_teach
select name from teacher where hometown != "little lever urban district"	course_teach
select name from teacher where hometown != "little lever urban district"	course_teach
select name from teacher where hometown != "little lever urban district"	course_teach
select name from teacher where hometown != "little lever urban district"	course_teach
SELECT Hometown FROM teacher ORDER BY Age ASC LIMIT 1	course_teach
SELECT Hometown FROM teacher GROUP BY Hometown ORDER BY COUNT(*) DESC LIMIT 1	course_teach
SELECT T3.Name FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID WHERE T2.Course = "Math"	course_teach
SELECT T3.Name FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID WHERE T2.Course = "Math"	course_teach
SELECT T3.Name FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID WHERE T2.Course = "Math"	course_teach
SELECT T3.Name FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID WHERE T2.Course = "Math"	course_teach
SELECT T3.Name FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID WHERE T2.Course = "Math"	course_teach
SELECT avg(age) FROM visitor WHERE Level_of_membership <= 4	museum_visit
SELECT name , Level_of_membership FROM visitor WHERE Level_of_membership > 4 ORDER BY age DESC	museum_visit
SELECT museum_id , name FROM museum ORDER BY num_of_staff DESC LIMIT 1	museum_visit
SELECT avg(num_of_staff) FROM museum WHERE open_year < 2009	museum_visit
SELECT avg(num_of_staff) FROM museum WHERE open_year < 2009	museum_visit
SELECT Num_of_Staff , Open_Year FROM museum WHERE name = 'Plaza Museum'	museum_visit
SELECT name FROM museum WHERE num_of_staff > (SELECT min(num_of_staff) FROM museum WHERE open_year > 2010)	museum_visit
SELECT name FROM museum WHERE num_of_staff > (SELECT min(num_of_staff) FROM museum WHERE open_year > 2010)	museum_visit
SELECT avg(num_of_ticket) , max(num_of_ticket) FROM visit	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 1	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 1	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 1	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 1	museum_visit
SELECT sum(t2.Total_spent) FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id WHERE t1.Level_of_membership = 1	museum_visit
SELECT winner_name , winner_rank_points FROM matches GROUP BY winner_name ORDER BY count(*) DESC LIMIT 1	wta_1
SELECT winner_name , winner_rank_points FROM matches GROUP BY winner_name ORDER BY count(*) DESC LIMIT 1	wta_1
SELECT avg(ranking) , T1.first_name FROM players AS T1 JOIN rankings AS T2 ON T1.player_id = T2.player_id GROUP BY T1.first_name	wta_1
SELECT avg(loser_age) , avg(winner_age) FROM matches	wta_1
SELECT avg(loser_age) , avg(winner_age) FROM matches	wta_1
SELECT avg(loser_age) , avg(winner_age) FROM matches	wta_1
SELECT avg(loser_age) , avg(winner_age) FROM matches	wta_1
SELECT winner_name , winner_rank_points FROM matches GROUP BY winner_name ORDER BY count(*) DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Australian Open' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Australian Open' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Australian Open' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Australian Open' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name , loser_name FROM matches ORDER BY minutes DESC LIMIT 1	wta_1
SELECT winner_name , loser_name FROM matches ORDER BY minutes DESC LIMIT 1	wta_1
SELECT winner_name , loser_name FROM matches ORDER BY minutes DESC LIMIT 1	wta_1
SELECT sum(ranking_points) , T1.first_name FROM players AS T1 JOIN rankings AS T2 ON T1.player_id = T2.player_id GROUP BY T1.first_name	wta_1
SELECT sum(ranking_points) , T1.first_name FROM players AS T1 JOIN rankings AS T2 ON T1.player_id = T2.player_id GROUP BY T1.first_name	wta_1
SELECT T1.first_name , T1.country_code , T1.birth_date FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id ORDER BY T2.winner_rank_points DESC LIMIT 1	wta_1
SELECT T1.first_name , T1.country_code , T1.birth_date FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id ORDER BY T2.winner_rank_points DESC LIMIT 1	wta_1
SELECT T1.killed , T1.injured FROM death AS T1 JOIN ship AS t2 ON T1.caused_by_ship_id = T2.id WHERE T2.tonnage = 't'	battle_death
SELECT T1.killed , T1.injured FROM death AS T1 JOIN ship AS t2 ON T1.caused_by_ship_id = T2.id WHERE T2.tonnage = 't'	battle_death
SELECT T1.killed , T1.injured FROM death AS T1 JOIN ship AS t2 ON T1.caused_by_ship_id = T2.id WHERE T2.tonnage = 't'	battle_death
SELECT max(killed) , min(killed) FROM death	battle_death
SELECT max(killed) , min(killed) FROM death	battle_death
SELECT max(killed) , min(killed) FROM death	battle_death
SELECT max(killed) , min(killed) FROM death	battle_death
SELECT max(killed) , min(killed) FROM death	battle_death
SELECT T1.id , T1.name FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle JOIN death AS T3 ON T2.id = T3.caused_by_ship_id GROUP BY T1.id HAVING sum(T3.killed) > 10	battle_death
SELECT T1.id , T1.name FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle JOIN death AS T3 ON T2.id = T3.caused_by_ship_id GROUP BY T1.id HAVING sum(T3.killed) > 10	battle_death
SELECT name FROM battle WHERE bulgarian_commander = 'Kaloyan' AND latin_commander = 'Baldwin I'	battle_death
SELECT name FROM battle WHERE bulgarian_commander = 'Kaloyan' AND latin_commander = 'Baldwin I'	battle_death
SELECT note FROM death WHERE note LIKE '%East%'	battle_death
SELECT section_name , section_description FROM Sections	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'math'	student_transcripts_tracking
SELECT line_1 , line_2 FROM addresses	student_transcripts_tracking
SELECT line_1 , line_2 FROM addresses	student_transcripts_tracking
SELECT line_1 , line_2 FROM addresses	student_transcripts_tracking
SELECT line_1 , line_2 FROM addresses	student_transcripts_tracking
SELECT section_name , section_description FROM Sections	student_transcripts_tracking
SELECT department_description FROM Departments WHERE department_name LIKE '%computer%'	student_transcripts_tracking
SELECT department_description FROM Departments WHERE department_name LIKE '%computer%'	student_transcripts_tracking
SELECT DISTINCT T1.first_name , T1.middle_name , T1.last_name FROM Students AS T1 JOIN Student_Enrolment AS T2 ON T1.student_id = T2.student_id JOIN Degree_Programs AS T3 ON T2.degree_program_id = T3.degree_program_id WHERE T3.degree_summary_name = 'Bachelor'	student_transcripts_tracking
select cell_mobile_number from students where first_name = 'timmothy' and last_name = 'ward'	student_transcripts_tracking
select cell_mobile_number from students where first_name = 'timmothy' and last_name = 'ward'	student_transcripts_tracking
select cell_mobile_number from students where first_name = 'timmothy' and last_name = 'ward'	student_transcripts_tracking
select cell_mobile_number from students where first_name = 'timmothy' and last_name = 'ward'	student_transcripts_tracking
select cell_mobile_number from students where first_name = 'timmothy' and last_name = 'ward'	student_transcripts_tracking
SELECT first_name , middle_name , last_name FROM Students ORDER BY date_first_registered ASC LIMIT 1	student_transcripts_tracking
SELECT transcript_date , other_details FROM Transcripts ORDER BY transcript_date ASC LIMIT 1	student_transcripts_tracking
SELECT transcript_date , other_details FROM Transcripts ORDER BY transcript_date ASC LIMIT 1	student_transcripts_tracking
SELECT transcript_date , other_details FROM Transcripts ORDER BY transcript_date ASC LIMIT 1	student_transcripts_tracking
SELECT transcript_date , other_details FROM Transcripts ORDER BY transcript_date ASC LIMIT 1	student_transcripts_tracking
SELECT transcript_date , other_details FROM Transcripts ORDER BY transcript_date ASC LIMIT 1	student_transcripts_tracking
SELECT DISTINCT T2.semester_id FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id WHERE degree_summary_name = 'Master' INTERSECT SELECT DISTINCT T2.semester_id FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id WHERE degree_summary_name = 'Bachelor'	student_transcripts_tracking
SELECT other_student_details FROM Students ORDER BY other_student_details DESC	student_transcripts_tracking
SELECT other_student_details FROM Students ORDER BY other_student_details DESC	student_transcripts_tracking
SELECT other_student_details FROM Students ORDER BY other_student_details DESC	student_transcripts_tracking
SELECT other_student_details FROM Students ORDER BY other_student_details DESC	student_transcripts_tracking
SELECT other_student_details FROM Students ORDER BY other_student_details DESC	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'h'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'h'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'h'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'h'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'h'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '09700166582'	student_transcripts_tracking
SELECT package_option , series_name FROM TV_Channel WHERE hight_definition_TV = "yes"	tvshow
SELECT package_option , series_name FROM TV_Channel WHERE hight_definition_TV = "yes"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "A Love of a Lifetime"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "A Love of a Lifetime"	tvshow
SELECT Content FROM TV_Channel WHERE series_name = "Sky Radio"	tvshow
SELECT Content FROM TV_Channel WHERE series_name = "Sky Radio"	tvshow
SELECT Content FROM TV_Channel WHERE series_name = "Sky Radio"	tvshow
SELECT Content FROM TV_Channel WHERE series_name = "Sky Radio"	tvshow
SELECT Title FROM Cartoon ORDER BY title	tvshow
SELECT title , Directed_by FROM Cartoon ORDER BY Original_air_date	tvshow
SELECT Title FROM Cartoon ORDER BY title	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "Joseph Kuhr"	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "Joseph Kuhr"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones" OR Directed_by = "Brandon Vietti"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones" OR Directed_by = "Brandon Vietti"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones" OR Directed_by = "Brandon Vietti"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones" OR Directed_by = "Brandon Vietti"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "Sky Radio"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "Sky Radio"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "Sky Radio"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "Sky Radio"	tvshow
SELECT max(SHARE) , min(SHARE) FROM TV_series	tvshow
SELECT max(SHARE) , min(SHARE) FROM TV_series	tvshow
SELECT max(SHARE) , min(SHARE) FROM TV_series	tvshow
SELECT max(SHARE) , min(SHARE) FROM TV_series	tvshow
SELECT package_option , series_name FROM TV_Channel WHERE hight_definition_TV = "yes"	tvshow
SELECT package_option , series_name FROM TV_Channel WHERE hight_definition_TV = "yes"	tvshow
SELECT package_option , series_name FROM TV_Channel WHERE hight_definition_TV = "yes"	tvshow
SELECT package_option , series_name FROM TV_Channel WHERE hight_definition_TV = "yes"	tvshow
SELECT package_option , series_name FROM TV_Channel WHERE hight_definition_TV = "yes"	tvshow
SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Michael Chang' INTERSECT SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Ben Jones'	tvshow
SELECT Pixel_aspect_ratio_PAR , country FROM tv_channel WHERE LANGUAGE != 'English'	tvshow
SELECT Pixel_aspect_ratio_PAR , country FROM tv_channel WHERE LANGUAGE != 'English'	tvshow
SELECT Pixel_aspect_ratio_PAR , country FROM tv_channel WHERE LANGUAGE != 'English'	tvshow
SELECT package_option FROM TV_Channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = 'Ben Jones')	tvshow
SELECT package_option FROM TV_Channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = 'Ben Jones')	tvshow
SELECT package_option FROM TV_Channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = 'Ben Jones')	tvshow
SELECT package_option FROM TV_Channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = 'Ben Jones')	tvshow
SELECT package_option FROM TV_Channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = 'Ben Jones')	tvshow
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T2.Earnings > 300000	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T2.Earnings > 300000	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T2.Earnings > 300000	poker_player
SELECT Earnings FROM poker_player ORDER BY Earnings DESC	poker_player
SELECT Earnings FROM poker_player ORDER BY Earnings DESC	poker_player
SELECT Nationality FROM people GROUP BY Nationality HAVING COUNT(*) >= 2	poker_player
SELECT Nationality FROM people GROUP BY Nationality HAVING COUNT(*) >= 2	poker_player
SELECT Nationality FROM people GROUP BY Nationality ORDER BY COUNT(*) DESC LIMIT 1	poker_player
SELECT Earnings FROM poker_player ORDER BY Earnings DESC	poker_player
SELECT Earnings FROM poker_player ORDER BY Earnings DESC	poker_player
SELECT avg(Earnings) FROM poker_player	poker_player
SELECT avg(Earnings) FROM poker_player	poker_player
SELECT Money_Rank FROM poker_player ORDER BY Earnings DESC LIMIT 1	poker_player
SELECT Money_Rank FROM poker_player ORDER BY Earnings DESC LIMIT 1	poker_player
SELECT max(Final_Table_Made) FROM poker_player WHERE Earnings < 200000	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T2.Earnings > 300000	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T2.Earnings > 300000	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T2.Earnings > 300000	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T2.Earnings > 300000	poker_player
SELECT T1.Birth_Date FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID ORDER BY T2.Earnings ASC LIMIT 1	poker_player
SELECT avg(T2.Earnings) FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Height > 200	poker_player
SELECT Nationality , COUNT(*) FROM people GROUP BY Nationality	poker_player
SELECT Name FROM people WHERE Nationality != "Russia"	poker_player
SELECT Name FROM people WHERE Nationality != "Russia"	poker_player
SELECT Name FROM people WHERE Nationality != "Russia"	poker_player
SELECT max(created) FROM votes WHERE state = 'CA'	voter_1
SELECT max(created) FROM votes WHERE state = 'CA'	voter_1
SELECT vote_id , phone_number , state FROM votes	voter_1
SELECT DISTINCT state , created FROM votes	voter_1
SELECT DISTINCT state , created FROM votes	voter_1
SELECT DISTINCT state , created FROM votes	voter_1
select t1.name from country as t1 join countrylanguage as t2 on t1.code = t2.countrycode where t2.language = "english" and isofficial = "t" union select t1.name from country as t1 join countrylanguage as t2 on t1.code = t2.countrycode where t2.language = "dutch" and isofficial = "t"	world_1
select t1.name from country as t1 join countrylanguage as t2 on t1.code = t2.countrycode where t2.language = "english" and isofficial = "t" union select t1.name from country as t1 join countrylanguage as t2 on t1.code = t2.countrycode where t2.language = "dutch" and isofficial = "t"	world_1
SELECT Name , population , HeadOfState FROM country ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT avg(GNP) , sum(population) FROM country WHERE GovernmentForm = "US Territory"	world_1
SELECT avg(GNP) , sum(population) FROM country WHERE GovernmentForm = "US Territory"	world_1
SELECT avg(GNP) , sum(population) FROM country WHERE GovernmentForm = "US Territory"	world_1
SELECT avg(GNP) , sum(population) FROM country WHERE GovernmentForm = "US Territory"	world_1
SELECT avg(GNP) , sum(population) FROM country WHERE GovernmentForm = "US Territory"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT count(DISTINCT T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE IndepYear < 1930 AND T2.IsOfficial = "T"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Chinese"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Chinese"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Chinese"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Chinese"	world_1
SELECT Name , Population , LifeExpectancy FROM country WHERE Continent = "Asia" ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT Name , Population , LifeExpectancy FROM country WHERE Continent = "Asia" ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT Name , Population , LifeExpectancy FROM country WHERE Continent = "Asia" ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT Name , population , HeadOfState FROM country ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT Name , population , HeadOfState FROM country ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT Name , population , HeadOfState FROM country ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT Name , population , HeadOfState FROM country ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT Name , population , HeadOfState FROM country ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT count(*) FROM country WHERE GovernmentForm = "Republic"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Caribbean"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Caribbean"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Caribbean"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Caribbean"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Caribbean"	world_1
SELECT Name FROM country WHERE Continent = "Asia" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "Asia" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "Asia" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = "Asia"	world_1
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = "Asia"	world_1
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = "Asia"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Continent = "Africa" AND GovernmentForm = "Republic"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Continent = "Africa" AND GovernmentForm = "Republic"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Continent = "Africa" AND GovernmentForm = "Republic"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "Europe"	world_1
SELECT avg(GNP) , sum(population) FROM country WHERE GovernmentForm = "US Territory"	world_1
SELECT avg(GNP) , sum(population) FROM country WHERE GovernmentForm = "US Territory"	world_1
SELECT avg(GNP) , sum(population) FROM country WHERE GovernmentForm = "US Territory"	world_1
SELECT avg(GNP) , sum(population) FROM country WHERE GovernmentForm = "US Territory"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Dutch" AND IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Continent = "Asia" GROUP BY T2.Language ORDER BY COUNT (*) DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.GovernmentForm = "Republic" GROUP BY T2.Language HAVING COUNT(*) = 1	world_1
SELECT Name , Population , LifeExpectancy FROM country WHERE Continent = "Asia" ORDER BY SurfaceArea DESC LIMIT 1	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T")	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "Beatrix" AND T2.IsOfficial = "T"	world_1
SELECT Name FROM country WHERE Continent = "Africa" AND population < (SELECT max(population) FROM country WHERE Continent = "Asia")	world_1
SELECT Name FROM country WHERE Continent = "Africa" AND population < (SELECT min(population) FROM country WHERE Continent = "Asia")	world_1
SELECT Name FROM country WHERE Continent = "Africa" AND population < (SELECT min(population) FROM country WHERE Continent = "Asia")	world_1
SELECT Name FROM country WHERE Continent = "Asia" AND population > (SELECT max(population) FROM country WHERE Continent = "Africa")	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "English"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "English"	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'English')	world_1
SELECT sum(Population) , GovernmentForm FROM country GROUP BY GovernmentForm HAVING avg(LifeExpectancy) > 72	world_1
SELECT sum(Population) , avg(LifeExpectancy) , Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 72	world_1
SELECT Name FROM country ORDER BY Population ASC LIMIT 3	world_1
SELECT Name FROM country WHERE continent = "Europe" AND Population = "80000"	world_1
SELECT Name FROM country WHERE continent = "Europe" AND Population = "80000"	world_1
select sum(population) , avg(surfacearea) from country where continent = "north america" and surfacearea > 3000	world_1
SELECT LANGUAGE , CountryCode , max(Percentage) FROM countrylanguage GROUP BY CountryCode	world_1
SELECT LANGUAGE , CountryCode , max(Percentage) FROM countrylanguage GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Spanish" GROUP BY CountryCode	world_1
SELECT Record_Company FROM orchestra WHERE Year_of_Founded < 2003 INTERSECT SELECT Record_Company FROM orchestra WHERE Year_of_Founded > 2003	orchestra
SELECT Record_Company FROM orchestra WHERE Year_of_Founded < 2003 INTERSECT SELECT Record_Company FROM orchestra WHERE Year_of_Founded > 2003	orchestra
SELECT Name FROM conductor WHERE Nationality != 'USA'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'USA'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'USA'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'USA'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'USA'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'USA'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'USA'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'USA'	orchestra
SELECT Record_Company FROM orchestra ORDER BY Year_of_Founded DESC	orchestra
SELECT avg(Attendance) FROM SHOW	orchestra
SELECT max(SHARE) , min(SHARE) FROM performance WHERE TYPE != "Live final"	orchestra
SELECT max(SHARE) , min(SHARE) FROM performance WHERE TYPE != "Live final"	orchestra
SELECT max(SHARE) , min(SHARE) FROM performance WHERE TYPE != "Live final"	orchestra
SELECT max(SHARE) , min(SHARE) FROM performance WHERE TYPE != "Live final"	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE Year_of_Founded > 2008	orchestra
SELECT Major_Record_Format FROM orchestra GROUP BY Major_Record_Format ORDER BY COUNT(*) ASC	orchestra
SELECT Major_Record_Format FROM orchestra GROUP BY Major_Record_Format ORDER BY COUNT(*) ASC	orchestra
SELECT Major_Record_Format FROM orchestra GROUP BY Major_Record_Format ORDER BY COUNT(*) ASC	orchestra
SELECT Major_Record_Format FROM orchestra GROUP BY Major_Record_Format ORDER BY COUNT(*) ASC	orchestra
SELECT Major_Record_Format FROM orchestra GROUP BY Major_Record_Format ORDER BY COUNT(*) ASC	orchestra
SELECT Record_Company FROM orchestra GROUP BY Record_Company ORDER BY COUNT(*) DESC LIMIT 1	orchestra
SELECT Record_Company FROM orchestra WHERE Year_of_Founded < 2003 INTERSECT SELECT Record_Company FROM orchestra WHERE Year_of_Founded > 2003	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "CD" OR Major_Record_Format = "DVD"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "CD" OR Major_Record_Format = "DVD"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "CD" OR Major_Record_Format = "DVD"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "CD" OR Major_Record_Format = "DVD"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "CD" OR Major_Record_Format = "DVD"	orchestra
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT DISTINCT T1.first_name , T3.treatment_type_description FROM professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id JOIN Treatment_types AS T3 ON T2.treatment_type_code = T3.treatment_type_code	dog_kennels
SELECT DISTINCT T1.first_name , T3.treatment_type_description FROM professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id JOIN Treatment_types AS T3 ON T2.treatment_type_code = T3.treatment_type_code	dog_kennels
SELECT DISTINCT T1.first_name , T1.last_name FROM Professionals AS T1 JOIN Treatments AS T2 WHERE cost_of_treatment < ( SELECT avg(cost_of_treatment) FROM Treatments )	dog_kennels
SELECT DISTINCT T1.first_name , T1.last_name FROM Professionals AS T1 JOIN Treatments AS T2 WHERE cost_of_treatment < ( SELECT avg(cost_of_treatment) FROM Treatments )	dog_kennels
SELECT DISTINCT T1.first_name , T1.last_name FROM Professionals AS T1 JOIN Treatments AS T2 WHERE cost_of_treatment < ( SELECT avg(cost_of_treatment) FROM Treatments )	dog_kennels
SELECT DISTINCT T1.first_name , T1.last_name FROM Professionals AS T1 JOIN Treatments AS T2 WHERE cost_of_treatment < ( SELECT avg(cost_of_treatment) FROM Treatments )	dog_kennels
SELECT DISTINCT T1.first_name , T1.last_name FROM Professionals AS T1 JOIN Treatments AS T2 WHERE cost_of_treatment < ( SELECT avg(cost_of_treatment) FROM Treatments )	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT email_address , cell_number , home_phone FROM professionals	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Indiana' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Indiana' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Indiana' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT DISTINCT breed_code , size_code FROM dogs	dog_kennels
SELECT DISTINCT breed_code , size_code FROM dogs	dog_kennels
select name from dogs where dog_id not in ( select dog_id from treatments group by dog_id having sum(cost_of_treatment) > 1000 )	dog_kennels
SELECT DISTINCT T1.first_name , T1.last_name FROM Professionals AS T1 JOIN Treatments AS T2 WHERE cost_of_treatment < ( SELECT avg(cost_of_treatment) FROM Treatments )	dog_kennels
SELECT DISTINCT T1.first_name , T1.last_name FROM Professionals AS T1 JOIN Treatments AS T2 WHERE cost_of_treatment < ( SELECT avg(cost_of_treatment) FROM Treatments )	dog_kennels
SELECT DISTINCT T1.first_name , T1.last_name FROM Professionals AS T1 JOIN Treatments AS T2 WHERE cost_of_treatment < ( SELECT avg(cost_of_treatment) FROM Treatments )	dog_kennels
select name from dogs where dog_id not in ( select dog_id from treatments group by dog_id having sum(cost_of_treatment) > 1000 )	dog_kennels
select name from dogs where dog_id not in ( select dog_id from treatments group by dog_id having sum(cost_of_treatment) > 1000 )	dog_kennels
select name from dogs where dog_id not in ( select dog_id from treatments group by dog_id having sum(cost_of_treatment) > 1000 )	dog_kennels
SELECT professional_id , role_code , email_address FROM Professionals EXCEPT SELECT T1.professional_id , T1.role_code , T1.email_address FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id	dog_kennels
SELECT professional_id , role_code , email_address FROM Professionals EXCEPT SELECT T1.professional_id , T1.role_code , T1.email_address FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id	dog_kennels
SELECT T1.treatment_type_description FROM Treatment_types AS T1 JOIN Treatments AS T2 ON T1.treatment_type_code = T2.treatment_type_code GROUP BY T1.treatment_type_code ORDER BY sum(cost_of_treatment) ASC LIMIT 1	dog_kennels
SELECT T1.treatment_type_description FROM Treatment_types AS T1 JOIN Treatments AS T2 ON T1.treatment_type_code = T2.treatment_type_code GROUP BY T1.treatment_type_code ORDER BY sum(cost_of_treatment) ASC LIMIT 1	dog_kennels
SELECT T1.treatment_type_description FROM Treatment_types AS T1 JOIN Treatments AS T2 ON T1.treatment_type_code = T2.treatment_type_code GROUP BY T1.treatment_type_code ORDER BY sum(cost_of_treatment) ASC LIMIT 1	dog_kennels
SELECT T1.treatment_type_description FROM Treatment_types AS T1 JOIN Treatments AS T2 ON T1.treatment_type_code = T2.treatment_type_code GROUP BY T1.treatment_type_code ORDER BY sum(cost_of_treatment) ASC LIMIT 1	dog_kennels
SELECT T1.owner_id , T1.zip_code FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY sum(T3.cost_of_treatment) DESC LIMIT 1	dog_kennels
SELECT T1.owner_id , T1.zip_code FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY sum(T3.cost_of_treatment) DESC LIMIT 1	dog_kennels
SELECT T1.professional_id , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) >= 2	dog_kennels
SELECT T1.professional_id , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) >= 2	dog_kennels
SELECT T1.professional_id , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) >= 2	dog_kennels
SELECT T1.professional_id , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) >= 2	dog_kennels
SELECT cost_of_treatment FROM Treatments ORDER BY date_of_treatment DESC LIMIT 1	dog_kennels
SELECT cost_of_treatment FROM Treatments ORDER BY date_of_treatment DESC LIMIT 1	dog_kennels
SELECT charge_type , charge_amount FROM Charges	dog_kennels
SELECT DISTINCT breed_code , size_code FROM dogs	dog_kennels
SELECT DISTINCT breed_code , size_code FROM dogs	dog_kennels
SELECT DISTINCT breed_code , size_code FROM dogs	dog_kennels
SELECT DISTINCT T1.first_name , T3.treatment_type_description FROM professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id JOIN Treatment_types AS T3 ON T2.treatment_type_code = T3.treatment_type_code	dog_kennels
SELECT Name FROM singer ORDER BY Net_Worth_Millions ASC	singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions ASC	singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions ASC	singer
SELECT Citizenship , COUNT(*) FROM singer GROUP BY Citizenship	singer
SELECT Citizenship , COUNT(*) FROM singer GROUP BY Citizenship	singer
SELECT Birth_Year , Citizenship FROM singer	singer
SELECT Birth_Year , Citizenship FROM singer	singer
SELECT Birth_Year , Citizenship FROM singer	singer
SELECT Birth_Year , Citizenship FROM singer	singer
SELECT Birth_Year , Citizenship FROM singer	singer
SELECT Birth_Year , Citizenship FROM singer	singer
SELECT Birth_Year , Citizenship FROM singer	singer
SELECT Name FROM singer WHERE Citizenship != "France"	singer
SELECT Name FROM singer WHERE Citizenship != "France"	singer
SELECT Name FROM singer WHERE Citizenship != "France"	singer
SELECT Name FROM singer WHERE Citizenship != "France"	singer
SELECT Name FROM singer WHERE Citizenship != "France"	singer
SELECT Name FROM singer WHERE Citizenship != "France"	singer
SELECT Name FROM singer WHERE Citizenship != "France"	singer
SELECT Name FROM singer WHERE Citizenship != "France"	singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions DESC LIMIT 1	singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions DESC LIMIT 1	singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions DESC LIMIT 1	singer
SELECT Citizenship , COUNT(*) FROM singer GROUP BY Citizenship	singer
SELECT Citizenship FROM singer GROUP BY Citizenship ORDER BY COUNT(*) DESC LIMIT 1	singer
SELECT Citizenship FROM singer GROUP BY Citizenship ORDER BY COUNT(*) DESC LIMIT 1	singer
select citizenship from singer group by citizenship order by count(*) desc limit 1	singer
SELECT Citizenship , max(Net_Worth_Millions) FROM singer GROUP BY Citizenship	singer
SELECT DISTINCT T1.Name FROM singer AS T1 JOIN song AS T2 ON T1.Singer_ID = T2.Singer_ID WHERE T2.Sales > 300000	singer
SELECT DISTINCT T1.Name FROM singer AS T1 JOIN song AS T2 ON T1.Singer_ID = T2.Singer_ID WHERE T2.Sales > 300000	singer
SELECT DISTINCT T1.Name FROM singer AS T1 JOIN song AS T2 ON T1.Singer_ID = T2.Singer_ID WHERE T2.Sales > 300000	singer
SELECT DISTINCT T1.Name FROM singer AS T1 JOIN song AS T2 ON T1.Singer_ID = T2.Singer_ID WHERE T2.Sales > 300000	singer
SELECT T2.property_type_description FROM Properties AS T1 JOIN Ref_Property_Types AS T2 ON T1.property_type_code = T2.property_type_code GROUP BY T1.property_type_code	real_estate_properties
