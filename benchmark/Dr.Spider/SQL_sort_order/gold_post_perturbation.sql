SELECT name , country , age FROM singer ORDER BY age ASC	concert_singer
SELECT name , country , age FROM singer ORDER BY age ASC	concert_singer
SELECT song_name , song_release_year FROM singer ORDER BY age DESC LIMIT 1	concert_singer
SELECT song_name , song_release_year FROM singer ORDER BY age DESC LIMIT 1	concert_singer
SELECT name , capacity FROM stadium ORDER BY average ASC LIMIT 1	concert_singer
SELECT name , capacity FROM stadium ORDER BY average ASC LIMIT 1	concert_singer
SELECT T2.name , T2.capacity FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year >= 2014 GROUP BY T2.stadium_id ORDER BY count(*) ASC LIMIT 1	concert_singer
select t2.name , t2.capacity from concert as t1 join stadium as t2 on t1.stadium_id = t2.stadium_id where t1.year > 2013 group by t2.stadium_id order by count(*) ASC limit 1	concert_singer
SELECT YEAR FROM concert GROUP BY YEAR ORDER BY count(*) ASC LIMIT 1	concert_singer
SELECT YEAR FROM concert GROUP BY YEAR ORDER BY count(*) ASC LIMIT 1	concert_singer
SELECT weight FROM pets ORDER BY pet_age DESC LIMIT 1	pets_1
SELECT weight FROM pets ORDER BY pet_age DESC LIMIT 1	pets_1
SELECT pettype , weight FROM pets ORDER BY pet_age DESC LIMIT 1	pets_1
SELECT pettype , weight FROM pets ORDER BY pet_age DESC LIMIT 1	pets_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.horsepower DESC LIMIT 1	car_1
SELECT T2.CountryName FROM CAR_MAKERS AS T1 JOIN COUNTRIES AS T2 ON T1.Country = T2.CountryId GROUP BY T1.Country ORDER BY Count(*) ASC LIMIT 1	car_1
SELECT T2.CountryName FROM CAR_MAKERS AS T1 JOIN COUNTRIES AS T2 ON T1.Country = T2.CountryId GROUP BY T1.Country ORDER BY Count(*) ASC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 3 ORDER BY T2.horsepower ASC LIMIT 1	car_1
SELECT T2.horsepower , T1.Make FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.cylinders = 3 ORDER BY T2.horsepower ASC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id ORDER BY T2.mpg ASC LIMIT 1	car_1
select t1.model from car_names as t1 join cars_data as t2 on t1.makeid = t2.id order by t2.mpg ASC limit 1	car_1
SELECT Model FROM CAR_NAMES GROUP BY Model ORDER BY count(*) ASC LIMIT 1	car_1
SELECT Model FROM CAR_NAMES GROUP BY Model ORDER BY count(*) ASC LIMIT 1	car_1
SELECT T1.horsepower FROM CARS_DATA AS T1 ORDER BY T1.accelerate ASC LIMIT 1	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Accelerate > ( SELECT Accelerate FROM CARS_DATA ORDER BY Horsepower ASC LIMIT 1 )	car_1
SELECT COUNT(*) FROM CARS_DATA WHERE Accelerate > ( SELECT Accelerate FROM CARS_DATA ORDER BY Horsepower ASC LIMIT 1 )	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 4 ORDER BY T2.horsepower ASC LIMIT 1	car_1
SELECT T1.Model FROM CAR_NAMES AS T1 JOIN CARS_DATA AS T2 ON T1.MakeId = T2.Id WHERE T2.Cylinders = 4 ORDER BY T2.horsepower ASC LIMIT 1	car_1
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline GROUP BY T1.Airline ORDER BY count(*) ASC LIMIT 1	flight_2
SELECT T1.Airline FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline GROUP BY T1.Airline ORDER BY count(*) ASC LIMIT 1	flight_2
SELECT T1.Abbreviation , T1.Country FROM AIRLINES AS T1 JOIN FLIGHTS AS T2 ON T1.uid = T2.Airline GROUP BY T1.Airline ORDER BY count(*) DESC LIMIT 1	flight_2
SELECT name FROM employee ORDER BY age DESC	employee_hire_evaluation
SELECT name FROM employee ORDER BY age DESC	employee_hire_evaluation
SELECT manager_name , district FROM shop ORDER BY number_products ASC LIMIT 1	employee_hire_evaluation
SELECT manager_name , district FROM shop ORDER BY number_products ASC LIMIT 1	employee_hire_evaluation
SELECT name , LOCATION , district FROM shop ORDER BY number_products ASC	employee_hire_evaluation
SELECT name , LOCATION , district FROM shop ORDER BY number_products ASC	employee_hire_evaluation
SELECT t1.name FROM employee AS t1 JOIN evaluation AS t2 ON t1.Employee_ID = t2.Employee_ID GROUP BY t2.Employee_ID ORDER BY count(*) ASC LIMIT 1	employee_hire_evaluation
SELECT t1.name FROM employee AS t1 JOIN evaluation AS t2 ON t1.Employee_ID = t2.Employee_ID GROUP BY t2.Employee_ID ORDER BY count(*) ASC LIMIT 1	employee_hire_evaluation
SELECT t1.name FROM employee AS t1 JOIN evaluation AS t2 ON t1.Employee_ID = t2.Employee_ID ORDER BY t2.bonus ASC LIMIT 1	employee_hire_evaluation
SELECT t2.name FROM hiring AS t1 JOIN shop AS t2 ON t1.shop_id = t2.shop_id GROUP BY t1.shop_id ORDER BY count(*) ASC LIMIT 1	employee_hire_evaluation
SELECT t2.name FROM hiring AS t1 JOIN shop AS t2 ON t1.shop_id = t2.shop_id GROUP BY t1.shop_id ORDER BY count(*) ASC LIMIT 1	employee_hire_evaluation
SELECT T1.template_id , T2.Template_Type_Code FROM Documents AS T1 JOIN Templates AS T2 ON T1.template_id = T2.template_id GROUP BY T1.template_id ORDER BY count(*) ASC LIMIT 1	cre_Doc_Template_Mgt
SELECT T1.template_id , T2.Template_Type_Code FROM Documents AS T1 JOIN Templates AS T2 ON T1.template_id = T2.template_id GROUP BY T1.template_id ORDER BY count(*) ASC LIMIT 1	cre_Doc_Template_Mgt
SELECT template_type_code FROM Templates GROUP BY template_type_code ORDER BY count(*) ASC LIMIT 1	cre_Doc_Template_Mgt
SELECT template_type_code FROM Templates GROUP BY template_type_code ORDER BY count(*) ASC LIMIT 1	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id GROUP BY T1.template_type_code ORDER BY count(*) ASC LIMIT 1	cre_Doc_Template_Mgt
SELECT T1.template_type_code FROM Templates AS T1 JOIN Documents AS T2 ON T1.template_id = T2.template_id GROUP BY T1.template_type_code ORDER BY count(*) ASC LIMIT 1	cre_Doc_Template_Mgt
SELECT T1.document_id , T2.document_name FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id GROUP BY T1.document_id ORDER BY count(*) ASC LIMIT 1	cre_Doc_Template_Mgt
SELECT T1.document_id , T2.document_name FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.document_id = T2.document_id GROUP BY T1.document_id ORDER BY count(*) ASC LIMIT 1	cre_Doc_Template_Mgt
SELECT document_id FROM Paragraphs GROUP BY document_id ORDER BY count(*) DESC LIMIT 1	cre_Doc_Template_Mgt
SELECT Name FROM teacher ORDER BY Age DESC	course_teach
SELECT Name FROM teacher ORDER BY Age DESC	course_teach
SELECT Hometown FROM teacher ORDER BY Age DESC LIMIT 1	course_teach
SELECT Hometown FROM teacher ORDER BY Age DESC LIMIT 1	course_teach
SELECT Hometown FROM teacher GROUP BY Hometown ORDER BY COUNT(*) ASC LIMIT 1	course_teach
SELECT Hometown FROM teacher GROUP BY Hometown ORDER BY COUNT(*) ASC LIMIT 1	course_teach
SELECT T3.Name , T2.Course FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID ORDER BY T3.Name DESC	course_teach
SELECT T3.Name , T2.Course FROM course_arrange AS T1 JOIN course AS T2 ON T1.Course_ID = T2.Course_ID JOIN teacher AS T3 ON T1.Teacher_ID = T3.Teacher_ID ORDER BY T3.Name DESC	course_teach
SELECT name FROM visitor WHERE Level_of_membership > 4 ORDER BY Level_of_membership ASC	museum_visit
SELECT name , Level_of_membership FROM visitor WHERE Level_of_membership > 4 ORDER BY age ASC	museum_visit
SELECT museum_id , name FROM museum ORDER BY num_of_staff ASC LIMIT 1	museum_visit
SELECT t2.visitor_id , t1.name , t1.Level_of_membership FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id GROUP BY t2.visitor_id ORDER BY sum(t2.Total_spent) ASC LIMIT 1	museum_visit
SELECT t2.Museum_ID , t1.name FROM museum AS t1 JOIN visit AS t2 ON t1.Museum_ID = t2.Museum_ID GROUP BY t2.Museum_ID ORDER BY count(*) ASC LIMIT 1	museum_visit
SELECT t1.name , t1.age FROM visitor AS t1 JOIN visit AS t2 ON t1.id = t2.visitor_id ORDER BY t2.num_of_ticket ASC LIMIT 1	museum_visit
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN rankings AS T2 ON T1.player_id = T2.player_id ORDER BY T2.tours ASC LIMIT 1	wta_1
SELECT T1.country_code , T1.first_name FROM players AS T1 JOIN rankings AS T2 ON T1.player_id = T2.player_id ORDER BY T2.tours ASC LIMIT 1	wta_1
SELECT YEAR FROM matches GROUP BY YEAR ORDER BY count(*) ASC LIMIT 1	wta_1
SELECT YEAR FROM matches GROUP BY YEAR ORDER BY count(*) ASC LIMIT 1	wta_1
SELECT winner_name , winner_rank_points FROM matches GROUP BY winner_name ORDER BY count(*) ASC LIMIT 1	wta_1
SELECT winner_name , winner_rank_points FROM matches GROUP BY winner_name ORDER BY count(*) ASC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Australian Open' ORDER BY winner_rank_points ASC LIMIT 1	wta_1
SELECT winner_name FROM matches WHERE tourney_name = 'Australian Open' ORDER BY winner_rank_points ASC LIMIT 1	wta_1
SELECT winner_name , loser_name FROM matches ORDER BY minutes ASC LIMIT 1	wta_1
SELECT winner_name , loser_name FROM matches ORDER BY minutes ASC LIMIT 1	wta_1
SELECT country_code FROM players GROUP BY country_code ORDER BY count(*) ASC LIMIT 1	wta_1
SELECT country_code FROM players GROUP BY country_code ORDER BY count(*) ASC LIMIT 1	wta_1
SELECT DISTINCT winner_name , winner_rank FROM matches ORDER BY winner_age DESC LIMIT 3	wta_1
SELECT DISTINCT winner_name , winner_rank FROM matches ORDER BY winner_age DESC LIMIT 3	wta_1
SELECT T1.first_name , T1.country_code , T1.birth_date FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id ORDER BY T2.winner_rank_points ASC LIMIT 1	wta_1
SELECT T1.first_name , T1.country_code , T1.birth_date FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id ORDER BY T2.winner_rank_points ASC LIMIT 1	wta_1
SELECT name , tonnage FROM ship ORDER BY name ASC	battle_death
SELECT T2.id , T2.name FROM death AS T1 JOIN ship AS t2 ON T1.caused_by_ship_id = T2.id GROUP BY T2.id ORDER BY count(*) ASC LIMIT 1	battle_death
SELECT T2.department_name , T1.department_id FROM Degree_Programs AS T1 JOIN Departments AS T2 ON T1.department_id = T2.department_id GROUP BY T1.department_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
select t2.department_name , t1.department_id from degree_programs as t1 join departments as t2 on t1.department_id = t2.department_id group by t1.department_id order by count(*) ASC limit 1	student_transcripts_tracking
SELECT section_name FROM Sections ORDER BY section_name ASC	student_transcripts_tracking
SELECT section_name FROM Sections ORDER BY section_name ASC	student_transcripts_tracking
SELECT T1.semester_name , T1.semester_id FROM Semesters AS T1 JOIN Student_Enrolment AS T2 ON T1.semester_id = T2.semester_id GROUP BY T1.semester_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.semester_name , T1.semester_id FROM Semesters AS T1 JOIN Student_Enrolment AS T2 ON T1.semester_id = T2.semester_id GROUP BY T1.semester_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.degree_summary_name FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id GROUP BY T1.degree_summary_name ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.degree_summary_name FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id GROUP BY T1.degree_summary_name ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.degree_program_id , T1.degree_summary_name FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id GROUP BY T1.degree_program_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.degree_program_id , T1.degree_summary_name FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id GROUP BY T1.degree_program_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.student_id , T1.first_name , T1.middle_name , T1.last_name , count(*) , T1.student_id FROM Students AS T1 JOIN Student_Enrolment AS T2 ON T1.student_id = T2.student_id GROUP BY T1.student_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.student_id , T1.first_name , T1.middle_name , T1.last_name , count(*) , T1.student_id FROM Students AS T1 JOIN Student_Enrolment AS T2 ON T1.student_id = T2.student_id GROUP BY T1.student_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.course_name FROM Courses AS T1 JOIN Student_Enrolment_Courses AS T2 ON T1.course_id = T2.course_id GROUP BY T1.course_name ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.course_name FROM Courses AS T1 JOIN Student_Enrolment_Courses AS T2 ON T1.course_id = T2.course_id GROUP BY T1.course_name ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT first_name , middle_name , last_name FROM Students ORDER BY date_left DESC LIMIT 1	student_transcripts_tracking
SELECT first_name , middle_name , last_name FROM Students ORDER BY date_left DESC LIMIT 1	student_transcripts_tracking
SELECT T1.address_id , T1.line_1 , T1.line_2 FROM Addresses AS T1 JOIN Students AS T2 ON T1.address_id = T2.current_address_id GROUP BY T1.address_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T1.address_id , T1.line_1 , T1.line_2 FROM Addresses AS T1 JOIN Students AS T2 ON T1.address_id = T2.current_address_id GROUP BY T1.address_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT transcript_date , other_details FROM Transcripts ORDER BY transcript_date DESC LIMIT 1	student_transcripts_tracking
SELECT count(*) , student_course_id FROM Transcript_Contents GROUP BY student_course_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT count(*) , student_course_id FROM Transcript_Contents GROUP BY student_course_id ORDER BY count(*) ASC LIMIT 1	student_transcripts_tracking
SELECT T2.transcript_date , T1.transcript_id FROM Transcript_Contents AS T1 JOIN Transcripts AS T2 ON T1.transcript_id = T2.transcript_id GROUP BY T1.transcript_id ORDER BY count(*) DESC LIMIT 1	student_transcripts_tracking
SELECT T2.transcript_date , T1.transcript_id FROM Transcript_Contents AS T1 JOIN Transcripts AS T2 ON T1.transcript_id = T2.transcript_id GROUP BY T1.transcript_id ORDER BY count(*) DESC LIMIT 1	student_transcripts_tracking
SELECT other_student_details FROM Students ORDER BY other_student_details ASC	student_transcripts_tracking
SELECT other_student_details FROM Students ORDER BY other_student_details ASC	student_transcripts_tracking
SELECT Title FROM Cartoon ORDER BY title DESC	tvshow
SELECT Country , count(*) FROM TV_Channel GROUP BY Country ORDER BY count(*) ASC LIMIT 1	tvshow
SELECT Country , count(*) FROM TV_Channel GROUP BY Country ORDER BY count(*) ASC LIMIT 1	tvshow
SELECT LANGUAGE , count(*) FROM TV_Channel GROUP BY LANGUAGE ORDER BY count(*) DESC LIMIT 1	tvshow
SELECT LANGUAGE , count(*) FROM TV_Channel GROUP BY LANGUAGE ORDER BY count(*) DESC LIMIT 1	tvshow
SELECT Episode , Rating FROM TV_series ORDER BY Rating ASC LIMIT 3	tvshow
SELECT Episode , Rating FROM TV_series ORDER BY Rating ASC LIMIT 3	tvshow
select production_code , channel from cartoon order by original_air_date ASC limit 1	tvshow
select production_code , channel from cartoon order by original_air_date ASC limit 1	tvshow
SELECT Earnings FROM poker_player ORDER BY Earnings ASC	poker_player
SELECT Earnings FROM poker_player ORDER BY Earnings ASC	poker_player
SELECT Money_Rank FROM poker_player ORDER BY Earnings ASC LIMIT 1	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID ORDER BY T2.Final_Table_Made DESC	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID ORDER BY T2.Final_Table_Made DESC	poker_player
SELECT T1.Birth_Date FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID ORDER BY T2.Earnings DESC LIMIT 1	poker_player
SELECT T1.Birth_Date FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID ORDER BY T2.Earnings DESC LIMIT 1	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID ORDER BY T2.Earnings ASC	poker_player
SELECT T1.Name FROM people AS T1 JOIN poker_player AS T2 ON T1.People_ID = T2.People_ID ORDER BY T2.Earnings ASC	poker_player
SELECT Nationality FROM people GROUP BY Nationality ORDER BY COUNT(*) ASC LIMIT 1	poker_player
SELECT Nationality FROM people GROUP BY Nationality ORDER BY COUNT(*) ASC LIMIT 1	poker_player
SELECT Name , Birth_Date FROM people ORDER BY Name DESC	poker_player
SELECT Name , Birth_Date FROM people ORDER BY Name DESC	poker_player
SELECT contestant_number , contestant_name FROM contestants ORDER BY contestant_name ASC	voter_1
SELECT T1.contestant_number , T1.contestant_name FROM contestants AS T1 JOIN votes AS T2 ON T1.contestant_number = T2.contestant_number GROUP BY T1.contestant_number ORDER BY count(*) DESC LIMIT 1	voter_1
SELECT T1.area_code FROM area_code_state AS T1 JOIN votes AS T2 ON T1.state = T2.state GROUP BY T1.area_code ORDER BY count(*) ASC LIMIT 1	voter_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Name = "Aruba" ORDER BY Percentage ASC LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "Asia" ORDER BY LifeExpectancy DESC LIMIT 1	world_1
SELECT Name FROM country WHERE Continent = "Asia" ORDER BY LifeExpectancy DESC LIMIT 1	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode GROUP BY T1.Name ORDER BY COUNT(*) ASC LIMIT 1	world_1
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode GROUP BY T1.Name ORDER BY COUNT(*) ASC LIMIT 1	world_1
SELECT T1.Continent FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode GROUP BY T1.Continent ORDER BY COUNT(*) ASC LIMIT 1	world_1
SELECT T1.Continent FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode GROUP BY T1.Continent ORDER BY COUNT(*) ASC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Continent = "Asia" GROUP BY T2.Language ORDER BY COUNT (*) ASC LIMIT 1	world_1
SELECT T2.Language FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T1.Continent = "Asia" GROUP BY T2.Language ORDER BY COUNT (*) ASC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "English" ORDER BY T1.Population ASC LIMIT 1	world_1
SELECT T1.Name , T1.Population FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = "English" ORDER BY T1.Population ASC LIMIT 1	world_1
SELECT Name , Population , LifeExpectancy FROM country WHERE Continent = "Asia" ORDER BY SurfaceArea ASC LIMIT 1	world_1
SELECT Name , Population , LifeExpectancy FROM country WHERE Continent = "Asia" ORDER BY SurfaceArea ASC LIMIT 1	world_1
SELECT Name , SurfaceArea , IndepYear FROM country ORDER BY Population DESC LIMIT 1	world_1
SELECT Name , SurfaceArea , IndepYear FROM country ORDER BY Population DESC LIMIT 1	world_1
SELECT Name , population , HeadOfState FROM country ORDER BY SurfaceArea ASC LIMIT 1	world_1
SELECT Name , population , HeadOfState FROM country ORDER BY SurfaceArea ASC LIMIT 1	world_1
SELECT Name , SurfaceArea FROM country ORDER BY SurfaceArea ASC LIMIT 5	world_1
SELECT Name , SurfaceArea FROM country ORDER BY SurfaceArea ASC LIMIT 5	world_1
SELECT Name FROM country ORDER BY Population ASC LIMIT 3	world_1
SELECT Name FROM country ORDER BY Population ASC LIMIT 3	world_1
SELECT Name FROM country ORDER BY Population DESC LIMIT 3	world_1
SELECT LANGUAGE FROM countrylanguage GROUP BY LANGUAGE ORDER BY count(*) ASC LIMIT 1	world_1
SELECT LANGUAGE FROM countrylanguage GROUP BY LANGUAGE ORDER BY count(*) ASC LIMIT 1	world_1
SELECT Name FROM conductor ORDER BY Age DESC	orchestra
SELECT Record_Company FROM orchestra ORDER BY Year_of_Founded ASC	orchestra
SELECT Record_Company FROM orchestra ORDER BY Year_of_Founded ASC	orchestra
SELECT Name FROM conductor ORDER BY Year_of_Work ASC	orchestra
SELECT Name FROM conductor ORDER BY Year_of_Work ASC	orchestra
SELECT Name FROM conductor ORDER BY Year_of_Work ASC LIMIT 1	orchestra
SELECT Name FROM conductor ORDER BY Year_of_Work ASC LIMIT 1	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID GROUP BY T2.Conductor_ID ORDER BY COUNT(*) ASC LIMIT 1	orchestra
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID GROUP BY T2.Conductor_ID ORDER BY COUNT(*) ASC LIMIT 1	orchestra
SELECT Major_Record_Format FROM orchestra GROUP BY Major_Record_Format ORDER BY COUNT(*) DESC	orchestra
SELECT Record_Company FROM orchestra GROUP BY Record_Company ORDER BY COUNT(*) ASC LIMIT 1	orchestra
SELECT Record_Company FROM orchestra GROUP BY Record_Company ORDER BY COUNT(*) ASC LIMIT 1	orchestra
SELECT grade FROM Highschooler GROUP BY grade ORDER BY count(*) ASC LIMIT 1	network_1
SELECT grade FROM Highschooler GROUP BY grade ORDER BY count(*) ASC LIMIT 1	network_1
SELECT T2.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id GROUP BY T1.student_id ORDER BY count(*) ASC LIMIT 1	network_1
SELECT T2.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.id GROUP BY T1.student_id ORDER BY count(*) ASC LIMIT 1	network_1
SELECT T1.owner_id , T2.first_name , T2.last_name FROM Dogs AS T1 JOIN Owners AS T2 ON T1.owner_id = T2.owner_id GROUP BY T1.owner_id ORDER BY count(*) ASC LIMIT 1	dog_kennels
SELECT T1.owner_id , T2.first_name , T2.last_name FROM Dogs AS T1 JOIN Owners AS T2 ON T1.owner_id = T2.owner_id GROUP BY T1.owner_id ORDER BY count(*) ASC LIMIT 1	dog_kennels
SELECT T1.breed_name FROM Breeds AS T1 JOIN Dogs AS T2 ON T1.breed_code = T2.breed_code GROUP BY T1.breed_name ORDER BY count(*) ASC LIMIT 1	dog_kennels
SELECT T1.breed_name FROM Breeds AS T1 JOIN Dogs AS T2 ON T1.breed_code = T2.breed_code GROUP BY T1.breed_name ORDER BY count(*) ASC LIMIT 1	dog_kennels
SELECT T1.owner_id , T1.last_name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY count(*) ASC LIMIT 1	dog_kennels
SELECT T1.owner_id , T1.last_name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY count(*) ASC LIMIT 1	dog_kennels
SELECT T1.treatment_type_description FROM Treatment_types AS T1 JOIN Treatments AS T2 ON T1.treatment_type_code = T2.treatment_type_code GROUP BY T1.treatment_type_code ORDER BY sum(cost_of_treatment) DESC LIMIT 1	dog_kennels
SELECT T1.treatment_type_description FROM Treatment_types AS T1 JOIN Treatments AS T2 ON T1.treatment_type_code = T2.treatment_type_code GROUP BY T1.treatment_type_code ORDER BY sum(cost_of_treatment) DESC LIMIT 1	dog_kennels
SELECT T1.owner_id , T1.zip_code FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY sum(T3.cost_of_treatment) ASC LIMIT 1	dog_kennels
SELECT T1.owner_id , T1.zip_code FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY sum(T3.cost_of_treatment) ASC LIMIT 1	dog_kennels
SELECT cost_of_treatment FROM Treatments ORDER BY date_of_treatment ASC LIMIT 1	dog_kennels
SELECT cost_of_treatment FROM Treatments ORDER BY date_of_treatment ASC LIMIT 1	dog_kennels
SELECT Name FROM singer ORDER BY Net_Worth_Millions DESC	singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions DESC	singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions ASC LIMIT 1	singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions ASC LIMIT 1	singer
SELECT Citizenship FROM singer GROUP BY Citizenship ORDER BY COUNT(*) ASC LIMIT 1	singer
select citizenship from singer group by citizenship order by count(*) ASC limit 1	singer
