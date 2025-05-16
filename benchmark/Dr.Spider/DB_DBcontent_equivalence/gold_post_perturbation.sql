SELECT singer.first_name , singer.last_name , singer.Country , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_0
SELECT singer.first_name , singer.last_name , singer.Country , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_0
SELECT singer.first_name , singer.last_name , count(*) FROM singer_in_concert JOIN singer ON singer_in_concert.Singer_ID = singer.Singer_ID GROUP BY singer.Singer_ID	concert_singer_0
SELECT singer.first_name , singer.last_name , count(*) FROM singer_in_concert JOIN singer ON singer_in_concert.Singer_ID = singer.Singer_ID GROUP BY singer.Singer_ID	concert_singer_0
SELECT singer.first_name , singer.last_name FROM singer_in_concert JOIN singer ON singer_in_concert.Singer_ID = singer.Singer_ID JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID WHERE concert.Year = 2014	concert_singer_0
SELECT singer.first_name , singer.last_name FROM singer_in_concert JOIN singer ON singer_in_concert.Singer_ID = singer.Singer_ID JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID WHERE concert.Year = 2014	concert_singer_0
SELECT singer.first_name , singer.last_name , singer.Country FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_0
SELECT singer.first_name , singer.last_name , singer.Country FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_0
SELECT singer.Song_Name , singer.Song_release_year FROM singer ORDER BY singer.birthyear desc LIMIT 1	concert_singer_1
SELECT singer.Song_Name , singer.Song_release_year FROM singer ORDER BY singer.birthyear desc LIMIT 1	concert_singer_1
SELECT singer.Song_Name FROM singer WHERE singer.birthyear < (SELECT avg(singer.birthyear) FROM singer)	concert_singer_1
SELECT singer.Song_Name FROM singer WHERE singer.birthyear < (SELECT avg(singer.birthyear) FROM singer)	concert_singer_1
SELECT singer.Song_Name , singer.Song_release_year FROM singer ORDER BY singer.birthyear desc LIMIT 1	concert_singer_5
SELECT singer.Song_Name , singer.Song_release_year FROM singer ORDER BY singer.birthyear desc LIMIT 1	concert_singer_5
SELECT singer.Song_Name FROM singer WHERE singer.birthyear < (SELECT avg(singer.birthyear) FROM singer)	concert_singer_5
SELECT singer.Song_Name FROM singer WHERE singer.birthyear < (SELECT avg(singer.birthyear) FROM singer)	concert_singer_5
SELECT singer.first_name , singer.last_name , count(*) FROM singer_in_concert JOIN singer ON singer_in_concert.Singer_ID = singer.Singer_ID GROUP BY singer.Singer_ID	concert_singer_5
SELECT singer.first_name , singer.last_name , count(*) FROM singer_in_concert JOIN singer ON singer_in_concert.Singer_ID = singer.Singer_ID GROUP BY singer.Singer_ID	concert_singer_5
SELECT singer.first_name , singer.last_name FROM singer_in_concert JOIN singer ON singer_in_concert.Singer_ID = singer.Singer_ID JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID WHERE concert.Year = 2014	concert_singer_5
SELECT singer.first_name , singer.last_name FROM singer_in_concert JOIN singer ON singer_in_concert.Singer_ID = singer.Singer_ID JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID WHERE concert.Year = 2014	concert_singer_5
SELECT singer.first_name , singer.last_name , singer.Country FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_5
SELECT singer.first_name , singer.last_name , singer.Country FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_5
SELECT Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_0
SELECT Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_0
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.is_male = "F" and Pets.is_dog = "T"	pets_1_0
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.is_male = "F" and Pets.is_dog = "T"	pets_1_0
SELECT DISTINCT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T" or Pets.is_dog = "T"	pets_1_0
SELECT DISTINCT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T" or Pets.is_dog = "T"	pets_1_0
SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T" INTERSECT SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_dog = "T"	pets_1_0
SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T" INTERSECT SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_dog = "T"	pets_1_0
SELECT Student.StuID FROM Student EXCEPT SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T"	pets_1_0
SELECT Student.StuID FROM Student EXCEPT SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T"	pets_1_0
SELECT Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_1
SELECT Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_1
SELECT Pets.PetType , Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_1
SELECT Pets.PetType , Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_1
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.is_male = "F" and Pets.PetType = "dog"	pets_1_2
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.is_male = "F" and Pets.PetType = "dog"	pets_1_2
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.Sex = "F" and Pets.is_dog = "T"	pets_1_4
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.Sex = "F" and Pets.is_dog = "T"	pets_1_4
SELECT DISTINCT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T" or Pets.is_dog = "T"	pets_1_4
SELECT DISTINCT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T" or Pets.is_dog = "T"	pets_1_4
SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T" INTERSECT SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_dog = "T"	pets_1_4
SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T" INTERSECT SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_dog = "T"	pets_1_4
SELECT Student.StuID FROM Student EXCEPT SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T"	pets_1_4
SELECT Student.StuID FROM Student EXCEPT SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.is_cat = "T"	pets_1_4
SELECT Student.LName FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_age = 3 and Pets.is_cat = "T"	pets_1_4
SELECT Student.LName FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_age = 3 and Pets.is_cat = "T"	pets_1_4
SELECT Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_5
SELECT Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_5
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.is_male = "F" and Pets.PetType = "dog"	pets_1_5
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.is_male = "F" and Pets.PetType = "dog"	pets_1_5
SELECT Pets.PetType , Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_5
SELECT Pets.PetType , Pets.weight FROM Pets ORDER BY Pets.birthyear desc LIMIT 1	pets_1_5
SELECT employee.first_name , employee.last_name FROM employee ORDER BY employee.Age asc	employee_hire_evaluation_0
SELECT employee.first_name , employee.last_name FROM employee ORDER BY employee.Age asc	employee_hire_evaluation_0
SELECT shop.manager_first_name , shop.manager_last_name , shop.District FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_0
SELECT shop.manager_first_name , shop.manager_last_name , shop.District FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_0
SELECT employee.first_name , employee.last_name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.Employee_ID GROUP BY evaluation.Employee_ID ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_0
SELECT employee.first_name , employee.last_name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.Employee_ID GROUP BY evaluation.Employee_ID ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_0
SELECT employee.first_name , employee.last_name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.Employee_ID ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_0
SELECT employee.first_name , employee.last_name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.Employee_ID ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_0
SELECT employee.first_name , employee.last_name FROM employee WHERE employee.Employee_ID NOT in (SELECT evaluation.Employee_ID FROM evaluation)	employee_hire_evaluation_0
SELECT employee.first_name , employee.last_name FROM employee WHERE employee.Employee_ID NOT in (SELECT evaluation.Employee_ID FROM evaluation)	employee_hire_evaluation_0
SELECT employee.Name FROM employee ORDER BY employee.birthyear desc	employee_hire_evaluation_1
SELECT employee.Name FROM employee ORDER BY employee.birthyear desc	employee_hire_evaluation_1
SELECT shop.manager_first_name , shop.manager_last_name , shop.District FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_4
SELECT shop.manager_first_name , shop.manager_last_name , shop.District FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_4
SELECT employee.first_name , employee.last_name FROM employee ORDER BY employee.birthyear desc	employee_hire_evaluation_5
SELECT employee.first_name , employee.last_name FROM employee ORDER BY employee.birthyear desc	employee_hire_evaluation_5
SELECT shop.manager_first_name , shop.manager_last_name , shop.District FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_5
SELECT shop.manager_first_name , shop.manager_last_name , shop.District FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_5
SELECT employee.first_name , employee.last_name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.Employee_ID GROUP BY evaluation.Employee_ID ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_5
SELECT employee.first_name , employee.last_name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.Employee_ID GROUP BY evaluation.Employee_ID ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_5
SELECT employee.first_name , employee.last_name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.Employee_ID ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_5
SELECT employee.first_name , employee.last_name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.Employee_ID ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_5
SELECT employee.first_name , employee.last_name FROM employee WHERE employee.Employee_ID NOT in (SELECT evaluation.Employee_ID FROM evaluation)	employee_hire_evaluation_5
SELECT employee.first_name , employee.last_name FROM employee WHERE employee.Employee_ID NOT in (SELECT evaluation.Employee_ID FROM evaluation)	employee_hire_evaluation_5
SELECT teacher.Name FROM teacher ORDER BY teacher.birthyear desc	course_teach_0
SELECT teacher.Name FROM teacher ORDER BY teacher.birthyear desc	course_teach_0
SELECT teacher.Hometown FROM teacher ORDER BY teacher.birthyear desc LIMIT 1	course_teach_0
SELECT teacher.Hometown FROM teacher ORDER BY teacher.birthyear desc LIMIT 1	course_teach_0
SELECT teacher.first_name , teacher.last_name FROM teacher ORDER BY teacher.Age asc	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM teacher ORDER BY teacher.Age asc	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Hometown != "little lever urban district"	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Hometown != "little lever urban district"	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Age = 32 or teacher.Age = 33	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Age = 32 or teacher.Age = 33	course_teach_1
SELECT teacher.first_name , teacher.last_name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID	course_teach_1
SELECT teacher.first_name , teacher.last_name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID	course_teach_1
SELECT teacher.first_name , teacher.last_name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID ORDER BY teacher.first_name , teacher.last_name asc	course_teach_1
SELECT teacher.first_name , teacher.last_name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID ORDER BY teacher.first_name , teacher.last_name asc	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID WHERE course.Course = "Math"	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID WHERE course.Course = "Math"	course_teach_1
SELECT teacher.first_name , teacher.last_name , count(*) FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID GROUP BY teacher.first_name , teacher.last_name	course_teach_1
SELECT teacher.first_name , teacher.last_name , count(*) FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID GROUP BY teacher.first_name , teacher.last_name	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID GROUP BY teacher.first_name , teacher.last_name HAVING count(*) >= 2	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID GROUP BY teacher.first_name , teacher.last_name HAVING count(*) >= 2	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Teacher_ID NOT in (SELECT course_arrange.Teacher_ID FROM course_arrange)	course_teach_1
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Teacher_ID NOT in (SELECT course_arrange.Teacher_ID FROM course_arrange)	course_teach_1
SELECT teacher.Name FROM teacher ORDER BY teacher.birthyear desc	course_teach_4
SELECT teacher.Name FROM teacher ORDER BY teacher.birthyear desc	course_teach_4
SELECT teacher.Hometown FROM teacher ORDER BY teacher.birthyear desc LIMIT 1	course_teach_4
SELECT teacher.Hometown FROM teacher ORDER BY teacher.birthyear desc LIMIT 1	course_teach_4
SELECT teacher.first_name , teacher.last_name FROM teacher ORDER BY teacher.birthyear desc	course_teach_5
SELECT teacher.first_name , teacher.last_name FROM teacher ORDER BY teacher.birthyear desc	course_teach_5
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Hometown != "little lever urban district"	course_teach_5
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Hometown != "little lever urban district"	course_teach_5
SELECT teacher.Hometown FROM teacher ORDER BY teacher.birthyear desc LIMIT 1	course_teach_5
SELECT teacher.Hometown FROM teacher ORDER BY teacher.birthyear desc LIMIT 1	course_teach_5
SELECT teacher.first_name , teacher.last_name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID	course_teach_5
SELECT teacher.first_name , teacher.last_name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID	course_teach_5
SELECT teacher.first_name , teacher.last_name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID ORDER BY teacher.first_name , teacher.last_name asc	course_teach_5
SELECT teacher.first_name , teacher.last_name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID ORDER BY teacher.first_name , teacher.last_name asc	course_teach_5
SELECT teacher.first_name , teacher.last_name FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID WHERE course.Course = "Math"	course_teach_5
SELECT teacher.first_name , teacher.last_name FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID WHERE course.Course = "Math"	course_teach_5
SELECT teacher.first_name , teacher.last_name , count(*) FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID GROUP BY teacher.first_name , teacher.last_name	course_teach_5
SELECT teacher.first_name , teacher.last_name , count(*) FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID GROUP BY teacher.first_name , teacher.last_name	course_teach_5
SELECT teacher.first_name , teacher.last_name FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID GROUP BY teacher.first_name , teacher.last_name HAVING count(*) >= 2	course_teach_5
SELECT teacher.first_name , teacher.last_name FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID GROUP BY teacher.first_name , teacher.last_name HAVING count(*) >= 2	course_teach_5
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Teacher_ID NOT in (SELECT course_arrange.Teacher_ID FROM course_arrange)	course_teach_5
SELECT teacher.first_name , teacher.last_name FROM teacher WHERE teacher.Teacher_ID NOT in (SELECT course_arrange.Teacher_ID FROM course_arrange)	course_teach_5
SELECT visitor.first_name , visitor.last_name FROM visitor WHERE visitor.Level_of_membership > 4 ORDER BY visitor.Level_of_membership desc	museum_visit_0
SELECT visitor.first_name , visitor.last_name , visitor.Level_of_membership FROM visitor WHERE visitor.Level_of_membership > 4 ORDER BY visitor.birthyear asc	museum_visit_0
SELECT visit.visitor_ID , visitor.first_name , visitor.last_name , visitor.Level_of_membership FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID GROUP BY visit.visitor_ID ORDER BY sum(visit.Total_spent) desc LIMIT 1	museum_visit_0
SELECT visitor.first_name , visitor.last_name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.Museum_ID WHERE museum.Open_Year < 2009 INTERSECT SELECT visitor.first_name , visitor.last_name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.Museum_ID WHERE museum.Open_Year > 2011	museum_visit_0
SELECT visitor.Name , visitor.Level_of_membership FROM visitor WHERE visitor.Level_of_membership > 4 ORDER BY visitor.birthyear asc	museum_visit_1
SELECT players.first_name , players.birthyear , players.bithday FROM players WHERE players.country_code = "USA"	wta_1_0
SELECT players.first_name , players.birthyear , players.bithday FROM players WHERE players.country_code = "USA"	wta_1_0
SELECT players.first_name , players.country_code FROM players ORDER BY players.birthyear , players.bithday asc LIMIT 1	wta_1_0
SELECT players.first_name , players.country_code FROM players ORDER BY players.birthyear , players.bithday asc LIMIT 1	wta_1_0
SELECT players.first_name , players.last_name FROM players ORDER BY players.birthyear , players.bithday asc	wta_1_0
SELECT players.first_name , players.last_name FROM players ORDER BY players.birthyear , players.bithday asc	wta_1_0
SELECT players.first_name , players.last_name FROM players WHERE players.is_right_handed = "F" ORDER BY players.birthyear , players.bithday asc	wta_1_0
SELECT players.first_name , players.last_name FROM players WHERE players.is_right_handed = "F" ORDER BY players.birthyear , players.bithday asc	wta_1_0
SELECT count(DISTINCT matches.winner_name) FROM matches WHERE matches.tourney_name = "WTA Championships" and matches.is_winner_right_handed = "F"	wta_1_0
SELECT count(DISTINCT matches.winner_name) FROM matches WHERE matches.tourney_name = "WTA Championships" and matches.is_winner_right_handed = "F"	wta_1_0
SELECT players.first_name , players.country_code , players.birthyear , players.bithday FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_0
SELECT players.first_name , players.country_code , players.birthyear , players.bithday FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_0
SELECT players.first_name , players.last_name FROM players WHERE players.is_right_handed = "F" ORDER BY players.birth_date asc	wta_1_3
SELECT players.first_name , players.last_name FROM players WHERE players.is_right_handed = "F" ORDER BY players.birth_date asc	wta_1_3
SELECT sum(rankings.tours) , rankings.year , rankings.month , rankings.day FROM rankings GROUP BY rankings.year , rankings.month , rankings.day	wta_1_4
SELECT sum(rankings.tours) , rankings.year , rankings.month , rankings.day FROM rankings GROUP BY rankings.year , rankings.month , rankings.day	wta_1_4
SELECT count(*) FROM ship WHERE ship.is_captured = "T"	battle_death_0
SELECT DISTINCT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.lost_in_battle WHERE ship.brig_ship = "T"	battle_death_0
SELECT count(*) FROM ship WHERE ship.is_captured = "T"	battle_death_1
SELECT Semesters.semester_term , Semesters.semester_year , Semesters.semester_id FROM Semesters JOIN Student_Enrolment ON Semesters.semester_id = Student_Enrolment.semester_id GROUP BY Semesters.semester_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Semesters.semester_term , Semesters.semester_year , Semesters.semester_id FROM Semesters JOIN Student_Enrolment ON Semesters.semester_id = Student_Enrolment.semester_id GROUP BY Semesters.semester_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.is_bachelor = "T"	student_transcripts_tracking_0
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.is_bachelor = "T"	student_transcripts_tracking_0
SELECT Semesters.semester_term , Semesters.semester_year FROM Semesters WHERE Semesters.semester_id NOT in (SELECT Student_Enrolment.semester_id FROM Student_Enrolment)	student_transcripts_tracking_0
SELECT Semesters.semester_term , Semesters.semester_year FROM Semesters WHERE Semesters.semester_id NOT in (SELECT Student_Enrolment.semester_id FROM Student_Enrolment)	student_transcripts_tracking_0
SELECT Transcripts.transcript_date , Transcripts.transcript_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_0
SELECT Transcripts.transcript_date , Transcripts.transcript_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_0
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.date_first_registered , Students.time_first_registered asc LIMIT 1	student_transcripts_tracking_0
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.date_first_registered , Students.time_first_registered asc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.transcript_date , Transcripts.transcript_time , Transcripts.other_details FROM Transcripts ORDER BY Transcripts.transcript_date , Transcripts.transcript_time asc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.transcript_date , Transcripts.transcript_time , Transcripts.other_details FROM Transcripts ORDER BY Transcripts.transcript_date , Transcripts.transcript_time asc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.transcript_date , Transcripts.transcript_time FROM Transcripts ORDER BY Transcripts.transcript_date , Transcripts.transcript_time desc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.transcript_date , Transcripts.transcript_time FROM Transcripts ORDER BY Transcripts.transcript_date , Transcripts.transcript_time desc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.transcript_date , Transcripts.transcript_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.transcript_date , Transcripts.transcript_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_0
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.is_master = "T" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.is_bachelor = "T"	student_transcripts_tracking_0
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.is_master = "T" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.is_bachelor = "T"	student_transcripts_tracking_0
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.year_first_registered , Students.month_first_registered , Students.day_first_registered , Students.time_first_registered asc LIMIT 1	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.year_first_registered , Students.month_first_registered , Students.day_first_registered , Students.time_first_registered asc LIMIT 1	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.date_left , Students.time_left asc LIMIT 1	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.date_left , Students.time_left asc LIMIT 1	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.year_first_registered , Students.month_first_registered , Students.day_first_registered , Students.time_first_registered asc LIMIT 1	student_transcripts_tracking_2
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.year_first_registered , Students.month_first_registered , Students.day_first_registered , Students.time_first_registered asc LIMIT 1	student_transcripts_tracking_2
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.is_bachelor = "T"	student_transcripts_tracking_3
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.is_bachelor = "T"	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.date_first_registered , Students.time_first_registered asc LIMIT 1	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.date_first_registered , Students.time_first_registered asc LIMIT 1	student_transcripts_tracking_3
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.is_master = "T" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.is_bachelor = "T"	student_transcripts_tracking_3
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.is_master = "T" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.is_bachelor = "T"	student_transcripts_tracking_3
SELECT Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_4
SELECT Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_4
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.date_left , Students.time_left asc LIMIT 1	student_transcripts_tracking_4
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.date_left , Students.time_left asc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time , Transcripts.other_details FROM Transcripts ORDER BY Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time asc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time , Transcripts.other_details FROM Transcripts ORDER BY Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time asc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time FROM Transcripts ORDER BY Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time desc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time FROM Transcripts ORDER BY Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time desc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.transcript_year , Transcripts.transcript_month , Transcripts.transcript_day , Transcripts.transcript_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_4
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_0
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_0
SELECT count(*) FROM Cartoon WHERE Cartoon.writer_firstname = "Joseph" and Cartoon.writer_lastname = "Kuhr"	tvshow_0
SELECT count(*) FROM Cartoon WHERE Cartoon.writer_firstname = "Joseph" and Cartoon.writer_lastname = "Kuhr"	tvshow_0
SELECT Cartoon.Title , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year asc	tvshow_0
SELECT Cartoon.Title , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year asc	tvshow_0
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones" or Cartoon.director_firstname = "Brandon" and Cartoon.director_lastname = "Vietti"	tvshow_0
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones" or Cartoon.director_firstname = "Brandon" and Cartoon.director_lastname = "Vietti"	tvshow_0
SELECT TV_series.air_month , TV_series.air_day , TV_series.air_year FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_0
SELECT TV_series.air_month , TV_series.air_day , TV_series.air_year FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_0
SELECT count(*) , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon GROUP BY Cartoon.director_firstname , Cartoon.director_lastname	tvshow_0
SELECT count(*) , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon GROUP BY Cartoon.director_firstname , Cartoon.director_lastname	tvshow_0
SELECT Cartoon.Production_code , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year desc LIMIT 1	tvshow_0
SELECT Cartoon.Production_code , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year desc LIMIT 1	tvshow_0
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer_firstname = "Todd" and Cartoon.writer_lastname = "Casey"	tvshow_0
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer_firstname = "Todd" and Cartoon.writer_lastname = "Casey"	tvshow_0
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer_firstname = "Todd" and Cartoon.writer_lastname = "Casey"	tvshow_0
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer_firstname = "Todd" and Cartoon.writer_lastname = "Casey"	tvshow_0
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Michael" and Cartoon.director_lastname = "Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_0
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Michael" and Cartoon.director_lastname = "Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_0
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_0
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_0
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones")	tvshow_0
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones")	tvshow_0
SELECT Cartoon.Title , Cartoon.Directed_by FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year asc	tvshow_1
SELECT Cartoon.Title , Cartoon.Directed_by FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year asc	tvshow_1
SELECT TV_series.air_month , TV_series.air_day , TV_series.air_year FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_1
SELECT TV_series.air_month , TV_series.air_day , TV_series.air_year FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_1
SELECT Cartoon.Production_code , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year desc LIMIT 1	tvshow_1
SELECT Cartoon.Production_code , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year desc LIMIT 1	tvshow_1
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_2
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_2
SELECT Cartoon.Title , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_2
SELECT Cartoon.Title , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_2
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones" or Cartoon.director_firstname = "Brandon" and Cartoon.director_lastname = "Vietti"	tvshow_2
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones" or Cartoon.director_firstname = "Brandon" and Cartoon.director_lastname = "Vietti"	tvshow_2
SELECT count(*) , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon GROUP BY Cartoon.director_firstname , Cartoon.director_lastname	tvshow_2
SELECT count(*) , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon GROUP BY Cartoon.director_firstname , Cartoon.director_lastname	tvshow_2
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Michael" and Cartoon.director_lastname = "Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_2
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Michael" and Cartoon.director_lastname = "Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_2
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_2
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_2
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones")	tvshow_2
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones")	tvshow_2
SELECT count(*) FROM Cartoon WHERE Cartoon.writer_firstname = "Joseph" and Cartoon.writer_lastname = "Kuhr"	tvshow_4
SELECT count(*) FROM Cartoon WHERE Cartoon.writer_firstname = "Joseph" and Cartoon.writer_lastname = "Kuhr"	tvshow_4
SELECT TV_series.air_month , TV_series.air_day , TV_series.air_year FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_4
SELECT TV_series.air_month , TV_series.air_day , TV_series.air_year FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_4
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer_firstname = "Todd" and Cartoon.writer_lastname = "Casey"	tvshow_4
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer_firstname = "Todd" and Cartoon.writer_lastname = "Casey"	tvshow_4
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer_firstname = "Todd" and Cartoon.writer_lastname = "Casey"	tvshow_4
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer_firstname = "Todd" and Cartoon.writer_lastname = "Casey"	tvshow_4
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_5
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_5
SELECT Cartoon.Title , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year asc	tvshow_5
SELECT Cartoon.Title , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year asc	tvshow_5
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones" or Cartoon.director_firstname = "Brandon" and Cartoon.director_lastname = "Vietti"	tvshow_5
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones" or Cartoon.director_firstname = "Brandon" and Cartoon.director_lastname = "Vietti"	tvshow_5
SELECT TV_series.air_month , TV_series.air_day , TV_series.air_year FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_5
SELECT TV_series.air_month , TV_series.air_day , TV_series.air_year FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_5
SELECT count(*) , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon GROUP BY Cartoon.director_firstname , Cartoon.director_lastname	tvshow_5
SELECT count(*) , Cartoon.director_firstname , Cartoon.director_lastname FROM Cartoon GROUP BY Cartoon.director_firstname , Cartoon.director_lastname	tvshow_5
SELECT Cartoon.Production_code , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year desc LIMIT 1	tvshow_5
SELECT Cartoon.Production_code , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.air_month , Cartoon.air_day , Cartoon.air_year desc LIMIT 1	tvshow_5
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Michael" and Cartoon.director_lastname = "Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_5
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Michael" and Cartoon.director_lastname = "Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_5
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_5
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones"	tvshow_5
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones")	tvshow_5
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director_firstname = "Ben" and Cartoon.director_lastname = "Jones")	tvshow_5
SELECT people.first_name , people.last_name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID	poker_player_0
SELECT people.first_name , people.last_name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID	poker_player_0
SELECT people.first_name , people.last_name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE poker_player.Earnings > 300000	poker_player_0
SELECT people.first_name , people.last_name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE poker_player.Earnings > 300000	poker_player_0
SELECT people.first_name , people.last_name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.Final_Table_Made asc	poker_player_0
SELECT people.first_name , people.last_name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.Final_Table_Made asc	poker_player_0
SELECT people.first_name , people.last_name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.Earnings desc	poker_player_0
SELECT people.first_name , people.last_name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.Earnings desc	poker_player_0
SELECT people.first_name , people.last_name , people.Birth_Date FROM people ORDER BY people.first_name , people.last_name asc	poker_player_0
SELECT people.first_name , people.last_name , people.Birth_Date FROM people ORDER BY people.first_name , people.last_name asc	poker_player_0
SELECT people.first_name , people.last_name FROM people WHERE people.Nationality != "Russia"	poker_player_0
SELECT people.first_name , people.last_name FROM people WHERE people.Nationality != "Russia"	poker_player_0
SELECT people.first_name , people.last_name FROM people WHERE people.People_ID NOT in (SELECT poker_player.People_ID FROM poker_player)	poker_player_0
SELECT people.first_name , people.last_name FROM people WHERE people.People_ID NOT in (SELECT poker_player.People_ID FROM poker_player)	poker_player_0
SELECT CONTESTANTS.contestant_number , CONTESTANTS.first_name , CONTESTANTS.last_name FROM CONTESTANTS ORDER BY CONTESTANTS.first_name , CONTESTANTS.last_name desc	voter_1_0
SELECT CONTESTANTS.first_name , CONTESTANTS.last_name FROM CONTESTANTS WHERE CONTESTANTS.first_name != "Jessie" and CONTESTANTS.last_name != "Alloway"	voter_1_0
SELECT DISTINCT VOTES.state , VOTES.created_year , VOTES.created_month , VOTES.created_day , VOTES.created_time FROM VOTES	voter_1_0
SELECT CONTESTANTS.contestant_number , CONTESTANTS.first_name , CONTESTANTS.last_name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number HAVING count(*) >= 2	voter_1_0
SELECT CONTESTANTS.contestant_number , CONTESTANTS.first_name , CONTESTANTS.last_name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number ORDER BY count(*) asc LIMIT 1	voter_1_0
SELECT VOTES.created_year , VOTES.created_month , VOTES.created_day , VOTES.created_time , VOTES.state , VOTES.phone_number FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number WHERE CONTESTANTS.first_name = "Tabatha" and CONTESTANTS.last_name = "Gehling"	voter_1_0
SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.first_name = "Tabatha" and CONTESTANTS.last_name = "Gehling" INTERSECT SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.first_name = "Kelly" and CONTESTANTS.last_name = "Clauss"	voter_1_0
SELECT DISTINCT VOTES.state , VOTES.created_year , VOTES.created_month , VOTES.created_day , VOTES.created_time FROM VOTES	voter_1_1
SELECT VOTES.created_year , VOTES.created_month , VOTES.created_day , VOTES.created_time , VOTES.state , VOTES.phone_number FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number WHERE CONTESTANTS.contestant_name = "Tabatha Gehling"	voter_1_1
SELECT DISTINCT VOTES.state , VOTES.created_date , VOTES.created_time FROM VOTES	voter_1_4
SELECT VOTES.created_date , VOTES.created_time , VOTES.state , VOTES.phone_number FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number WHERE CONTESTANTS.contestant_name = "Tabatha Gehling"	voter_1_4
SELECT CONTESTANTS.contestant_number , CONTESTANTS.first_name , CONTESTANTS.last_name FROM CONTESTANTS ORDER BY CONTESTANTS.first_name , CONTESTANTS.last_name desc	voter_1_7
SELECT CONTESTANTS.first_name , CONTESTANTS.last_name FROM CONTESTANTS WHERE CONTESTANTS.first_name != "Jessie" and CONTESTANTS.last_name != "Alloway"	voter_1_7
SELECT DISTINCT VOTES.state , VOTES.created_date , VOTES.created_time FROM VOTES	voter_1_7
SELECT CONTESTANTS.contestant_number , CONTESTANTS.first_name , CONTESTANTS.last_name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number HAVING count(*) >= 2	voter_1_7
SELECT CONTESTANTS.contestant_number , CONTESTANTS.first_name , CONTESTANTS.last_name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number ORDER BY count(*) asc LIMIT 1	voter_1_7
SELECT VOTES.created_date , VOTES.created_time , VOTES.state , VOTES.phone_number FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number WHERE CONTESTANTS.first_name = "Tabatha" and CONTESTANTS.last_name = "Gehling"	voter_1_7
SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.first_name = "Tabatha" and CONTESTANTS.last_name = "Gehling" INTERSECT SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.first_name = "Kelly" and CONTESTANTS.last_name = "Clauss"	voter_1_7
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.birthyear desc	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.birthyear desc	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor WHERE conductor.Nationality != "USA"	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor WHERE conductor.Nationality != "USA"	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.year_start_to_work asc	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.year_start_to_work asc	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.year_start_to_work asc LIMIT 1	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.year_start_to_work asc LIMIT 1	orchestra_0
SELECT conductor.first_name , conductor.last_name , orchestra.Orchestra FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID	orchestra_0
SELECT conductor.first_name , conductor.last_name , orchestra.Orchestra FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID HAVING count(*) > 1	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID HAVING count(*) > 1	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID ORDER BY count(*) desc LIMIT 1	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID ORDER BY count(*) desc LIMIT 1	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID WHERE orchestra.Year_of_Founded > 2008	orchestra_0
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID WHERE orchestra.Year_of_Founded > 2008	orchestra_0
SELECT orchestra.Record_Company FROM orchestra ORDER BY orchestra.year_of_existence asc	orchestra_1
SELECT orchestra.Record_Company FROM orchestra ORDER BY orchestra.year_of_existence asc	orchestra_1
SELECT conductor.Name FROM conductor ORDER BY conductor.year_start_to_work asc	orchestra_1
SELECT conductor.Name FROM conductor ORDER BY conductor.year_start_to_work asc	orchestra_1
SELECT conductor.Name FROM conductor ORDER BY conductor.year_start_to_work asc LIMIT 1	orchestra_1
SELECT conductor.Name FROM conductor ORDER BY conductor.year_start_to_work asc LIMIT 1	orchestra_1
SELECT conductor.Name FROM conductor ORDER BY conductor.year_start_to_work asc	orchestra_2
SELECT conductor.Name FROM conductor ORDER BY conductor.year_start_to_work asc	orchestra_2
SELECT conductor.Name FROM conductor ORDER BY conductor.year_start_to_work asc LIMIT 1	orchestra_2
SELECT conductor.Name FROM conductor ORDER BY conductor.year_start_to_work asc LIMIT 1	orchestra_2
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.Age asc	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.Age asc	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor WHERE conductor.Nationality != "USA"	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor WHERE conductor.Nationality != "USA"	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.year_start_to_work asc	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.year_start_to_work asc	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.year_start_to_work asc LIMIT 1	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor ORDER BY conductor.year_start_to_work asc LIMIT 1	orchestra_3
SELECT conductor.first_name , conductor.last_name , orchestra.Orchestra FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID	orchestra_3
SELECT conductor.first_name , conductor.last_name , orchestra.Orchestra FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID HAVING count(*) > 1	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID HAVING count(*) > 1	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID ORDER BY count(*) desc LIMIT 1	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID ORDER BY count(*) desc LIMIT 1	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID WHERE orchestra.Year_of_Founded > 2008	orchestra_3
SELECT conductor.first_name , conductor.last_name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID WHERE orchestra.Year_of_Founded > 2008	orchestra_3
SELECT orchestra.Record_Company FROM orchestra ORDER BY orchestra.year_of_existence asc	orchestra_4
SELECT orchestra.Record_Company FROM orchestra ORDER BY orchestra.year_of_existence asc	orchestra_4
SELECT Treatments.date_of_treatment , Treatments.time_of_treatment , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_0
SELECT Treatments.date_of_treatment , Treatments.time_of_treatment , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_0
SELECT Dogs.name , Treatments.date_of_treatment , Treatments.time_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_0
SELECT Dogs.name , Treatments.date_of_treatment , Treatments.time_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_0
SELECT DISTINCT Dogs.year_arrived , Dogs.month_arrived , Dogs.day_arrived , Dogs.time_arrived , Dogs.date_departed , Dogs.time_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_0
SELECT DISTINCT Dogs.year_arrived , Dogs.month_arrived , Dogs.day_arrived , Dogs.time_arrived , Dogs.date_departed , Dogs.time_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_0
SELECT Dogs.year_arrived , Dogs.month_arrived , Dogs.day_arrived , Dogs.time_arrived , Dogs.date_departed , Dogs.time_departed FROM Dogs	dog_kennels_0
SELECT Dogs.year_arrived , Dogs.month_arrived , Dogs.day_arrived , Dogs.time_arrived , Dogs.date_departed , Dogs.time_departed FROM Dogs	dog_kennels_0
SELECT Treatments.cost_of_treatment FROM Treatments ORDER BY Treatments.date_of_treatment , Treatments.time_of_treatment desc LIMIT 1	dog_kennels_0
SELECT Treatments.cost_of_treatment FROM Treatments ORDER BY Treatments.date_of_treatment , Treatments.time_of_treatment desc LIMIT 1	dog_kennels_0
SELECT Treatments.year_of_treatment , Treatments.month_of_treatment , Treatments.day_of_treatment , Treatments.time_of_treatment , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_1
SELECT Treatments.year_of_treatment , Treatments.month_of_treatment , Treatments.day_of_treatment , Treatments.time_of_treatment , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_1
SELECT Dogs.name , Treatments.year_of_treatment , Treatments.month_of_treatment , Treatments.day_of_treatment , Treatments.time_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_1
SELECT Dogs.name , Treatments.year_of_treatment , Treatments.month_of_treatment , Treatments.day_of_treatment , Treatments.time_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_1
SELECT DISTINCT Dogs.date_arrived , Dogs.time_arrived , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_1
SELECT DISTINCT Dogs.date_arrived , Dogs.time_arrived , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_1
SELECT Dogs.date_arrived , Dogs.time_arrived , Dogs.date_departed FROM Dogs	dog_kennels_1
SELECT Dogs.date_arrived , Dogs.time_arrived , Dogs.date_departed FROM Dogs	dog_kennels_1
SELECT Treatments.cost_of_treatment FROM Treatments ORDER BY Treatments.year_of_treatment , Treatments.month_of_treatment , Treatments.day_of_treatment , Treatments.time_of_treatment desc LIMIT 1	dog_kennels_1
SELECT Treatments.cost_of_treatment FROM Treatments ORDER BY Treatments.year_of_treatment , Treatments.month_of_treatment , Treatments.day_of_treatment , Treatments.time_of_treatment desc LIMIT 1	dog_kennels_1
SELECT DISTINCT Dogs.year_arrived , Dogs.month_arrived , Dogs.day_arrived , Dogs.time_arrived , Dogs.date_departed , Dogs.time_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_4
SELECT DISTINCT Dogs.year_arrived , Dogs.month_arrived , Dogs.day_arrived , Dogs.time_arrived , Dogs.date_departed , Dogs.time_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_4
SELECT Dogs.year_arrived , Dogs.month_arrived , Dogs.day_arrived , Dogs.time_arrived , Dogs.date_departed , Dogs.time_departed FROM Dogs	dog_kennels_4
SELECT Dogs.year_arrived , Dogs.month_arrived , Dogs.day_arrived , Dogs.time_arrived , Dogs.date_departed , Dogs.time_departed FROM Dogs	dog_kennels_4
SELECT Treatments.date_of_treatment , Treatments.time_of_treatment , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_5
SELECT Treatments.date_of_treatment , Treatments.time_of_treatment , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_5
SELECT Dogs.name , Treatments.date_of_treatment , Treatments.time_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_5
SELECT Dogs.name , Treatments.date_of_treatment , Treatments.time_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_5
SELECT DISTINCT Dogs.date_arrived , Dogs.time_arrived , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_5
SELECT DISTINCT Dogs.date_arrived , Dogs.time_arrived , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_5
SELECT Dogs.date_arrived , Dogs.time_arrived , Dogs.date_departed FROM Dogs	dog_kennels_5
SELECT Dogs.date_arrived , Dogs.time_arrived , Dogs.date_departed FROM Dogs	dog_kennels_5
SELECT Treatments.cost_of_treatment FROM Treatments ORDER BY Treatments.date_of_treatment , Treatments.time_of_treatment desc LIMIT 1	dog_kennels_5
SELECT Treatments.cost_of_treatment FROM Treatments ORDER BY Treatments.date_of_treatment , Treatments.time_of_treatment desc LIMIT 1	dog_kennels_5
SELECT singer.first_name , singer.last_name FROM singer ORDER BY singer.Net_Worth_Millions asc	singer_0
SELECT singer.first_name , singer.last_name FROM singer ORDER BY singer.Net_Worth_Millions asc	singer_0
SELECT singer.first_name , singer.last_name FROM singer WHERE singer.Citizenship != "France"	singer_0
SELECT singer.first_name , singer.last_name FROM singer WHERE singer.Citizenship != "France"	singer_0
SELECT singer.first_name , singer.last_name FROM singer ORDER BY singer.Net_Worth_Millions desc LIMIT 1	singer_0
SELECT singer.first_name , singer.last_name FROM singer ORDER BY singer.Net_Worth_Millions desc LIMIT 1	singer_0
SELECT song.Title , singer.first_name , singer.last_name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID	singer_0
SELECT song.Title , singer.first_name , singer.last_name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID	singer_0
SELECT DISTINCT singer.first_name , singer.last_name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID WHERE song.Sales > 300000	singer_0
SELECT DISTINCT singer.first_name , singer.last_name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID WHERE song.Sales > 300000	singer_0
SELECT singer.first_name , singer.last_name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.first_name , singer.last_name HAVING count(*) > 1	singer_0
SELECT singer.first_name , singer.last_name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.first_name , singer.last_name HAVING count(*) > 1	singer_0
SELECT singer.first_name , singer.last_name , sum(song.Sales) FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.first_name , singer.last_name	singer_0
SELECT singer.first_name , singer.last_name , sum(song.Sales) FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.first_name , singer.last_name	singer_0
SELECT singer.first_name , singer.last_name FROM singer WHERE singer.Singer_ID NOT in (SELECT song.Singer_ID FROM song)	singer_0
SELECT singer.first_name , singer.last_name FROM singer WHERE singer.Singer_ID NOT in (SELECT song.Singer_ID FROM song)	singer_0
