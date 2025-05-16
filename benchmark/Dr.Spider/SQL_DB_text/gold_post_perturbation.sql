SELECT avg(age) , min(age) , max(age) FROM singer WHERE country = 'Netherlands'	concert_singer
SELECT avg(age) , min(age) , max(age) FROM singer WHERE country = 'United States'	concert_singer
SELECT count(*) FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T2.petid = T3.petid WHERE T1.sex = 'F' AND T3.pettype = 'cat'	pets_1
SELECT count(*) FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T2.petid = T3.petid WHERE T1.sex = 'F' AND T3.pettype = 'cat'	pets_1
SELECT DISTINCT T1.Fname FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'cat' OR T3.pettype = 'cat'	pets_1
SELECT DISTINCT T1.Fname FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'dog' OR T3.pettype = 'dog'	pets_1
SELECT DISTINCT T1.Fname FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'cat' OR T3.pettype = 'cat'	pets_1
SELECT DISTINCT T1.Fname FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'dog' OR T3.pettype = 'dog'	pets_1
SELECT major , age FROM student WHERE stuid NOT IN (SELECT T1.stuid FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'dog')	pets_1
SELECT major , age FROM student WHERE stuid NOT IN (SELECT T1.stuid FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'dog')	pets_1
SELECT stuid FROM student EXCEPT SELECT T1.stuid FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'dog'	pets_1
SELECT T2.petid FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid WHERE T1.Lname = 'Kim'	pets_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN COUNTRIES AS T2 ON T1.Country = T2.CountryId WHERE T2.CountryName = 'germany'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN COUNTRIES AS T2 ON T1.Country = T2.CountryId WHERE T2.CountryName = 'uk'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN COUNTRIES AS T2 ON T1.Country = T2.CountryId WHERE T2.CountryName = 'usa'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN COUNTRIES AS T2 ON T1.Country = T2.CountryId WHERE T2.CountryName = 'sweden'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN COUNTRIES AS T2 ON T1.Country = T2.CountryId WHERE T2.CountryName = 'japan'	car_1
SELECT count(*) FROM MODEL_LIST AS T1 JOIN CAR_MAKERS AS T2 ON T1.Maker = T2.Id JOIN COUNTRIES AS T3 ON T2.Country = T3.CountryId WHERE T3.CountryName = 'germany'	car_1
SELECT count(*) FROM MODEL_LIST AS T1 JOIN CAR_MAKERS AS T2 ON T1.Maker = T2.Id JOIN COUNTRIES AS T3 ON T2.Country = T3.CountryId WHERE T3.CountryName = 'uk'	car_1
SELECT count(*) FROM MODEL_LIST AS T1 JOIN CAR_MAKERS AS T2 ON T1.Maker = T2.Id JOIN COUNTRIES AS T3 ON T2.Country = T3.CountryId WHERE T3.CountryName = 'sweden'	car_1
SELECT count(*) FROM MODEL_LIST AS T1 JOIN CAR_MAKERS AS T2 ON T1.Maker = T2.Id JOIN COUNTRIES AS T3 ON T2.Country = T3.CountryId WHERE T3.CountryName = 'japan'	car_1
SELECT count(*) FROM MODEL_LIST AS T1 JOIN CAR_MAKERS AS T2 ON T1.Maker = T2.Id JOIN COUNTRIES AS T3 ON T2.Country = T3.CountryId WHERE T3.CountryName = 'italy'	car_1
SELECT T1.CountryName FROM COUNTRIES AS T1 JOIN CONTINENTS AS T2 ON T1.Continent = T2.ContId JOIN CAR_MAKERS AS T3 ON T1.CountryId = T3.Country WHERE T2.Continent = 'america' GROUP BY T1.CountryName HAVING count(*) >= 3	car_1
SELECT T1.CountryName FROM COUNTRIES AS T1 JOIN CONTINENTS AS T2 ON T1.Continent = T2.ContId JOIN CAR_MAKERS AS T3 ON T1.CountryId = T3.Country WHERE T2.Continent = 'asia' GROUP BY T1.CountryName HAVING count(*) >= 3	car_1
SELECT avg(T2.edispl) FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T1.Model = 'honda'	car_1
SELECT avg(T2.edispl) FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T1.Model = 'buick'	car_1
SELECT avg(T2.edispl) FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T1.Model = 'chrysler'	car_1
SELECT avg(T2.edispl) FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T1.Model = 'chevrolet'	car_1
SELECT avg(T2.edispl) FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T1.Model = 'amc'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'General Motors'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'Volkswagen'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'Ford Motor Company'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'Toyota'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'Chrysler'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'General Motors'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'Volkswagen'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'Ford Motor Company'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'Toyota'	car_1
SELECT count(*) FROM CAR_MAKERS AS T1 JOIN MODEL_LIST AS T2 ON T1.Id = T2.Maker WHERE T1.FullName = 'Chrysler'	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Fiat' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Renault' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Peugeaut' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Volkswagen' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Honda' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Fiat' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Renault' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Peugeaut' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Volkswagen' OR T4.weight > 3500	car_1
SELECT DISTINCT T2.Model FROM CAR_NAMES AS T1 JOIN MODEL_LIST AS T2 ON T1.Model = T2.Model JOIN CAR_MAKERS AS T3 ON T2.Maker = T3.Id JOIN CARS_DATA AS T4 ON T1.MakeId = T4.Id WHERE T3.FullName = 'Honda' OR T4.weight > 3500	car_1
SELECT T1.cylinders FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T2.Model = 'honda' ORDER BY T1.accelerate ASC LIMIT 1	car_1
SELECT T1.cylinders FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T2.Model = 'buick' ORDER BY T1.accelerate ASC LIMIT 1	car_1
SELECT T1.cylinders FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T2.Model = 'chrysler' ORDER BY T1.accelerate ASC LIMIT 1	car_1
SELECT T1.cylinders FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T2.Model = 'chevrolet' ORDER BY T1.accelerate ASC LIMIT 1	car_1
SELECT T1.cylinders FROM CARS_DATA AS T1 JOIN CAR_NAMES AS T2 ON T1.Id = T2.MakeId WHERE T2.Model = 'amc' ORDER BY T1.accelerate ASC LIMIT 1	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'Fiat'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'General Motors'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'Renault'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'Peugeaut'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'Volkswagen'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'Fiat'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'General Motors'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'Renault'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'Peugeaut'	car_1
SELECT DISTINCT T1.model FROM MODEL_LIST AS T1 JOIN CAR_NAMES AS T2 ON T1.Model = T2.Model JOIN CARS_DATA AS T3 ON T2.MakeId = T3.Id JOIN CAR_MAKERS AS T4 ON T1.Maker = T4.Id WHERE T3.weight < 3500 AND T4.FullName != 'Volkswagen'	car_1
SELECT Abbreviation FROM AIRLINES WHERE Airline = "Northwest Airlines"	flight_2
SELECT Abbreviation FROM AIRLINES WHERE Airline = "United Airlines"	flight_2
SELECT Abbreviation FROM AIRLINES WHERE Airline = "US Airways"	flight_2
SELECT Abbreviation FROM AIRLINES WHERE Airline = "Delta Airlines"	flight_2
SELECT Abbreviation FROM AIRLINES WHERE Airline = "American Airlines"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "American"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "Northwest"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "Continental"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "USAir"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "Allegiant"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "American"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "Northwest"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "Continental"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "USAir"	flight_2
SELECT Airline FROM AIRLINES WHERE Abbreviation = "Allegiant"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "ANQ"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "ALM"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "LTS"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "RLI"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "AKC"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "ANQ"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "ALM"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "LTS"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "RLI"	flight_2
SELECT AirportName FROM AIRPORTS WHERE AirportCode = "AKC"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "Northwest Airlines"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "US Airways"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "JetBlue Airways"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "Delta Airlines"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "American Airlines"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "Northwest Airlines"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "US Airways"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "JetBlue Airways"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "Delta Airlines"	flight_2
SELECT T1.FlightNo FROM FLIGHTS AS T1 JOIN AIRLINES AS T2 ON T2.uid = T1.Airline WHERE T2.Airline = "American Airlines"	flight_2
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Understanding DB"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Palm reading"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Summer Show"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "How to read a book"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Customer reviews"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Understanding DB"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Palm reading"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Summer Show"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "How to read a book"	cre_Doc_Template_Mgt
SELECT document_id , template_id , Document_Description FROM Documents WHERE document_name = "Customer reviews"	cre_Doc_Template_Mgt
SELECT count(*) FROM Documents AS T1 JOIN Templates AS T2 ON T1.Template_ID = T2.Template_ID WHERE T2.Template_Type_Code = 'PP'	cre_Doc_Template_Mgt
SELECT count(*) FROM Documents AS T1 JOIN Templates AS T2 ON T1.Template_ID = T2.Template_ID WHERE T2.Template_Type_Code = 'BK'	cre_Doc_Template_Mgt
SELECT count(*) FROM Documents AS T1 JOIN Templates AS T2 ON T1.Template_ID = T2.Template_ID WHERE T2.Template_Type_Code = 'PP'	cre_Doc_Template_Mgt
SELECT count(*) FROM Documents AS T1 JOIN Templates AS T2 ON T1.Template_ID = T2.Template_ID WHERE T2.Template_Type_Code = 'BK'	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PPT" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "CV" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "AD" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "BK" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "CV"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "AD"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "PP"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "BK"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PPT" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "CV" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "AD" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "BK" OR template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "CV"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "AD"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "PP"	cre_Doc_Template_Mgt
SELECT template_id FROM Templates WHERE template_type_code = "PP" OR template_type_code = "BK"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "AD"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "PP"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "BK"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "AD"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "PP"	cre_Doc_Template_Mgt
SELECT count(*) FROM Templates WHERE template_type_code = "BK"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Understanding DB"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Summer Show"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Customer reviews"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "How Google people work"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Welcome to NY"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Understanding DB"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Summer Show"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Customer reviews"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "How Google people work"	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T2.document_name = "Welcome to NY"	cre_Doc_Template_Mgt
SELECT T2.document_name FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T1.template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT T2.document_name FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T1.template_type_code = "AD"	cre_Doc_Template_Mgt
SELECT T2.document_name FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T1.template_type_code = "PP"	cre_Doc_Template_Mgt
SELECT T2.document_name FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T1.template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT T2.document_name FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T1.template_type_code = "AD"	cre_Doc_Template_Mgt
SELECT T2.document_name FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id WHERE T1.template_type_code = "PP"	cre_Doc_Template_Mgt
SELECT template_type_description FROM Ref_template_types WHERE template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_type_description FROM Ref_template_types WHERE template_type_code = "CV"	cre_Doc_Template_Mgt
SELECT template_type_description FROM Ref_template_types WHERE template_type_code = "PP"	cre_Doc_Template_Mgt
SELECT template_type_description FROM Ref_template_types WHERE template_type_code = "BK"	cre_Doc_Template_Mgt
SELECT template_type_description FROM Ref_template_types WHERE template_type_code = "PPT"	cre_Doc_Template_Mgt
SELECT template_type_description FROM Ref_template_types WHERE template_type_code = "CV"	cre_Doc_Template_Mgt
SELECT template_type_description FROM Ref_template_types WHERE template_type_code = "PP"	cre_Doc_Template_Mgt
SELECT template_type_description FROM Ref_template_types WHERE template_type_code = "BK"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "CV"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "Advertisement"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "Paper"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "Presentation"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "CV"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "Advertisement"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "Paper"	cre_Doc_Template_Mgt
SELECT template_type_code FROM Ref_template_types WHERE template_type_description = "Presentation"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "CV"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Book"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Advertisement"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Paper"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "CV"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Book"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Advertisement"	cre_Doc_Template_Mgt
SELECT T2.template_id FROM Ref_template_types AS T1 JOIN Templates AS T2 ON T1.template_type_code = T2.template_type_code WHERE T1.template_type_description = "Paper"	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'Customer reviews'	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'Welcome to NY'	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'How to write a CV'	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'A history of Arts'	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'Customer reviews'	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'Welcome to NY'	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'How to write a CV'	cre_Doc_Template_Mgt
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_ID = T2.document_ID WHERE T2.document_name = 'A history of Arts'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'Palm reading'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'Summer Show'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'Customer reviews'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'About Korea'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'How Google people work'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'Palm reading'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'Summer Show'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'Customer reviews'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'About Korea'	cre_Doc_Template_Mgt
SELECT T1.paragraph_id , T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.Document_Name = 'How Google people work'	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Palm reading"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Summer Show"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "About Korea"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "How Google people work"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Welcome to NY"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Palm reading"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Summer Show"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "About Korea"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "How Google people work"	cre_Doc_Template_Mgt
SELECT T1.paragraph_text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id WHERE T2.document_name = "Welcome to NY"	cre_Doc_Template_Mgt
SELECT Num_of_Staff , Open_Year FROM museum WHERE name = 'RiverPark Museum'	museum_visit
SELECT Num_of_Staff , Open_Year FROM museum WHERE name = 'Capital Plaza Museum'	museum_visit
SELECT Num_of_Staff , Open_Year FROM museum WHERE name = 'ZirMed Gateway Museum'	museum_visit
SELECT Num_of_Staff , Open_Year FROM museum WHERE name = 'Willow Grande Museum'	museum_visit
SELECT Num_of_Staff , Open_Year FROM museum WHERE name = 'Central City District Residential Museum'	museum_visit
SELECT first_name , birth_date FROM players WHERE country_code = 'EST'	wta_1
SELECT first_name , birth_date FROM players WHERE country_code = 'ECA'	wta_1
SELECT first_name , birth_date FROM players WHERE country_code = 'URS'	wta_1
SELECT first_name , birth_date FROM players WHERE country_code = 'CGO'	wta_1
SELECT first_name , birth_date FROM players WHERE country_code = 'REU'	wta_1
SELECT first_name , birth_date FROM players WHERE country_code = 'EST'	wta_1
SELECT first_name , birth_date FROM players WHERE country_code = 'ECA'	wta_1
SELECT first_name , birth_date FROM players WHERE country_code = 'URS'	wta_1
SELECT first_name , birth_date FROM players WHERE country_code = 'CGO'	wta_1
SELECT first_name , birth_date FROM players WHERE country_code = 'REU'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Cincinnati'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Birmingham'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Charleston'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Wuhan'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Monterrey'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Cincinnati' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Birmingham' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Monterrey' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Rabat' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Cincinnati'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Birmingham'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Charleston'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Wuhan'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Monterrey'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Cincinnati' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Birmingham' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Monterrey' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Rabat' INTERSECT SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'	wta_1
SELECT first_name , last_name FROM players WHERE hand = 'R' ORDER BY birth_date	wta_1
SELECT first_name , last_name FROM players WHERE hand = '' ORDER BY birth_date	wta_1
SELECT first_name , last_name FROM players WHERE hand = 'U' ORDER BY birth_date	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Cincinnati' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Istanbul' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Birmingham' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Limoges' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 's-Hertogenbosch' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Cincinnati' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Istanbul' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Birmingham' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Limoges' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 's-Hertogenbosch' ORDER BY winner_rank_points DESC LIMIT 1	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Cincinnati' AND winner_hand = 'L'	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Birmingham' AND winner_hand = 'L'	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Wuhan' AND winner_hand = 'L'	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Monterrey' AND winner_hand = 'L'	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Brisbane' AND winner_hand = 'L'	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Cincinnati' AND winner_hand = 'L'	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Birmingham' AND winner_hand = 'L'	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Wuhan' AND winner_hand = 'L'	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Monterrey' AND winner_hand = 'L'	wta_1
SELECT count(DISTINCT winner_name) FROM matches WHERE tourney_name = 'Brisbane' AND winner_hand = 'L'	wta_1
SELECT count(*) FROM ship WHERE disposition_of_ship = 'Wrecked'	battle_death
SELECT count(*) FROM ship WHERE disposition_of_ship = 'Sank'	battle_death
SELECT count(*) FROM ship WHERE disposition_of_ship = 'Scuttled'	battle_death
SELECT T1.killed , T1.injured FROM death AS T1 JOIN ship AS t2 ON T1.caused_by_ship_id = T2.id WHERE T2.tonnage = '391'	battle_death
SELECT name , RESULT FROM battle WHERE bulgarian_commander != 'Unknown'	battle_death
SELECT name , RESULT FROM battle WHERE bulgarian_commander != 'Kaloyan'	battle_death
SELECT name , RESULT FROM battle WHERE bulgarian_commander != 'Ivan Asen II'	battle_death
SELECT DISTINCT T1.id , T1.name FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle WHERE T2.ship_type = '8 gun Brig'	battle_death
SELECT DISTINCT T1.id , T1.name FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle WHERE T2.ship_type = '18-gun Brig'	battle_death
SELECT name FROM battle WHERE bulgarian_commander = 'Kaloyan' AND latin_commander = 'Thierry de Termond'	battle_death
SELECT name FROM battle WHERE bulgarian_commander = 'Kaloyan' AND latin_commander = 'Unknown'	battle_death
SELECT count(*) FROM battle WHERE id NOT IN ( SELECT lost_in_battle FROM ship WHERE tonnage = 't' )	battle_death
SELECT name , RESULT , bulgarian_commander FROM battle EXCEPT SELECT T1.name , T1.result , T1.bulgarian_commander FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle WHERE T2.location = 'SW Approaches'	battle_death
SELECT name , RESULT , bulgarian_commander FROM battle EXCEPT SELECT T1.name , T1.result , T1.bulgarian_commander FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle WHERE T2.location = 'Mid-Atlantic'	battle_death
SELECT course_description FROM Courses WHERE course_name = 'ds'	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'oop'	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'en'	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'cal'	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'dl'	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'ds'	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'oop'	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'en'	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'cal'	student_transcripts_tracking
SELECT course_description FROM Courses WHERE course_name = 'dl'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'Michelleburgh'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'Lake Careyberg'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'New Clemensburgh'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'South Palma'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'Mariliehaven'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'Michelleburgh'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'Lake Careyberg'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'New Clemensburgh'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'South Palma'	student_transcripts_tracking
SELECT zip_postcode FROM Addresses WHERE city = 'Mariliehaven'	student_transcripts_tracking
SELECT DISTINCT T1.first_name , T1.middle_name , T1.last_name FROM Students AS T1 JOIN Student_Enrolment AS T2 ON T1.student_id = T2.student_id JOIN Degree_Programs AS T3 ON T2.degree_program_id = T3.degree_program_id WHERE T3.degree_summary_name = 'Master'	student_transcripts_tracking
SELECT DISTINCT T2.semester_id FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id WHERE degree_summary_name = 'Bachelor' INTERSECT SELECT DISTINCT T2.semester_id FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id WHERE degree_summary_name = 'Bachelor'	student_transcripts_tracking
SELECT DISTINCT T2.semester_id FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id WHERE degree_summary_name = 'Master' INTERSECT SELECT DISTINCT T2.semester_id FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id WHERE degree_summary_name = 'Master'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'c'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'k'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'f'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'a'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'e'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'c'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'k'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'f'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'a'	student_transcripts_tracking
SELECT section_description FROM Sections WHERE section_name = 'e'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '1-879-796-8987x164'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '436.613.7683'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '877.549.9067x8723'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '677.401.9382'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '(462)246-7921'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '1-879-796-8987x164'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '436.613.7683'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '877.549.9067x8723'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '677.401.9382'	student_transcripts_tracking
select t1.first_name from students as t1 join addresses as t2 on t1.permanent_address_id = t2.address_id where t2.country = 'haiti' or t1.cell_mobile_number = '(462)246-7921'	student_transcripts_tracking
SELECT Title FROM Cartoon WHERE Directed_by = "Brandon Vietti"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Michael Chang"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Brandon Vietti"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Michael Chang"	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "James Krieg"	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "Matt Wayne"	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "Adam Beechen"	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "Michael Jelenic"	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "James Krieg"	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "Matt Wayne"	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "Adam Beechen"	tvshow
SELECT count(*) FROM Cartoon WHERE Written_by = "Michael Jelenic"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones" OR Directed_by = "Ben Jones"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones" OR Directed_by = "Michael Chang"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Brandon Vietti" OR Directed_by = "Brandon Vietti"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Michael Chang" OR Directed_by = "Brandon Vietti"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones" OR Directed_by = "Ben Jones"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones" OR Directed_by = "Michael Chang"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Brandon Vietti" OR Directed_by = "Brandon Vietti"	tvshow
SELECT Title FROM Cartoon WHERE Directed_by = "Michael Chang" OR Directed_by = "Brandon Vietti"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "Classica"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "MTV Music"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "MTV Live HD"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "Classica"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "MTV Music"	tvshow
SELECT Package_Option FROM TV_Channel WHERE series_name = "MTV Live HD"	tvshow
SELECT count(*) FROM TV_Channel WHERE LANGUAGE = "Italian"	tvshow
SELECT count(*) FROM TV_Channel WHERE LANGUAGE = "Italian"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Title = "Journey to the Center of the Bat!"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Title = "Evil Under the Sea!"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Title = "Dawn of the Dead Man!"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Title = "Day of the Dark Knight!"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Title = "Enter the Outsiders!"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Classic"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Rocks"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "Classica"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Hits"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Music"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Classic"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Rocks"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "Classica"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Hits"	tvshow
SELECT T2.Title FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Music"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Emily"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Blowback"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Winterland"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Home By Another Way"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Friendly Skies"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Emily"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Blowback"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Winterland"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Home By Another Way"	tvshow
SELECT Air_Date FROM TV_series WHERE Episode = "Friendly Skies"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Emily"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Blowback"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Winterland"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Home By Another Way"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Friendly Skies"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Emily"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Blowback"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Winterland"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Home By Another Way"	tvshow
SELECT Weekly_Rank FROM TV_series WHERE Episode = "Friendly Skies"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Emily"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Blowback"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Winterland"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Home By Another Way"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Friendly Skies"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Emily"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Blowback"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Winterland"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Home By Another Way"	tvshow
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "Friendly Skies"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "Classica"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "myDeejay"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Music"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Dance"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "Rock TV"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "Classica"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "myDeejay"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Music"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "MTV Dance"	tvshow
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "Rock TV"	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Steven Melching'	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'James Krieg'	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Joseph Kuhr'	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Matt Wayne'	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'J. M. DeMatteis'	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Steven Melching'	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'James Krieg'	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Joseph Kuhr'	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Matt Wayne'	tvshow
SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'J. M. DeMatteis'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'James Krieg'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Matt Wayne'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'J. M. DeMatteis'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Adam Beechen'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Michael Jelenic'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'James Krieg'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Matt Wayne'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'J. M. DeMatteis'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Adam Beechen'	tvshow
SELECT country FROM TV_Channel EXCEPT SELECT T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.written_by = 'Michael Jelenic'	tvshow
SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Michael Chang' INTERSECT SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Michael Chang'	tvshow
SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Ben Jones' INTERSECT SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Ben Jones'	tvshow
SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Brandon Vietti' INTERSECT SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Ben Jones'	tvshow
SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Michael Chang' INTERSECT SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Michael Chang'	tvshow
SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Ben Jones' INTERSECT SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Ben Jones'	tvshow
SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Brandon Vietti' INTERSECT SELECT T1.series_name , T1.country FROM TV_Channel AS T1 JOIN cartoon AS T2 ON T1.id = T2.Channel WHERE T2.directed_by = 'Ben Jones'	tvshow
SELECT Pixel_aspect_ratio_PAR , country FROM tv_channel WHERE LANGUAGE != 'Italian'	tvshow
SELECT Pixel_aspect_ratio_PAR , country FROM tv_channel WHERE LANGUAGE != 'Italian'	tvshow
SELECT id FROM TV_Channel EXCEPT SELECT channel FROM cartoon WHERE directed_by = 'Brandon Vietti'	tvshow
SELECT id FROM TV_Channel EXCEPT SELECT channel FROM cartoon WHERE directed_by = 'Michael Chang'	tvshow
SELECT id FROM TV_Channel EXCEPT SELECT channel FROM cartoon WHERE directed_by = 'Brandon Vietti'	tvshow
SELECT id FROM TV_Channel EXCEPT SELECT channel FROM cartoon WHERE directed_by = 'Michael Chang'	tvshow
SELECT package_option FROM TV_Channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = 'Brandon Vietti')	tvshow
SELECT package_option FROM TV_Channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = 'Michael Chang')	tvshow
SELECT package_option FROM TV_Channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = 'Brandon Vietti')	tvshow
SELECT package_option FROM TV_Channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = 'Michael Chang')	tvshow
SELECT Name FROM people WHERE Nationality != "Bulgaria"	poker_player
SELECT Name FROM people WHERE Nationality != "Bulgaria"	poker_player
SELECT max(created) FROM votes WHERE state = 'NJ\n'	voter_1
SELECT max(created) FROM votes WHERE state = 'NY'	voter_1
SELECT contestant_name FROM contestants WHERE contestant_name != 'Nita Coster'	voter_1
SELECT contestant_name FROM contestants WHERE contestant_name != 'Kurt Walser'	voter_1
SELECT contestant_name FROM contestants WHERE contestant_name != 'Kelly Clauss'	voter_1
SELECT contestant_name FROM contestants WHERE contestant_name != 'Edwina Burnam'	voter_1
SELECT contestant_name FROM contestants WHERE contestant_name != 'Alana Bregman'	voter_1
SELECT count(*) FROM votes WHERE state = 'NJ\n' OR state = 'CA'	voter_1
SELECT count(*) FROM votes WHERE state = 'CA' OR state = 'CA'	voter_1
SELECT count(*) FROM votes WHERE state = 'NY' OR state = 'NY'	voter_1
SELECT T2.created , T2.state , T2.phone_number FROM contestants AS T1 JOIN votes AS T2 ON T1.contestant_number = T2.contestant_number WHERE T1.contestant_name = 'Kelly Clauss'	voter_1
SELECT T2.created , T2.state , T2.phone_number FROM contestants AS T1 JOIN votes AS T2 ON T1.contestant_number = T2.contestant_number WHERE T1.contestant_name = 'Alana Bregman'	voter_1
SELECT T3.area_code FROM contestants AS T1 JOIN votes AS T2 ON T1.contestant_number = T2.contestant_number JOIN area_code_state AS T3 ON T2.state = T3.state WHERE T1.contestant_name = 'Kelly Clauss' INTERSECT SELECT T3.area_code FROM contestants AS T1 JOIN votes AS T2 ON T1.contestant_number = T2.contestant_number JOIN area_code_state AS T3 ON T2.state = T3.state WHERE T1.contestant_name = 'Kelly Clauss'	voter_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Southern and Central Asia"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Australia and New Zealand"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Eastern Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Southern Africa"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Region = "Micronesia"	world_1
SELECT Continent FROM country WHERE Name = "Nepal"	world_1
SELECT Continent FROM country WHERE Name = "Hong Kong"	world_1
SELECT Continent FROM country WHERE Name = "Lesotho"	world_1
SELECT Continent FROM country WHERE Name = "Bouvet Island"	world_1
SELECT Continent FROM country WHERE Name = "Slovakia"	world_1
SELECT Continent FROM country WHERE Name = "Nepal"	world_1
SELECT Continent FROM country WHERE Name = "Hong Kong"	world_1
SELECT Continent FROM country WHERE Name = "Lesotho"	world_1
SELECT Continent FROM country WHERE Name = "Bouvet Island"	world_1
SELECT Continent FROM country WHERE Name = "Slovakia"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Ikorodu"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Sete Lagoas"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Iseyin"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Ahome"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Clarksville"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Ikorodu"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Sete Lagoas"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Iseyin"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Ahome"	world_1
SELECT Region FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Clarksville"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Nepal" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Hong Kong" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Dominican Republic" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Lesotho" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Slovakia" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Nepal" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Hong Kong" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Dominican Republic" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Lesotho" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Slovakia" ORDER BY Percentage DESC LIMIT 1	world_1
SELECT Population , LifeExpectancy FROM country WHERE Name = "Nepal"	world_1
SELECT Population , LifeExpectancy FROM country WHERE Name = "Hong Kong"	world_1
SELECT Population , LifeExpectancy FROM country WHERE Name = "Dominican Republic"	world_1
SELECT Population , LifeExpectancy FROM country WHERE Name = "Lesotho"	world_1
SELECT Population , LifeExpectancy FROM country WHERE Name = "Bouvet Island"	world_1
SELECT Population , Region FROM country WHERE Name = "Nepal"	world_1
SELECT Population , Region FROM country WHERE Name = "Hong Kong"	world_1
SELECT Population , Region FROM country WHERE Name = "Dominican Republic"	world_1
SELECT Population , Region FROM country WHERE Name = "Lesotho"	world_1
SELECT Population , Region FROM country WHERE Name = "Bouvet Island"	world_1
SELECT Population , Region FROM country WHERE Name = "Nepal"	world_1
SELECT Population , Region FROM country WHERE Name = "Hong Kong"	world_1
SELECT Population , Region FROM country WHERE Name = "Dominican Republic"	world_1
SELECT Population , Region FROM country WHERE Name = "Lesotho"	world_1
SELECT Population , Region FROM country WHERE Name = "Bouvet Island"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Southern and Central Asia"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Australia and New Zealand"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Caribbean"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Eastern Europe"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Southern Africa"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Southern and Central Asia"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Australia and New Zealand"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Caribbean"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Eastern Europe"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Region = "Southern Africa"	world_1
SELECT Name FROM country WHERE Continent = "Oceania" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "South America" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "Europe" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "Antarctica" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "North America" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "Oceania" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "South America" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "Europe" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "Antarctica" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "North America" ORDER BY LifeExpectancy LIMIT 1	world_1
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = "Oceania"	world_1
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = "South America"	world_1
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = "Europe"	world_1
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = "Antarctica"	world_1
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = "North America"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Continent = "Oceania" AND GovernmentForm = "Republic"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Continent = "South America" AND GovernmentForm = "Republic"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Continent = "Asia" AND GovernmentForm = "Republic"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Continent = "Europe" AND GovernmentForm = "Republic"	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Continent = "Antarctica" AND GovernmentForm = "Republic"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Oceania" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "South America" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Europe" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Antarctica" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "North America" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "Oceania"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "South America"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "Asia"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "Antarctica"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "North America"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Oceania" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "South America" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Europe" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Antarctica" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "North America" OR Continent = "Europe"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "Oceania"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "South America"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "Asia"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "Antarctica"	world_1
SELECT sum(SurfaceArea) FROM country WHERE Continent = "Asia" OR Continent = "North America"	world_1
SELECT sum(Population) FROM city WHERE District = "Binh Dinh"	world_1
SELECT sum(Population) FROM city WHERE District = "Indiana"	world_1
SELECT sum(Population) FROM city WHERE District = "Thimphu"	world_1
SELECT sum(Population) FROM city WHERE District = "Oromia"	world_1
SELECT sum(Population) FROM city WHERE District = "Monagas"	world_1
SELECT sum(Population) FROM city WHERE District = "Binh Dinh"	world_1
SELECT sum(Population) FROM city WHERE District = "Indiana"	world_1
SELECT sum(Population) FROM city WHERE District = "Thimphu"	world_1
SELECT sum(Population) FROM city WHERE District = "Oromia"	world_1
SELECT sum(Population) FROM city WHERE District = "Monagas"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "Oceania"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "South America"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "Asia"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "Antarctica"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "North America"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "Oceania"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "South America"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "Asia"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "Antarctica"	world_1
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = "North America"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Nepal"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Hong Kong"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Dominican Republic"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Lesotho"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Slovakia"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Nepal"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Hong Kong"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Dominican Republic"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Lesotho"	world_1
SELECT COUNT(T2.Language) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Slovakia"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Nepal" AND IsOfficial = "T"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Hong Kong" AND IsOfficial = "T"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Dominican Republic" AND IsOfficial = "T"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Slovakia" AND IsOfficial = "T"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Bolivia" AND IsOfficial = "T"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Nepal" AND IsOfficial = "T"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Hong Kong" AND IsOfficial = "T"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Dominican Republic" AND IsOfficial = "T"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Slovakia" AND IsOfficial = "T"	world_1
SELECT COUNT(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Bolivia" AND IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Catalan" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Swahili" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Japanese" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Crioulo" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Malagasy" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Tokelau"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Palau"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Malay"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Catalan" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Swahili" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Japanese" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Crioulo" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Malagasy" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Tokelau"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Palau"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Malay"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Malagasy" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Bislama" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "German" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Kirundi" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Palau" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Chamorro" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Zulu" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Irish" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Malagasy" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Bislama" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "German" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Kirundi" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "French" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Palau" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Chamorro" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Zulu" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T"	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND T2.IsOfficial = "T" INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Irish" AND T2.IsOfficial = "T"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu"	world_1
SELECT COUNT( DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Nepali"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Limba"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Ndebele"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Ainu"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Maranao"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali" OR T2.Language = "Dutch"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba" OR T2.Language = "Dutch"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele" OR T2.Language = "Dutch"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu" OR T2.Language = "Dutch"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao" OR T2.Language = "Dutch"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Nepali"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Limba"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Ndebele"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Ainu"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" OR T2.Language = "Maranao"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali" OR T2.Language = "Dutch"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba" OR T2.Language = "Dutch"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele" OR T2.Language = "Dutch"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu" OR T2.Language = "Dutch"	world_1
SELECT DISTINCT T1.Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao" OR T2.Language = "Dutch"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali" AND IsOfficial = "T"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba" AND IsOfficial = "T"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele" AND IsOfficial = "T"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu" AND IsOfficial = "T"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "English" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao" AND IsOfficial = "T"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Dutch" AND IsOfficial = "T"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Dutch" AND IsOfficial = "T"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Dutch" AND IsOfficial = "T"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Dutch" AND IsOfficial = "T"	world_1
SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao" AND IsOfficial = "T" UNION SELECT * FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Dutch" AND IsOfficial = "T"	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Nepali" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Limba" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Ndebele" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Ainu" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Maranao" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Nepali" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Limba" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Ndebele" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Ainu" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "Maranao" ORDER BY T1.Population DESC LIMIT 1	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu" AND T2.IsOfficial = "T")	world_1
SELECT avg(LifeExpectancy) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao" AND T2.IsOfficial = "T")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Nepali")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Limba")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ndebele")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Ainu")	world_1
SELECT sum(Population) FROM country WHERE Name NOT IN (SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = "Maranao")	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "Bakili Muluzi" AND T2.IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "Albert II" AND T2.IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "Ricardo Lagos Escobar" AND T2.IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "George W. Bush" AND T2.IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "Jiang Zemin" AND T2.IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "Bakili Muluzi" AND T2.IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "Albert II" AND T2.IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "Ricardo Lagos Escobar" AND T2.IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "George W. Bush" AND T2.IsOfficial = "T"	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.HeadOfState = "Jiang Zemin" AND T2.IsOfficial = "T"	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "Oceania")	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "South America")	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "Asia")	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "Antarctica")	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "North America")	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "Oceania")	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "South America")	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "Asia")	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "Antarctica")	world_1
SELECT Name FROM country WHERE SurfaceArea > (SELECT min(SurfaceArea) FROM country WHERE Continent = "North America")	world_1
SELECT Name FROM country WHERE Continent = "Africa" AND population < (SELECT max(population) FROM country WHERE Continent = "Oceania")	world_1
SELECT Name FROM country WHERE Continent = "Africa" AND population < (SELECT max(population) FROM country WHERE Continent = "Africa")	world_1
SELECT Name FROM country WHERE Continent = "Africa" AND population < (SELECT min(population) FROM country WHERE Continent = "South America")	world_1
SELECT Name FROM country WHERE Continent = "Africa" AND population < (SELECT min(population) FROM country WHERE Continent = "Europe")	world_1
SELECT Name FROM country WHERE Continent = "Africa" AND population < (SELECT min(population) FROM country WHERE Continent = "North America")	world_1
SELECT Name FROM country WHERE Continent = "Asia" AND population > (SELECT max(population) FROM country WHERE Continent = "Oceania")	world_1
SELECT Name FROM country WHERE Continent = "Asia" AND population > (SELECT max(population) FROM country WHERE Continent = "South America")	world_1
SELECT Name FROM country WHERE Continent = "Asia" AND population > (SELECT max(population) FROM country WHERE Continent = "Europe")	world_1
SELECT Name FROM country WHERE Continent = "Asia" AND population > (SELECT max(population) FROM country WHERE Continent = "Antarctica")	world_1
SELECT Name FROM country WHERE Continent = "Asia" AND population > (SELECT max(population) FROM country WHERE Continent = "North America")	world_1
SELECT Name FROM country WHERE Continent = "Asia" AND population > (SELECT min(population) FROM country WHERE Continent = "Asia")	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Nepali"	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Limba"	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Ndebele"	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Ainu"	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Maranao"	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Nepali"	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Limba"	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Ndebele"	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Ainu"	world_1
SELECT CountryCode FROM countrylanguage EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Maranao"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Nepali"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Limba"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Ndebele"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Ainu"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Maranao"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Nepali"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Limba"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Ndebele"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Ainu"	world_1
SELECT DISTINCT CountryCode FROM countrylanguage WHERE LANGUAGE != "Maranao"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Nepali"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Limba"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Ndebele"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Ainu"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Maranao"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Constitutional Monarchy (Emirate)" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "English"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Monarchy (Sultanate)" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "English"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Autonomous Area" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "English"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Constitutional Monarchy" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "English"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Territorial Collectivity of France" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "English"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Nepali"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Limba"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Ndebele"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Ainu"	world_1
SELECT Code FROM country WHERE GovernmentForm != "Republic" EXCEPT SELECT CountryCode FROM countrylanguage WHERE LANGUAGE = "Maranao"	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Nepali')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Limba')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Ndebele')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Ainu')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Maranao')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Oceania' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'English')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'South America' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'English')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Asia' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'English')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'North America' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'English')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Africa' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'English')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Nepali')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Limba')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Ndebele')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Ainu')	world_1
SELECT DISTINCT T2.Name FROM country AS T1 JOIN city AS T2 ON T2.CountryCode = T1.Code WHERE T1.Continent = 'Europe' AND T1.Name NOT IN (SELECT T3.Name FROM country AS T3 JOIN countrylanguage AS T4 ON T3.Code = T4.CountryCode WHERE T4.IsOfficial = 'T' AND T4.Language = 'Maranao')	world_1
SELECT DISTINCT T3.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode JOIN city AS T3 ON T1.Code = T3.CountryCode WHERE T2.IsOfficial = 'T' AND T2.Language = 'Nepali' AND T1.Continent = "Asia"	world_1
SELECT DISTINCT T3.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode JOIN city AS T3 ON T1.Code = T3.CountryCode WHERE T2.IsOfficial = 'T' AND T2.Language = 'Kirgiz' AND T1.Continent = "Asia"	world_1
SELECT DISTINCT T3.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode JOIN city AS T3 ON T1.Code = T3.CountryCode WHERE T2.IsOfficial = 'T' AND T2.Language = 'Dzongkha' AND T1.Continent = "Asia"	world_1
SELECT DISTINCT T3.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode JOIN city AS T3 ON T1.Code = T3.CountryCode WHERE T2.IsOfficial = 'T' AND T2.Language = 'Thai' AND T1.Continent = "Asia"	world_1
SELECT DISTINCT T3.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode JOIN city AS T3 ON T1.Code = T3.CountryCode WHERE T2.IsOfficial = 'T' AND T2.Language = 'Malay' AND T1.Continent = "Asia"	world_1
SELECT count(*) FROM country WHERE continent = "Oceania"	world_1
SELECT count(*) FROM country WHERE continent = "South America"	world_1
SELECT count(*) FROM country WHERE continent = "Europe"	world_1
SELECT count(*) FROM country WHERE continent = "Antarctica"	world_1
SELECT count(*) FROM country WHERE continent = "North America"	world_1
SELECT count(*) FROM country WHERE continent = "Oceania"	world_1
SELECT count(*) FROM country WHERE continent = "South America"	world_1
SELECT count(*) FROM country WHERE continent = "Europe"	world_1
SELECT count(*) FROM country WHERE continent = "Antarctica"	world_1
SELECT count(*) FROM country WHERE continent = "North America"	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Nepali" GROUP BY CountryCode	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Limba" GROUP BY CountryCode	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Ndebele" GROUP BY CountryCode	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Ainu" GROUP BY CountryCode	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Maranao" GROUP BY CountryCode	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Nepali" GROUP BY CountryCode	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Limba" GROUP BY CountryCode	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Ndebele" GROUP BY CountryCode	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Ainu" GROUP BY CountryCode	world_1
SELECT count(*) , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Maranao" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Nepali" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Limba" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Ndebele" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Ainu" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Maranao" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Nepali" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Limba" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Ndebele" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Ainu" GROUP BY CountryCode	world_1
SELECT CountryCode , max(Percentage) FROM countrylanguage WHERE LANGUAGE = "Maranao" GROUP BY CountryCode	world_1
SELECT Name FROM conductor WHERE Nationality != 'UK'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'France'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'UK'	orchestra
SELECT Name FROM conductor WHERE Nationality != 'France'	orchestra
SELECT max(SHARE) , min(SHARE) FROM performance WHERE TYPE != "Auditions 1"	orchestra
SELECT max(SHARE) , min(SHARE) FROM performance WHERE TYPE != "Live final results"	orchestra
SELECT max(SHARE) , min(SHARE) FROM performance WHERE TYPE != "Auditions 1"	orchestra
SELECT max(SHARE) , min(SHARE) FROM performance WHERE TYPE != "Live final results"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "DVD" OR Major_Record_Format = "DVD"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "CD / LP" OR Major_Record_Format = "DVD"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "CD" OR Major_Record_Format = "CD"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "DVD" OR Major_Record_Format = "DVD"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "CD / LP" OR Major_Record_Format = "DVD"	orchestra
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format = "CD" OR Major_Record_Format = "CD"	orchestra
SELECT grade FROM Highschooler WHERE name = "Tiffany"	network_1
SELECT grade FROM Highschooler WHERE name = "Kris"	network_1
SELECT grade FROM Highschooler WHERE name = "Gabriel"	network_1
SELECT grade FROM Highschooler WHERE name = "Alexis"	network_1
SELECT grade FROM Highschooler WHERE name = "Jessica"	network_1
SELECT grade FROM Highschooler WHERE name = "Tiffany"	network_1
SELECT grade FROM Highschooler WHERE name = "Kris"	network_1
SELECT grade FROM Highschooler WHERE name = "Gabriel"	network_1
SELECT grade FROM Highschooler WHERE name = "Alexis"	network_1
SELECT grade FROM Highschooler WHERE name = "Jessica"	network_1
SELECT ID FROM Highschooler WHERE name = "Tiffany"	network_1
SELECT ID FROM Highschooler WHERE name = "Logan"	network_1
SELECT ID FROM Highschooler WHERE name = "Kris"	network_1
SELECT ID FROM Highschooler WHERE name = "Gabriel"	network_1
SELECT ID FROM Highschooler WHERE name = "Alexis"	network_1
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id JOIN Highschooler AS T3 ON T1.friend_id = T3.id WHERE T2.name = "Tiffany"	network_1
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id JOIN Highschooler AS T3 ON T1.friend_id = T3.id WHERE T2.name = "Logan"	network_1
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id JOIN Highschooler AS T3 ON T1.friend_id = T3.id WHERE T2.name = "Kris"	network_1
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id JOIN Highschooler AS T3 ON T1.friend_id = T3.id WHERE T2.name = "Gabriel"	network_1
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id JOIN Highschooler AS T3 ON T1.friend_id = T3.id WHERE T2.name = "Alexis"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Kris"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Gabriel"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Alexis"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Jordan"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Andrew"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Kris"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Gabriel"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Alexis"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Jordan"	network_1
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Andrew"	network_1
SELECT count(*) FROM Likes AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Gabriel"	network_1
SELECT count(*) FROM Likes AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id WHERE T2.name = "Gabriel"	network_1
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Montana' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'SouthCarolina' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Alabama' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Hawaii' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Mississippi' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Montana' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'SouthCarolina' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Alabama' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Hawaii' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT professional_id , last_name , cell_number FROM Professionals WHERE state = 'Mississippi' UNION SELECT T1.professional_id , T1.last_name , T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING count(*) > 2	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'Arizona'	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'Vermont'	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'NewYork'	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'Wisconsin'	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'Maryland'	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'Arizona'	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'Vermont'	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'NewYork'	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'Wisconsin'	dog_kennels
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'Maryland'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Montana' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'SouthCarolina' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Alabama' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Mississippi' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Wisconsin' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'Montana'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'SouthCarolina'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'Alabama'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'Hawaii'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'Mississippi'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Montana' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'SouthCarolina' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Alabama' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Mississippi' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Wisconsin' OR state = 'Wisconsin'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'Montana'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'SouthCarolina'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'Alabama'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'Hawaii'	dog_kennels
SELECT email_address FROM Professionals WHERE state = 'Hawaii' OR state = 'Mississippi'	dog_kennels
SELECT Name FROM singer WHERE Citizenship != "Germany"	singer
SELECT Name FROM singer WHERE Citizenship != "Australia"	singer
SELECT Name FROM singer WHERE Citizenship != "United States"	singer
SELECT Name FROM singer WHERE Citizenship != "Chile"	singer
SELECT T2.feature_type_name FROM Other_Available_Features AS T1 JOIN Ref_Feature_Types AS T2 ON T1.feature_type_code = T2.feature_type_code WHERE T1.feature_name = "BurglarAlarm"	real_estate_properties
