SELECT singer.Name , singer.nation , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_0
SELECT singer.Name , singer.nation , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_0
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.nation = "France"	concert_singer_0
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.nation = "France"	concert_singer_0
SELECT singer.tune_name , singer.tune_release_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_0
SELECT singer.tune_name , singer.tune_release_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_0
SELECT DISTINCT singer.nation FROM singer WHERE singer.Age > 20	concert_singer_0
SELECT DISTINCT singer.nation FROM singer WHERE singer.Age > 20	concert_singer_0
SELECT singer.nation , count(*) FROM singer GROUP BY singer.nation	concert_singer_0
SELECT singer.nation , count(*) FROM singer GROUP BY singer.nation	concert_singer_0
SELECT singer.tune_name FROM singer WHERE singer.Age > (SELECT avg(singer.Age) FROM singer)	concert_singer_0
SELECT singer.tune_name FROM singer WHERE singer.Age > (SELECT avg(singer.Age) FROM singer)	concert_singer_0
SELECT stadium.position , stadium.Name FROM stadium WHERE stadium.max_carrying_number BETWEEN 5000 AND 10000	concert_singer_0
SELECT stadium.position , stadium.Name FROM stadium WHERE stadium.max_carrying_number BETWEEN 5000 AND 10000	concert_singer_0
SELECT max(stadium.max_carrying_number) , stadium.mean FROM stadium	concert_singer_0
SELECT avg(stadium.max_carrying_number) , max(stadium.max_carrying_number) FROM stadium	concert_singer_0
SELECT stadium.Name , stadium.max_carrying_number FROM stadium ORDER BY stadium.mean desc LIMIT 1	concert_singer_0
SELECT stadium.Name , stadium.max_carrying_number FROM stadium ORDER BY stadium.mean desc LIMIT 1	concert_singer_0
SELECT stadium.Name , stadium.max_carrying_number FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year >= 2014 GROUP BY stadium.Stadium_ID ORDER BY count(*) desc LIMIT 1	concert_singer_0
SELECT stadium.Name , stadium.max_carrying_number FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year > 2013 GROUP BY stadium.Stadium_ID ORDER BY count(*) desc LIMIT 1	concert_singer_0
SELECT singer.nation FROM singer WHERE singer.Age > 40 INTERSECT SELECT singer.nation FROM singer WHERE singer.Age < 30	concert_singer_0
SELECT concert.concert_Name , concert.style , count(*) FROM singer_in_concert JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID GROUP BY concert.concert_ID	concert_singer_0
SELECT concert.concert_Name , concert.style , count(*) FROM singer_in_concert JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID GROUP BY concert.concert_ID	concert_singer_0
SELECT singer.Name , singer.nation FROM singer WHERE singer.tune_name like "%Hey%"	concert_singer_0
SELECT singer.Name , singer.nation FROM singer WHERE singer.tune_name like "%Hey%"	concert_singer_0
SELECT stadium.Name , stadium.position FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.position FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2015	concert_singer_0
SELECT stadium.Name , stadium.position FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.position FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2015	concert_singer_0
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.Stadium_ID FROM stadium ORDER BY stadium.max_carrying_number desc LIMIT 1)	concert_singer_0
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.Stadium_ID FROM stadium ORDER BY stadium.max_carrying_number desc LIMIT 1)	concert_singer_0
SELECT singer.Name , singer.nation , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_1
SELECT singer.Name , singer.nation , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_1
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.nation = "France"	concert_singer_1
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.nation = "France"	concert_singer_1
SELECT DISTINCT singer.nation FROM singer WHERE singer.Age > 20	concert_singer_1
SELECT DISTINCT singer.nation FROM singer WHERE singer.Age > 20	concert_singer_1
SELECT singer.nation , count(*) FROM singer GROUP BY singer.nation	concert_singer_1
SELECT singer.nation , count(*) FROM singer GROUP BY singer.nation	concert_singer_1
SELECT stadium.Location , stadium.Name FROM stadium WHERE stadium.max_carrying_number BETWEEN 5000 AND 10000	concert_singer_1
SELECT stadium.Location , stadium.Name FROM stadium WHERE stadium.max_carrying_number BETWEEN 5000 AND 10000	concert_singer_1
SELECT max(stadium.max_carrying_number) , stadium.Average FROM stadium	concert_singer_1
SELECT avg(stadium.max_carrying_number) , max(stadium.max_carrying_number) FROM stadium	concert_singer_1
SELECT stadium.Name , stadium.max_carrying_number FROM stadium ORDER BY stadium.Average desc LIMIT 1	concert_singer_1
SELECT stadium.Name , stadium.max_carrying_number FROM stadium ORDER BY stadium.Average desc LIMIT 1	concert_singer_1
SELECT stadium.Name , stadium.max_carrying_number FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year >= 2014 GROUP BY stadium.Stadium_ID ORDER BY count(*) desc LIMIT 1	concert_singer_1
SELECT stadium.Name , stadium.max_carrying_number FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year > 2013 GROUP BY stadium.Stadium_ID ORDER BY count(*) desc LIMIT 1	concert_singer_1
SELECT singer.nation FROM singer WHERE singer.Age > 40 INTERSECT SELECT singer.nation FROM singer WHERE singer.Age < 30	concert_singer_1
SELECT concert.event_name , concert.Theme , count(*) FROM singer_in_concert JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID GROUP BY concert.concert_ID	concert_singer_1
SELECT concert.event_name , concert.Theme , count(*) FROM singer_in_concert JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID GROUP BY concert.concert_ID	concert_singer_1
SELECT singer.Name , singer.nation FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_1
SELECT singer.Name , singer.nation FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_1
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.Stadium_ID FROM stadium ORDER BY stadium.max_carrying_number desc LIMIT 1)	concert_singer_1
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.Stadium_ID FROM stadium ORDER BY stadium.max_carrying_number desc LIMIT 1)	concert_singer_1
SELECT singer.Song_Name , singer.publish_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_2
SELECT singer.Song_Name , singer.publish_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_2
SELECT singer.Song_Name , singer.air_date FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_3
SELECT singer.Song_Name , singer.air_date FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_3
SELECT stadium.whereabouts , stadium.Name FROM stadium WHERE stadium.Capacity BETWEEN 5000 AND 10000	concert_singer_3
SELECT stadium.whereabouts , stadium.Name FROM stadium WHERE stadium.Capacity BETWEEN 5000 AND 10000	concert_singer_3
SELECT max(stadium.Capacity) , stadium.mean FROM stadium	concert_singer_3
SELECT stadium.Name , stadium.Capacity FROM stadium ORDER BY stadium.mean desc LIMIT 1	concert_singer_3
SELECT stadium.Name , stadium.Capacity FROM stadium ORDER BY stadium.mean desc LIMIT 1	concert_singer_3
SELECT concert.concert_Name , concert.category , count(*) FROM singer_in_concert JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID GROUP BY concert.concert_ID	concert_singer_3
SELECT concert.concert_Name , concert.category , count(*) FROM singer_in_concert JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID GROUP BY concert.concert_ID	concert_singer_3
SELECT stadium.Name , stadium.whereabouts FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.whereabouts FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2015	concert_singer_3
SELECT stadium.Name , stadium.whereabouts FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.whereabouts FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2015	concert_singer_3
SELECT singer.tune_name , singer.air_time FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_4
SELECT singer.tune_name , singer.air_time FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_4
SELECT singer.tune_name FROM singer WHERE singer.Age > (SELECT avg(singer.Age) FROM singer)	concert_singer_4
SELECT singer.tune_name FROM singer WHERE singer.Age > (SELECT avg(singer.Age) FROM singer)	concert_singer_4
SELECT stadium.Location , stadium.Name FROM stadium WHERE stadium.stadium_capacity BETWEEN 5000 AND 10000	concert_singer_4
SELECT stadium.Location , stadium.Name FROM stadium WHERE stadium.stadium_capacity BETWEEN 5000 AND 10000	concert_singer_4
SELECT max(stadium.stadium_capacity) , stadium.Average FROM stadium	concert_singer_4
SELECT avg(stadium.stadium_capacity) , max(stadium.stadium_capacity) FROM stadium	concert_singer_4
SELECT stadium.Name , stadium.stadium_capacity FROM stadium ORDER BY stadium.Average desc LIMIT 1	concert_singer_4
SELECT stadium.Name , stadium.stadium_capacity FROM stadium ORDER BY stadium.Average desc LIMIT 1	concert_singer_4
SELECT stadium.Name , stadium.stadium_capacity FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year >= 2014 GROUP BY stadium.Stadium_ID ORDER BY count(*) desc LIMIT 1	concert_singer_4
SELECT stadium.Name , stadium.stadium_capacity FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year > 2013 GROUP BY stadium.Stadium_ID ORDER BY count(*) desc LIMIT 1	concert_singer_4
SELECT concert.show , concert.Theme , count(*) FROM singer_in_concert JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID GROUP BY concert.concert_ID	concert_singer_4
SELECT concert.show , concert.Theme , count(*) FROM singer_in_concert JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID GROUP BY concert.concert_ID	concert_singer_4
SELECT singer.Name , singer.Country FROM singer WHERE singer.tune_name like "%Hey%"	concert_singer_4
SELECT singer.Name , singer.Country FROM singer WHERE singer.tune_name like "%Hey%"	concert_singer_4
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.Stadium_ID FROM stadium ORDER BY stadium.stadium_capacity desc LIMIT 1)	concert_singer_4
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.Stadium_ID FROM stadium ORDER BY stadium.stadium_capacity desc LIMIT 1)	concert_singer_4
SELECT count(*) FROM Pets WHERE Pets.mass > 10	pets_1_0
SELECT count(*) FROM Pets WHERE Pets.mass > 10	pets_1_0
SELECT Pets.mass FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_0
SELECT Pets.mass FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_0
SELECT max(Pets.mass) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_0
SELECT max(Pets.mass) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_0
SELECT count(*) FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID WHERE Student.Age > 20	pets_1_0
SELECT count(*) FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID WHERE Student.Age > 20	pets_1_0
SELECT count(*) FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.sexuality = "F" and Pets.pet_class = "dog"	pets_1_0
SELECT count(*) FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.sexuality = "F" and Pets.pet_class = "dog"	pets_1_0
SELECT count(DISTINCT Pets.pet_class) FROM Pets	pets_1_0
SELECT count(DISTINCT Pets.pet_class) FROM Pets	pets_1_0
SELECT DISTINCT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat" or Pets.pet_class = "dog"	pets_1_0
SELECT DISTINCT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat" or Pets.pet_class = "dog"	pets_1_0
SELECT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat" INTERSECT SELECT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "dog"	pets_1_0
SELECT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat" INTERSECT SELECT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "dog"	pets_1_0
SELECT Student.program , Student.Age FROM Student WHERE Student.information NOT in (SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat")	pets_1_0
SELECT Student.program , Student.Age FROM Student WHERE Student.information NOT in (SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat")	pets_1_0
SELECT Student.information FROM Student EXCEPT SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat"	pets_1_0
SELECT Student.information FROM Student EXCEPT SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat"	pets_1_0
SELECT Student.forename , Student.Age FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "dog" and Student.information NOT in (SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat")	pets_1_0
SELECT Student.forename , Student.Age FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "dog" and Student.information NOT in (SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat")	pets_1_0
SELECT Pets.pet_class , Pets.mass FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_0
SELECT Pets.pet_class , Pets.mass FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_0
SELECT Pets.PetID , Pets.mass FROM Pets WHERE Pets.pet_age > 1	pets_1_0
SELECT Pets.PetID , Pets.mass FROM Pets WHERE Pets.pet_age > 1	pets_1_0
SELECT avg(Pets.pet_age) , max(Pets.pet_age) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_0
SELECT avg(Pets.pet_age) , max(Pets.pet_age) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_0
SELECT avg(Pets.mass) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_0
SELECT avg(Pets.mass) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_0
SELECT DISTINCT Student.forename , Student.Age FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID	pets_1_0
SELECT DISTINCT Student.forename , Student.Age FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID	pets_1_0
SELECT Has_Pet.PetID FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID WHERE Student.ending_name = "Smith"	pets_1_0
SELECT Has_Pet.PetID FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID WHERE Student.ending_name = "Smith"	pets_1_0
SELECT count(*) , Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID GROUP BY Student.information	pets_1_0
SELECT count(*) , Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID GROUP BY Student.information	pets_1_0
SELECT Student.forename , Student.sexuality FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID GROUP BY Student.information HAVING count(*) > 1	pets_1_0
SELECT Student.forename , Student.sexuality FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID GROUP BY Student.information HAVING count(*) > 1	pets_1_0
SELECT Student.ending_name FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_age = 3 and Pets.pet_class = "cat"	pets_1_0
SELECT Student.ending_name FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_age = 3 and Pets.pet_class = "cat"	pets_1_0
SELECT avg(Student.Age) FROM Student WHERE Student.information NOT in (SELECT Has_Pet.StuID FROM Has_Pet)	pets_1_0
SELECT avg(Student.Age) FROM Student WHERE Student.information NOT in (SELECT Has_Pet.StuID FROM Has_Pet)	pets_1_0
SELECT Pets.weight FROM Pets ORDER BY Pets.how_old asc LIMIT 1	pets_1_1
SELECT Pets.weight FROM Pets ORDER BY Pets.how_old asc LIMIT 1	pets_1_1
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.gender = "F" and Pets.PetType = "dog"	pets_1_1
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.gender = "F" and Pets.PetType = "dog"	pets_1_1
SELECT Pets.PetType , Pets.weight FROM Pets ORDER BY Pets.how_old asc LIMIT 1	pets_1_1
SELECT Pets.PetType , Pets.weight FROM Pets ORDER BY Pets.how_old asc LIMIT 1	pets_1_1
SELECT Pets.PetID , Pets.weight FROM Pets WHERE Pets.how_old > 1	pets_1_1
SELECT Pets.PetID , Pets.weight FROM Pets WHERE Pets.how_old > 1	pets_1_1
SELECT avg(Pets.how_old) , max(Pets.how_old) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_1
SELECT avg(Pets.how_old) , max(Pets.how_old) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_1
SELECT Has_Pet.PetID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID WHERE Student.ending_name = "Smith"	pets_1_1
SELECT Has_Pet.PetID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID WHERE Student.ending_name = "Smith"	pets_1_1
SELECT Student.Fname , Student.gender FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID GROUP BY Student.StuID HAVING count(*) > 1	pets_1_1
SELECT Student.Fname , Student.gender FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID GROUP BY Student.StuID HAVING count(*) > 1	pets_1_1
SELECT Student.ending_name FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.how_old = 3 and Pets.PetType = "cat"	pets_1_1
SELECT Student.ending_name FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.how_old = 3 and Pets.PetType = "cat"	pets_1_1
SELECT max(Pets.weight) , Pets.type_of_animal FROM Pets GROUP BY Pets.type_of_animal	pets_1_2
SELECT max(Pets.weight) , Pets.type_of_animal FROM Pets GROUP BY Pets.type_of_animal	pets_1_2
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.Sex = "F" and Pets.type_of_animal = "dog"	pets_1_2
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.Sex = "F" and Pets.type_of_animal = "dog"	pets_1_2
SELECT count(DISTINCT Pets.type_of_animal) FROM Pets	pets_1_2
SELECT count(DISTINCT Pets.type_of_animal) FROM Pets	pets_1_2
SELECT DISTINCT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat" or Pets.type_of_animal = "dog"	pets_1_2
SELECT DISTINCT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat" or Pets.type_of_animal = "dog"	pets_1_2
SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat" INTERSECT SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "dog"	pets_1_2
SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat" INTERSECT SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "dog"	pets_1_2
SELECT Student.Major , Student.Age FROM Student WHERE Student.StuID NOT in (SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat")	pets_1_2
SELECT Student.Major , Student.Age FROM Student WHERE Student.StuID NOT in (SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat")	pets_1_2
SELECT Student.StuID FROM Student EXCEPT SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat"	pets_1_2
SELECT Student.StuID FROM Student EXCEPT SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat"	pets_1_2
SELECT Student.Fname , Student.Age FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "dog" and Student.StuID NOT in (SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat")	pets_1_2
SELECT Student.Fname , Student.Age FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "dog" and Student.StuID NOT in (SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.type_of_animal = "cat")	pets_1_2
SELECT Pets.type_of_animal , Pets.weight FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_2
SELECT Pets.type_of_animal , Pets.weight FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_2
SELECT avg(Pets.pet_age) , max(Pets.pet_age) , Pets.type_of_animal FROM Pets GROUP BY Pets.type_of_animal	pets_1_2
SELECT avg(Pets.pet_age) , max(Pets.pet_age) , Pets.type_of_animal FROM Pets GROUP BY Pets.type_of_animal	pets_1_2
SELECT avg(Pets.weight) , Pets.type_of_animal FROM Pets GROUP BY Pets.type_of_animal	pets_1_2
SELECT avg(Pets.weight) , Pets.type_of_animal FROM Pets GROUP BY Pets.type_of_animal	pets_1_2
SELECT Student.LName FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_age = 3 and Pets.type_of_animal = "cat"	pets_1_2
SELECT Student.LName FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_age = 3 and Pets.type_of_animal = "cat"	pets_1_2
SELECT count(*) FROM Pets WHERE Pets.heaviness > 10	pets_1_3
SELECT count(*) FROM Pets WHERE Pets.heaviness > 10	pets_1_3
SELECT Pets.heaviness FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_3
SELECT Pets.heaviness FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_3
SELECT max(Pets.heaviness) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_3
SELECT max(Pets.heaviness) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_3
SELECT count(*) FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID WHERE Student.Age > 20	pets_1_3
SELECT count(*) FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID WHERE Student.Age > 20	pets_1_3
SELECT count(*) FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.Sex = "F" and Pets.pet_class = "dog"	pets_1_3
SELECT count(*) FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.Sex = "F" and Pets.pet_class = "dog"	pets_1_3
SELECT count(DISTINCT Pets.pet_class) FROM Pets	pets_1_3
SELECT count(DISTINCT Pets.pet_class) FROM Pets	pets_1_3
SELECT DISTINCT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat" or Pets.pet_class = "dog"	pets_1_3
SELECT DISTINCT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat" or Pets.pet_class = "dog"	pets_1_3
SELECT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat" INTERSECT SELECT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "dog"	pets_1_3
SELECT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat" INTERSECT SELECT Student.forename FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "dog"	pets_1_3
SELECT Student.Major , Student.Age FROM Student WHERE Student.information NOT in (SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat")	pets_1_3
SELECT Student.Major , Student.Age FROM Student WHERE Student.information NOT in (SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat")	pets_1_3
SELECT Student.information FROM Student EXCEPT SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat"	pets_1_3
SELECT Student.information FROM Student EXCEPT SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat"	pets_1_3
SELECT Student.forename , Student.Age FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "dog" and Student.information NOT in (SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat")	pets_1_3
SELECT Student.forename , Student.Age FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "dog" and Student.information NOT in (SELECT Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_class = "cat")	pets_1_3
SELECT Pets.pet_class , Pets.heaviness FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_3
SELECT Pets.pet_class , Pets.heaviness FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_3
SELECT Pets.PetID , Pets.heaviness FROM Pets WHERE Pets.pet_age > 1	pets_1_3
SELECT Pets.PetID , Pets.heaviness FROM Pets WHERE Pets.pet_age > 1	pets_1_3
SELECT avg(Pets.pet_age) , max(Pets.pet_age) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_3
SELECT avg(Pets.pet_age) , max(Pets.pet_age) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_3
SELECT avg(Pets.heaviness) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_3
SELECT avg(Pets.heaviness) , Pets.pet_class FROM Pets GROUP BY Pets.pet_class	pets_1_3
SELECT DISTINCT Student.forename , Student.Age FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID	pets_1_3
SELECT DISTINCT Student.forename , Student.Age FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID	pets_1_3
SELECT Has_Pet.PetID FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID WHERE Student.LName = "Smith"	pets_1_3
SELECT Has_Pet.PetID FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID WHERE Student.LName = "Smith"	pets_1_3
SELECT count(*) , Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID GROUP BY Student.information	pets_1_3
SELECT count(*) , Student.information FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID GROUP BY Student.information	pets_1_3
SELECT Student.forename , Student.Sex FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID GROUP BY Student.information HAVING count(*) > 1	pets_1_3
SELECT Student.forename , Student.Sex FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID GROUP BY Student.information HAVING count(*) > 1	pets_1_3
SELECT Student.LName FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_age = 3 and Pets.pet_class = "cat"	pets_1_3
SELECT Student.LName FROM Student JOIN Has_Pet ON Student.information = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.pet_age = 3 and Pets.pet_class = "cat"	pets_1_3
SELECT avg(Student.Age) FROM Student WHERE Student.information NOT in (SELECT Has_Pet.StuID FROM Has_Pet)	pets_1_3
SELECT avg(Student.Age) FROM Student WHERE Student.information NOT in (SELECT Has_Pet.StuID FROM Has_Pet)	pets_1_3
SELECT Pets.weight FROM Pets ORDER BY Pets.how_old asc LIMIT 1	pets_1_4
SELECT Pets.weight FROM Pets ORDER BY Pets.how_old asc LIMIT 1	pets_1_4
SELECT max(Pets.weight) , Pets.animal_category FROM Pets GROUP BY Pets.animal_category	pets_1_4
SELECT max(Pets.weight) , Pets.animal_category FROM Pets GROUP BY Pets.animal_category	pets_1_4
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.Sex = "F" and Pets.animal_category = "dog"	pets_1_4
SELECT count(*) FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE Student.Sex = "F" and Pets.animal_category = "dog"	pets_1_4
SELECT count(DISTINCT Pets.animal_category) FROM Pets	pets_1_4
SELECT count(DISTINCT Pets.animal_category) FROM Pets	pets_1_4
SELECT DISTINCT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat" or Pets.animal_category = "dog"	pets_1_4
SELECT DISTINCT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat" or Pets.animal_category = "dog"	pets_1_4
SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat" INTERSECT SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "dog"	pets_1_4
SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat" INTERSECT SELECT Student.Fname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "dog"	pets_1_4
SELECT Student.program , Student.Age FROM Student WHERE Student.StuID NOT in (SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat")	pets_1_4
SELECT Student.program , Student.Age FROM Student WHERE Student.StuID NOT in (SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat")	pets_1_4
SELECT Student.StuID FROM Student EXCEPT SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat"	pets_1_4
SELECT Student.StuID FROM Student EXCEPT SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat"	pets_1_4
SELECT Student.Fname , Student.Age FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "dog" and Student.StuID NOT in (SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat")	pets_1_4
SELECT Student.Fname , Student.Age FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "dog" and Student.StuID NOT in (SELECT Student.StuID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.animal_category = "cat")	pets_1_4
SELECT Pets.animal_category , Pets.weight FROM Pets ORDER BY Pets.how_old asc LIMIT 1	pets_1_4
SELECT Pets.animal_category , Pets.weight FROM Pets ORDER BY Pets.how_old asc LIMIT 1	pets_1_4
SELECT Pets.PetID , Pets.weight FROM Pets WHERE Pets.how_old > 1	pets_1_4
SELECT Pets.PetID , Pets.weight FROM Pets WHERE Pets.how_old > 1	pets_1_4
SELECT avg(Pets.how_old) , max(Pets.how_old) , Pets.animal_category FROM Pets GROUP BY Pets.animal_category	pets_1_4
SELECT avg(Pets.how_old) , max(Pets.how_old) , Pets.animal_category FROM Pets GROUP BY Pets.animal_category	pets_1_4
SELECT avg(Pets.weight) , Pets.animal_category FROM Pets GROUP BY Pets.animal_category	pets_1_4
SELECT avg(Pets.weight) , Pets.animal_category FROM Pets GROUP BY Pets.animal_category	pets_1_4
SELECT Has_Pet.PetID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID WHERE Student.surname = "Smith"	pets_1_4
SELECT Has_Pet.PetID FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID WHERE Student.surname = "Smith"	pets_1_4
SELECT Student.surname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.how_old = 3 and Pets.animal_category = "cat"	pets_1_4
SELECT Student.surname FROM Student JOIN Has_Pet ON Student.StuID = Has_Pet.StuID JOIN Pets ON Pets.PetID = Has_Pet.PetID WHERE Pets.how_old = 3 and Pets.animal_category = "cat"	pets_1_4
SELECT continents.ContId , continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.mainland GROUP BY continents.ContId	car_1_0
SELECT continents.ContId , continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.mainland GROUP BY continents.ContId	car_1_0
SELECT car_makers.full_appellation , car_makers.Id , count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer GROUP BY car_makers.Id	car_1_0
SELECT car_makers.full_appellation , car_makers.Id , count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer GROUP BY car_makers.Id	car_1_0
SELECT car_names.mode FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.hp asc LIMIT 1	car_1_0
SELECT car_names.mode FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.hp asc LIMIT 1	car_1_0
SELECT car_names.mode FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.heaviness < (SELECT avg(cars_data.heaviness) FROM cars_data)	car_1_0
SELECT car_names.mode FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.heaviness < (SELECT avg(cars_data.heaviness) FROM cars_data)	car_1_0
SELECT DISTINCT car_makers.producer FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer JOIN car_names ON model_list.version = car_names.mode JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_0
SELECT DISTINCT car_makers.producer FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer JOIN car_names ON model_list.version = car_names.mode JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_0
SELECT car_names.manufacture , cars_data.Year FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Year = (SELECT min(cars_data.Year) FROM cars_data)	car_1_0
SELECT car_names.manufacture , cars_data.Year FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Year = (SELECT min(cars_data.Year) FROM cars_data)	car_1_0
SELECT DISTINCT model_list.version FROM model_list JOIN car_names ON model_list.version = car_names.mode JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_0
SELECT DISTINCT model_list.version FROM model_list JOIN car_names ON model_list.version = car_names.mode JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_0
SELECT continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.mainland JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY continents.Continent	car_1_0
SELECT continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.mainland JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY continents.Continent	car_1_0
SELECT countries.nation_designation FROM car_makers JOIN countries ON car_makers.nation = countries.CountryId GROUP BY car_makers.nation ORDER BY count(*) desc LIMIT 1	car_1_0
SELECT countries.nation_designation FROM car_makers JOIN countries ON car_makers.nation = countries.CountryId GROUP BY car_makers.nation ORDER BY count(*) desc LIMIT 1	car_1_0
SELECT count(*) , car_makers.full_appellation FROM model_list JOIN car_makers ON model_list.producer = car_makers.Id GROUP BY car_makers.Id	car_1_0
SELECT count(*) , car_makers.full_appellation , car_makers.Id FROM model_list JOIN car_makers ON model_list.producer = car_makers.Id GROUP BY car_makers.Id	car_1_0
SELECT cars_data.speed_up FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.manufacture = "amc hornet sportabout (sw)"	car_1_0
SELECT cars_data.speed_up FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.manufacture = "amc hornet sportabout (sw)"	car_1_0
SELECT count(*) FROM car_makers JOIN countries ON car_makers.nation = countries.CountryId WHERE countries.nation_designation = "france"	car_1_0
SELECT count(*) FROM car_makers JOIN countries ON car_makers.nation = countries.CountryId WHERE countries.nation_designation = "france"	car_1_0
SELECT count(*) FROM model_list JOIN car_makers ON model_list.producer = car_makers.Id JOIN countries ON car_makers.nation = countries.CountryId WHERE countries.nation_designation = "usa"	car_1_0
SELECT count(*) FROM model_list JOIN car_makers ON model_list.producer = car_makers.Id JOIN countries ON car_makers.nation = countries.CountryId WHERE countries.nation_designation = "usa"	car_1_0
SELECT avg(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.cylinder_number = 4	car_1_0
SELECT avg(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.cylinder_number = 4	car_1_0
SELECT min(cars_data.heaviness) FROM cars_data WHERE cars_data.cylinder_number = 8 and cars_data.Year = 1974	car_1_0
SELECT min(cars_data.heaviness) FROM cars_data WHERE cars_data.cylinder_number = 8 and cars_data.Year = 1974	car_1_0
SELECT model_list.producer , model_list.version FROM model_list	car_1_0
SELECT model_list.producer , model_list.version FROM model_list	car_1_0
SELECT countries.nation_designation , countries.CountryId FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) >= 1	car_1_0
SELECT countries.nation_designation , countries.CountryId FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) >= 1	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.hp > 150	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.hp > 150	car_1_0
SELECT avg(cars_data.heaviness) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_0
SELECT avg(cars_data.heaviness) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_0
SELECT countries.nation_designation FROM countries JOIN continents ON countries.mainland = continents.ContId JOIN car_makers ON countries.CountryId = car_makers.nation WHERE continents.Continent = "europe" GROUP BY countries.nation_designation HAVING count(*) >= 3	car_1_0
SELECT countries.nation_designation FROM countries JOIN continents ON countries.mainland = continents.ContId JOIN car_makers ON countries.CountryId = car_makers.nation WHERE continents.Continent = "europe" GROUP BY countries.nation_designation HAVING count(*) >= 3	car_1_0
SELECT cars_data.hp , car_names.manufacture FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 3 ORDER BY cars_data.hp desc LIMIT 1	car_1_0
SELECT cars_data.hp , car_names.manufacture FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 3 ORDER BY cars_data.hp desc LIMIT 1	car_1_0
SELECT car_names.mode FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.miles_per_gallon desc LIMIT 1	car_1_0
SELECT car_names.mode FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.miles_per_gallon desc LIMIT 1	car_1_0
SELECT avg(cars_data.hp) FROM cars_data WHERE cars_data.Year < 1980	car_1_0
SELECT avg(cars_data.hp) FROM cars_data WHERE cars_data.Year < 1980	car_1_0
SELECT avg(cars_data.Edispl) FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_names.mode = "volvo"	car_1_0
SELECT avg(cars_data.Edispl) FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_names.mode = "volvo"	car_1_0
SELECT max(cars_data.speed_up) , cars_data.cylinder_number FROM cars_data GROUP BY cars_data.cylinder_number	car_1_0
SELECT max(cars_data.speed_up) , cars_data.cylinder_number FROM cars_data GROUP BY cars_data.cylinder_number	car_1_0
SELECT car_names.mode FROM car_names GROUP BY car_names.mode ORDER BY count(*) desc LIMIT 1	car_1_0
SELECT car_names.mode FROM car_names GROUP BY car_names.mode ORDER BY count(*) desc LIMIT 1	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 4	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 4	car_1_0
SELECT count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer WHERE car_makers.full_appellation = "American Motor Company"	car_1_0
SELECT count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer WHERE car_makers.full_appellation = "American Motor Company"	car_1_0
SELECT car_makers.full_appellation , car_makers.Id FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer GROUP BY car_makers.Id HAVING count(*) > 3	car_1_0
SELECT car_makers.full_appellation , car_makers.Id FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer GROUP BY car_makers.Id HAVING count(*) > 3	car_1_0
SELECT DISTINCT model_list.version FROM car_names JOIN model_list ON car_names.mode = model_list.version JOIN car_makers ON model_list.producer = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.full_appellation = "General Motors" or cars_data.heaviness > 3500	car_1_0
SELECT DISTINCT model_list.version FROM car_names JOIN model_list ON car_names.mode = model_list.version JOIN car_makers ON model_list.producer = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.full_appellation = "General Motors" or cars_data.heaviness > 3500	car_1_0
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.heaviness BETWEEN 3000 AND 4000	car_1_0
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.heaviness BETWEEN 3000 AND 4000	car_1_0
SELECT cars_data.hp FROM cars_data ORDER BY cars_data.speed_up desc LIMIT 1	car_1_0
SELECT cars_data.hp FROM cars_data ORDER BY cars_data.speed_up desc LIMIT 1	car_1_0
SELECT cars_data.cylinder_number FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.mode = "volvo" ORDER BY cars_data.speed_up asc LIMIT 1	car_1_0
SELECT cars_data.cylinder_number FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.mode = "volvo" ORDER BY cars_data.speed_up asc LIMIT 1	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.speed_up > (SELECT cars_data.speed_up FROM cars_data ORDER BY cars_data.hp desc LIMIT 1)	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.speed_up > (SELECT cars_data.speed_up FROM cars_data ORDER BY cars_data.hp desc LIMIT 1)	car_1_0
SELECT count(*) FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) > 2	car_1_0
SELECT count(*) FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) > 2	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 6	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 6	car_1_0
SELECT car_names.mode FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 4 ORDER BY cars_data.hp desc LIMIT 1	car_1_0
SELECT car_names.mode FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 4 ORDER BY cars_data.hp desc LIMIT 1	car_1_0
SELECT car_names.MakeId , car_names.manufacture FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.hp > (SELECT min(cars_data.hp) FROM cars_data) and cars_data.cylinder_number <= 3	car_1_0
SELECT car_names.MakeId , car_names.manufacture FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.hp > (SELECT min(cars_data.hp) FROM cars_data) and cars_data.cylinder_number < 4	car_1_0
SELECT max(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.cylinder_number = 8 or cars_data.Year < 1980	car_1_0
SELECT max(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.cylinder_number = 8 or cars_data.Year < 1980	car_1_0
SELECT DISTINCT model_list.version FROM model_list JOIN car_names ON model_list.version = car_names.mode JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.producer = car_makers.Id WHERE cars_data.heaviness < 3500 and car_makers.full_appellation != "Ford Motor Company"	car_1_0
SELECT DISTINCT model_list.version FROM model_list JOIN car_names ON model_list.version = car_names.mode JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.producer = car_makers.Id WHERE cars_data.heaviness < 3500 and car_makers.full_appellation != "Ford Motor Company"	car_1_0
SELECT countries.nation_designation FROM countries EXCEPT SELECT countries.nation_designation FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation	car_1_0
SELECT countries.nation_designation FROM countries EXCEPT SELECT countries.nation_designation FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation	car_1_0
SELECT car_makers.Id , car_makers.producer FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.producer FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer JOIN car_names ON model_list.version = car_names.mode GROUP BY car_makers.Id HAVING count(*) > 3	car_1_0
SELECT car_makers.Id , car_makers.producer FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.producer FROM car_makers JOIN model_list ON car_makers.Id = model_list.producer JOIN car_names ON model_list.version = car_names.mode GROUP BY car_makers.Id HAVING count(*) > 3	car_1_0
SELECT countries.CountryId , countries.nation_designation FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.nation_designation FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation JOIN model_list ON car_makers.Id = model_list.producer WHERE model_list.version = "fiat"	car_1_0
SELECT countries.CountryId , countries.nation_designation FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.nation_designation FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation JOIN model_list ON car_makers.Id = model_list.producer WHERE model_list.version = "fiat"	car_1_0
SELECT countries.nation FROM car_makers JOIN countries ON car_makers.Country = countries.CountryId GROUP BY car_makers.Country ORDER BY count(*) desc LIMIT 1	car_1_1
SELECT countries.nation FROM car_makers JOIN countries ON car_makers.Country = countries.CountryId GROUP BY car_makers.Country ORDER BY count(*) desc LIMIT 1	car_1_1
SELECT cars_data.speed_up FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Make = "amc hornet sportabout (sw)"	car_1_1
SELECT cars_data.speed_up FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Make = "amc hornet sportabout (sw)"	car_1_1
SELECT count(*) FROM car_makers JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.nation = "france"	car_1_1
SELECT count(*) FROM car_makers JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.nation = "france"	car_1_1
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.nation = "usa"	car_1_1
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.nation = "usa"	car_1_1
SELECT avg(cars_data.MPG) FROM cars_data WHERE cars_data.cylinder_number = 4	car_1_1
SELECT avg(cars_data.MPG) FROM cars_data WHERE cars_data.cylinder_number = 4	car_1_1
SELECT min(cars_data.Weight) FROM cars_data WHERE cars_data.cylinder_number = 8 and cars_data.Year = 1974	car_1_1
SELECT min(cars_data.Weight) FROM cars_data WHERE cars_data.cylinder_number = 8 and cars_data.Year = 1974	car_1_1
SELECT countries.nation , countries.CountryId FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) >= 1	car_1_1
SELECT countries.nation , countries.CountryId FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) >= 1	car_1_1
SELECT countries.nation FROM countries JOIN continents ON countries.Continent = continents.ContId JOIN car_makers ON countries.CountryId = car_makers.Country WHERE continents.Continent = "europe" GROUP BY countries.nation HAVING count(*) >= 3	car_1_1
SELECT countries.nation FROM countries JOIN continents ON countries.Continent = continents.ContId JOIN car_makers ON countries.CountryId = car_makers.Country WHERE continents.Continent = "europe" GROUP BY countries.nation HAVING count(*) >= 3	car_1_1
SELECT cars_data.Horsepower , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 3 ORDER BY cars_data.Horsepower desc LIMIT 1	car_1_1
SELECT cars_data.Horsepower , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 3 ORDER BY cars_data.Horsepower desc LIMIT 1	car_1_1
SELECT max(cars_data.speed_up) , cars_data.cylinder_number FROM cars_data GROUP BY cars_data.cylinder_number	car_1_1
SELECT max(cars_data.speed_up) , cars_data.cylinder_number FROM cars_data GROUP BY cars_data.cylinder_number	car_1_1
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 4	car_1_1
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 4	car_1_1
SELECT cars_data.Horsepower FROM cars_data ORDER BY cars_data.speed_up desc LIMIT 1	car_1_1
SELECT cars_data.Horsepower FROM cars_data ORDER BY cars_data.speed_up desc LIMIT 1	car_1_1
SELECT cars_data.cylinder_number FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Model = "volvo" ORDER BY cars_data.speed_up asc LIMIT 1	car_1_1
SELECT cars_data.cylinder_number FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Model = "volvo" ORDER BY cars_data.speed_up asc LIMIT 1	car_1_1
SELECT count(*) FROM cars_data WHERE cars_data.speed_up > (SELECT cars_data.speed_up FROM cars_data ORDER BY cars_data.Horsepower desc LIMIT 1)	car_1_1
SELECT count(*) FROM cars_data WHERE cars_data.speed_up > (SELECT cars_data.speed_up FROM cars_data ORDER BY cars_data.Horsepower desc LIMIT 1)	car_1_1
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 6	car_1_1
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 6	car_1_1
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 4 ORDER BY cars_data.Horsepower desc LIMIT 1	car_1_1
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 4 ORDER BY cars_data.Horsepower desc LIMIT 1	car_1_1
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Horsepower > (SELECT min(cars_data.Horsepower) FROM cars_data) and cars_data.cylinder_number <= 3	car_1_1
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Horsepower > (SELECT min(cars_data.Horsepower) FROM cars_data) and cars_data.cylinder_number < 4	car_1_1
SELECT max(cars_data.MPG) FROM cars_data WHERE cars_data.cylinder_number = 8 or cars_data.Year < 1980	car_1_1
SELECT max(cars_data.MPG) FROM cars_data WHERE cars_data.cylinder_number = 8 or cars_data.Year < 1980	car_1_1
SELECT countries.nation FROM countries EXCEPT SELECT countries.nation FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country	car_1_1
SELECT countries.nation FROM countries EXCEPT SELECT countries.nation FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country	car_1_1
SELECT countries.CountryId , countries.nation FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.nation FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.Model = "fiat"	car_1_1
SELECT countries.CountryId , countries.nation FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.nation FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.Model = "fiat"	car_1_1
SELECT continents.ContId , continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.mainland GROUP BY continents.ContId	car_1_2
SELECT continents.ContId , continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.mainland GROUP BY continents.ContId	car_1_2
SELECT car_makers.complete_name , car_makers.Id , count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by GROUP BY car_makers.Id	car_1_2
SELECT car_makers.complete_name , car_makers.Id , count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by GROUP BY car_makers.Id	car_1_2
SELECT car_names.model_name FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.engine asc LIMIT 1	car_1_2
SELECT car_names.model_name FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.engine asc LIMIT 1	car_1_2
SELECT car_names.model_name FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.mass < (SELECT avg(cars_data.mass) FROM cars_data)	car_1_2
SELECT car_names.model_name FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.mass < (SELECT avg(cars_data.mass) FROM cars_data)	car_1_2
SELECT DISTINCT car_makers.creator FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by JOIN car_names ON model_list.mode = car_names.model_name JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_2
SELECT DISTINCT car_makers.creator FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by JOIN car_names ON model_list.mode = car_names.model_name JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_2
SELECT car_names.manufacture , cars_data.Year FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Year = (SELECT min(cars_data.Year) FROM cars_data)	car_1_2
SELECT car_names.manufacture , cars_data.Year FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Year = (SELECT min(cars_data.Year) FROM cars_data)	car_1_2
SELECT DISTINCT model_list.mode FROM model_list JOIN car_names ON model_list.mode = car_names.model_name JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_2
SELECT DISTINCT model_list.mode FROM model_list JOIN car_names ON model_list.mode = car_names.model_name JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_2
SELECT continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.mainland JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY continents.Continent	car_1_2
SELECT continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.mainland JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY continents.Continent	car_1_2
SELECT countries.state FROM car_makers JOIN countries ON car_makers.nation = countries.CountryId GROUP BY car_makers.nation ORDER BY count(*) desc LIMIT 1	car_1_2
SELECT countries.state FROM car_makers JOIN countries ON car_makers.nation = countries.CountryId GROUP BY car_makers.nation ORDER BY count(*) desc LIMIT 1	car_1_2
SELECT count(*) , car_makers.complete_name FROM model_list JOIN car_makers ON model_list.produced_by = car_makers.Id GROUP BY car_makers.Id	car_1_2
SELECT count(*) , car_makers.complete_name , car_makers.Id FROM model_list JOIN car_makers ON model_list.produced_by = car_makers.Id GROUP BY car_makers.Id	car_1_2
SELECT cars_data.speed_up FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.manufacture = "amc hornet sportabout (sw)"	car_1_2
SELECT cars_data.speed_up FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.manufacture = "amc hornet sportabout (sw)"	car_1_2
SELECT count(*) FROM car_makers JOIN countries ON car_makers.nation = countries.CountryId WHERE countries.state = "france"	car_1_2
SELECT count(*) FROM car_makers JOIN countries ON car_makers.nation = countries.CountryId WHERE countries.state = "france"	car_1_2
SELECT count(*) FROM model_list JOIN car_makers ON model_list.produced_by = car_makers.Id JOIN countries ON car_makers.nation = countries.CountryId WHERE countries.state = "usa"	car_1_2
SELECT count(*) FROM model_list JOIN car_makers ON model_list.produced_by = car_makers.Id JOIN countries ON car_makers.nation = countries.CountryId WHERE countries.state = "usa"	car_1_2
SELECT avg(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.number_cylinder = 4	car_1_2
SELECT avg(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.number_cylinder = 4	car_1_2
SELECT min(cars_data.mass) FROM cars_data WHERE cars_data.number_cylinder = 8 and cars_data.Year = 1974	car_1_2
SELECT min(cars_data.mass) FROM cars_data WHERE cars_data.number_cylinder = 8 and cars_data.Year = 1974	car_1_2
SELECT model_list.produced_by , model_list.mode FROM model_list	car_1_2
SELECT model_list.produced_by , model_list.mode FROM model_list	car_1_2
SELECT countries.state , countries.CountryId FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) >= 1	car_1_2
SELECT countries.state , countries.CountryId FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) >= 1	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.engine > 150	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.engine > 150	car_1_2
SELECT avg(cars_data.mass) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_2
SELECT avg(cars_data.mass) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_2
SELECT countries.state FROM countries JOIN continents ON countries.mainland = continents.ContId JOIN car_makers ON countries.CountryId = car_makers.nation WHERE continents.Continent = "europe" GROUP BY countries.state HAVING count(*) >= 3	car_1_2
SELECT countries.state FROM countries JOIN continents ON countries.mainland = continents.ContId JOIN car_makers ON countries.CountryId = car_makers.nation WHERE continents.Continent = "europe" GROUP BY countries.state HAVING count(*) >= 3	car_1_2
SELECT cars_data.engine , car_names.manufacture FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.number_cylinder = 3 ORDER BY cars_data.engine desc LIMIT 1	car_1_2
SELECT cars_data.engine , car_names.manufacture FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.number_cylinder = 3 ORDER BY cars_data.engine desc LIMIT 1	car_1_2
SELECT car_names.model_name FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.miles_per_gallon desc LIMIT 1	car_1_2
SELECT car_names.model_name FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.miles_per_gallon desc LIMIT 1	car_1_2
SELECT avg(cars_data.engine) FROM cars_data WHERE cars_data.Year < 1980	car_1_2
SELECT avg(cars_data.engine) FROM cars_data WHERE cars_data.Year < 1980	car_1_2
SELECT avg(cars_data.Edispl) FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_names.model_name = "volvo"	car_1_2
SELECT avg(cars_data.Edispl) FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_names.model_name = "volvo"	car_1_2
SELECT max(cars_data.speed_up) , cars_data.number_cylinder FROM cars_data GROUP BY cars_data.number_cylinder	car_1_2
SELECT max(cars_data.speed_up) , cars_data.number_cylinder FROM cars_data GROUP BY cars_data.number_cylinder	car_1_2
SELECT car_names.model_name FROM car_names GROUP BY car_names.model_name ORDER BY count(*) desc LIMIT 1	car_1_2
SELECT car_names.model_name FROM car_names GROUP BY car_names.model_name ORDER BY count(*) desc LIMIT 1	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.number_cylinder > 4	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.number_cylinder > 4	car_1_2
SELECT count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by WHERE car_makers.complete_name = "American Motor Company"	car_1_2
SELECT count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by WHERE car_makers.complete_name = "American Motor Company"	car_1_2
SELECT car_makers.complete_name , car_makers.Id FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by GROUP BY car_makers.Id HAVING count(*) > 3	car_1_2
SELECT car_makers.complete_name , car_makers.Id FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by GROUP BY car_makers.Id HAVING count(*) > 3	car_1_2
SELECT DISTINCT model_list.mode FROM car_names JOIN model_list ON car_names.model_name = model_list.mode JOIN car_makers ON model_list.produced_by = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.complete_name = "General Motors" or cars_data.mass > 3500	car_1_2
SELECT DISTINCT model_list.mode FROM car_names JOIN model_list ON car_names.model_name = model_list.mode JOIN car_makers ON model_list.produced_by = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.complete_name = "General Motors" or cars_data.mass > 3500	car_1_2
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.mass BETWEEN 3000 AND 4000	car_1_2
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.mass BETWEEN 3000 AND 4000	car_1_2
SELECT cars_data.engine FROM cars_data ORDER BY cars_data.speed_up desc LIMIT 1	car_1_2
SELECT cars_data.engine FROM cars_data ORDER BY cars_data.speed_up desc LIMIT 1	car_1_2
SELECT cars_data.number_cylinder FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.model_name = "volvo" ORDER BY cars_data.speed_up asc LIMIT 1	car_1_2
SELECT cars_data.number_cylinder FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.model_name = "volvo" ORDER BY cars_data.speed_up asc LIMIT 1	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.speed_up > (SELECT cars_data.speed_up FROM cars_data ORDER BY cars_data.engine desc LIMIT 1)	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.speed_up > (SELECT cars_data.speed_up FROM cars_data ORDER BY cars_data.engine desc LIMIT 1)	car_1_2
SELECT count(*) FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) > 2	car_1_2
SELECT count(*) FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) > 2	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.number_cylinder > 6	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.number_cylinder > 6	car_1_2
SELECT car_names.model_name FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.number_cylinder = 4 ORDER BY cars_data.engine desc LIMIT 1	car_1_2
SELECT car_names.model_name FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.number_cylinder = 4 ORDER BY cars_data.engine desc LIMIT 1	car_1_2
SELECT car_names.MakeId , car_names.manufacture FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.engine > (SELECT min(cars_data.engine) FROM cars_data) and cars_data.number_cylinder <= 3	car_1_2
SELECT car_names.MakeId , car_names.manufacture FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.engine > (SELECT min(cars_data.engine) FROM cars_data) and cars_data.number_cylinder < 4	car_1_2
SELECT max(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.number_cylinder = 8 or cars_data.Year < 1980	car_1_2
SELECT max(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.number_cylinder = 8 or cars_data.Year < 1980	car_1_2
SELECT DISTINCT model_list.mode FROM model_list JOIN car_names ON model_list.mode = car_names.model_name JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.produced_by = car_makers.Id WHERE cars_data.mass < 3500 and car_makers.complete_name != "Ford Motor Company"	car_1_2
SELECT DISTINCT model_list.mode FROM model_list JOIN car_names ON model_list.mode = car_names.model_name JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.produced_by = car_makers.Id WHERE cars_data.mass < 3500 and car_makers.complete_name != "Ford Motor Company"	car_1_2
SELECT countries.state FROM countries EXCEPT SELECT countries.state FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation	car_1_2
SELECT countries.state FROM countries EXCEPT SELECT countries.state FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation	car_1_2
SELECT car_makers.Id , car_makers.creator FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.creator FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by JOIN car_names ON model_list.mode = car_names.model_name GROUP BY car_makers.Id HAVING count(*) > 3	car_1_2
SELECT car_makers.Id , car_makers.creator FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.creator FROM car_makers JOIN model_list ON car_makers.Id = model_list.produced_by JOIN car_names ON model_list.mode = car_names.model_name GROUP BY car_makers.Id HAVING count(*) > 3	car_1_2
SELECT countries.CountryId , countries.state FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.state FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation JOIN model_list ON car_makers.Id = model_list.produced_by WHERE model_list.mode = "fiat"	car_1_2
SELECT countries.CountryId , countries.state FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.state FROM countries JOIN car_makers ON countries.CountryId = car_makers.nation JOIN model_list ON car_makers.Id = model_list.produced_by WHERE model_list.mode = "fiat"	car_1_2
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.engine asc LIMIT 1	car_1_3
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.engine asc LIMIT 1	car_1_3
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.mass < (SELECT avg(cars_data.mass) FROM cars_data)	car_1_3
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.mass < (SELECT avg(cars_data.mass) FROM cars_data)	car_1_3
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.model_name = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_3
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.model_name = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_3
SELECT DISTINCT model_list.model_name FROM model_list JOIN car_names ON model_list.model_name = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_3
SELECT DISTINCT model_list.model_name FROM model_list JOIN car_names ON model_list.model_name = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_3
SELECT avg(cars_data.MPG) FROM cars_data WHERE cars_data.cylinder_number = 4	car_1_3
SELECT avg(cars_data.MPG) FROM cars_data WHERE cars_data.cylinder_number = 4	car_1_3
SELECT min(cars_data.mass) FROM cars_data WHERE cars_data.cylinder_number = 8 and cars_data.Year = 1974	car_1_3
SELECT min(cars_data.mass) FROM cars_data WHERE cars_data.cylinder_number = 8 and cars_data.Year = 1974	car_1_3
SELECT model_list.Maker , model_list.model_name FROM model_list	car_1_3
SELECT model_list.Maker , model_list.model_name FROM model_list	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.engine > 150	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.engine > 150	car_1_3
SELECT avg(cars_data.mass) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_3
SELECT avg(cars_data.mass) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_3
SELECT cars_data.engine , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 3 ORDER BY cars_data.engine desc LIMIT 1	car_1_3
SELECT cars_data.engine , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 3 ORDER BY cars_data.engine desc LIMIT 1	car_1_3
SELECT avg(cars_data.engine) FROM cars_data WHERE cars_data.Year < 1980	car_1_3
SELECT avg(cars_data.engine) FROM cars_data WHERE cars_data.Year < 1980	car_1_3
SELECT max(cars_data.Accelerate) , cars_data.cylinder_number FROM cars_data GROUP BY cars_data.cylinder_number	car_1_3
SELECT max(cars_data.Accelerate) , cars_data.cylinder_number FROM cars_data GROUP BY cars_data.cylinder_number	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 4	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 4	car_1_3
SELECT DISTINCT model_list.model_name FROM car_names JOIN model_list ON car_names.Model = model_list.model_name JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.mass > 3500	car_1_3
SELECT DISTINCT model_list.model_name FROM car_names JOIN model_list ON car_names.Model = model_list.model_name JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.mass > 3500	car_1_3
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.mass BETWEEN 3000 AND 4000	car_1_3
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.mass BETWEEN 3000 AND 4000	car_1_3
SELECT cars_data.engine FROM cars_data ORDER BY cars_data.Accelerate desc LIMIT 1	car_1_3
SELECT cars_data.engine FROM cars_data ORDER BY cars_data.Accelerate desc LIMIT 1	car_1_3
SELECT cars_data.cylinder_number FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Model = "volvo" ORDER BY cars_data.Accelerate asc LIMIT 1	car_1_3
SELECT cars_data.cylinder_number FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Model = "volvo" ORDER BY cars_data.Accelerate asc LIMIT 1	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.Accelerate > (SELECT cars_data.Accelerate FROM cars_data ORDER BY cars_data.engine desc LIMIT 1)	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.Accelerate > (SELECT cars_data.Accelerate FROM cars_data ORDER BY cars_data.engine desc LIMIT 1)	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 6	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.cylinder_number > 6	car_1_3
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 4 ORDER BY cars_data.engine desc LIMIT 1	car_1_3
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.cylinder_number = 4 ORDER BY cars_data.engine desc LIMIT 1	car_1_3
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.engine > (SELECT min(cars_data.engine) FROM cars_data) and cars_data.cylinder_number <= 3	car_1_3
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.engine > (SELECT min(cars_data.engine) FROM cars_data) and cars_data.cylinder_number < 4	car_1_3
SELECT max(cars_data.MPG) FROM cars_data WHERE cars_data.cylinder_number = 8 or cars_data.Year < 1980	car_1_3
SELECT max(cars_data.MPG) FROM cars_data WHERE cars_data.cylinder_number = 8 or cars_data.Year < 1980	car_1_3
SELECT DISTINCT model_list.model_name FROM model_list JOIN car_names ON model_list.model_name = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.mass < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_3
SELECT DISTINCT model_list.model_name FROM model_list JOIN car_names ON model_list.model_name = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.mass < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_3
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.model_name = car_names.Model GROUP BY car_makers.Id HAVING count(*) > 3	car_1_3
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.model_name = car_names.Model GROUP BY car_makers.Id HAVING count(*) > 3	car_1_3
SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.model_name = "fiat"	car_1_3
SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.model_name = "fiat"	car_1_3
SELECT car_makers.FullName , car_makers.Id , count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder GROUP BY car_makers.Id	car_1_4
SELECT car_makers.FullName , car_makers.Id , count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder GROUP BY car_makers.Id	car_1_4
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.heaviness < (SELECT avg(cars_data.heaviness) FROM cars_data)	car_1_4
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.heaviness < (SELECT avg(cars_data.heaviness) FROM cars_data)	car_1_4
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder JOIN car_names ON model_list.Model = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_4
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder JOIN car_names ON model_list.Model = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_4
SELECT car_names.manufacture , cars_data.Year FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Year = (SELECT min(cars_data.Year) FROM cars_data)	car_1_4
SELECT car_names.manufacture , cars_data.Year FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Year = (SELECT min(cars_data.Year) FROM cars_data)	car_1_4
SELECT count(*) , car_makers.FullName FROM model_list JOIN car_makers ON model_list.builder = car_makers.Id GROUP BY car_makers.Id	car_1_4
SELECT count(*) , car_makers.FullName , car_makers.Id FROM model_list JOIN car_makers ON model_list.builder = car_makers.Id GROUP BY car_makers.Id	car_1_4
SELECT cars_data.Accelerate FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.manufacture = "amc hornet sportabout (sw)"	car_1_4
SELECT cars_data.Accelerate FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.manufacture = "amc hornet sportabout (sw)"	car_1_4
SELECT count(*) FROM model_list JOIN car_makers ON model_list.builder = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.CountryName = "usa"	car_1_4
SELECT count(*) FROM model_list JOIN car_makers ON model_list.builder = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.CountryName = "usa"	car_1_4
SELECT avg(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.Cylinders = 4	car_1_4
SELECT avg(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.Cylinders = 4	car_1_4
SELECT min(cars_data.heaviness) FROM cars_data WHERE cars_data.Cylinders = 8 and cars_data.Year = 1974	car_1_4
SELECT min(cars_data.heaviness) FROM cars_data WHERE cars_data.Cylinders = 8 and cars_data.Year = 1974	car_1_4
SELECT model_list.builder , model_list.Model FROM model_list	car_1_4
SELECT model_list.builder , model_list.Model FROM model_list	car_1_4
SELECT avg(cars_data.heaviness) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_4
SELECT avg(cars_data.heaviness) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_4
SELECT cars_data.Horsepower , car_names.manufacture FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 3 ORDER BY cars_data.Horsepower desc LIMIT 1	car_1_4
SELECT cars_data.Horsepower , car_names.manufacture FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 3 ORDER BY cars_data.Horsepower desc LIMIT 1	car_1_4
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.miles_per_gallon desc LIMIT 1	car_1_4
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.miles_per_gallon desc LIMIT 1	car_1_4
SELECT count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder WHERE car_makers.FullName = "American Motor Company"	car_1_4
SELECT count(*) FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder WHERE car_makers.FullName = "American Motor Company"	car_1_4
SELECT car_makers.FullName , car_makers.Id FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder GROUP BY car_makers.Id HAVING count(*) > 3	car_1_4
SELECT car_makers.FullName , car_makers.Id FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder GROUP BY car_makers.Id HAVING count(*) > 3	car_1_4
SELECT DISTINCT model_list.Model FROM car_names JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.builder = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.heaviness > 3500	car_1_4
SELECT DISTINCT model_list.Model FROM car_names JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.builder = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.heaviness > 3500	car_1_4
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.heaviness BETWEEN 3000 AND 4000	car_1_4
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.heaviness BETWEEN 3000 AND 4000	car_1_4
SELECT car_names.MakeId , car_names.manufacture FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Horsepower > (SELECT min(cars_data.Horsepower) FROM cars_data) and cars_data.Cylinders <= 3	car_1_4
SELECT car_names.MakeId , car_names.manufacture FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Horsepower > (SELECT min(cars_data.Horsepower) FROM cars_data) and cars_data.Cylinders < 4	car_1_4
SELECT max(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.Cylinders = 8 or cars_data.Year < 1980	car_1_4
SELECT max(cars_data.miles_per_gallon) FROM cars_data WHERE cars_data.Cylinders = 8 or cars_data.Year < 1980	car_1_4
SELECT DISTINCT model_list.Model FROM model_list JOIN car_names ON model_list.Model = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.builder = car_makers.Id WHERE cars_data.heaviness < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_4
SELECT DISTINCT model_list.Model FROM model_list JOIN car_names ON model_list.Model = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.builder = car_makers.Id WHERE cars_data.heaviness < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_4
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder JOIN car_names ON model_list.Model = car_names.Model GROUP BY car_makers.Id HAVING count(*) > 3	car_1_4
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.builder JOIN car_names ON model_list.Model = car_names.Model GROUP BY car_makers.Id HAVING count(*) > 3	car_1_4
SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.builder WHERE model_list.Model = "fiat"	car_1_4
SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.builder WHERE model_list.Model = "fiat"	car_1_4
SELECT airlines.nation FROM airlines WHERE airlines.air_service = "JetBlue Airways"	flight_2_0
SELECT airlines.nation FROM airlines WHERE airlines.air_service = "JetBlue Airways"	flight_2_0
SELECT airlines.Abbreviation FROM airlines WHERE airlines.air_service = "JetBlue Airways"	flight_2_0
SELECT airlines.Abbreviation FROM airlines WHERE airlines.air_service = "JetBlue Airways"	flight_2_0
SELECT airlines.air_service , airlines.Abbreviation FROM airlines WHERE airlines.nation = "USA"	flight_2_0
SELECT airlines.air_service , airlines.Abbreviation FROM airlines WHERE airlines.nation = "USA"	flight_2_0
SELECT airports.AirportCode , airports.airport_designation FROM airports WHERE airports.capital = "Anthony"	flight_2_0
SELECT airports.AirportCode , airports.airport_designation FROM airports WHERE airports.capital = "Anthony"	flight_2_0
SELECT airlines.air_service FROM airlines WHERE airlines.Abbreviation = "UAL"	flight_2_0
SELECT airlines.air_service FROM airlines WHERE airlines.Abbreviation = "UAL"	flight_2_0
SELECT count(*) FROM airlines WHERE airlines.nation = "USA"	flight_2_0
SELECT count(*) FROM airlines WHERE airlines.nation = "USA"	flight_2_0
SELECT airports.capital , airports.Country FROM airports WHERE airports.airport_designation = "Alton"	flight_2_0
SELECT airports.capital , airports.Country FROM airports WHERE airports.airport_designation = "Alton"	flight_2_0
SELECT airports.airport_designation FROM airports WHERE airports.AirportCode = "AKO"	flight_2_0
SELECT airports.airport_designation FROM airports WHERE airports.AirportCode = "AKO"	flight_2_0
SELECT airports.airport_designation FROM airports WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT airports.airport_designation FROM airports WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights WHERE flights.flight_from = "APG"	flight_2_0
SELECT count(*) FROM flights WHERE flights.flight_from = "APG"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.flight_from = airports.AirportCode WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.flight_from = airports.AirportCode WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.DestAirport = T2.AirportCode JOIN airports AS T3 ON T1.flight_from = T3.AirportCode WHERE T2.capital = "Ashley" and T3.capital = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.DestAirport = T2.AirportCode JOIN airports AS T3 ON T1.flight_from = T3.AirportCode WHERE T2.capital = "Ashley" and T3.capital = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airlines ON flights.aircraft_company = airlines.uid WHERE airlines.air_service = "JetBlue Airways"	flight_2_0
SELECT count(*) FROM flights JOIN airlines ON flights.aircraft_company = airlines.uid WHERE airlines.air_service = "JetBlue Airways"	flight_2_0
SELECT count(*) FROM airlines JOIN flights ON flights.aircraft_company = airlines.uid WHERE airlines.air_service = "United Airlines" and flights.DestAirport = "ASY"	flight_2_0
SELECT count(*) FROM airlines JOIN flights ON flights.aircraft_company = airlines.uid WHERE airlines.air_service = "United Airlines" and flights.DestAirport = "ASY"	flight_2_0
SELECT count(*) FROM airlines JOIN flights ON flights.aircraft_company = airlines.uid WHERE airlines.air_service = "United Airlines" and flights.flight_from = "AHD"	flight_2_0
SELECT count(*) FROM airlines JOIN flights ON flights.aircraft_company = airlines.uid WHERE airlines.air_service = "United Airlines" and flights.flight_from = "AHD"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode JOIN airlines ON airlines.uid = flights.aircraft_company WHERE airports.capital = "Aberdeen" and airlines.air_service = "United Airlines"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode JOIN airlines ON airlines.uid = flights.aircraft_company WHERE airports.capital = "Aberdeen" and airlines.air_service = "United Airlines"	flight_2_0
SELECT airports.capital FROM airports JOIN flights ON airports.AirportCode = flights.DestAirport GROUP BY airports.capital ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airports.capital FROM airports JOIN flights ON airports.AirportCode = flights.DestAirport GROUP BY airports.capital ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airports.capital FROM airports JOIN flights ON airports.AirportCode = flights.flight_from GROUP BY airports.capital ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airports.capital FROM airports JOIN flights ON airports.AirportCode = flights.flight_from GROUP BY airports.capital ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company GROUP BY airlines.air_service ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company GROUP BY airlines.air_service ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airlines.Abbreviation , airlines.nation FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company GROUP BY airlines.air_service ORDER BY count(*) asc LIMIT 1	flight_2_0
SELECT airlines.Abbreviation , airlines.nation FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company GROUP BY airlines.air_service ORDER BY count(*) asc LIMIT 1	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "AHD"	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "AHD"	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.DestAirport = "AHD"	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.DestAirport = "AHD"	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "APG" INTERSECT SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "CVO"	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "APG" INTERSECT SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "CVO"	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "CVO" EXCEPT SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "APG"	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "CVO" EXCEPT SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company WHERE flights.flight_from = "APG"	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company GROUP BY airlines.air_service HAVING count(*) > 10	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company GROUP BY airlines.air_service HAVING count(*) > 10	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company GROUP BY airlines.air_service HAVING count(*) < 200	flight_2_0
SELECT airlines.air_service FROM airlines JOIN flights ON airlines.uid = flights.aircraft_company GROUP BY airlines.air_service HAVING count(*) < 200	flight_2_0
SELECT flights.plane_digits FROM flights JOIN airlines ON airlines.uid = flights.aircraft_company WHERE airlines.air_service = "United Airlines"	flight_2_0
SELECT flights.plane_digits FROM flights JOIN airlines ON airlines.uid = flights.aircraft_company WHERE airlines.air_service = "United Airlines"	flight_2_0
SELECT flights.plane_digits FROM flights WHERE flights.flight_from = "APG"	flight_2_0
SELECT flights.plane_digits FROM flights WHERE flights.flight_from = "APG"	flight_2_0
SELECT flights.plane_digits FROM flights WHERE flights.DestAirport = "APG"	flight_2_0
SELECT flights.plane_digits FROM flights WHERE flights.DestAirport = "APG"	flight_2_0
SELECT flights.plane_digits FROM flights JOIN airports ON flights.flight_from = airports.AirportCode WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT flights.plane_digits FROM flights JOIN airports ON flights.flight_from = airports.AirportCode WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT flights.plane_digits FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT flights.plane_digits FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode WHERE airports.capital = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode WHERE airports.capital = "Aberdeen" or airports.capital = "Abilene"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode WHERE airports.capital = "Aberdeen" or airports.capital = "Abilene"	flight_2_0
SELECT airports.airport_designation FROM airports WHERE airports.AirportCode NOT in (SELECT flights.flight_from FROM flights UNION SELECT flights.DestAirport FROM flights)	flight_2_0
SELECT airports.airport_designation FROM airports WHERE airports.AirportCode NOT in (SELECT flights.flight_from FROM flights UNION SELECT flights.DestAirport FROM flights)	flight_2_0
SELECT airports.City , airports.nation FROM airports WHERE airports.AirportName = "Alton"	flight_2_1
SELECT airports.City , airports.nation FROM airports WHERE airports.AirportName = "Alton"	flight_2_1
SELECT count(*) FROM flights WHERE flights.flying_to = "ATO"	flight_2_1
SELECT count(*) FROM flights WHERE flights.flying_to = "ATO"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.flying_to = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.flying_to = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.flying_to = T2.AirportCode JOIN airports AS T3 ON T1.SourceAirport = T3.AirportCode WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.flying_to = T2.AirportCode JOIN airports AS T3 ON T1.SourceAirport = T3.AirportCode WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM airlines JOIN flights ON flights.Airline = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.flying_to = "ASY"	flight_2_1
SELECT count(*) FROM airlines JOIN flights ON flights.Airline = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.flying_to = "ASY"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.flying_to = airports.AirportCode JOIN airlines ON airlines.uid = flights.Airline WHERE airports.City = "Aberdeen" and airlines.Airline = "United Airlines"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.flying_to = airports.AirportCode JOIN airlines ON airlines.uid = flights.Airline WHERE airports.City = "Aberdeen" and airlines.Airline = "United Airlines"	flight_2_1
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.flying_to GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.flying_to GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.flying_to GROUP BY airports.AirportCode ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.flying_to GROUP BY airports.AirportCode ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.flying_to GROUP BY airports.AirportCode ORDER BY count(*) asc LIMIT 1	flight_2_1
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.flying_to GROUP BY airports.AirportCode ORDER BY count(*) asc LIMIT 1	flight_2_1
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.Airline WHERE flights.flying_to = "AHD"	flight_2_1
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.Airline WHERE flights.flying_to = "AHD"	flight_2_1
SELECT flights.aircraft_code FROM flights JOIN airlines ON airlines.uid = flights.Airline WHERE airlines.Airline = "United Airlines"	flight_2_1
SELECT flights.aircraft_code FROM flights JOIN airlines ON airlines.uid = flights.Airline WHERE airlines.Airline = "United Airlines"	flight_2_1
SELECT flights.aircraft_code FROM flights WHERE flights.SourceAirport = "APG"	flight_2_1
SELECT flights.aircraft_code FROM flights WHERE flights.SourceAirport = "APG"	flight_2_1
SELECT flights.aircraft_code FROM flights WHERE flights.flying_to = "APG"	flight_2_1
SELECT flights.aircraft_code FROM flights WHERE flights.flying_to = "APG"	flight_2_1
SELECT flights.aircraft_code FROM flights JOIN airports ON flights.SourceAirport = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_1
SELECT flights.aircraft_code FROM flights JOIN airports ON flights.SourceAirport = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_1
SELECT flights.aircraft_code FROM flights JOIN airports ON flights.flying_to = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_1
SELECT flights.aircraft_code FROM flights JOIN airports ON flights.flying_to = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.flying_to = airports.AirportCode WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.flying_to = airports.AirportCode WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_1
SELECT airports.AirportName FROM airports WHERE airports.AirportCode NOT in (SELECT flights.SourceAirport FROM flights UNION SELECT flights.flying_to FROM flights)	flight_2_1
SELECT airports.AirportName FROM airports WHERE airports.AirportCode NOT in (SELECT flights.SourceAirport FROM flights UNION SELECT flights.flying_to FROM flights)	flight_2_1
SELECT count(*) FROM flights JOIN airlines ON flights.air_way = airlines.uid WHERE airlines.Airline = "JetBlue Airways"	flight_2_2
SELECT count(*) FROM flights JOIN airlines ON flights.air_way = airlines.uid WHERE airlines.Airline = "JetBlue Airways"	flight_2_2
SELECT count(*) FROM airlines JOIN flights ON flights.air_way = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.DestAirport = "ASY"	flight_2_2
SELECT count(*) FROM airlines JOIN flights ON flights.air_way = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.DestAirport = "ASY"	flight_2_2
SELECT count(*) FROM airlines JOIN flights ON flights.air_way = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.SourceAirport = "AHD"	flight_2_2
SELECT count(*) FROM airlines JOIN flights ON flights.air_way = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.SourceAirport = "AHD"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode JOIN airlines ON airlines.uid = flights.air_way WHERE airports.City = "Aberdeen" and airlines.Airline = "United Airlines"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode JOIN airlines ON airlines.uid = flights.air_way WHERE airports.City = "Aberdeen" and airlines.Airline = "United Airlines"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way GROUP BY airlines.Airline ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way GROUP BY airlines.Airline ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airlines.Abbreviation , airlines.Country FROM airlines JOIN flights ON airlines.uid = flights.air_way GROUP BY airlines.Airline ORDER BY count(*) asc LIMIT 1	flight_2_2
SELECT airlines.Abbreviation , airlines.Country FROM airlines JOIN flights ON airlines.uid = flights.air_way GROUP BY airlines.Airline ORDER BY count(*) asc LIMIT 1	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "AHD"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "AHD"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.DestAirport = "AHD"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.DestAirport = "AHD"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "APG" INTERSECT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "CVO"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "APG" INTERSECT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "CVO"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "CVO" EXCEPT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "APG"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "CVO" EXCEPT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way WHERE flights.SourceAirport = "APG"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way GROUP BY airlines.Airline HAVING count(*) > 10	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way GROUP BY airlines.Airline HAVING count(*) > 10	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way GROUP BY airlines.Airline HAVING count(*) < 200	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_way GROUP BY airlines.Airline HAVING count(*) < 200	flight_2_2
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air_way WHERE airlines.Airline = "United Airlines"	flight_2_2
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air_way WHERE airlines.Airline = "United Airlines"	flight_2_2
SELECT airlines.Country FROM airlines WHERE airlines.air_company_name = "JetBlue Airways"	flight_2_3
SELECT airlines.Country FROM airlines WHERE airlines.air_company_name = "JetBlue Airways"	flight_2_3
SELECT airlines.Abbreviation FROM airlines WHERE airlines.air_company_name = "JetBlue Airways"	flight_2_3
SELECT airlines.Abbreviation FROM airlines WHERE airlines.air_company_name = "JetBlue Airways"	flight_2_3
SELECT airlines.air_company_name , airlines.Abbreviation FROM airlines WHERE airlines.Country = "USA"	flight_2_3
SELECT airlines.air_company_name , airlines.Abbreviation FROM airlines WHERE airlines.Country = "USA"	flight_2_3
SELECT airports.AirportCode , airports.airdrome FROM airports WHERE airports.City = "Anthony"	flight_2_3
SELECT airports.AirportCode , airports.airdrome FROM airports WHERE airports.City = "Anthony"	flight_2_3
SELECT airlines.air_company_name FROM airlines WHERE airlines.Abbreviation = "UAL"	flight_2_3
SELECT airlines.air_company_name FROM airlines WHERE airlines.Abbreviation = "UAL"	flight_2_3
SELECT airports.City , airports.state FROM airports WHERE airports.airdrome = "Alton"	flight_2_3
SELECT airports.City , airports.state FROM airports WHERE airports.airdrome = "Alton"	flight_2_3
SELECT airports.airdrome FROM airports WHERE airports.AirportCode = "AKO"	flight_2_3
SELECT airports.airdrome FROM airports WHERE airports.AirportCode = "AKO"	flight_2_3
SELECT airports.airdrome FROM airports WHERE airports.City = "Aberdeen"	flight_2_3
SELECT airports.airdrome FROM airports WHERE airports.City = "Aberdeen"	flight_2_3
SELECT count(*) FROM flights JOIN airlines ON flights.Airline = airlines.airline WHERE airlines.air_company_name = "JetBlue Airways"	flight_2_3
SELECT count(*) FROM flights JOIN airlines ON flights.Airline = airlines.airline WHERE airlines.air_company_name = "JetBlue Airways"	flight_2_3
SELECT count(*) FROM airlines JOIN flights ON flights.Airline = airlines.airline WHERE airlines.air_company_name = "United Airlines" and flights.DestAirport = "ASY"	flight_2_3
SELECT count(*) FROM airlines JOIN flights ON flights.Airline = airlines.airline WHERE airlines.air_company_name = "United Airlines" and flights.DestAirport = "ASY"	flight_2_3
SELECT count(*) FROM airlines JOIN flights ON flights.Airline = airlines.airline WHERE airlines.air_company_name = "United Airlines" and flights.SourceAirport = "AHD"	flight_2_3
SELECT count(*) FROM airlines JOIN flights ON flights.Airline = airlines.airline WHERE airlines.air_company_name = "United Airlines" and flights.SourceAirport = "AHD"	flight_2_3
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode JOIN airlines ON airlines.airline = flights.Airline WHERE airports.City = "Aberdeen" and airlines.air_company_name = "United Airlines"	flight_2_3
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode JOIN airlines ON airlines.airline = flights.Airline WHERE airports.City = "Aberdeen" and airlines.air_company_name = "United Airlines"	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline GROUP BY airlines.air_company_name ORDER BY count(*) desc LIMIT 1	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline GROUP BY airlines.air_company_name ORDER BY count(*) desc LIMIT 1	flight_2_3
SELECT airlines.Abbreviation , airlines.Country FROM airlines JOIN flights ON airlines.airline = flights.Airline GROUP BY airlines.air_company_name ORDER BY count(*) asc LIMIT 1	flight_2_3
SELECT airlines.Abbreviation , airlines.Country FROM airlines JOIN flights ON airlines.airline = flights.Airline GROUP BY airlines.air_company_name ORDER BY count(*) asc LIMIT 1	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "AHD"	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "AHD"	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.DestAirport = "AHD"	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.DestAirport = "AHD"	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "APG" INTERSECT SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "CVO"	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "APG" INTERSECT SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "CVO"	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "CVO" EXCEPT SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "APG"	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "CVO" EXCEPT SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline WHERE flights.SourceAirport = "APG"	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline GROUP BY airlines.air_company_name HAVING count(*) > 10	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline GROUP BY airlines.air_company_name HAVING count(*) > 10	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline GROUP BY airlines.air_company_name HAVING count(*) < 200	flight_2_3
SELECT airlines.air_company_name FROM airlines JOIN flights ON airlines.airline = flights.Airline GROUP BY airlines.air_company_name HAVING count(*) < 200	flight_2_3
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.airline = flights.Airline WHERE airlines.air_company_name = "United Airlines"	flight_2_3
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.airline = flights.Airline WHERE airlines.air_company_name = "United Airlines"	flight_2_3
SELECT airports.airdrome FROM airports WHERE airports.AirportCode NOT in (SELECT flights.SourceAirport FROM flights UNION SELECT flights.DestAirport FROM flights)	flight_2_3
SELECT airports.airdrome FROM airports WHERE airports.AirportCode NOT in (SELECT flights.SourceAirport FROM flights UNION SELECT flights.DestAirport FROM flights)	flight_2_3
SELECT airlines.nation FROM airlines WHERE airlines.Airline = "JetBlue Airways"	flight_2_4
SELECT airlines.nation FROM airlines WHERE airlines.Airline = "JetBlue Airways"	flight_2_4
SELECT airlines.Airline , airlines.Abbreviation FROM airlines WHERE airlines.nation = "USA"	flight_2_4
SELECT airlines.Airline , airlines.Abbreviation FROM airlines WHERE airlines.nation = "USA"	flight_2_4
SELECT airports.AirportCode , airports.airfield_designation FROM airports WHERE airports.City = "Anthony"	flight_2_4
SELECT airports.AirportCode , airports.airfield_designation FROM airports WHERE airports.City = "Anthony"	flight_2_4
SELECT count(*) FROM airlines WHERE airlines.nation = "USA"	flight_2_4
SELECT count(*) FROM airlines WHERE airlines.nation = "USA"	flight_2_4
SELECT airports.City , airports.Country FROM airports WHERE airports.airfield_designation = "Alton"	flight_2_4
SELECT airports.City , airports.Country FROM airports WHERE airports.airfield_designation = "Alton"	flight_2_4
SELECT airports.airfield_designation FROM airports WHERE airports.AirportCode = "AKO"	flight_2_4
SELECT airports.airfield_designation FROM airports WHERE airports.AirportCode = "AKO"	flight_2_4
SELECT airports.airfield_designation FROM airports WHERE airports.City = "Aberdeen"	flight_2_4
SELECT airports.airfield_designation FROM airports WHERE airports.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights WHERE flights.source_airfield = "APG"	flight_2_4
SELECT count(*) FROM flights WHERE flights.source_airfield = "APG"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.source_airfield = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.source_airfield = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.DestAirport = T2.AirportCode JOIN airports AS T3 ON T1.source_airfield = T3.AirportCode WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.DestAirport = T2.AirportCode JOIN airports AS T3 ON T1.source_airfield = T3.AirportCode WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights JOIN airlines ON flights.air_service = airlines.uid WHERE airlines.Airline = "JetBlue Airways"	flight_2_4
SELECT count(*) FROM flights JOIN airlines ON flights.air_service = airlines.uid WHERE airlines.Airline = "JetBlue Airways"	flight_2_4
SELECT count(*) FROM airlines JOIN flights ON flights.air_service = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.DestAirport = "ASY"	flight_2_4
SELECT count(*) FROM airlines JOIN flights ON flights.air_service = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.DestAirport = "ASY"	flight_2_4
SELECT count(*) FROM airlines JOIN flights ON flights.air_service = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.source_airfield = "AHD"	flight_2_4
SELECT count(*) FROM airlines JOIN flights ON flights.air_service = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.source_airfield = "AHD"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode JOIN airlines ON airlines.uid = flights.air_service WHERE airports.City = "Aberdeen" and airlines.Airline = "United Airlines"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.DestAirport = airports.AirportCode JOIN airlines ON airlines.uid = flights.air_service WHERE airports.City = "Aberdeen" and airlines.Airline = "United Airlines"	flight_2_4
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.source_airfield GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.source_airfield GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service GROUP BY airlines.Airline ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service GROUP BY airlines.Airline ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airlines.Abbreviation , airlines.nation FROM airlines JOIN flights ON airlines.uid = flights.air_service GROUP BY airlines.Airline ORDER BY count(*) asc LIMIT 1	flight_2_4
SELECT airlines.Abbreviation , airlines.nation FROM airlines JOIN flights ON airlines.uid = flights.air_service GROUP BY airlines.Airline ORDER BY count(*) asc LIMIT 1	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "AHD"	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "AHD"	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.DestAirport = "AHD"	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.DestAirport = "AHD"	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "APG" INTERSECT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "CVO"	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "APG" INTERSECT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "CVO"	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "CVO" EXCEPT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "APG"	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "CVO" EXCEPT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service WHERE flights.source_airfield = "APG"	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service GROUP BY airlines.Airline HAVING count(*) > 10	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service GROUP BY airlines.Airline HAVING count(*) > 10	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service GROUP BY airlines.Airline HAVING count(*) < 200	flight_2_4
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air_service GROUP BY airlines.Airline HAVING count(*) < 200	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air_service WHERE airlines.Airline = "United Airlines"	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air_service WHERE airlines.Airline = "United Airlines"	flight_2_4
SELECT flights.FlightNo FROM flights WHERE flights.source_airfield = "APG"	flight_2_4
SELECT flights.FlightNo FROM flights WHERE flights.source_airfield = "APG"	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airports ON flights.source_airfield = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airports ON flights.source_airfield = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT airports.airfield_designation FROM airports WHERE airports.AirportCode NOT in (SELECT flights.source_airfield FROM flights UNION SELECT flights.DestAirport FROM flights)	flight_2_4
SELECT airports.airfield_designation FROM airports WHERE airports.AirportCode NOT in (SELECT flights.source_airfield FROM flights UNION SELECT flights.DestAirport FROM flights)	flight_2_4
SELECT count(*) , employee.metropolis FROM employee GROUP BY employee.metropolis	employee_hire_evaluation_0
SELECT count(*) , employee.metropolis FROM employee GROUP BY employee.metropolis	employee_hire_evaluation_0
SELECT employee.metropolis FROM employee WHERE employee.Age < 30 GROUP BY employee.metropolis HAVING count(*) > 1	employee_hire_evaluation_0
SELECT employee.metropolis FROM employee WHERE employee.Age < 30 GROUP BY employee.metropolis HAVING count(*) > 1	employee_hire_evaluation_0
SELECT count(*) , shop.whereabouts FROM shop GROUP BY shop.whereabouts	employee_hire_evaluation_0
SELECT count(*) , shop.whereabouts FROM shop GROUP BY shop.whereabouts	employee_hire_evaluation_0
SELECT shop.head , shop.area FROM shop ORDER BY shop.commodity_quantity desc LIMIT 1	employee_hire_evaluation_0
SELECT shop.head , shop.area FROM shop ORDER BY shop.commodity_quantity desc LIMIT 1	employee_hire_evaluation_0
SELECT min(shop.commodity_quantity) , max(shop.commodity_quantity) FROM shop	employee_hire_evaluation_0
SELECT min(shop.commodity_quantity) , max(shop.commodity_quantity) FROM shop	employee_hire_evaluation_0
SELECT shop.Name , shop.whereabouts , shop.area FROM shop ORDER BY shop.commodity_quantity desc	employee_hire_evaluation_0
SELECT shop.Name , shop.whereabouts , shop.area FROM shop ORDER BY shop.commodity_quantity desc	employee_hire_evaluation_0
SELECT shop.Name FROM shop WHERE shop.commodity_quantity > (SELECT avg(shop.commodity_quantity) FROM shop)	employee_hire_evaluation_0
SELECT shop.Name FROM shop WHERE shop.commodity_quantity > (SELECT avg(shop.commodity_quantity) FROM shop)	employee_hire_evaluation_0
SELECT shop.area FROM shop WHERE shop.commodity_quantity < 3000 INTERSECT SELECT shop.area FROM shop WHERE shop.commodity_quantity > 10000	employee_hire_evaluation_0
SELECT shop.area FROM shop WHERE shop.commodity_quantity < 3000 INTERSECT SELECT shop.area FROM shop WHERE shop.commodity_quantity > 10000	employee_hire_evaluation_0
SELECT count(DISTINCT shop.whereabouts) FROM shop	employee_hire_evaluation_0
SELECT count(DISTINCT shop.whereabouts) FROM shop	employee_hire_evaluation_0
SELECT shop.Manager_name , shop.District FROM shop ORDER BY shop.products_number desc LIMIT 1	employee_hire_evaluation_2
SELECT shop.Manager_name , shop.District FROM shop ORDER BY shop.products_number desc LIMIT 1	employee_hire_evaluation_2
SELECT min(shop.products_number) , max(shop.products_number) FROM shop	employee_hire_evaluation_2
SELECT min(shop.products_number) , max(shop.products_number) FROM shop	employee_hire_evaluation_2
SELECT shop.Name , shop.Location , shop.District FROM shop ORDER BY shop.products_number desc	employee_hire_evaluation_2
SELECT shop.Name , shop.Location , shop.District FROM shop ORDER BY shop.products_number desc	employee_hire_evaluation_2
SELECT shop.Name FROM shop WHERE shop.products_number > (SELECT avg(shop.products_number) FROM shop)	employee_hire_evaluation_2
SELECT shop.Name FROM shop WHERE shop.products_number > (SELECT avg(shop.products_number) FROM shop)	employee_hire_evaluation_2
SELECT shop.District FROM shop WHERE shop.products_number < 3000 INTERSECT SELECT shop.District FROM shop WHERE shop.products_number > 10000	employee_hire_evaluation_2
SELECT shop.District FROM shop WHERE shop.products_number < 3000 INTERSECT SELECT shop.District FROM shop WHERE shop.products_number > 10000	employee_hire_evaluation_2
SELECT count(*) , employee.metropolis FROM employee GROUP BY employee.metropolis	employee_hire_evaluation_3
SELECT count(*) , employee.metropolis FROM employee GROUP BY employee.metropolis	employee_hire_evaluation_3
SELECT employee.metropolis FROM employee WHERE employee.Age < 30 GROUP BY employee.metropolis HAVING count(*) > 1	employee_hire_evaluation_3
SELECT employee.metropolis FROM employee WHERE employee.Age < 30 GROUP BY employee.metropolis HAVING count(*) > 1	employee_hire_evaluation_3
SELECT count(*) , shop.position FROM shop GROUP BY shop.position	employee_hire_evaluation_3
SELECT count(*) , shop.position FROM shop GROUP BY shop.position	employee_hire_evaluation_3
SELECT shop.Name , shop.position , shop.District FROM shop ORDER BY shop.Number_products desc	employee_hire_evaluation_3
SELECT shop.Name , shop.position , shop.District FROM shop ORDER BY shop.Number_products desc	employee_hire_evaluation_3
SELECT count(DISTINCT shop.position) FROM shop	employee_hire_evaluation_3
SELECT count(DISTINCT shop.position) FROM shop	employee_hire_evaluation_3
SELECT count(*) , shop.whereabouts FROM shop GROUP BY shop.whereabouts	employee_hire_evaluation_4
SELECT count(*) , shop.whereabouts FROM shop GROUP BY shop.whereabouts	employee_hire_evaluation_4
SELECT shop.Manager_name , shop.region FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_4
SELECT shop.Manager_name , shop.region FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_4
SELECT shop.Name , shop.whereabouts , shop.region FROM shop ORDER BY shop.Number_products desc	employee_hire_evaluation_4
SELECT shop.Name , shop.whereabouts , shop.region FROM shop ORDER BY shop.Number_products desc	employee_hire_evaluation_4
SELECT shop.region FROM shop WHERE shop.Number_products < 3000 INTERSECT SELECT shop.region FROM shop WHERE shop.Number_products > 10000	employee_hire_evaluation_4
SELECT shop.region FROM shop WHERE shop.Number_products < 3000 INTERSECT SELECT shop.region FROM shop WHERE shop.Number_products > 10000	employee_hire_evaluation_4
SELECT count(DISTINCT shop.whereabouts) FROM shop	employee_hire_evaluation_4
SELECT count(DISTINCT shop.whereabouts) FROM shop	employee_hire_evaluation_4
SELECT Documents.Document_ID , Documents.document_designation , Documents.explanation FROM Documents	cre_Doc_Template_Mgt_0
SELECT Documents.Document_ID , Documents.document_designation , Documents.explanation FROM Documents	cre_Doc_Template_Mgt_0
SELECT Documents.document_designation , Documents.Template_ID FROM Documents WHERE Documents.explanation like "%w%"	cre_Doc_Template_Mgt_0
SELECT Documents.document_designation , Documents.Template_ID FROM Documents WHERE Documents.explanation like "%w%"	cre_Doc_Template_Mgt_0
SELECT Documents.Document_ID , Documents.Template_ID , Documents.explanation FROM Documents WHERE Documents.document_designation = "Robbin CV"	cre_Doc_Template_Mgt_0
SELECT Documents.Document_ID , Documents.Template_ID , Documents.explanation FROM Documents WHERE Documents.document_designation = "Robbin CV"	cre_Doc_Template_Mgt_0
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID WHERE Templates.tempalte_class_cipher = "PPT"	cre_Doc_Template_Mgt_0
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID WHERE Templates.tempalte_class_cipher = "PPT"	cre_Doc_Template_Mgt_0
SELECT Documents.Template_ID , Templates.tempalte_class_cipher FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Documents.Template_ID , Templates.tempalte_class_cipher FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Templates.Template_ID , Templates.Version_Number , Templates.tempalte_class_cipher FROM Templates	cre_Doc_Template_Mgt_0
SELECT Templates.Template_ID , Templates.Version_Number , Templates.tempalte_class_cipher FROM Templates	cre_Doc_Template_Mgt_0
SELECT DISTINCT Templates.tempalte_class_cipher FROM Templates	cre_Doc_Template_Mgt_0
SELECT DISTINCT Templates.tempalte_class_cipher FROM Templates	cre_Doc_Template_Mgt_0
SELECT Templates.Template_ID FROM Templates WHERE Templates.tempalte_class_cipher = "PP" or Templates.tempalte_class_cipher = "PPT"	cre_Doc_Template_Mgt_0
SELECT Templates.Template_ID FROM Templates WHERE Templates.tempalte_class_cipher = "PP" or Templates.tempalte_class_cipher = "PPT"	cre_Doc_Template_Mgt_0
SELECT count(*) FROM Templates WHERE Templates.tempalte_class_cipher = "CV"	cre_Doc_Template_Mgt_0
SELECT count(*) FROM Templates WHERE Templates.tempalte_class_cipher = "CV"	cre_Doc_Template_Mgt_0
SELECT Templates.Version_Number , Templates.tempalte_class_cipher FROM Templates WHERE Templates.Version_Number > 5	cre_Doc_Template_Mgt_0
SELECT Templates.Version_Number , Templates.tempalte_class_cipher FROM Templates WHERE Templates.Version_Number > 5	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher , count(*) FROM Templates GROUP BY Templates.tempalte_class_cipher	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher , count(*) FROM Templates GROUP BY Templates.tempalte_class_cipher	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates GROUP BY Templates.tempalte_class_cipher ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates GROUP BY Templates.tempalte_class_cipher ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates GROUP BY Templates.tempalte_class_cipher HAVING count(*) < 3	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates GROUP BY Templates.tempalte_class_cipher HAVING count(*) < 3	cre_Doc_Template_Mgt_0
SELECT min(Templates.Version_Number) , Templates.tempalte_class_cipher FROM Templates	cre_Doc_Template_Mgt_0
SELECT min(Templates.Version_Number) , Templates.tempalte_class_cipher FROM Templates	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.document_designation = "Data base"	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.document_designation = "Data base"	cre_Doc_Template_Mgt_0
SELECT Documents.document_designation FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.tempalte_class_cipher = "BK"	cre_Doc_Template_Mgt_0
SELECT Documents.document_designation FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.tempalte_class_cipher = "BK"	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.tempalte_class_cipher	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.tempalte_class_cipher	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.tempalte_class_cipher ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.tempalte_class_cipher ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates EXCEPT SELECT Templates.tempalte_class_cipher FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_0
SELECT Templates.tempalte_class_cipher FROM Templates EXCEPT SELECT Templates.tempalte_class_cipher FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_0
SELECT Ref_Template_Types.category_code , Ref_Template_Types.description FROM Ref_Template_Types	cre_Doc_Template_Mgt_0
SELECT Ref_Template_Types.category_code , Ref_Template_Types.description FROM Ref_Template_Types	cre_Doc_Template_Mgt_0
SELECT Ref_Template_Types.description FROM Ref_Template_Types WHERE Ref_Template_Types.category_code = "AD"	cre_Doc_Template_Mgt_0
SELECT Ref_Template_Types.description FROM Ref_Template_Types WHERE Ref_Template_Types.category_code = "AD"	cre_Doc_Template_Mgt_0
SELECT Ref_Template_Types.category_code FROM Ref_Template_Types WHERE Ref_Template_Types.description = "Book"	cre_Doc_Template_Mgt_0
SELECT Ref_Template_Types.category_code FROM Ref_Template_Types WHERE Ref_Template_Types.description = "Book"	cre_Doc_Template_Mgt_0
SELECT DISTINCT Ref_Template_Types.description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_code = Templates.tempalte_class_cipher JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_0
SELECT DISTINCT Ref_Template_Types.description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_code = Templates.tempalte_class_cipher JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_0
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_code = Templates.tempalte_class_cipher WHERE Ref_Template_Types.description = "Presentation"	cre_Doc_Template_Mgt_0
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_code = Templates.tempalte_class_cipher WHERE Ref_Template_Types.description = "Presentation"	cre_Doc_Template_Mgt_0
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.document_designation = "Summer Show"	cre_Doc_Template_Mgt_0
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.document_designation = "Summer Show"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.particularities FROM Paragraphs WHERE Paragraphs.content like "korea"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.particularities FROM Paragraphs WHERE Paragraphs.content like "korea"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Paragraph_ID , Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.document_designation = "Welcome to NY"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Paragraph_ID , Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.document_designation = "Welcome to NY"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.document_designation = "Customer reviews"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.document_designation = "Customer reviews"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Document_ID , Documents.document_designation , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Document_ID , Documents.document_designation , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Document_ID , Documents.document_designation FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Document_ID , Documents.document_designation FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Brazil" INTERSECT SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Ireland"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Brazil" INTERSECT SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Ireland"	cre_Doc_Template_Mgt_0
SELECT Documents.Document_ID , Documents.filename , Documents.Document_Description FROM Documents	cre_Doc_Template_Mgt_1
SELECT Documents.Document_ID , Documents.filename , Documents.Document_Description FROM Documents	cre_Doc_Template_Mgt_1
SELECT Documents.filename , Documents.Template_ID FROM Documents WHERE Documents.Document_Description like "%w%"	cre_Doc_Template_Mgt_1
SELECT Documents.filename , Documents.Template_ID FROM Documents WHERE Documents.Document_Description like "%w%"	cre_Doc_Template_Mgt_1
SELECT Documents.Document_ID , Documents.Template_ID , Documents.Document_Description FROM Documents WHERE Documents.filename = "Robbin CV"	cre_Doc_Template_Mgt_1
SELECT Documents.Document_ID , Documents.Template_ID , Documents.Document_Description FROM Documents WHERE Documents.filename = "Robbin CV"	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.filename = "Data base"	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.filename = "Data base"	cre_Doc_Template_Mgt_1
SELECT Documents.filename FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.Template_Type_Code = "BK"	cre_Doc_Template_Mgt_1
SELECT Documents.filename FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.Template_Type_Code = "BK"	cre_Doc_Template_Mgt_1
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.filename = "Summer Show"	cre_Doc_Template_Mgt_1
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.filename = "Summer Show"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.else_details FROM Paragraphs WHERE Paragraphs.Paragraph_Text like "korea"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.else_details FROM Paragraphs WHERE Paragraphs.Paragraph_Text like "korea"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Paragraph_ID , Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.filename = "Welcome to NY"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Paragraph_ID , Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.filename = "Welcome to NY"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.filename = "Customer reviews"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.filename = "Customer reviews"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Document_ID , Documents.filename , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Document_ID , Documents.filename , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Document_ID , Documents.filename FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Document_ID , Documents.filename FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Documents.Document_ID , Documents.file_designation , Documents.file_elaboration FROM Documents	cre_Doc_Template_Mgt_2
SELECT Documents.Document_ID , Documents.file_designation , Documents.file_elaboration FROM Documents	cre_Doc_Template_Mgt_2
SELECT Documents.file_designation , Documents.Template_ID FROM Documents WHERE Documents.file_elaboration like "%w%"	cre_Doc_Template_Mgt_2
SELECT Documents.file_designation , Documents.Template_ID FROM Documents WHERE Documents.file_elaboration like "%w%"	cre_Doc_Template_Mgt_2
SELECT Documents.Document_ID , Documents.Template_ID , Documents.file_elaboration FROM Documents WHERE Documents.file_designation = "Robbin CV"	cre_Doc_Template_Mgt_2
SELECT Documents.Document_ID , Documents.Template_ID , Documents.file_elaboration FROM Documents WHERE Documents.file_designation = "Robbin CV"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID WHERE Templates.template_kind_codification = "PPT"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID WHERE Templates.template_kind_codification = "PPT"	cre_Doc_Template_Mgt_2
SELECT Documents.Template_ID , Templates.template_kind_codification FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Documents.Template_ID , Templates.template_kind_codification FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID , Templates.Version_Number , Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID , Templates.Version_Number , Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_2
SELECT DISTINCT Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_2
SELECT DISTINCT Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Templates WHERE Templates.template_kind_codification = "PP" or Templates.template_kind_codification = "PPT"	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Templates WHERE Templates.template_kind_codification = "PP" or Templates.template_kind_codification = "PPT"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Templates WHERE Templates.template_kind_codification = "CV"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Templates WHERE Templates.template_kind_codification = "CV"	cre_Doc_Template_Mgt_2
SELECT Templates.Version_Number , Templates.template_kind_codification FROM Templates WHERE Templates.Version_Number > 5	cre_Doc_Template_Mgt_2
SELECT Templates.Version_Number , Templates.template_kind_codification FROM Templates WHERE Templates.Version_Number > 5	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification , count(*) FROM Templates GROUP BY Templates.template_kind_codification	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification , count(*) FROM Templates GROUP BY Templates.template_kind_codification	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates GROUP BY Templates.template_kind_codification ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates GROUP BY Templates.template_kind_codification ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates GROUP BY Templates.template_kind_codification HAVING count(*) < 3	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates GROUP BY Templates.template_kind_codification HAVING count(*) < 3	cre_Doc_Template_Mgt_2
SELECT min(Templates.Version_Number) , Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_2
SELECT min(Templates.Version_Number) , Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.file_designation = "Data base"	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.file_designation = "Data base"	cre_Doc_Template_Mgt_2
SELECT Documents.file_designation FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.template_kind_codification = "BK"	cre_Doc_Template_Mgt_2
SELECT Documents.file_designation FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.template_kind_codification = "BK"	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.template_kind_codification	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.template_kind_codification	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.template_kind_codification ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.template_kind_codification ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates EXCEPT SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_2
SELECT Templates.template_kind_codification FROM Templates EXCEPT SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.category_cipher , Ref_Template_Types.description FROM Ref_Template_Types	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.category_cipher , Ref_Template_Types.description FROM Ref_Template_Types	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.description FROM Ref_Template_Types WHERE Ref_Template_Types.category_cipher = "AD"	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.description FROM Ref_Template_Types WHERE Ref_Template_Types.category_cipher = "AD"	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.category_cipher FROM Ref_Template_Types WHERE Ref_Template_Types.description = "Book"	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.category_cipher FROM Ref_Template_Types WHERE Ref_Template_Types.description = "Book"	cre_Doc_Template_Mgt_2
SELECT DISTINCT Ref_Template_Types.description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_cipher = Templates.template_kind_codification JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_2
SELECT DISTINCT Ref_Template_Types.description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_cipher = Templates.template_kind_codification JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_cipher = Templates.template_kind_codification WHERE Ref_Template_Types.description = "Presentation"	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_cipher = Templates.template_kind_codification WHERE Ref_Template_Types.description = "Presentation"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.file_designation = "Summer Show"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.file_designation = "Summer Show"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.particularities FROM Paragraphs WHERE Paragraphs.content like "korea"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.particularities FROM Paragraphs WHERE Paragraphs.content like "korea"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Paragraph_ID , Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.file_designation = "Welcome to NY"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Paragraph_ID , Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.file_designation = "Welcome to NY"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.file_designation = "Customer reviews"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.file_designation = "Customer reviews"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Document_ID , Documents.file_designation , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Document_ID , Documents.file_designation , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Document_ID , Documents.file_designation FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Document_ID , Documents.file_designation FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Brazil" INTERSECT SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Ireland"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Brazil" INTERSECT SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Ireland"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID WHERE Templates.template_kind_codification = "PPT"	cre_Doc_Template_Mgt_3
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID WHERE Templates.template_kind_codification = "PPT"	cre_Doc_Template_Mgt_3
SELECT Documents.Template_ID , Templates.template_kind_codification FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_3
SELECT Documents.Template_ID , Templates.template_kind_codification FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_3
SELECT Templates.Template_ID , Templates.Version_Number , Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_3
SELECT Templates.Template_ID , Templates.Version_Number , Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_3
SELECT DISTINCT Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_3
SELECT DISTINCT Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_3
SELECT Templates.Template_ID FROM Templates WHERE Templates.template_kind_codification = "PP" or Templates.template_kind_codification = "PPT"	cre_Doc_Template_Mgt_3
SELECT Templates.Template_ID FROM Templates WHERE Templates.template_kind_codification = "PP" or Templates.template_kind_codification = "PPT"	cre_Doc_Template_Mgt_3
SELECT count(*) FROM Templates WHERE Templates.template_kind_codification = "CV"	cre_Doc_Template_Mgt_3
SELECT count(*) FROM Templates WHERE Templates.template_kind_codification = "CV"	cre_Doc_Template_Mgt_3
SELECT Templates.Version_Number , Templates.template_kind_codification FROM Templates WHERE Templates.Version_Number > 5	cre_Doc_Template_Mgt_3
SELECT Templates.Version_Number , Templates.template_kind_codification FROM Templates WHERE Templates.Version_Number > 5	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification , count(*) FROM Templates GROUP BY Templates.template_kind_codification	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification , count(*) FROM Templates GROUP BY Templates.template_kind_codification	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates GROUP BY Templates.template_kind_codification ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates GROUP BY Templates.template_kind_codification ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates GROUP BY Templates.template_kind_codification HAVING count(*) < 3	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates GROUP BY Templates.template_kind_codification HAVING count(*) < 3	cre_Doc_Template_Mgt_3
SELECT min(Templates.Version_Number) , Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_3
SELECT min(Templates.Version_Number) , Templates.template_kind_codification FROM Templates	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.Document_Name = "Data base"	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.Document_Name = "Data base"	cre_Doc_Template_Mgt_3
SELECT Documents.Document_Name FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.template_kind_codification = "BK"	cre_Doc_Template_Mgt_3
SELECT Documents.Document_Name FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.template_kind_codification = "BK"	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.template_kind_codification	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.template_kind_codification	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.template_kind_codification ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.template_kind_codification ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates EXCEPT SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_3
SELECT Templates.template_kind_codification FROM Templates EXCEPT SELECT Templates.template_kind_codification FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_3
SELECT Ref_Template_Types.category_cipher , Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types	cre_Doc_Template_Mgt_3
SELECT Ref_Template_Types.category_cipher , Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types	cre_Doc_Template_Mgt_3
SELECT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types WHERE Ref_Template_Types.category_cipher = "AD"	cre_Doc_Template_Mgt_3
SELECT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types WHERE Ref_Template_Types.category_cipher = "AD"	cre_Doc_Template_Mgt_3
SELECT Ref_Template_Types.category_cipher FROM Ref_Template_Types WHERE Ref_Template_Types.Template_Type_Description = "Book"	cre_Doc_Template_Mgt_3
SELECT Ref_Template_Types.category_cipher FROM Ref_Template_Types WHERE Ref_Template_Types.Template_Type_Description = "Book"	cre_Doc_Template_Mgt_3
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_cipher = Templates.template_kind_codification JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_3
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_cipher = Templates.template_kind_codification JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_3
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_cipher = Templates.template_kind_codification WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_3
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.category_cipher = Templates.template_kind_codification WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_3
SELECT Documents.Document_ID , Documents.Document_Name , Documents.detailing FROM Documents	cre_Doc_Template_Mgt_4
SELECT Documents.Document_ID , Documents.Document_Name , Documents.detailing FROM Documents	cre_Doc_Template_Mgt_4
SELECT Documents.Document_Name , Documents.Template_ID FROM Documents WHERE Documents.detailing like "%w%"	cre_Doc_Template_Mgt_4
SELECT Documents.Document_Name , Documents.Template_ID FROM Documents WHERE Documents.detailing like "%w%"	cre_Doc_Template_Mgt_4
SELECT Documents.Document_ID , Documents.Template_ID , Documents.detailing FROM Documents WHERE Documents.Document_Name = "Robbin CV"	cre_Doc_Template_Mgt_4
SELECT Documents.Document_ID , Documents.Template_ID , Documents.detailing FROM Documents WHERE Documents.Document_Name = "Robbin CV"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Other_Details FROM Paragraphs WHERE Paragraphs.content like "korea"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Other_Details FROM Paragraphs WHERE Paragraphs.content like "korea"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Paragraph_ID , Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.Document_Name = "Welcome to NY"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Paragraph_ID , Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.Document_Name = "Welcome to NY"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.Document_Name = "Customer reviews"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.content FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.Document_ID WHERE Documents.Document_Name = "Customer reviews"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Brazil" INTERSECT SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Ireland"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Brazil" INTERSECT SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.content = "Ireland"	cre_Doc_Template_Mgt_4
SELECT visitor.Name FROM visitor WHERE visitor.type_of_membership > 4 ORDER BY visitor.type_of_membership desc	museum_visit_0
SELECT avg(visitor.Age) FROM visitor WHERE visitor.type_of_membership <= 4	museum_visit_0
SELECT visitor.Name , visitor.type_of_membership FROM visitor WHERE visitor.type_of_membership > 4 ORDER BY visitor.Age desc	museum_visit_0
SELECT museum.Museum_ID , museum.Name FROM museum ORDER BY museum.staff_num desc LIMIT 1	museum_visit_0
SELECT avg(museum.staff_num) FROM museum WHERE museum.accessible_from < 2009	museum_visit_0
SELECT museum.staff_num , museum.accessible_from FROM museum WHERE museum.Name = "Plaza Museum"	museum_visit_0
SELECT museum.Name FROM museum WHERE museum.staff_num > (SELECT min(museum.staff_num) FROM museum WHERE museum.accessible_from > 2010.0)	museum_visit_0
SELECT visit.visitor_ID , visitor.Name , visitor.type_of_membership FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID GROUP BY visit.visitor_ID ORDER BY sum(visit.Total_spent) desc LIMIT 1	museum_visit_0
SELECT visitor.Name , visitor.Age FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID ORDER BY visit.coupon_quantity desc LIMIT 1	museum_visit_0
SELECT avg(visit.coupon_quantity) , max(visit.coupon_quantity) FROM visit	museum_visit_0
SELECT sum(visit.Total_spent) FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID WHERE visitor.type_of_membership = 1	museum_visit_0
SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.Museum_ID WHERE museum.accessible_from < 2009 INTERSECT SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.Museum_ID WHERE museum.accessible_from > 2011	museum_visit_0
SELECT count(*) FROM visitor WHERE visitor.ID NOT in (SELECT visit.visitor_ID FROM museum JOIN visit ON museum.Museum_ID = visit.Museum_ID WHERE museum.accessible_from > 2010.0)	museum_visit_0
SELECT count(*) FROM museum WHERE museum.accessible_from > 2013 or museum.accessible_from < 2008	museum_visit_0
SELECT museum.Museum_ID , museum.Name FROM museum ORDER BY museum.staff_num desc LIMIT 1	museum_visit_1
SELECT avg(museum.staff_num) FROM museum WHERE museum.Open_Year < 2009	museum_visit_1
SELECT museum.staff_num , museum.Open_Year FROM museum WHERE museum.Name = "Plaza Museum"	museum_visit_1
SELECT museum.Name FROM museum WHERE museum.staff_num > (SELECT min(museum.staff_num) FROM museum WHERE museum.Open_Year > 2010.0)	museum_visit_1
SELECT visitor.Name , visitor.Age FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID ORDER BY visit.coupon_quantity desc LIMIT 1	museum_visit_1
SELECT avg(visit.coupon_quantity) , max(visit.coupon_quantity) FROM visit	museum_visit_1
SELECT avg(museum.Num_of_Staff) FROM museum WHERE museum.airing_year < 2009	museum_visit_2
SELECT museum.Num_of_Staff , museum.airing_year FROM museum WHERE museum.Name = "Plaza Museum"	museum_visit_2
SELECT museum.Name FROM museum WHERE museum.Num_of_Staff > (SELECT min(museum.Num_of_Staff) FROM museum WHERE museum.airing_year > 2010.0)	museum_visit_2
SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.Museum_ID WHERE museum.airing_year < 2009 INTERSECT SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.Museum_ID WHERE museum.airing_year > 2011	museum_visit_2
SELECT count(*) FROM visitor WHERE visitor.ID NOT in (SELECT visit.visitor_ID FROM museum JOIN visit ON museum.Museum_ID = visit.Museum_ID WHERE museum.airing_year > 2010.0)	museum_visit_2
SELECT count(*) FROM museum WHERE museum.airing_year > 2013 or museum.airing_year < 2008	museum_visit_2
SELECT museum.Museum_ID , museum.Name FROM museum ORDER BY museum.how_many_workers desc LIMIT 1	museum_visit_3
SELECT avg(museum.how_many_workers) FROM museum WHERE museum.Open_Year < 2009	museum_visit_3
SELECT museum.how_many_workers , museum.Open_Year FROM museum WHERE museum.Name = "Plaza Museum"	museum_visit_3
SELECT museum.Name FROM museum WHERE museum.how_many_workers > (SELECT min(museum.how_many_workers) FROM museum WHERE museum.Open_Year > 2010.0)	museum_visit_3
SELECT visitor.Name , visitor.Age FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID ORDER BY visit.coupon_quantity desc LIMIT 1	museum_visit_3
SELECT avg(visit.coupon_quantity) , max(visit.coupon_quantity) FROM visit	museum_visit_3
SELECT visitor.Name FROM visitor WHERE visitor.fellowship_classification > 4 ORDER BY visitor.fellowship_classification desc	museum_visit_4
SELECT avg(visitor.Age) FROM visitor WHERE visitor.fellowship_classification <= 4	museum_visit_4
SELECT visitor.Name , visitor.fellowship_classification FROM visitor WHERE visitor.fellowship_classification > 4 ORDER BY visitor.Age desc	museum_visit_4
SELECT museum.Museum_ID , museum.Name FROM museum ORDER BY museum.staff_num desc LIMIT 1	museum_visit_4
SELECT avg(museum.staff_num) FROM museum WHERE museum.Open_Year < 2009	museum_visit_4
SELECT museum.staff_num , museum.Open_Year FROM museum WHERE museum.Name = "Plaza Museum"	museum_visit_4
SELECT museum.Name FROM museum WHERE museum.staff_num > (SELECT min(museum.staff_num) FROM museum WHERE museum.Open_Year > 2010.0)	museum_visit_4
SELECT visit.visitor_ID , visitor.Name , visitor.fellowship_classification FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID GROUP BY visit.visitor_ID ORDER BY sum(visit.Total_spent) desc LIMIT 1	museum_visit_4
SELECT sum(visit.Total_spent) FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID WHERE visitor.fellowship_classification = 1	museum_visit_4
SELECT players.given_name , players.birthday FROM players WHERE players.state_code = "USA"	wta_1_0
SELECT players.given_name , players.birthday FROM players WHERE players.state_code = "USA"	wta_1_0
SELECT avg(matches.total_loss) , avg(matches.victor_how_old) FROM matches	wta_1_0
SELECT avg(matches.total_loss) , avg(matches.victor_how_old) FROM matches	wta_1_0
SELECT avg(matches.achiever_ranking) FROM matches	wta_1_0
SELECT avg(matches.achiever_ranking) FROM matches	wta_1_0
SELECT count(DISTINCT players.state_code) FROM players	wta_1_0
SELECT count(DISTINCT players.state_code) FROM players	wta_1_0
SELECT count(DISTINCT matches.failure) FROM matches	wta_1_0
SELECT count(DISTINCT matches.failure) FROM matches	wta_1_0
SELECT matches.event_name FROM matches GROUP BY matches.event_name HAVING count(*) > 10	wta_1_0
SELECT matches.event_name FROM matches GROUP BY matches.event_name HAVING count(*) > 10	wta_1_0
SELECT matches.victor_name FROM matches WHERE matches.year = 2013 INTERSECT SELECT matches.victor_name FROM matches WHERE matches.year = 2016	wta_1_0
SELECT matches.victor_name FROM matches WHERE matches.year = 2013 INTERSECT SELECT matches.victor_name FROM matches WHERE matches.year = 2016	wta_1_0
SELECT players.state_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.event_name = "WTA Championships" INTERSECT SELECT players.state_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.event_name = "Australian Open"	wta_1_0
SELECT players.state_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.event_name = "WTA Championships" INTERSECT SELECT players.state_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.event_name = "Australian Open"	wta_1_0
SELECT players.given_name , players.state_code FROM players ORDER BY players.birthday asc LIMIT 1	wta_1_0
SELECT players.given_name , players.state_code FROM players ORDER BY players.birthday asc LIMIT 1	wta_1_0
SELECT players.given_name , players.final_name FROM players ORDER BY players.birthday asc	wta_1_0
SELECT players.given_name , players.final_name FROM players ORDER BY players.birthday asc	wta_1_0
SELECT players.given_name , players.final_name FROM players WHERE players.hand = "L" ORDER BY players.birthday asc	wta_1_0
SELECT players.given_name , players.final_name FROM players WHERE players.hand = "L" ORDER BY players.birthday asc	wta_1_0
SELECT players.state_code , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_0
SELECT players.state_code , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_0
SELECT matches.victor_name , matches.winner_rank_points FROM matches GROUP BY matches.victor_name ORDER BY count(*) desc LIMIT 1	wta_1_0
SELECT matches.victor_name , matches.winner_rank_points FROM matches GROUP BY matches.victor_name ORDER BY count(*) desc LIMIT 1	wta_1_0
SELECT matches.victor_name FROM matches WHERE matches.event_name = "Australian Open" ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_0
SELECT matches.victor_name FROM matches WHERE matches.event_name = "Australian Open" ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_0
SELECT matches.victor_name , matches.failure FROM matches ORDER BY matches.minutes desc LIMIT 1	wta_1_0
SELECT matches.victor_name , matches.failure FROM matches ORDER BY matches.minutes desc LIMIT 1	wta_1_0
SELECT avg(rankings.position) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_0
SELECT avg(rankings.position) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_0
SELECT sum(rankings.ranking_points) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_0
SELECT sum(rankings.ranking_points) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_0
SELECT count(*) , players.state_code FROM players GROUP BY players.state_code	wta_1_0
SELECT count(*) , players.state_code FROM players GROUP BY players.state_code	wta_1_0
SELECT players.state_code FROM players GROUP BY players.state_code ORDER BY count(*) desc LIMIT 1	wta_1_0
SELECT players.state_code FROM players GROUP BY players.state_code ORDER BY count(*) desc LIMIT 1	wta_1_0
SELECT players.state_code FROM players GROUP BY players.state_code HAVING count(*) > 50	wta_1_0
SELECT players.state_code FROM players GROUP BY players.state_code HAVING count(*) > 50	wta_1_0
SELECT sum(rankings.tours) , rankings.ranking_time FROM rankings GROUP BY rankings.ranking_time	wta_1_0
SELECT sum(rankings.tours) , rankings.ranking_time FROM rankings GROUP BY rankings.ranking_time	wta_1_0
SELECT DISTINCT matches.victor_name , matches.achiever_ranking FROM matches ORDER BY matches.victor_how_old asc LIMIT 3	wta_1_0
SELECT DISTINCT matches.victor_name , matches.achiever_ranking FROM matches ORDER BY matches.victor_how_old asc LIMIT 3	wta_1_0
SELECT count(DISTINCT matches.victor_name) FROM matches WHERE matches.event_name = "WTA Championships" and matches.victor_side = "L"	wta_1_0
SELECT count(DISTINCT matches.victor_name) FROM matches WHERE matches.event_name = "WTA Championships" and matches.victor_side = "L"	wta_1_0
SELECT players.given_name , players.state_code , players.birthday FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_0
SELECT players.given_name , players.state_code , players.birthday FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_0
SELECT players.given_name , players.born_date FROM players WHERE players.country_code = "USA"	wta_1_1
SELECT players.given_name , players.born_date FROM players WHERE players.country_code = "USA"	wta_1_1
SELECT min(matches.loser_position) FROM matches	wta_1_1
SELECT min(matches.loser_position) FROM matches	wta_1_1
SELECT matches.champ_name FROM matches WHERE matches.year = 2013 INTERSECT SELECT matches.champ_name FROM matches WHERE matches.year = 2016	wta_1_1
SELECT matches.champ_name FROM matches WHERE matches.year = 2013 INTERSECT SELECT matches.champ_name FROM matches WHERE matches.year = 2016	wta_1_1
SELECT players.country_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.country_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_1
SELECT players.country_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.country_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_1
SELECT players.given_name , players.country_code FROM players ORDER BY players.born_date asc LIMIT 1	wta_1_1
SELECT players.given_name , players.country_code FROM players ORDER BY players.born_date asc LIMIT 1	wta_1_1
SELECT players.given_name , players.last_name FROM players ORDER BY players.born_date asc	wta_1_1
SELECT players.given_name , players.last_name FROM players ORDER BY players.born_date asc	wta_1_1
SELECT players.given_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.born_date asc	wta_1_1
SELECT players.given_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.born_date asc	wta_1_1
SELECT players.country_code , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_1
SELECT players.country_code , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_1
SELECT matches.champ_name , matches.winner_rank_points FROM matches GROUP BY matches.champ_name ORDER BY count(*) desc LIMIT 1	wta_1_1
SELECT matches.champ_name , matches.winner_rank_points FROM matches GROUP BY matches.champ_name ORDER BY count(*) desc LIMIT 1	wta_1_1
SELECT matches.champ_name FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_1
SELECT matches.champ_name FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_1
SELECT matches.champ_name , matches.loser_name FROM matches ORDER BY matches.minutes desc LIMIT 1	wta_1_1
SELECT matches.champ_name , matches.loser_name FROM matches ORDER BY matches.minutes desc LIMIT 1	wta_1_1
SELECT avg(rankings.position) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_1
SELECT avg(rankings.position) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_1
SELECT sum(rankings.ranking_points) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_1
SELECT sum(rankings.ranking_points) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_1
SELECT DISTINCT matches.champ_name , matches.winner_rank FROM matches ORDER BY matches.winner_age asc LIMIT 3	wta_1_1
SELECT DISTINCT matches.champ_name , matches.winner_rank FROM matches ORDER BY matches.winner_age asc LIMIT 3	wta_1_1
SELECT count(DISTINCT matches.champ_name) FROM matches WHERE matches.tourney_name = "WTA Championships" and matches.winner_hand = "L"	wta_1_1
SELECT count(DISTINCT matches.champ_name) FROM matches WHERE matches.tourney_name = "WTA Championships" and matches.winner_hand = "L"	wta_1_1
SELECT players.given_name , players.country_code , players.born_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_1
SELECT players.given_name , players.country_code , players.born_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_1
SELECT avg(matches.champion_ranking) FROM matches	wta_1_2
SELECT avg(matches.champion_ranking) FROM matches	wta_1_2
SELECT matches.winner_name , matches.person_won_rank_scores FROM matches GROUP BY matches.winner_name ORDER BY count(*) desc LIMIT 1	wta_1_2
SELECT matches.winner_name , matches.person_won_rank_scores FROM matches GROUP BY matches.winner_name ORDER BY count(*) desc LIMIT 1	wta_1_2
SELECT matches.winner_name FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.person_won_rank_scores desc LIMIT 1	wta_1_2
SELECT matches.winner_name FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.person_won_rank_scores desc LIMIT 1	wta_1_2
SELECT DISTINCT matches.winner_name , matches.champion_ranking FROM matches ORDER BY matches.winner_age asc LIMIT 3	wta_1_2
SELECT DISTINCT matches.winner_name , matches.champion_ranking FROM matches ORDER BY matches.winner_age asc LIMIT 3	wta_1_2
SELECT players.first_name , players.country_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.person_won_rank_scores desc LIMIT 1	wta_1_2
SELECT players.first_name , players.country_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.person_won_rank_scores desc LIMIT 1	wta_1_2
SELECT players.given_name , players.birth_date FROM players WHERE players.nation_code = "USA"	wta_1_3
SELECT players.given_name , players.birth_date FROM players WHERE players.nation_code = "USA"	wta_1_3
SELECT avg(matches.total_loss) , avg(matches.winner_age) FROM matches	wta_1_3
SELECT avg(matches.total_loss) , avg(matches.winner_age) FROM matches	wta_1_3
SELECT avg(matches.champ_position) FROM matches	wta_1_3
SELECT avg(matches.champ_position) FROM matches	wta_1_3
SELECT min(matches.loser_ordering) FROM matches	wta_1_3
SELECT min(matches.loser_ordering) FROM matches	wta_1_3
SELECT count(DISTINCT players.nation_code) FROM players	wta_1_3
SELECT count(DISTINCT players.nation_code) FROM players	wta_1_3
SELECT matches.who_won FROM matches WHERE matches.year = 2013 INTERSECT SELECT matches.who_won FROM matches WHERE matches.year = 2016	wta_1_3
SELECT matches.who_won FROM matches WHERE matches.year = 2013 INTERSECT SELECT matches.who_won FROM matches WHERE matches.year = 2016	wta_1_3
SELECT players.nation_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.nation_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_3
SELECT players.nation_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.nation_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_3
SELECT players.given_name , players.nation_code FROM players ORDER BY players.birth_date asc LIMIT 1	wta_1_3
SELECT players.given_name , players.nation_code FROM players ORDER BY players.birth_date asc LIMIT 1	wta_1_3
SELECT players.given_name , players.last_name FROM players ORDER BY players.birth_date asc	wta_1_3
SELECT players.given_name , players.last_name FROM players ORDER BY players.birth_date asc	wta_1_3
SELECT players.given_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.birth_date asc	wta_1_3
SELECT players.given_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.birth_date asc	wta_1_3
SELECT players.nation_code , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_3
SELECT players.nation_code , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_3
SELECT matches.who_won , matches.winner_positionresult_points FROM matches GROUP BY matches.who_won ORDER BY count(*) desc LIMIT 1	wta_1_3
SELECT matches.who_won , matches.winner_positionresult_points FROM matches GROUP BY matches.who_won ORDER BY count(*) desc LIMIT 1	wta_1_3
SELECT matches.who_won FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.winner_positionresult_points desc LIMIT 1	wta_1_3
SELECT matches.who_won FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.winner_positionresult_points desc LIMIT 1	wta_1_3
SELECT matches.who_won , matches.loser_name FROM matches ORDER BY matches.minutes desc LIMIT 1	wta_1_3
SELECT matches.who_won , matches.loser_name FROM matches ORDER BY matches.minutes desc LIMIT 1	wta_1_3
SELECT avg(rankings.ranking) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_3
SELECT avg(rankings.ranking) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_3
SELECT sum(rankings.ranking_points) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_3
SELECT sum(rankings.ranking_points) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_3
SELECT count(*) , players.nation_code FROM players GROUP BY players.nation_code	wta_1_3
SELECT count(*) , players.nation_code FROM players GROUP BY players.nation_code	wta_1_3
SELECT players.nation_code FROM players GROUP BY players.nation_code ORDER BY count(*) desc LIMIT 1	wta_1_3
SELECT players.nation_code FROM players GROUP BY players.nation_code ORDER BY count(*) desc LIMIT 1	wta_1_3
SELECT players.nation_code FROM players GROUP BY players.nation_code HAVING count(*) > 50	wta_1_3
SELECT players.nation_code FROM players GROUP BY players.nation_code HAVING count(*) > 50	wta_1_3
SELECT sum(rankings.tours) , rankings.ranking_time FROM rankings GROUP BY rankings.ranking_time	wta_1_3
SELECT sum(rankings.tours) , rankings.ranking_time FROM rankings GROUP BY rankings.ranking_time	wta_1_3
SELECT DISTINCT matches.who_won , matches.champ_position FROM matches ORDER BY matches.winner_age asc LIMIT 3	wta_1_3
SELECT DISTINCT matches.who_won , matches.champ_position FROM matches ORDER BY matches.winner_age asc LIMIT 3	wta_1_3
SELECT count(DISTINCT matches.who_won) FROM matches WHERE matches.tourney_name = "WTA Championships" and matches.winner_hand = "L"	wta_1_3
SELECT count(DISTINCT matches.who_won) FROM matches WHERE matches.tourney_name = "WTA Championships" and matches.winner_hand = "L"	wta_1_3
SELECT players.given_name , players.nation_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_positionresult_points desc LIMIT 1	wta_1_3
SELECT players.given_name , players.nation_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_positionresult_points desc LIMIT 1	wta_1_3
SELECT players.given_name , players.birth_date FROM players WHERE players.nation_code = "USA"	wta_1_4
SELECT players.given_name , players.birth_date FROM players WHERE players.nation_code = "USA"	wta_1_4
SELECT avg(matches.loser_age) , avg(matches.champ_age) FROM matches	wta_1_4
SELECT avg(matches.loser_age) , avg(matches.champ_age) FROM matches	wta_1_4
SELECT count(DISTINCT players.nation_code) FROM players	wta_1_4
SELECT count(DISTINCT players.nation_code) FROM players	wta_1_4
SELECT count(DISTINCT matches.failure) FROM matches	wta_1_4
SELECT count(DISTINCT matches.failure) FROM matches	wta_1_4
SELECT matches.champ_name FROM matches WHERE matches.year = 2013 INTERSECT SELECT matches.champ_name FROM matches WHERE matches.year = 2016	wta_1_4
SELECT matches.champ_name FROM matches WHERE matches.year = 2013 INTERSECT SELECT matches.champ_name FROM matches WHERE matches.year = 2016	wta_1_4
SELECT players.nation_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.nation_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_4
SELECT players.nation_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.nation_code , players.given_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_4
SELECT players.given_name , players.nation_code FROM players ORDER BY players.birth_date asc LIMIT 1	wta_1_4
SELECT players.given_name , players.nation_code FROM players ORDER BY players.birth_date asc LIMIT 1	wta_1_4
SELECT players.given_name , players.last_name FROM players ORDER BY players.birth_date asc	wta_1_4
SELECT players.given_name , players.last_name FROM players ORDER BY players.birth_date asc	wta_1_4
SELECT players.given_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.birth_date asc	wta_1_4
SELECT players.given_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.birth_date asc	wta_1_4
SELECT players.nation_code , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_4
SELECT players.nation_code , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_4
SELECT matches.champ_name , matches.winner_tier_scores FROM matches GROUP BY matches.champ_name ORDER BY count(*) desc LIMIT 1	wta_1_4
SELECT matches.champ_name , matches.winner_tier_scores FROM matches GROUP BY matches.champ_name ORDER BY count(*) desc LIMIT 1	wta_1_4
SELECT matches.champ_name FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.winner_tier_scores desc LIMIT 1	wta_1_4
SELECT matches.champ_name FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.winner_tier_scores desc LIMIT 1	wta_1_4
SELECT matches.champ_name , matches.failure FROM matches ORDER BY matches.minutes desc LIMIT 1	wta_1_4
SELECT matches.champ_name , matches.failure FROM matches ORDER BY matches.minutes desc LIMIT 1	wta_1_4
SELECT avg(rankings.rank) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_4
SELECT avg(rankings.rank) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_4
SELECT sum(rankings.ranking_points) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_4
SELECT sum(rankings.ranking_points) , players.given_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.given_name	wta_1_4
SELECT count(*) , players.nation_code FROM players GROUP BY players.nation_code	wta_1_4
SELECT count(*) , players.nation_code FROM players GROUP BY players.nation_code	wta_1_4
SELECT players.nation_code FROM players GROUP BY players.nation_code ORDER BY count(*) desc LIMIT 1	wta_1_4
SELECT players.nation_code FROM players GROUP BY players.nation_code ORDER BY count(*) desc LIMIT 1	wta_1_4
SELECT players.nation_code FROM players GROUP BY players.nation_code HAVING count(*) > 50	wta_1_4
SELECT players.nation_code FROM players GROUP BY players.nation_code HAVING count(*) > 50	wta_1_4
SELECT DISTINCT matches.champ_name , matches.winner_rank FROM matches ORDER BY matches.champ_age asc LIMIT 3	wta_1_4
SELECT DISTINCT matches.champ_name , matches.winner_rank FROM matches ORDER BY matches.champ_age asc LIMIT 3	wta_1_4
SELECT count(DISTINCT matches.champ_name) FROM matches WHERE matches.tourney_name = "WTA Championships" and matches.success_side = "L"	wta_1_4
SELECT count(DISTINCT matches.champ_name) FROM matches WHERE matches.tourney_name = "WTA Championships" and matches.success_side = "L"	wta_1_4
SELECT players.given_name , players.nation_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_tier_scores desc LIMIT 1	wta_1_4
SELECT players.given_name , players.nation_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_tier_scores desc LIMIT 1	wta_1_4
SELECT ship.name , ship.vessel FROM ship ORDER BY ship.name desc	battle_death_0
SELECT death.killed , death.injured FROM death JOIN ship ON death.caused_by_ship_id = ship.id WHERE ship.vessel = "t"	battle_death_0
SELECT battle.name , battle.ending FROM battle WHERE battle.bulgarian_head != "Boril"	battle_death_0
SELECT DISTINCT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.missed_in_warfare WHERE ship.craft_classification = "Brig"	battle_death_0
SELECT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.missed_in_warfare JOIN death ON ship.id = death.caused_by_ship_id GROUP BY battle.id HAVING sum(death.killed) > 10	battle_death_0
SELECT battle.name FROM battle WHERE battle.bulgarian_head = "Kaloyan" and battle.latin_commander = "Baldwin I"	battle_death_0
SELECT count(DISTINCT battle.ending) FROM battle	battle_death_0
SELECT count(*) FROM battle WHERE battle.id NOT in (SELECT ship.missed_in_warfare FROM ship WHERE ship.vessel = "225")	battle_death_0
SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.missed_in_warfare WHERE ship.name = "Lettice" INTERSECT SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.missed_in_warfare WHERE ship.name = "HMS Atalanta"	battle_death_0
SELECT battle.name , battle.ending , battle.bulgarian_head FROM battle EXCEPT SELECT battle.name , battle.ending , battle.bulgarian_head FROM battle JOIN ship ON battle.id = ship.missed_in_warfare WHERE ship.spot = "English Channel"	battle_death_0
SELECT death.mark FROM death WHERE death.mark like "%East%"	battle_death_0
SELECT count(*) FROM ship WHERE ship.vessel_disposition = "Captured"	battle_death_1
SELECT battle.name , battle.result , battle.bulgarian_commander FROM battle EXCEPT SELECT battle.name , battle.result , battle.bulgarian_commander FROM battle JOIN ship ON battle.id = ship.lost_in_battle WHERE ship.site = "English Channel"	battle_death_1
SELECT death.notice FROM death WHERE death.notice like "%East%"	battle_death_1
SELECT ship.name , ship.heaviness FROM ship ORDER BY ship.name desc	battle_death_2
SELECT death.killed , death.injured FROM death JOIN ship ON death.caused_by_ship_id = ship.id WHERE ship.heaviness = "t"	battle_death_2
SELECT count(*) FROM battle WHERE battle.id NOT in (SELECT ship.lost_in_battle FROM ship WHERE ship.heaviness = "225")	battle_death_2
SELECT count(*) FROM ship WHERE ship.how_vessel_disposed = "Captured"	battle_death_3
SELECT battle.name , battle.consequence FROM battle WHERE battle.bulgarian_head != "Boril"	battle_death_3
SELECT battle.name FROM battle WHERE battle.bulgarian_head = "Kaloyan" and battle.latin_commander = "Baldwin I"	battle_death_3
SELECT count(DISTINCT battle.consequence) FROM battle	battle_death_3
SELECT battle.name , battle.consequence , battle.bulgarian_head FROM battle EXCEPT SELECT battle.name , battle.consequence , battle.bulgarian_head FROM battle JOIN ship ON battle.id = ship.lost_in_battle WHERE ship.position = "English Channel"	battle_death_3
SELECT count(*) FROM ship WHERE ship.how_ship_disposed = "Captured"	battle_death_4
SELECT battle.name , battle.effect FROM battle WHERE battle.bulgarian_commander != "Boril"	battle_death_4
SELECT DISTINCT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.forfeited_in_combat WHERE ship.ship_type = "Brig"	battle_death_4
SELECT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.forfeited_in_combat JOIN death ON ship.id = death.caused_by_ship_id GROUP BY battle.id HAVING sum(death.killed) > 10	battle_death_4
SELECT count(DISTINCT battle.effect) FROM battle	battle_death_4
SELECT count(*) FROM battle WHERE battle.id NOT in (SELECT ship.forfeited_in_combat FROM ship WHERE ship.tonnage = "225")	battle_death_4
SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.forfeited_in_combat WHERE ship.name = "Lettice" INTERSECT SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.forfeited_in_combat WHERE ship.name = "HMS Atalanta"	battle_death_4
SELECT battle.name , battle.effect , battle.bulgarian_commander FROM battle EXCEPT SELECT battle.name , battle.effect , battle.bulgarian_commander FROM battle JOIN ship ON battle.id = ship.forfeited_in_combat WHERE ship.location = "English Channel"	battle_death_4
SELECT death.info FROM death WHERE death.info like "%East%"	battle_death_4
SELECT Addresses.path_1 , Addresses.line_2 FROM Addresses	student_transcripts_tracking_0
SELECT Addresses.path_1 , Addresses.line_2 FROM Addresses	student_transcripts_tracking_0
SELECT Courses.course_description FROM Courses WHERE Courses.lesson_name = "math"	student_transcripts_tracking_0
SELECT Courses.course_description FROM Courses WHERE Courses.lesson_name = "math"	student_transcripts_tracking_0
SELECT Addresses.zip_postal_code FROM Addresses WHERE Addresses.capital_area = "Port Chelsea"	student_transcripts_tracking_0
SELECT Addresses.zip_postal_code FROM Addresses WHERE Addresses.capital_area = "Port Chelsea"	student_transcripts_tracking_0
SELECT count(DISTINCT Degree_Programs.degree_synopsis) FROM Degree_Programs	student_transcripts_tracking_0
SELECT count(DISTINCT Degree_Programs.degree_synopsis) FROM Degree_Programs	student_transcripts_tracking_0
SELECT Sections.section_designation , Sections.section_description FROM Sections	student_transcripts_tracking_0
SELECT Sections.section_designation , Sections.section_description FROM Sections	student_transcripts_tracking_0
SELECT Courses.lesson_name , Courses.course_id FROM Courses JOIN Sections ON Courses.course_id = Sections.course_id GROUP BY Courses.course_id HAVING count(*) <= 2	student_transcripts_tracking_0
SELECT Courses.lesson_name , Courses.course_id FROM Courses JOIN Sections ON Courses.course_id = Sections.course_id GROUP BY Courses.course_id HAVING count(*) <= 2	student_transcripts_tracking_0
SELECT Sections.section_designation FROM Sections ORDER BY Sections.section_designation desc	student_transcripts_tracking_0
SELECT Sections.section_designation FROM Sections ORDER BY Sections.section_designation desc	student_transcripts_tracking_0
SELECT Students.forename , Students.middle_name , Students.last_name , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id HAVING count(*) = 2	student_transcripts_tracking_0
SELECT Students.forename , Students.middle_name , Students.last_name , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id HAVING count(*) = 2	student_transcripts_tracking_0
SELECT DISTINCT Students.forename , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.degree_synopsis = "Bachelor"	student_transcripts_tracking_0
SELECT DISTINCT Students.forename , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.degree_synopsis = "Bachelor"	student_transcripts_tracking_0
SELECT Degree_Programs.degree_synopsis FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_synopsis ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Degree_Programs.degree_synopsis FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_synopsis ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Degree_Programs.degree_program_id , Degree_Programs.degree_synopsis FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_program_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Degree_Programs.degree_program_id , Degree_Programs.degree_synopsis FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_program_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Students.student_id , Students.forename , Students.middle_name , Students.last_name , count(*) , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Students.student_id , Students.forename , Students.middle_name , Students.last_name , count(*) , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT DISTINCT Courses.lesson_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.course_id = Student_Enrolment_Courses.course_id	student_transcripts_tracking_0
SELECT DISTINCT Courses.lesson_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.course_id = Student_Enrolment_Courses.course_id	student_transcripts_tracking_0
SELECT Courses.lesson_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.course_id = Student_Enrolment_Courses.course_id GROUP BY Courses.lesson_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Courses.lesson_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.course_id = Student_Enrolment_Courses.course_id GROUP BY Courses.lesson_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.record_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_0
SELECT Transcripts.record_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_0
SELECT Students.phone_number FROM Students WHERE Students.forename = "Timmothy" and Students.last_name = "Ward"	student_transcripts_tracking_0
SELECT Students.phone_number FROM Students WHERE Students.forename = "timmothy" and Students.last_name = "ward"	student_transcripts_tracking_0
SELECT Students.forename , Students.middle_name , Students.last_name FROM Students ORDER BY Students.initially_enrolled_at asc LIMIT 1	student_transcripts_tracking_0
SELECT Students.forename , Students.middle_name , Students.last_name FROM Students ORDER BY Students.initially_enrolled_at asc LIMIT 1	student_transcripts_tracking_0
SELECT Students.forename , Students.middle_name , Students.last_name FROM Students ORDER BY Students.time_of_depart asc LIMIT 1	student_transcripts_tracking_0
SELECT Students.forename , Students.middle_name , Students.last_name FROM Students ORDER BY Students.time_of_depart asc LIMIT 1	student_transcripts_tracking_0
SELECT Students.forename FROM Students WHERE Students.current_address_id != Students.permanent_address_id	student_transcripts_tracking_0
SELECT Students.forename FROM Students WHERE Students.current_address_id != Students.permanent_address_id	student_transcripts_tracking_0
SELECT Addresses.address_id , Addresses.path_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.address_id = Students.current_address_id GROUP BY Addresses.address_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Addresses.address_id , Addresses.path_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.address_id = Students.current_address_id GROUP BY Addresses.address_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT avg(Transcripts.record_time) FROM Transcripts	student_transcripts_tracking_0
SELECT avg(Transcripts.record_time) FROM Transcripts	student_transcripts_tracking_0
SELECT Transcripts.record_time , Transcripts.other_details FROM Transcripts ORDER BY Transcripts.record_time asc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.record_time , Transcripts.other_details FROM Transcripts ORDER BY Transcripts.record_time asc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.record_time FROM Transcripts ORDER BY Transcripts.record_time desc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.record_time FROM Transcripts ORDER BY Transcripts.record_time desc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.record_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_0
SELECT Transcripts.record_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_0
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_synopsis = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_synopsis = "Bachelor"	student_transcripts_tracking_0
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_synopsis = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_synopsis = "Bachelor"	student_transcripts_tracking_0
SELECT Students.specifics FROM Students ORDER BY Students.specifics desc	student_transcripts_tracking_0
SELECT Students.specifics FROM Students ORDER BY Students.specifics desc	student_transcripts_tracking_0
SELECT Sections.section_description FROM Sections WHERE Sections.section_designation = "h"	student_transcripts_tracking_0
SELECT Sections.section_description FROM Sections WHERE Sections.section_designation = "h"	student_transcripts_tracking_0
SELECT Students.forename FROM Students JOIN Addresses ON Students.permanent_address_id = Addresses.address_id WHERE Addresses.nation = "haiti" or Students.phone_number = "09700166582"	student_transcripts_tracking_0
SELECT Students.forename FROM Students JOIN Addresses ON Students.permanent_address_id = Addresses.address_id WHERE Addresses.nation = "haiti" or Students.phone_number = "09700166582"	student_transcripts_tracking_0
SELECT Courses.course_name , Courses.number_of_course FROM Courses JOIN Sections ON Courses.number_of_course = Sections.course_id GROUP BY Courses.number_of_course HAVING count(*) <= 2	student_transcripts_tracking_1
SELECT Courses.course_name , Courses.number_of_course FROM Courses JOIN Sections ON Courses.number_of_course = Sections.course_id GROUP BY Courses.number_of_course HAVING count(*) <= 2	student_transcripts_tracking_1
SELECT Departments.specification FROM Departments WHERE Departments.department_name like "%computer%"	student_transcripts_tracking_1
SELECT Departments.specification FROM Departments WHERE Departments.department_name like "%computer%"	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.ending_name , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id HAVING count(*) = 2	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.ending_name , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id HAVING count(*) = 2	student_transcripts_tracking_1
SELECT DISTINCT Students.first_name , Students.middle_name , Students.ending_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.degree_summary_name = "Bachelor"	student_transcripts_tracking_1
SELECT DISTINCT Students.first_name , Students.middle_name , Students.ending_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.degree_summary_name = "Bachelor"	student_transcripts_tracking_1
SELECT Students.student_id , Students.first_name , Students.middle_name , Students.ending_name , count(*) , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Students.student_id , Students.first_name , Students.middle_name , Students.ending_name , count(*) , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT DISTINCT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.number_of_course = Student_Enrolment_Courses.course_id	student_transcripts_tracking_1
SELECT DISTINCT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.number_of_course = Student_Enrolment_Courses.course_id	student_transcripts_tracking_1
SELECT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.number_of_course = Student_Enrolment_Courses.course_id GROUP BY Courses.course_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.number_of_course = Student_Enrolment_Courses.course_id GROUP BY Courses.course_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Students.ending_name FROM Students JOIN Addresses ON Students.current_address_id = Addresses.address_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.ending_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id	student_transcripts_tracking_1
SELECT Students.ending_name FROM Students JOIN Addresses ON Students.current_address_id = Addresses.address_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.ending_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id	student_transcripts_tracking_1
SELECT Students.cell_mobile_number FROM Students WHERE Students.first_name = "Timmothy" and Students.ending_name = "Ward"	student_transcripts_tracking_1
SELECT Students.cell_mobile_number FROM Students WHERE Students.first_name = "timmothy" and Students.ending_name = "ward"	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.ending_name FROM Students ORDER BY Students.date_first_registered asc LIMIT 1	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.ending_name FROM Students ORDER BY Students.date_first_registered asc LIMIT 1	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.ending_name FROM Students ORDER BY Students.when_left asc LIMIT 1	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.ending_name FROM Students ORDER BY Students.when_left asc LIMIT 1	student_transcripts_tracking_1
SELECT Students.see_also FROM Students ORDER BY Students.see_also desc	student_transcripts_tracking_1
SELECT Students.see_also FROM Students ORDER BY Students.see_also desc	student_transcripts_tracking_1
SELECT Courses.course_details FROM Courses WHERE Courses.course_name = "math"	student_transcripts_tracking_2
SELECT Courses.course_details FROM Courses WHERE Courses.course_name = "math"	student_transcripts_tracking_2
SELECT Transcripts.transcript_date , Transcripts.see_also FROM Transcripts ORDER BY Transcripts.transcript_date asc LIMIT 1	student_transcripts_tracking_2
SELECT Transcripts.transcript_date , Transcripts.see_also FROM Transcripts ORDER BY Transcripts.transcript_date asc LIMIT 1	student_transcripts_tracking_2
SELECT Addresses.line_1 , Addresses.path_2 FROM Addresses	student_transcripts_tracking_3
SELECT Addresses.line_1 , Addresses.path_2 FROM Addresses	student_transcripts_tracking_3
SELECT Courses.course_description FROM Courses WHERE Courses.course_designation = "math"	student_transcripts_tracking_3
SELECT Courses.course_description FROM Courses WHERE Courses.course_designation = "math"	student_transcripts_tracking_3
SELECT count(DISTINCT Degree_Programs.degree_digest_designation) FROM Degree_Programs	student_transcripts_tracking_3
SELECT count(DISTINCT Degree_Programs.degree_digest_designation) FROM Degree_Programs	student_transcripts_tracking_3
SELECT Sections.section_name , Sections.detailing FROM Sections	student_transcripts_tracking_3
SELECT Sections.section_name , Sections.detailing FROM Sections	student_transcripts_tracking_3
SELECT Courses.course_designation , Courses.prerequisite FROM Courses JOIN Sections ON Courses.prerequisite = Sections.course_id GROUP BY Courses.prerequisite HAVING count(*) <= 2	student_transcripts_tracking_3
SELECT Courses.course_designation , Courses.prerequisite FROM Courses JOIN Sections ON Courses.prerequisite = Sections.course_id GROUP BY Courses.prerequisite HAVING count(*) <= 2	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.surname , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id HAVING count(*) = 2	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.surname , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id HAVING count(*) = 2	student_transcripts_tracking_3
SELECT DISTINCT Students.first_name , Students.middle_name , Students.surname FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.degree_digest_designation = "Bachelor"	student_transcripts_tracking_3
SELECT DISTINCT Students.first_name , Students.middle_name , Students.surname FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.degree_digest_designation = "Bachelor"	student_transcripts_tracking_3
SELECT Degree_Programs.degree_digest_designation FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_digest_designation ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Degree_Programs.degree_digest_designation FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_digest_designation ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Degree_Programs.degree_program_id , Degree_Programs.degree_digest_designation FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_program_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Degree_Programs.degree_program_id , Degree_Programs.degree_digest_designation FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_program_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Students.student_id , Students.first_name , Students.middle_name , Students.surname , count(*) , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Students.student_id , Students.first_name , Students.middle_name , Students.surname , count(*) , Students.student_id FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id GROUP BY Students.student_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT DISTINCT Courses.course_designation FROM Courses JOIN Student_Enrolment_Courses ON Courses.prerequisite = Student_Enrolment_Courses.course_id	student_transcripts_tracking_3
SELECT DISTINCT Courses.course_designation FROM Courses JOIN Student_Enrolment_Courses ON Courses.prerequisite = Student_Enrolment_Courses.course_id	student_transcripts_tracking_3
SELECT Courses.course_designation FROM Courses JOIN Student_Enrolment_Courses ON Courses.prerequisite = Student_Enrolment_Courses.course_id GROUP BY Courses.course_designation ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Courses.course_designation FROM Courses JOIN Student_Enrolment_Courses ON Courses.prerequisite = Student_Enrolment_Courses.course_id GROUP BY Courses.course_designation ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Students.surname FROM Students JOIN Addresses ON Students.current_address_id = Addresses.address_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.surname FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id	student_transcripts_tracking_3
SELECT Students.surname FROM Students JOIN Addresses ON Students.current_address_id = Addresses.address_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.surname FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id	student_transcripts_tracking_3
SELECT Transcripts.when_record , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_3
SELECT Transcripts.when_record , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_3
SELECT Students.cell_mobile_number FROM Students WHERE Students.first_name = "Timmothy" and Students.surname = "Ward"	student_transcripts_tracking_3
SELECT Students.cell_mobile_number FROM Students WHERE Students.first_name = "timmothy" and Students.surname = "ward"	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.surname FROM Students ORDER BY Students.date_first_registered asc LIMIT 1	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.surname FROM Students ORDER BY Students.date_first_registered asc LIMIT 1	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.surname FROM Students ORDER BY Students.date_left asc LIMIT 1	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.surname FROM Students ORDER BY Students.date_left asc LIMIT 1	student_transcripts_tracking_3
SELECT Addresses.address_id , Addresses.line_1 , Addresses.path_2 FROM Addresses JOIN Students ON Addresses.address_id = Students.current_address_id GROUP BY Addresses.address_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Addresses.address_id , Addresses.line_1 , Addresses.path_2 FROM Addresses JOIN Students ON Addresses.address_id = Students.current_address_id GROUP BY Addresses.address_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT avg(Transcripts.when_record) FROM Transcripts	student_transcripts_tracking_3
SELECT avg(Transcripts.when_record) FROM Transcripts	student_transcripts_tracking_3
SELECT Transcripts.when_record , Transcripts.other_details FROM Transcripts ORDER BY Transcripts.when_record asc LIMIT 1	student_transcripts_tracking_3
SELECT Transcripts.when_record , Transcripts.other_details FROM Transcripts ORDER BY Transcripts.when_record asc LIMIT 1	student_transcripts_tracking_3
SELECT Transcripts.when_record FROM Transcripts ORDER BY Transcripts.when_record desc LIMIT 1	student_transcripts_tracking_3
SELECT Transcripts.when_record FROM Transcripts ORDER BY Transcripts.when_record desc LIMIT 1	student_transcripts_tracking_3
SELECT Transcripts.when_record , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_3
SELECT Transcripts.when_record , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_3
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_digest_designation = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_digest_designation = "Bachelor"	student_transcripts_tracking_3
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_digest_designation = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_digest_designation = "Bachelor"	student_transcripts_tracking_3
SELECT Students.student_additional_information FROM Students ORDER BY Students.student_additional_information desc	student_transcripts_tracking_3
SELECT Students.student_additional_information FROM Students ORDER BY Students.student_additional_information desc	student_transcripts_tracking_3
SELECT Sections.detailing FROM Sections WHERE Sections.section_name = "h"	student_transcripts_tracking_3
SELECT Sections.detailing FROM Sections WHERE Sections.section_name = "h"	student_transcripts_tracking_3
SELECT Addresses.line_1 , Addresses.path_2 FROM Addresses	student_transcripts_tracking_4
SELECT Addresses.line_1 , Addresses.path_2 FROM Addresses	student_transcripts_tracking_4
SELECT count(DISTINCT Degree_Programs.summary_appellation) FROM Degree_Programs	student_transcripts_tracking_4
SELECT count(DISTINCT Degree_Programs.summary_appellation) FROM Degree_Programs	student_transcripts_tracking_4
SELECT Sections.session_name , Sections.section_description FROM Sections	student_transcripts_tracking_4
SELECT Sections.session_name , Sections.section_description FROM Sections	student_transcripts_tracking_4
SELECT Courses.course_name , Courses.prerequisite FROM Courses JOIN Sections ON Courses.prerequisite = Sections.course_id GROUP BY Courses.prerequisite HAVING count(*) <= 2	student_transcripts_tracking_4
SELECT Courses.course_name , Courses.prerequisite FROM Courses JOIN Sections ON Courses.prerequisite = Sections.course_id GROUP BY Courses.prerequisite HAVING count(*) <= 2	student_transcripts_tracking_4
SELECT Sections.session_name FROM Sections ORDER BY Sections.session_name desc	student_transcripts_tracking_4
SELECT Sections.session_name FROM Sections ORDER BY Sections.session_name desc	student_transcripts_tracking_4
SELECT Semesters.semester_designation , Semesters.semester_id FROM Semesters JOIN Student_Enrolment ON Semesters.semester_id = Student_Enrolment.semester_id GROUP BY Semesters.semester_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Semesters.semester_designation , Semesters.semester_id FROM Semesters JOIN Student_Enrolment ON Semesters.semester_id = Student_Enrolment.semester_id GROUP BY Semesters.semester_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.summary_appellation = "Bachelor"	student_transcripts_tracking_4
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_program_id WHERE Degree_Programs.summary_appellation = "Bachelor"	student_transcripts_tracking_4
SELECT Degree_Programs.summary_appellation FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.summary_appellation ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Degree_Programs.summary_appellation FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.summary_appellation ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Degree_Programs.degree_program_id , Degree_Programs.summary_appellation FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_program_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Degree_Programs.degree_program_id , Degree_Programs.summary_appellation FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_program_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Semesters.semester_designation FROM Semesters WHERE Semesters.semester_id NOT in (SELECT Student_Enrolment.semester_id FROM Student_Enrolment)	student_transcripts_tracking_4
SELECT Semesters.semester_designation FROM Semesters WHERE Semesters.semester_id NOT in (SELECT Student_Enrolment.semester_id FROM Student_Enrolment)	student_transcripts_tracking_4
SELECT DISTINCT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.prerequisite = Student_Enrolment_Courses.course_id	student_transcripts_tracking_4
SELECT DISTINCT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.prerequisite = Student_Enrolment_Courses.course_id	student_transcripts_tracking_4
SELECT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.prerequisite = Student_Enrolment_Courses.course_id GROUP BY Courses.course_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.prerequisite = Student_Enrolment_Courses.course_id GROUP BY Courses.course_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.record_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_4
SELECT Transcripts.record_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id HAVING count(*) >= 2	student_transcripts_tracking_4
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.day_initally_itemized asc LIMIT 1	student_transcripts_tracking_4
SELECT Students.first_name , Students.middle_name , Students.last_name FROM Students ORDER BY Students.day_initally_itemized asc LIMIT 1	student_transcripts_tracking_4
SELECT Addresses.address_id , Addresses.line_1 , Addresses.path_2 FROM Addresses JOIN Students ON Addresses.address_id = Students.current_address_id GROUP BY Addresses.address_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Addresses.address_id , Addresses.line_1 , Addresses.path_2 FROM Addresses JOIN Students ON Addresses.address_id = Students.current_address_id GROUP BY Addresses.address_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT avg(Transcripts.record_time) FROM Transcripts	student_transcripts_tracking_4
SELECT avg(Transcripts.record_time) FROM Transcripts	student_transcripts_tracking_4
SELECT Transcripts.record_time , Transcripts.particularities FROM Transcripts ORDER BY Transcripts.record_time asc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.record_time , Transcripts.particularities FROM Transcripts ORDER BY Transcripts.record_time asc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.record_time FROM Transcripts ORDER BY Transcripts.record_time desc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.record_time FROM Transcripts ORDER BY Transcripts.record_time desc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.record_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.record_time , Transcript_Contents.transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY count(*) asc LIMIT 1	student_transcripts_tracking_4
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.summary_appellation = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.summary_appellation = "Bachelor"	student_transcripts_tracking_4
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.summary_appellation = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_program_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.summary_appellation = "Bachelor"	student_transcripts_tracking_4
SELECT Sections.section_description FROM Sections WHERE Sections.session_name = "h"	student_transcripts_tracking_4
SELECT Sections.section_description FROM Sections WHERE Sections.session_name = "h"	student_transcripts_tracking_4
SELECT Cartoon.cover_title FROM Cartoon ORDER BY Cartoon.cover_title asc	tvshow_0
SELECT Cartoon.cover_title FROM Cartoon ORDER BY Cartoon.cover_title asc	tvshow_0
SELECT Cartoon.cover_title FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_0
SELECT Cartoon.cover_title FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_0
SELECT Cartoon.cover_title , Cartoon.Directed_by FROM Cartoon ORDER BY Cartoon.earliest_air_date asc	tvshow_0
SELECT Cartoon.cover_title , Cartoon.Directed_by FROM Cartoon ORDER BY Cartoon.earliest_air_date asc	tvshow_0
SELECT Cartoon.cover_title FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones" or Cartoon.Directed_by = "Brandon Vietti"	tvshow_0
SELECT Cartoon.cover_title FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones" or Cartoon.Directed_by = "Brandon Vietti"	tvshow_0
SELECT count(DISTINCT TV_Channel.series_name) , count(DISTINCT TV_Channel.substance) FROM TV_Channel	tvshow_0
SELECT count(DISTINCT TV_Channel.series_name) , count(DISTINCT TV_Channel.substance) FROM TV_Channel	tvshow_0
SELECT TV_Channel.substance FROM TV_Channel WHERE TV_Channel.series_name = "Sky Radio"	tvshow_0
SELECT TV_Channel.substance FROM TV_Channel WHERE TV_Channel.series_name = "Sky Radio"	tvshow_0
SELECT count(*) FROM TV_Channel WHERE TV_Channel.dialect = "English"	tvshow_0
SELECT count(*) FROM TV_Channel WHERE TV_Channel.dialect = "English"	tvshow_0
SELECT TV_Channel.dialect , count(*) FROM TV_Channel GROUP BY TV_Channel.dialect ORDER BY count(*) asc LIMIT 1	tvshow_0
SELECT TV_Channel.dialect , count(*) FROM TV_Channel GROUP BY TV_Channel.dialect ORDER BY count(*) asc LIMIT 1	tvshow_0
SELECT TV_Channel.dialect , count(*) FROM TV_Channel GROUP BY TV_Channel.dialect	tvshow_0
SELECT TV_Channel.dialect , count(*) FROM TV_Channel GROUP BY TV_Channel.dialect	tvshow_0
SELECT TV_Channel.series_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.cover_title = "The Rise of the Blue Beetle!"	tvshow_0
SELECT TV_Channel.series_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.cover_title = "The Rise of the Blue Beetle!"	tvshow_0
SELECT Cartoon.cover_title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE TV_Channel.series_name = "Sky Radio"	tvshow_0
SELECT Cartoon.cover_title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE TV_Channel.series_name = "Sky Radio"	tvshow_0
SELECT TV_series.chapter FROM TV_series ORDER BY TV_series.grades asc	tvshow_0
SELECT TV_series.chapter FROM TV_series ORDER BY TV_series.grades asc	tvshow_0
SELECT TV_series.chapter , TV_series.grades FROM TV_series ORDER BY TV_series.grades desc LIMIT 3	tvshow_0
SELECT TV_series.chapter , TV_series.grades FROM TV_series ORDER BY TV_series.grades desc LIMIT 3	tvshow_0
SELECT max(TV_series.portion) , min(TV_series.portion) FROM TV_series	tvshow_0
SELECT max(TV_series.portion) , min(TV_series.portion) FROM TV_series	tvshow_0
SELECT TV_series.release_day FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_0
SELECT TV_series.release_day FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_0
SELECT TV_series.every_week_ranking FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_0
SELECT TV_series.every_week_ranking FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_0
SELECT TV_Channel.series_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_station WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_0
SELECT TV_Channel.series_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_station WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_0
SELECT TV_series.chapter FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_station WHERE TV_Channel.series_name = "Sky Radio"	tvshow_0
SELECT TV_series.chapter FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_station WHERE TV_Channel.series_name = "Sky Radio"	tvshow_0
SELECT Cartoon.manufacture_codification , Cartoon.medium FROM Cartoon ORDER BY Cartoon.earliest_air_date desc LIMIT 1	tvshow_0
SELECT Cartoon.manufacture_codification , Cartoon.medium FROM Cartoon ORDER BY Cartoon.earliest_air_date desc LIMIT 1	tvshow_0
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.Written_by = "Todd Casey"	tvshow_0
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.Written_by = "Todd Casey"	tvshow_0
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.Written_by = "Todd Casey"	tvshow_0
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.Written_by = "Todd Casey"	tvshow_0
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.Directed_by = "Michael Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_0
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.Directed_by = "Michael Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.medium WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_0
SELECT TV_Channel.pixel_aspect_percentage_par , TV_Channel.Country FROM TV_Channel WHERE TV_Channel.dialect != "English"	tvshow_0
SELECT TV_Channel.pixel_aspect_percentage_par , TV_Channel.Country FROM TV_Channel WHERE TV_Channel.dialect != "English"	tvshow_0
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.medium FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_0
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.medium FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_0
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.medium FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones")	tvshow_0
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.medium FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones")	tvshow_0
SELECT Cartoon.Title , Cartoon.Directed_by FROM Cartoon ORDER BY Cartoon.initial_air_date asc	tvshow_1
SELECT Cartoon.Title , Cartoon.Directed_by FROM Cartoon ORDER BY Cartoon.initial_air_date asc	tvshow_1
SELECT TV_series.chapter FROM TV_series ORDER BY TV_series.Rating asc	tvshow_1
SELECT TV_series.chapter FROM TV_series ORDER BY TV_series.Rating asc	tvshow_1
SELECT TV_series.chapter , TV_series.Rating FROM TV_series ORDER BY TV_series.Rating desc LIMIT 3	tvshow_1
SELECT TV_series.chapter , TV_series.Rating FROM TV_series ORDER BY TV_series.Rating desc LIMIT 3	tvshow_1
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_1
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_1
SELECT TV_series.every_week_ranking FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_1
SELECT TV_series.every_week_ranking FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_1
SELECT TV_Channel.series_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_channel WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_1
SELECT TV_Channel.series_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_channel WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_1
SELECT TV_series.chapter FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_channel WHERE TV_Channel.series_name = "Sky Radio"	tvshow_1
SELECT TV_series.chapter FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_channel WHERE TV_Channel.series_name = "Sky Radio"	tvshow_1
SELECT Cartoon.manufacture_codification , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.initial_air_date desc LIMIT 1	tvshow_1
SELECT Cartoon.manufacture_codification , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.initial_air_date desc LIMIT 1	tvshow_1
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director = "Ben Jones"	tvshow_2
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director = "Ben Jones"	tvshow_2
SELECT count(*) FROM Cartoon WHERE Cartoon.scripted_by = "Joseph Kuhr"	tvshow_2
SELECT count(*) FROM Cartoon WHERE Cartoon.scripted_by = "Joseph Kuhr"	tvshow_2
SELECT Cartoon.Title , Cartoon.director FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_2
SELECT Cartoon.Title , Cartoon.director FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_2
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director = "Ben Jones" or Cartoon.director = "Brandon Vietti"	tvshow_2
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.director = "Ben Jones" or Cartoon.director = "Brandon Vietti"	tvshow_2
SELECT count(*) , Cartoon.director FROM Cartoon GROUP BY Cartoon.director	tvshow_2
SELECT count(*) , Cartoon.director FROM Cartoon GROUP BY Cartoon.director	tvshow_2
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.scripted_by = "Todd Casey"	tvshow_2
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.scripted_by = "Todd Casey"	tvshow_2
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.scripted_by = "Todd Casey"	tvshow_2
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.scripted_by = "Todd Casey"	tvshow_2
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director = "Michael Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director = "Ben Jones"	tvshow_2
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director = "Michael Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.director = "Ben Jones"	tvshow_2
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director = "Ben Jones"	tvshow_2
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director = "Ben Jones"	tvshow_2
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director = "Ben Jones")	tvshow_2
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.director = "Ben Jones")	tvshow_2
SELECT Cartoon.cover_name FROM Cartoon ORDER BY Cartoon.cover_name asc	tvshow_3
SELECT Cartoon.cover_name FROM Cartoon ORDER BY Cartoon.cover_name asc	tvshow_3
SELECT Cartoon.cover_name FROM Cartoon WHERE Cartoon.conductor = "Ben Jones"	tvshow_3
SELECT Cartoon.cover_name FROM Cartoon WHERE Cartoon.conductor = "Ben Jones"	tvshow_3
SELECT Cartoon.cover_name , Cartoon.conductor FROM Cartoon ORDER BY Cartoon.initial_air_date asc	tvshow_3
SELECT Cartoon.cover_name , Cartoon.conductor FROM Cartoon ORDER BY Cartoon.initial_air_date asc	tvshow_3
SELECT Cartoon.cover_name FROM Cartoon WHERE Cartoon.conductor = "Ben Jones" or Cartoon.conductor = "Brandon Vietti"	tvshow_3
SELECT Cartoon.cover_name FROM Cartoon WHERE Cartoon.conductor = "Ben Jones" or Cartoon.conductor = "Brandon Vietti"	tvshow_3
SELECT count(DISTINCT TV_Channel.series_name) , count(DISTINCT TV_Channel.substance) FROM TV_Channel	tvshow_3
SELECT count(DISTINCT TV_Channel.series_name) , count(DISTINCT TV_Channel.substance) FROM TV_Channel	tvshow_3
SELECT TV_Channel.substance FROM TV_Channel WHERE TV_Channel.series_name = "Sky Radio"	tvshow_3
SELECT TV_Channel.substance FROM TV_Channel WHERE TV_Channel.series_name = "Sky Radio"	tvshow_3
SELECT TV_Channel.series_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.cover_name = "The Rise of the Blue Beetle!"	tvshow_3
SELECT TV_Channel.series_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.cover_name = "The Rise of the Blue Beetle!"	tvshow_3
SELECT Cartoon.cover_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE TV_Channel.series_name = "Sky Radio"	tvshow_3
SELECT Cartoon.cover_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE TV_Channel.series_name = "Sky Radio"	tvshow_3
SELECT max(TV_series.portion) , min(TV_series.portion) FROM TV_series	tvshow_3
SELECT max(TV_series.portion) , min(TV_series.portion) FROM TV_series	tvshow_3
SELECT TV_series.first_show FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_3
SELECT TV_series.first_show FROM TV_series WHERE TV_series.Episode = "A Love of a Lifetime"	tvshow_3
SELECT count(*) , Cartoon.conductor FROM Cartoon GROUP BY Cartoon.conductor	tvshow_3
SELECT count(*) , Cartoon.conductor FROM Cartoon GROUP BY Cartoon.conductor	tvshow_3
SELECT Cartoon.manufacture_codification , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.initial_air_date desc LIMIT 1	tvshow_3
SELECT Cartoon.manufacture_codification , Cartoon.Channel FROM Cartoon ORDER BY Cartoon.initial_air_date desc LIMIT 1	tvshow_3
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.conductor = "Michael Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.conductor = "Ben Jones"	tvshow_3
SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.conductor = "Michael Chang" INTERSECT SELECT TV_Channel.series_name , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.conductor = "Ben Jones"	tvshow_3
SELECT TV_Channel.pixel_aspect_percentage_par , TV_Channel.Country FROM TV_Channel WHERE TV_Channel.Language != "English"	tvshow_3
SELECT TV_Channel.pixel_aspect_percentage_par , TV_Channel.Country FROM TV_Channel WHERE TV_Channel.Language != "English"	tvshow_3
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.conductor = "Ben Jones"	tvshow_3
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.conductor = "Ben Jones"	tvshow_3
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.conductor = "Ben Jones")	tvshow_3
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.conductor = "Ben Jones")	tvshow_3
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.conductor = "Ben Jones"	tvshow_4
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.conductor = "Ben Jones"	tvshow_4
SELECT count(*) FROM Cartoon WHERE Cartoon.writer = "Joseph Kuhr"	tvshow_4
SELECT count(*) FROM Cartoon WHERE Cartoon.writer = "Joseph Kuhr"	tvshow_4
SELECT Cartoon.Title , Cartoon.conductor FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_4
SELECT Cartoon.Title , Cartoon.conductor FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_4
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.conductor = "Ben Jones" or Cartoon.conductor = "Brandon Vietti"	tvshow_4
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.conductor = "Ben Jones" or Cartoon.conductor = "Brandon Vietti"	tvshow_4
SELECT count(DISTINCT TV_Channel.series_designation) , count(DISTINCT TV_Channel.Content) FROM TV_Channel	tvshow_4
SELECT count(DISTINCT TV_Channel.series_designation) , count(DISTINCT TV_Channel.Content) FROM TV_Channel	tvshow_4
SELECT TV_Channel.Content FROM TV_Channel WHERE TV_Channel.series_designation = "Sky Radio"	tvshow_4
SELECT TV_Channel.Content FROM TV_Channel WHERE TV_Channel.series_designation = "Sky Radio"	tvshow_4
SELECT TV_Channel.pack_possible_choices FROM TV_Channel WHERE TV_Channel.series_designation = "Sky Radio"	tvshow_4
SELECT TV_Channel.pack_possible_choices FROM TV_Channel WHERE TV_Channel.series_designation = "Sky Radio"	tvshow_4
SELECT TV_Channel.series_designation FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_4
SELECT TV_Channel.series_designation FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_4
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE TV_Channel.series_designation = "Sky Radio"	tvshow_4
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE TV_Channel.series_designation = "Sky Radio"	tvshow_4
SELECT TV_series.chapter FROM TV_series ORDER BY TV_series.Rating asc	tvshow_4
SELECT TV_series.chapter FROM TV_series ORDER BY TV_series.Rating asc	tvshow_4
SELECT TV_series.chapter , TV_series.Rating FROM TV_series ORDER BY TV_series.Rating desc LIMIT 3	tvshow_4
SELECT TV_series.chapter , TV_series.Rating FROM TV_series ORDER BY TV_series.Rating desc LIMIT 3	tvshow_4
SELECT max(TV_series.portion) , min(TV_series.portion) FROM TV_series	tvshow_4
SELECT max(TV_series.portion) , min(TV_series.portion) FROM TV_series	tvshow_4
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_4
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_4
SELECT TV_series.Weekly_Rank FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_4
SELECT TV_series.Weekly_Rank FROM TV_series WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_4
SELECT TV_Channel.series_designation FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_channel WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_4
SELECT TV_Channel.series_designation FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_channel WHERE TV_series.chapter = "A Love of a Lifetime"	tvshow_4
SELECT TV_series.chapter FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_channel WHERE TV_Channel.series_designation = "Sky Radio"	tvshow_4
SELECT TV_series.chapter FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.tv_channel WHERE TV_Channel.series_designation = "Sky Radio"	tvshow_4
SELECT count(*) , Cartoon.conductor FROM Cartoon GROUP BY Cartoon.conductor	tvshow_4
SELECT count(*) , Cartoon.conductor FROM Cartoon GROUP BY Cartoon.conductor	tvshow_4
SELECT TV_Channel.pack_possible_choices , TV_Channel.series_designation FROM TV_Channel WHERE TV_Channel.Hight_definition_TV = "yes"	tvshow_4
SELECT TV_Channel.pack_possible_choices , TV_Channel.series_designation FROM TV_Channel WHERE TV_Channel.Hight_definition_TV = "yes"	tvshow_4
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer = "Todd Casey"	tvshow_4
SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer = "Todd Casey"	tvshow_4
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer = "Todd Casey"	tvshow_4
SELECT TV_Channel.Country FROM TV_Channel EXCEPT SELECT TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.writer = "Todd Casey"	tvshow_4
SELECT TV_Channel.series_designation , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.conductor = "Michael Chang" INTERSECT SELECT TV_Channel.series_designation , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.conductor = "Ben Jones"	tvshow_4
SELECT TV_Channel.series_designation , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.conductor = "Michael Chang" INTERSECT SELECT TV_Channel.series_designation , TV_Channel.Country FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.conductor = "Ben Jones"	tvshow_4
SELECT TV_Channel.pixel_aspect_relative_amount_par , TV_Channel.Country FROM TV_Channel WHERE TV_Channel.Language != "English"	tvshow_4
SELECT TV_Channel.pixel_aspect_relative_amount_par , TV_Channel.Country FROM TV_Channel WHERE TV_Channel.Language != "English"	tvshow_4
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.conductor = "Ben Jones"	tvshow_4
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.conductor = "Ben Jones"	tvshow_4
SELECT TV_Channel.pack_possible_choices FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.conductor = "Ben Jones")	tvshow_4
SELECT TV_Channel.pack_possible_choices FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.conductor = "Ben Jones")	tvshow_4
SELECT poker_player.last_table_made , poker_player.highest_terminate FROM poker_player	poker_player_0
SELECT poker_player.last_table_made , poker_player.highest_terminate FROM poker_player	poker_player_0
SELECT poker_player.money_tier FROM poker_player ORDER BY poker_player.Earnings desc LIMIT 1	poker_player_0
SELECT poker_player.money_tier FROM poker_player ORDER BY poker_player.Earnings desc LIMIT 1	poker_player_0
SELECT max(poker_player.last_table_made) FROM poker_player WHERE poker_player.Earnings < 200000	poker_player_0
SELECT max(poker_player.last_table_made) FROM poker_player WHERE poker_player.Earnings < 200000	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.last_table_made asc	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.last_table_made asc	poker_player_0
SELECT people.time_of_born FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_0
SELECT people.time_of_born FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_0
SELECT poker_player.money_tier FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_0
SELECT poker_player.money_tier FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_0
SELECT people.Name , people.time_of_born FROM people ORDER BY people.Name asc	poker_player_0
SELECT people.Name , people.time_of_born FROM people ORDER BY people.Name asc	poker_player_0
SELECT poker_player.income FROM poker_player ORDER BY poker_player.income desc	poker_player_1
SELECT poker_player.income FROM poker_player ORDER BY poker_player.income desc	poker_player_1
SELECT avg(poker_player.income) FROM poker_player	poker_player_1
SELECT avg(poker_player.income) FROM poker_player	poker_player_1
SELECT poker_player.currency_standing FROM poker_player ORDER BY poker_player.income desc LIMIT 1	poker_player_1
SELECT poker_player.currency_standing FROM poker_player ORDER BY poker_player.income desc LIMIT 1	poker_player_1
SELECT max(poker_player.Final_Table_Made) FROM poker_player WHERE poker_player.income < 200000	poker_player_1
SELECT max(poker_player.Final_Table_Made) FROM poker_player WHERE poker_player.income < 200000	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE poker_player.income > 300000	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE poker_player.income > 300000	poker_player_1
SELECT people.Birth_Date FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.income asc LIMIT 1	poker_player_1
SELECT people.Birth_Date FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.income asc LIMIT 1	poker_player_1
SELECT poker_player.currency_standing FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_1
SELECT poker_player.currency_standing FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_1
SELECT avg(poker_player.income) FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE people.Height > 200	poker_player_1
SELECT avg(poker_player.income) FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE people.Height > 200	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.income desc	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.income desc	poker_player_1
SELECT poker_player.money_tier FROM poker_player ORDER BY poker_player.Earnings desc LIMIT 1	poker_player_2
SELECT poker_player.money_tier FROM poker_player ORDER BY poker_player.Earnings desc LIMIT 1	poker_player_2
SELECT poker_player.money_tier FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_2
SELECT poker_player.money_tier FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_2
SELECT poker_player.last_table_made , poker_player.Best_Finish FROM poker_player	poker_player_3
SELECT poker_player.last_table_made , poker_player.Best_Finish FROM poker_player	poker_player_3
SELECT poker_player.currency_standing FROM poker_player ORDER BY poker_player.Earnings desc LIMIT 1	poker_player_3
SELECT poker_player.currency_standing FROM poker_player ORDER BY poker_player.Earnings desc LIMIT 1	poker_player_3
SELECT max(poker_player.last_table_made) FROM poker_player WHERE poker_player.Earnings < 200000	poker_player_3
SELECT max(poker_player.last_table_made) FROM poker_player WHERE poker_player.Earnings < 200000	poker_player_3
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.last_table_made asc	poker_player_3
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.last_table_made asc	poker_player_3
SELECT poker_player.currency_standing FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_3
SELECT poker_player.currency_standing FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_3
SELECT poker_player.revenue FROM poker_player ORDER BY poker_player.revenue desc	poker_player_4
SELECT poker_player.revenue FROM poker_player ORDER BY poker_player.revenue desc	poker_player_4
SELECT avg(poker_player.revenue) FROM poker_player	poker_player_4
SELECT avg(poker_player.revenue) FROM poker_player	poker_player_4
SELECT poker_player.Money_Rank FROM poker_player ORDER BY poker_player.revenue desc LIMIT 1	poker_player_4
SELECT poker_player.Money_Rank FROM poker_player ORDER BY poker_player.revenue desc LIMIT 1	poker_player_4
SELECT max(poker_player.Final_Table_Made) FROM poker_player WHERE poker_player.revenue < 200000	poker_player_4
SELECT max(poker_player.Final_Table_Made) FROM poker_player WHERE poker_player.revenue < 200000	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE poker_player.revenue > 300000	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE poker_player.revenue > 300000	poker_player_4
SELECT people.Birth_Date FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.revenue asc LIMIT 1	poker_player_4
SELECT people.Birth_Date FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.revenue asc LIMIT 1	poker_player_4
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.tallness desc LIMIT 1	poker_player_4
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY people.tallness desc LIMIT 1	poker_player_4
SELECT avg(poker_player.revenue) FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE people.tallness > 200	poker_player_4
SELECT avg(poker_player.revenue) FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE people.tallness > 200	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.revenue desc	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.revenue desc	poker_player_4
SELECT CONTESTANTS.competitor_digits , CONTESTANTS.participant FROM CONTESTANTS ORDER BY CONTESTANTS.participant desc	voter_1_0
SELECT max(AREA_CODE_STATE.region_digits) , min(AREA_CODE_STATE.region_digits) FROM AREA_CODE_STATE	voter_1_0
SELECT CONTESTANTS.participant FROM CONTESTANTS WHERE CONTESTANTS.participant != "Jessie Alloway"	voter_1_0
SELECT CONTESTANTS.competitor_digits , CONTESTANTS.participant FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.competitor_digits = VOTES.competitor_digits GROUP BY CONTESTANTS.competitor_digits HAVING count(*) >= 2	voter_1_0
SELECT CONTESTANTS.competitor_digits , CONTESTANTS.participant FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.competitor_digits = VOTES.competitor_digits GROUP BY CONTESTANTS.competitor_digits ORDER BY count(*) asc LIMIT 1	voter_1_0
SELECT count(*) FROM CONTESTANTS WHERE CONTESTANTS.competitor_digits NOT in (SELECT VOTES.competitor_digits FROM VOTES)	voter_1_0
SELECT AREA_CODE_STATE.region_digits FROM AREA_CODE_STATE JOIN VOTES ON AREA_CODE_STATE.state = VOTES.state GROUP BY AREA_CODE_STATE.region_digits ORDER BY count(*) desc LIMIT 1	voter_1_0
SELECT VOTES.created , VOTES.state , VOTES.phone_number FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.competitor_digits = VOTES.competitor_digits WHERE CONTESTANTS.participant = "Tabatha Gehling"	voter_1_0
SELECT AREA_CODE_STATE.region_digits FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.competitor_digits = VOTES.competitor_digits JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.participant = "Tabatha Gehling" INTERSECT SELECT AREA_CODE_STATE.region_digits FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.competitor_digits = VOTES.competitor_digits JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.participant = "Kelly Clauss"	voter_1_0
SELECT CONTESTANTS.participant FROM CONTESTANTS WHERE CONTESTANTS.participant like "%al%"	voter_1_0
SELECT CONTESTANTS.contestant_number , CONTESTANTS.competitor_cognomen FROM CONTESTANTS ORDER BY CONTESTANTS.competitor_cognomen desc	voter_1_1
SELECT VOTES.vote_id , VOTES.ring_up , VOTES.state FROM VOTES	voter_1_1
SELECT CONTESTANTS.competitor_cognomen FROM CONTESTANTS WHERE CONTESTANTS.competitor_cognomen != "Jessie Alloway"	voter_1_1
SELECT CONTESTANTS.contestant_number , CONTESTANTS.competitor_cognomen FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number HAVING count(*) >= 2	voter_1_1
SELECT CONTESTANTS.contestant_number , CONTESTANTS.competitor_cognomen FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number ORDER BY count(*) asc LIMIT 1	voter_1_1
SELECT VOTES.created , VOTES.state , VOTES.ring_up FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number WHERE CONTESTANTS.competitor_cognomen = "Tabatha Gehling"	voter_1_1
SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.competitor_cognomen = "Tabatha Gehling" INTERSECT SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.competitor_cognomen = "Kelly Clauss"	voter_1_1
SELECT CONTESTANTS.competitor_cognomen FROM CONTESTANTS WHERE CONTESTANTS.competitor_cognomen like "%al%"	voter_1_1
SELECT CONTESTANTS.contestant_number , CONTESTANTS.participant FROM CONTESTANTS ORDER BY CONTESTANTS.participant desc	voter_1_2
SELECT CONTESTANTS.participant FROM CONTESTANTS WHERE CONTESTANTS.participant != "Jessie Alloway"	voter_1_2
SELECT CONTESTANTS.contestant_number , CONTESTANTS.participant FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number HAVING count(*) >= 2	voter_1_2
SELECT CONTESTANTS.contestant_number , CONTESTANTS.participant FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number ORDER BY count(*) asc LIMIT 1	voter_1_2
SELECT VOTES.created , VOTES.state , VOTES.phone_number FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number WHERE CONTESTANTS.participant = "Tabatha Gehling"	voter_1_2
SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.participant = "Tabatha Gehling" INTERSECT SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.participant = "Kelly Clauss"	voter_1_2
SELECT CONTESTANTS.participant FROM CONTESTANTS WHERE CONTESTANTS.participant like "%al%"	voter_1_2
SELECT CONTESTANTS.contestant_number , CONTESTANTS.competitor_cognomen FROM CONTESTANTS ORDER BY CONTESTANTS.competitor_cognomen desc	voter_1_3
SELECT max(AREA_CODE_STATE.region_digits) , min(AREA_CODE_STATE.region_digits) FROM AREA_CODE_STATE	voter_1_3
SELECT CONTESTANTS.competitor_cognomen FROM CONTESTANTS WHERE CONTESTANTS.competitor_cognomen != "Jessie Alloway"	voter_1_3
SELECT CONTESTANTS.contestant_number , CONTESTANTS.competitor_cognomen FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number HAVING count(*) >= 2	voter_1_3
SELECT CONTESTANTS.contestant_number , CONTESTANTS.competitor_cognomen FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number ORDER BY count(*) asc LIMIT 1	voter_1_3
SELECT AREA_CODE_STATE.region_digits FROM AREA_CODE_STATE JOIN VOTES ON AREA_CODE_STATE.state = VOTES.state GROUP BY AREA_CODE_STATE.region_digits ORDER BY count(*) desc LIMIT 1	voter_1_3
SELECT VOTES.created , VOTES.state , VOTES.phone_number FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number WHERE CONTESTANTS.competitor_cognomen = "Tabatha Gehling"	voter_1_3
SELECT AREA_CODE_STATE.region_digits FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.competitor_cognomen = "Tabatha Gehling" INTERSECT SELECT AREA_CODE_STATE.region_digits FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.competitor_cognomen = "Kelly Clauss"	voter_1_3
SELECT CONTESTANTS.competitor_cognomen FROM CONTESTANTS WHERE CONTESTANTS.competitor_cognomen like "%al%"	voter_1_3
SELECT VOTES.vote_id , VOTES.call_up , VOTES.state FROM VOTES	voter_1_4
SELECT max(VOTES.made) FROM VOTES WHERE VOTES.state = "CA"	voter_1_4
SELECT DISTINCT VOTES.state , VOTES.made FROM VOTES	voter_1_4
SELECT VOTES.made , VOTES.state , VOTES.call_up FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number WHERE CONTESTANTS.contestant_name = "Tabatha Gehling"	voter_1_4
SELECT count(*) FROM country WHERE country.political_form = "Republic"	world_1_0
SELECT count(*) FROM country WHERE country.political_form = "Republic"	world_1_0
SELECT sum(country.landscape) FROM country WHERE country.place = "Caribbean"	world_1_0
SELECT sum(country.landscape) FROM country WHERE country.place = "Caribbean"	world_1_0
SELECT country.mainland FROM country WHERE country.Name = "Anguilla"	world_1_0
SELECT country.mainland FROM country WHERE country.Name = "Anguilla"	world_1_0
SELECT country.place FROM country JOIN city ON country.Code = city.CountryCode WHERE city.Name = "Kabul"	world_1_0
SELECT country.place FROM country JOIN city ON country.Code = city.CountryCode WHERE city.Name = "Kabul"	world_1_0
SELECT countrylanguage.official_language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.share desc LIMIT 1	world_1_0
SELECT countrylanguage.official_language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.share desc LIMIT 1	world_1_0
SELECT country.people_number , country.life_expectation FROM country WHERE country.Name = "Brazil"	world_1_0
SELECT country.people_number , country.life_expectation FROM country WHERE country.Name = "Brazil"	world_1_0
SELECT country.people_number , country.place FROM country WHERE country.Name = "Angola"	world_1_0
SELECT country.people_number , country.place FROM country WHERE country.Name = "Angola"	world_1_0
SELECT avg(country.life_expectation) FROM country WHERE country.place = "Central Africa"	world_1_0
SELECT avg(country.life_expectation) FROM country WHERE country.place = "Central Africa"	world_1_0
SELECT country.Name FROM country WHERE country.mainland = "Asia" ORDER BY country.life_expectation asc LIMIT 1	world_1_0
SELECT country.Name FROM country WHERE country.mainland = "Asia" ORDER BY country.life_expectation asc LIMIT 1	world_1_0
SELECT sum(country.people_number) , max(country.net_national_product) FROM country WHERE country.mainland = "Asia"	world_1_0
SELECT sum(country.people_number) , max(country.net_national_product) FROM country WHERE country.mainland = "Asia"	world_1_0
SELECT avg(country.life_expectation) FROM country WHERE country.mainland = "Africa" and country.political_form = "Republic"	world_1_0
SELECT avg(country.life_expectation) FROM country WHERE country.mainland = "Africa" and country.political_form = "Republic"	world_1_0
SELECT sum(country.landscape) FROM country WHERE country.mainland = "Asia" or country.mainland = "Europe"	world_1_0
SELECT sum(country.landscape) FROM country WHERE country.mainland = "Asia" or country.mainland = "Europe"	world_1_0
SELECT sum(city.native) FROM city WHERE city.region = "Gelderland"	world_1_0
SELECT sum(city.native) FROM city WHERE city.region = "Gelderland"	world_1_0
SELECT avg(country.net_national_product) , sum(country.people_number) FROM country WHERE country.political_form = "US Territory"	world_1_0
SELECT avg(country.net_national_product) , sum(country.people_number) FROM country WHERE country.political_form = "US Territory"	world_1_0
SELECT count(DISTINCT countrylanguage.official_language) FROM countrylanguage	world_1_0
SELECT count(DISTINCT countrylanguage.official_language) FROM countrylanguage	world_1_0
SELECT count(DISTINCT country.political_form) FROM country WHERE country.mainland = "Africa"	world_1_0
SELECT count(DISTINCT country.political_form) FROM country WHERE country.mainland = "Africa"	world_1_0
SELECT count(countrylanguage.official_language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba"	world_1_0
SELECT count(countrylanguage.official_language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba"	world_1_0
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.is_formal = "T"	world_1_0
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.is_formal = "T"	world_1_0
SELECT country.mainland FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.mainland ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT country.mainland FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.mainland ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "Dutch" )	world_1_0
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "Dutch" )	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "French"	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "French"	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" and countrylanguage.is_formal = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "French" and countrylanguage.is_formal = "T"	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" and countrylanguage.is_formal = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "French" and countrylanguage.is_formal = "T"	world_1_0
SELECT count(DISTINCT country.mainland) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "Chinese"	world_1_0
SELECT count(DISTINCT country.mainland) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "Chinese"	world_1_0
SELECT DISTINCT country.place FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" or countrylanguage.official_language = "Dutch"	world_1_0
SELECT DISTINCT country.place FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" or countrylanguage.official_language = "Dutch"	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "english" and countrylanguage.is_formal = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "dutch" and countrylanguage.is_formal = "t"	world_1_0
SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" and countrylanguage.is_formal = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "Dutch" and countrylanguage.is_formal = "T"	world_1_0
SELECT countrylanguage.official_language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.mainland = "Asia" GROUP BY countrylanguage.official_language ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT countrylanguage.official_language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.mainland = "Asia" GROUP BY countrylanguage.official_language ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT countrylanguage.official_language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.political_form = "Republic" GROUP BY countrylanguage.official_language HAVING count(*) = 1	world_1_0
SELECT countrylanguage.official_language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.political_form = "Republic" GROUP BY countrylanguage.official_language HAVING count(*) = 1	world_1_0
SELECT city.Name , city.native FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" ORDER BY city.native desc LIMIT 1	world_1_0
SELECT city.Name , city.native FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" ORDER BY city.native desc LIMIT 1	world_1_0
SELECT country.Name , country.people_number , country.life_expectation FROM country WHERE country.mainland = "Asia" ORDER BY country.landscape desc LIMIT 1	world_1_0
SELECT country.Name , country.people_number , country.life_expectation FROM country WHERE country.mainland = "Asia" ORDER BY country.landscape desc LIMIT 1	world_1_0
SELECT avg(country.life_expectation) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" and countrylanguage.is_formal = "T")	world_1_0
SELECT avg(country.life_expectation) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English" and countrylanguage.is_formal = "T")	world_1_0
SELECT sum(country.people_number) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English")	world_1_0
SELECT sum(country.people_number) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.official_language = "English")	world_1_0
SELECT countrylanguage.official_language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.HeadOfState = "Beatrix" and countrylanguage.is_formal = "T"	world_1_0
SELECT countrylanguage.official_language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.HeadOfState = "Beatrix" and countrylanguage.is_formal = "T"	world_1_0
SELECT count(DISTINCT countrylanguage.official_language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.is_formal = "T"	world_1_0
SELECT count(DISTINCT countrylanguage.official_language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.is_formal = "T"	world_1_0
SELECT country.Name FROM country WHERE country.landscape > (SELECT min(country.landscape) FROM country WHERE country.mainland = "Europe")	world_1_0
SELECT country.Name FROM country WHERE country.landscape > (SELECT min(country.landscape) FROM country WHERE country.mainland = "Europe")	world_1_0
SELECT country.Name FROM country WHERE country.mainland = "Africa" and country.people_number < (SELECT max(country.people_number) FROM country WHERE country.mainland = "Asia")	world_1_0
SELECT country.Name FROM country WHERE country.mainland = "Africa" and country.people_number < (SELECT min(country.people_number) FROM country WHERE country.mainland = "Asia")	world_1_0
SELECT country.Name FROM country WHERE country.mainland = "Asia" and country.people_number > (SELECT max(country.people_number) FROM country WHERE country.mainland = "Africa")	world_1_0
SELECT country.Name FROM country WHERE country.mainland = "Asia" and country.people_number > (SELECT min(country.people_number) FROM country WHERE country.mainland = "Africa")	world_1_0
SELECT countrylanguage.CountryCode FROM countrylanguage EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.official_language = "English"	world_1_0
SELECT countrylanguage.CountryCode FROM countrylanguage EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.official_language = "English"	world_1_0
SELECT DISTINCT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.official_language != "English"	world_1_0
SELECT DISTINCT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.official_language != "English"	world_1_0
SELECT country.Code FROM country WHERE country.political_form != "Republic" EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.official_language = "English"	world_1_0
SELECT country.Code FROM country WHERE country.political_form != "Republic" EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.official_language = "English"	world_1_0
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.mainland = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.is_formal = "T" and countrylanguage.official_language = "English")	world_1_0
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.mainland = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.is_formal = "T" and countrylanguage.official_language = "English")	world_1_0
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.is_formal = "t" and countrylanguage.official_language = "chinese" and country.mainland = "asia"	world_1_0
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.is_formal = "T" and countrylanguage.official_language = "Chinese" and country.mainland = "Asia"	world_1_0
SELECT country.Name , country.landscape , country.IndepYear FROM country ORDER BY country.people_number asc LIMIT 1	world_1_0
SELECT country.Name , country.landscape , country.IndepYear FROM country ORDER BY country.people_number asc LIMIT 1	world_1_0
SELECT country.Name , country.people_number , country.HeadOfState FROM country ORDER BY country.landscape desc LIMIT 1	world_1_0
SELECT country.Name , country.people_number , country.HeadOfState FROM country ORDER BY country.landscape desc LIMIT 1	world_1_0
SELECT count(countrylanguage.official_language) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Name HAVING count(*) > 2	world_1_0
SELECT count(countrylanguage.official_language) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Name HAVING count(*) > 2	world_1_0
SELECT count(*) , city.region FROM city WHERE city.native > (SELECT avg(city.native) FROM city) GROUP BY city.region	world_1_0
SELECT count(*) , city.region FROM city WHERE city.native > (SELECT avg(city.native) FROM city) GROUP BY city.region	world_1_0
SELECT sum(country.people_number) , country.political_form FROM country GROUP BY country.political_form HAVING avg(country.life_expectation) > 72	world_1_0
SELECT sum(country.people_number) , country.political_form FROM country GROUP BY country.political_form HAVING avg(country.life_expectation) > 72	world_1_0
SELECT sum(country.people_number) , avg(country.life_expectation) , country.mainland FROM country GROUP BY country.mainland HAVING avg(country.life_expectation) < 72	world_1_0
SELECT sum(country.people_number) , avg(country.life_expectation) , country.mainland FROM country GROUP BY country.mainland HAVING avg(country.life_expectation) < 72	world_1_0
SELECT country.Name , country.landscape FROM country ORDER BY country.landscape desc LIMIT 5	world_1_0
SELECT country.Name , country.landscape FROM country ORDER BY country.landscape desc LIMIT 5	world_1_0
SELECT country.Name FROM country ORDER BY country.people_number desc LIMIT 3	world_1_0
SELECT country.Name FROM country ORDER BY country.people_number desc LIMIT 3	world_1_0
SELECT country.Name FROM country ORDER BY country.people_number asc LIMIT 3	world_1_0
SELECT country.Name FROM country ORDER BY country.people_number asc LIMIT 3	world_1_0
SELECT count(*) FROM country WHERE country.mainland = "Asia"	world_1_0
SELECT count(*) FROM country WHERE country.mainland = "Asia"	world_1_0
SELECT country.Name FROM country WHERE country.mainland = "Europe" and country.people_number = "80000"	world_1_0
SELECT country.Name FROM country WHERE country.mainland = "Europe" and country.people_number = "80000"	world_1_0
SELECT sum(country.people_number) , avg(country.landscape) FROM country WHERE country.mainland = "north america" and country.landscape > 3000	world_1_0
SELECT sum(country.people_number) , avg(country.landscape) FROM country WHERE country.mainland = "north america" and country.landscape > 3000	world_1_0
SELECT city.Name FROM city WHERE city.native BETWEEN 160000 AND 900000	world_1_0
SELECT city.Name FROM city WHERE city.native BETWEEN 160000 AND 900000	world_1_0
SELECT countrylanguage.official_language FROM countrylanguage GROUP BY countrylanguage.official_language ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT countrylanguage.official_language FROM countrylanguage GROUP BY countrylanguage.official_language ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT countrylanguage.official_language , countrylanguage.CountryCode , max(countrylanguage.share) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_0
SELECT countrylanguage.official_language , countrylanguage.CountryCode , max(countrylanguage.share) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_0
SELECT count(*) , max(countrylanguage.share) FROM countrylanguage WHERE countrylanguage.official_language = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_0
SELECT count(*) , max(countrylanguage.share) FROM countrylanguage WHERE countrylanguage.official_language = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_0
SELECT countrylanguage.CountryCode , max(countrylanguage.share) FROM countrylanguage WHERE countrylanguage.official_language = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_0
SELECT countrylanguage.CountryCode , max(countrylanguage.share) FROM countrylanguage WHERE countrylanguage.official_language = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_0
SELECT country.mainland FROM country WHERE country.Name = "Anguilla"	world_1_1
SELECT country.mainland FROM country WHERE country.Name = "Anguilla"	world_1_1
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.Percentage desc LIMIT 1	world_1_1
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.Percentage desc LIMIT 1	world_1_1
SELECT country.Population , country.life_expectation FROM country WHERE country.Name = "Brazil"	world_1_1
SELECT country.Population , country.life_expectation FROM country WHERE country.Name = "Brazil"	world_1_1
SELECT avg(country.life_expectation) FROM country WHERE country.Region = "Central Africa"	world_1_1
SELECT avg(country.life_expectation) FROM country WHERE country.Region = "Central Africa"	world_1_1
SELECT country.Name FROM country WHERE country.mainland = "Asia" ORDER BY country.life_expectation asc LIMIT 1	world_1_1
SELECT country.Name FROM country WHERE country.mainland = "Asia" ORDER BY country.life_expectation asc LIMIT 1	world_1_1
SELECT sum(country.Population) , max(country.gross_national_product) FROM country WHERE country.mainland = "Asia"	world_1_1
SELECT sum(country.Population) , max(country.gross_national_product) FROM country WHERE country.mainland = "Asia"	world_1_1
SELECT avg(country.life_expectation) FROM country WHERE country.mainland = "Africa" and country.GovernmentForm = "Republic"	world_1_1
SELECT avg(country.life_expectation) FROM country WHERE country.mainland = "Africa" and country.GovernmentForm = "Republic"	world_1_1
SELECT sum(country.SurfaceArea) FROM country WHERE country.mainland = "Asia" or country.mainland = "Europe"	world_1_1
SELECT sum(country.SurfaceArea) FROM country WHERE country.mainland = "Asia" or country.mainland = "Europe"	world_1_1
SELECT avg(country.gross_national_product) , sum(country.Population) FROM country WHERE country.GovernmentForm = "US Territory"	world_1_1
SELECT avg(country.gross_national_product) , sum(country.Population) FROM country WHERE country.GovernmentForm = "US Territory"	world_1_1
SELECT count(DISTINCT countrylanguage.dialect) FROM countrylanguage	world_1_1
SELECT count(DISTINCT countrylanguage.dialect) FROM countrylanguage	world_1_1
SELECT count(DISTINCT country.GovernmentForm) FROM country WHERE country.mainland = "Africa"	world_1_1
SELECT count(DISTINCT country.GovernmentForm) FROM country WHERE country.mainland = "Africa"	world_1_1
SELECT count(countrylanguage.dialect) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba"	world_1_1
SELECT count(countrylanguage.dialect) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba"	world_1_1
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.is_formal = "T"	world_1_1
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.is_formal = "T"	world_1_1
SELECT country.mainland FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.mainland ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT country.mainland FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.mainland ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Dutch" )	world_1_1
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Dutch" )	world_1_1
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "French"	world_1_1
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "French"	world_1_1
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.is_formal = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "French" and countrylanguage.is_formal = "T"	world_1_1
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.is_formal = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "French" and countrylanguage.is_formal = "T"	world_1_1
SELECT count(DISTINCT country.mainland) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Chinese"	world_1_1
SELECT count(DISTINCT country.mainland) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Chinese"	world_1_1
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" or countrylanguage.dialect = "Dutch"	world_1_1
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" or countrylanguage.dialect = "Dutch"	world_1_1
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "english" and countrylanguage.is_formal = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "dutch" and countrylanguage.is_formal = "t"	world_1_1
SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.is_formal = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Dutch" and countrylanguage.is_formal = "T"	world_1_1
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.mainland = "Asia" GROUP BY countrylanguage.dialect ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.mainland = "Asia" GROUP BY countrylanguage.dialect ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.GovernmentForm = "Republic" GROUP BY countrylanguage.dialect HAVING count(*) = 1	world_1_1
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.GovernmentForm = "Republic" GROUP BY countrylanguage.dialect HAVING count(*) = 1	world_1_1
SELECT city.Name , city.Population FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" ORDER BY city.Population desc LIMIT 1	world_1_1
SELECT city.Name , city.Population FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" ORDER BY city.Population desc LIMIT 1	world_1_1
SELECT country.Name , country.Population , country.life_expectation FROM country WHERE country.mainland = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_1
SELECT country.Name , country.Population , country.life_expectation FROM country WHERE country.mainland = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_1
SELECT avg(country.life_expectation) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.is_formal = "T")	world_1_1
SELECT avg(country.life_expectation) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.is_formal = "T")	world_1_1
SELECT sum(country.Population) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English")	world_1_1
SELECT sum(country.Population) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English")	world_1_1
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.HeadOfState = "Beatrix" and countrylanguage.is_formal = "T"	world_1_1
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.HeadOfState = "Beatrix" and countrylanguage.is_formal = "T"	world_1_1
SELECT count(DISTINCT countrylanguage.dialect) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.is_formal = "T"	world_1_1
SELECT count(DISTINCT countrylanguage.dialect) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.is_formal = "T"	world_1_1
SELECT country.Name FROM country WHERE country.SurfaceArea > (SELECT min(country.SurfaceArea) FROM country WHERE country.mainland = "Europe")	world_1_1
SELECT country.Name FROM country WHERE country.SurfaceArea > (SELECT min(country.SurfaceArea) FROM country WHERE country.mainland = "Europe")	world_1_1
SELECT country.Name FROM country WHERE country.mainland = "Africa" and country.Population < (SELECT max(country.Population) FROM country WHERE country.mainland = "Asia")	world_1_1
SELECT country.Name FROM country WHERE country.mainland = "Africa" and country.Population < (SELECT min(country.Population) FROM country WHERE country.mainland = "Asia")	world_1_1
SELECT country.Name FROM country WHERE country.mainland = "Asia" and country.Population > (SELECT max(country.Population) FROM country WHERE country.mainland = "Africa")	world_1_1
SELECT country.Name FROM country WHERE country.mainland = "Asia" and country.Population > (SELECT min(country.Population) FROM country WHERE country.mainland = "Africa")	world_1_1
SELECT countrylanguage.CountryCode FROM countrylanguage EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect = "English"	world_1_1
SELECT countrylanguage.CountryCode FROM countrylanguage EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect = "English"	world_1_1
SELECT DISTINCT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect != "English"	world_1_1
SELECT DISTINCT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect != "English"	world_1_1
SELECT country.Code FROM country WHERE country.GovernmentForm != "Republic" EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect = "English"	world_1_1
SELECT country.Code FROM country WHERE country.GovernmentForm != "Republic" EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect = "English"	world_1_1
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.mainland = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.is_formal = "T" and countrylanguage.dialect = "English")	world_1_1
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.mainland = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.is_formal = "T" and countrylanguage.dialect = "English")	world_1_1
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.is_formal = "t" and countrylanguage.dialect = "chinese" and country.mainland = "asia"	world_1_1
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.is_formal = "T" and countrylanguage.dialect = "Chinese" and country.mainland = "Asia"	world_1_1
SELECT count(countrylanguage.dialect) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Name HAVING count(*) > 2	world_1_1
SELECT count(countrylanguage.dialect) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Name HAVING count(*) > 2	world_1_1
SELECT sum(country.Population) , country.GovernmentForm FROM country GROUP BY country.GovernmentForm HAVING avg(country.life_expectation) > 72	world_1_1
SELECT sum(country.Population) , country.GovernmentForm FROM country GROUP BY country.GovernmentForm HAVING avg(country.life_expectation) > 72	world_1_1
SELECT sum(country.Population) , avg(country.life_expectation) , country.mainland FROM country GROUP BY country.mainland HAVING avg(country.life_expectation) < 72	world_1_1
SELECT sum(country.Population) , avg(country.life_expectation) , country.mainland FROM country GROUP BY country.mainland HAVING avg(country.life_expectation) < 72	world_1_1
SELECT count(*) FROM country WHERE country.mainland = "Asia"	world_1_1
SELECT count(*) FROM country WHERE country.mainland = "Asia"	world_1_1
SELECT country.Name FROM country WHERE country.mainland = "Europe" and country.Population = "80000"	world_1_1
SELECT country.Name FROM country WHERE country.mainland = "Europe" and country.Population = "80000"	world_1_1
SELECT sum(country.Population) , avg(country.SurfaceArea) FROM country WHERE country.mainland = "north america" and country.SurfaceArea > 3000	world_1_1
SELECT sum(country.Population) , avg(country.SurfaceArea) FROM country WHERE country.mainland = "north america" and country.SurfaceArea > 3000	world_1_1
SELECT countrylanguage.dialect FROM countrylanguage GROUP BY countrylanguage.dialect ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT countrylanguage.dialect FROM countrylanguage GROUP BY countrylanguage.dialect ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT countrylanguage.dialect , countrylanguage.CountryCode , max(countrylanguage.Percentage) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_1
SELECT countrylanguage.dialect , countrylanguage.CountryCode , max(countrylanguage.Percentage) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_1
SELECT count(*) , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.dialect = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_1
SELECT count(*) , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.dialect = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_1
SELECT countrylanguage.CountryCode , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.dialect = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_1
SELECT countrylanguage.CountryCode , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.dialect = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_1
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.Name = "Aruba" ORDER BY countrylanguage.Percentage desc LIMIT 1	world_1_2
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.Name = "Aruba" ORDER BY countrylanguage.Percentage desc LIMIT 1	world_1_2
SELECT count(countrylanguage.Language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.Name = "Aruba"	world_1_2
SELECT count(countrylanguage.Language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.Name = "Aruba"	world_1_2
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.Name = "Afghanistan" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.Name = "Afghanistan" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT country.Continent FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher GROUP BY country.Continent ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT country.Continent FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher GROUP BY country.Continent ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "Dutch" )	world_1_2
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "Dutch" )	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "French"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "French"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "French" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "French" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT count(DISTINCT country.Continent) FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "Chinese"	world_1_2
SELECT count(DISTINCT country.Continent) FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "Chinese"	world_1_2
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" or countrylanguage.Language = "Dutch"	world_1_2
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" or countrylanguage.Language = "Dutch"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "english" and countrylanguage.IsOfficial = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "dutch" and countrylanguage.IsOfficial = "t"	world_1_2
SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "Dutch" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.Continent = "Asia" GROUP BY countrylanguage.Language ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.Continent = "Asia" GROUP BY countrylanguage.Language ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.GovernmentForm = "Republic" GROUP BY countrylanguage.Language HAVING count(*) = 1	world_1_2
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.GovernmentForm = "Republic" GROUP BY countrylanguage.Language HAVING count(*) = 1	world_1_2
SELECT city.Name , city.Population FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" ORDER BY city.Population desc LIMIT 1	world_1_2
SELECT city.Name , city.Population FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" ORDER BY city.Population desc LIMIT 1	world_1_2
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T")	world_1_2
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T")	world_1_2
SELECT sum(country.Population) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English")	world_1_2
SELECT sum(country.Population) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.Language = "English")	world_1_2
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.country_head = "Beatrix" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.country_head = "Beatrix" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT count(DISTINCT countrylanguage.Language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.IndepYear < 1930 and countrylanguage.IsOfficial = "T"	world_1_2
SELECT count(DISTINCT countrylanguage.Language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE country.IndepYear < 1930 and countrylanguage.IsOfficial = "T"	world_1_2
SELECT countrylanguage.country_cipher FROM countrylanguage EXCEPT SELECT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language = "English"	world_1_2
SELECT countrylanguage.country_cipher FROM countrylanguage EXCEPT SELECT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language = "English"	world_1_2
SELECT DISTINCT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language != "English"	world_1_2
SELECT DISTINCT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language != "English"	world_1_2
SELECT country.Code FROM country WHERE country.GovernmentForm != "Republic" EXCEPT SELECT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language = "English"	world_1_2
SELECT country.Code FROM country WHERE country.GovernmentForm != "Republic" EXCEPT SELECT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language = "English"	world_1_2
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.Continent = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.IsOfficial = "T" and countrylanguage.Language = "English")	world_1_2
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.Continent = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher WHERE countrylanguage.IsOfficial = "T" and countrylanguage.Language = "English")	world_1_2
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.IsOfficial = "t" and countrylanguage.Language = "chinese" and country.Continent = "asia"	world_1_2
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.IsOfficial = "T" and countrylanguage.Language = "Chinese" and country.Continent = "Asia"	world_1_2
SELECT country.Name , country.Population , country.country_head FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_2
SELECT country.Name , country.Population , country.country_head FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_2
SELECT count(countrylanguage.Language) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher GROUP BY country.Name HAVING count(*) > 2	world_1_2
SELECT count(countrylanguage.Language) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.country_cipher GROUP BY country.Name HAVING count(*) > 2	world_1_2
SELECT countrylanguage.Language , countrylanguage.country_cipher , max(countrylanguage.Percentage) FROM countrylanguage GROUP BY countrylanguage.country_cipher	world_1_2
SELECT countrylanguage.Language , countrylanguage.country_cipher , max(countrylanguage.Percentage) FROM countrylanguage GROUP BY countrylanguage.country_cipher	world_1_2
SELECT count(*) , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.country_cipher	world_1_2
SELECT count(*) , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.country_cipher	world_1_2
SELECT countrylanguage.country_cipher , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.country_cipher	world_1_2
SELECT countrylanguage.country_cipher , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.country_cipher	world_1_2
SELECT count(*) FROM country WHERE country.political_form = "Republic"	world_1_3
SELECT count(*) FROM country WHERE country.political_form = "Republic"	world_1_3
SELECT sum(country.SurfaceArea) FROM country WHERE country.place = "Caribbean"	world_1_3
SELECT sum(country.SurfaceArea) FROM country WHERE country.place = "Caribbean"	world_1_3
SELECT country.place FROM country JOIN city ON country.Code = city.CountryCode WHERE city.Name = "Kabul"	world_1_3
SELECT country.place FROM country JOIN city ON country.Code = city.CountryCode WHERE city.Name = "Kabul"	world_1_3
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.Percentage desc LIMIT 1	world_1_3
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.Percentage desc LIMIT 1	world_1_3
SELECT country.how_many_people , country.LifeExpectancy FROM country WHERE country.Name = "Brazil"	world_1_3
SELECT country.how_many_people , country.LifeExpectancy FROM country WHERE country.Name = "Brazil"	world_1_3
SELECT country.how_many_people , country.place FROM country WHERE country.Name = "Angola"	world_1_3
SELECT country.how_many_people , country.place FROM country WHERE country.Name = "Angola"	world_1_3
SELECT avg(country.LifeExpectancy) FROM country WHERE country.place = "Central Africa"	world_1_3
SELECT avg(country.LifeExpectancy) FROM country WHERE country.place = "Central Africa"	world_1_3
SELECT sum(country.how_many_people) , max(country.GNP) FROM country WHERE country.Continent = "Asia"	world_1_3
SELECT sum(country.how_many_people) , max(country.GNP) FROM country WHERE country.Continent = "Asia"	world_1_3
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Continent = "Africa" and country.political_form = "Republic"	world_1_3
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Continent = "Africa" and country.political_form = "Republic"	world_1_3
SELECT sum(city.total_citizens) FROM city WHERE city.District = "Gelderland"	world_1_3
SELECT sum(city.total_citizens) FROM city WHERE city.District = "Gelderland"	world_1_3
SELECT avg(country.GNP) , sum(country.how_many_people) FROM country WHERE country.political_form = "US Territory"	world_1_3
SELECT avg(country.GNP) , sum(country.how_many_people) FROM country WHERE country.political_form = "US Territory"	world_1_3
SELECT count(DISTINCT countrylanguage.dialect) FROM countrylanguage	world_1_3
SELECT count(DISTINCT countrylanguage.dialect) FROM countrylanguage	world_1_3
SELECT count(DISTINCT country.political_form) FROM country WHERE country.Continent = "Africa"	world_1_3
SELECT count(DISTINCT country.political_form) FROM country WHERE country.Continent = "Africa"	world_1_3
SELECT count(countrylanguage.dialect) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba"	world_1_3
SELECT count(countrylanguage.dialect) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba"	world_1_3
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.formal = "T"	world_1_3
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.formal = "T"	world_1_3
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Dutch" )	world_1_3
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Dutch" )	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "French"	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "French"	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.formal = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "French" and countrylanguage.formal = "T"	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.formal = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "French" and countrylanguage.formal = "T"	world_1_3
SELECT count(DISTINCT country.Continent) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Chinese"	world_1_3
SELECT count(DISTINCT country.Continent) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Chinese"	world_1_3
SELECT DISTINCT country.place FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" or countrylanguage.dialect = "Dutch"	world_1_3
SELECT DISTINCT country.place FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" or countrylanguage.dialect = "Dutch"	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "english" and countrylanguage.formal = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "dutch" and countrylanguage.formal = "t"	world_1_3
SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.formal = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "Dutch" and countrylanguage.formal = "T"	world_1_3
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = "Asia" GROUP BY countrylanguage.dialect ORDER BY count(*) desc LIMIT 1	world_1_3
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = "Asia" GROUP BY countrylanguage.dialect ORDER BY count(*) desc LIMIT 1	world_1_3
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.political_form = "Republic" GROUP BY countrylanguage.dialect HAVING count(*) = 1	world_1_3
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.political_form = "Republic" GROUP BY countrylanguage.dialect HAVING count(*) = 1	world_1_3
SELECT city.Name , city.total_citizens FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" ORDER BY city.total_citizens desc LIMIT 1	world_1_3
SELECT city.Name , city.total_citizens FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" ORDER BY city.total_citizens desc LIMIT 1	world_1_3
SELECT country.Name , country.how_many_people , country.LifeExpectancy FROM country WHERE country.Continent = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_3
SELECT country.Name , country.how_many_people , country.LifeExpectancy FROM country WHERE country.Continent = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_3
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.formal = "T")	world_1_3
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English" and countrylanguage.formal = "T")	world_1_3
SELECT sum(country.how_many_people) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English")	world_1_3
SELECT sum(country.how_many_people) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.dialect = "English")	world_1_3
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.nation_president = "Beatrix" and countrylanguage.formal = "T"	world_1_3
SELECT countrylanguage.dialect FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.nation_president = "Beatrix" and countrylanguage.formal = "T"	world_1_3
SELECT count(DISTINCT countrylanguage.dialect) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.formal = "T"	world_1_3
SELECT count(DISTINCT countrylanguage.dialect) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.formal = "T"	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Africa" and country.how_many_people < (SELECT max(country.how_many_people) FROM country WHERE country.Continent = "Asia")	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Africa" and country.how_many_people < (SELECT min(country.how_many_people) FROM country WHERE country.Continent = "Asia")	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Asia" and country.how_many_people > (SELECT max(country.how_many_people) FROM country WHERE country.Continent = "Africa")	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Asia" and country.how_many_people > (SELECT min(country.how_many_people) FROM country WHERE country.Continent = "Africa")	world_1_3
SELECT countrylanguage.CountryCode FROM countrylanguage EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect = "English"	world_1_3
SELECT countrylanguage.CountryCode FROM countrylanguage EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect = "English"	world_1_3
SELECT DISTINCT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect != "English"	world_1_3
SELECT DISTINCT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect != "English"	world_1_3
SELECT country.Code FROM country WHERE country.political_form != "Republic" EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect = "English"	world_1_3
SELECT country.Code FROM country WHERE country.political_form != "Republic" EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.dialect = "English"	world_1_3
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.Continent = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.formal = "T" and countrylanguage.dialect = "English")	world_1_3
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.Continent = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.formal = "T" and countrylanguage.dialect = "English")	world_1_3
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.formal = "t" and countrylanguage.dialect = "chinese" and country.Continent = "asia"	world_1_3
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.formal = "T" and countrylanguage.dialect = "Chinese" and country.Continent = "Asia"	world_1_3
SELECT country.Name , country.SurfaceArea , country.IndepYear FROM country ORDER BY country.how_many_people asc LIMIT 1	world_1_3
SELECT country.Name , country.SurfaceArea , country.IndepYear FROM country ORDER BY country.how_many_people asc LIMIT 1	world_1_3
SELECT country.Name , country.how_many_people , country.nation_president FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_3
SELECT country.Name , country.how_many_people , country.nation_president FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_3
SELECT count(countrylanguage.dialect) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Name HAVING count(*) > 2	world_1_3
SELECT count(countrylanguage.dialect) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Name HAVING count(*) > 2	world_1_3
SELECT count(*) , city.District FROM city WHERE city.total_citizens > (SELECT avg(city.total_citizens) FROM city) GROUP BY city.District	world_1_3
SELECT count(*) , city.District FROM city WHERE city.total_citizens > (SELECT avg(city.total_citizens) FROM city) GROUP BY city.District	world_1_3
SELECT sum(country.how_many_people) , country.political_form FROM country GROUP BY country.political_form HAVING avg(country.LifeExpectancy) > 72	world_1_3
SELECT sum(country.how_many_people) , country.political_form FROM country GROUP BY country.political_form HAVING avg(country.LifeExpectancy) > 72	world_1_3
SELECT sum(country.how_many_people) , avg(country.LifeExpectancy) , country.Continent FROM country GROUP BY country.Continent HAVING avg(country.LifeExpectancy) < 72	world_1_3
SELECT sum(country.how_many_people) , avg(country.LifeExpectancy) , country.Continent FROM country GROUP BY country.Continent HAVING avg(country.LifeExpectancy) < 72	world_1_3
SELECT country.Name FROM country ORDER BY country.how_many_people desc LIMIT 3	world_1_3
SELECT country.Name FROM country ORDER BY country.how_many_people desc LIMIT 3	world_1_3
SELECT country.Name FROM country ORDER BY country.how_many_people asc LIMIT 3	world_1_3
SELECT country.Name FROM country ORDER BY country.how_many_people asc LIMIT 3	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Europe" and country.how_many_people = "80000"	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Europe" and country.how_many_people = "80000"	world_1_3
SELECT sum(country.how_many_people) , avg(country.SurfaceArea) FROM country WHERE country.Continent = "north america" and country.SurfaceArea > 3000	world_1_3
SELECT sum(country.how_many_people) , avg(country.SurfaceArea) FROM country WHERE country.Continent = "north america" and country.SurfaceArea > 3000	world_1_3
SELECT city.Name FROM city WHERE city.total_citizens BETWEEN 160000 AND 900000	world_1_3
SELECT city.Name FROM city WHERE city.total_citizens BETWEEN 160000 AND 900000	world_1_3
SELECT countrylanguage.dialect FROM countrylanguage GROUP BY countrylanguage.dialect ORDER BY count(*) desc LIMIT 1	world_1_3
SELECT countrylanguage.dialect FROM countrylanguage GROUP BY countrylanguage.dialect ORDER BY count(*) desc LIMIT 1	world_1_3
SELECT countrylanguage.dialect , countrylanguage.CountryCode , max(countrylanguage.Percentage) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_3
SELECT countrylanguage.dialect , countrylanguage.CountryCode , max(countrylanguage.Percentage) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_3
SELECT count(*) , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.dialect = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_3
SELECT count(*) , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.dialect = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_3
SELECT countrylanguage.CountryCode , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.dialect = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_3
SELECT countrylanguage.CountryCode , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.dialect = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_3
SELECT country.mainland FROM country WHERE country.Name = "Anguilla"	world_1_4
SELECT country.mainland FROM country WHERE country.Name = "Anguilla"	world_1_4
SELECT country.Region FROM country JOIN city ON country.codification = city.country_num WHERE city.Name = "Kabul"	world_1_4
SELECT country.Region FROM country JOIN city ON country.codification = city.country_num WHERE city.Name = "Kabul"	world_1_4
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.Name = "Aruba" ORDER BY countrylanguage.Percentage desc LIMIT 1	world_1_4
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.Name = "Aruba" ORDER BY countrylanguage.Percentage desc LIMIT 1	world_1_4
SELECT country.citizens , country.LifeExpectancy FROM country WHERE country.Name = "Brazil"	world_1_4
SELECT country.citizens , country.LifeExpectancy FROM country WHERE country.Name = "Brazil"	world_1_4
SELECT country.citizens , country.Region FROM country WHERE country.Name = "Angola"	world_1_4
SELECT country.citizens , country.Region FROM country WHERE country.Name = "Angola"	world_1_4
SELECT country.Name FROM country WHERE country.mainland = "Asia" ORDER BY country.LifeExpectancy asc LIMIT 1	world_1_4
SELECT country.Name FROM country WHERE country.mainland = "Asia" ORDER BY country.LifeExpectancy asc LIMIT 1	world_1_4
SELECT sum(country.citizens) , max(country.net_national_product) FROM country WHERE country.mainland = "Asia"	world_1_4
SELECT sum(country.citizens) , max(country.net_national_product) FROM country WHERE country.mainland = "Asia"	world_1_4
SELECT avg(country.LifeExpectancy) FROM country WHERE country.mainland = "Africa" and country.GovernmentForm = "Republic"	world_1_4
SELECT avg(country.LifeExpectancy) FROM country WHERE country.mainland = "Africa" and country.GovernmentForm = "Republic"	world_1_4
SELECT sum(country.SurfaceArea) FROM country WHERE country.mainland = "Asia" or country.mainland = "Europe"	world_1_4
SELECT sum(country.SurfaceArea) FROM country WHERE country.mainland = "Asia" or country.mainland = "Europe"	world_1_4
SELECT avg(country.net_national_product) , sum(country.citizens) FROM country WHERE country.GovernmentForm = "US Territory"	world_1_4
SELECT avg(country.net_national_product) , sum(country.citizens) FROM country WHERE country.GovernmentForm = "US Territory"	world_1_4
SELECT count(DISTINCT country.GovernmentForm) FROM country WHERE country.mainland = "Africa"	world_1_4
SELECT count(DISTINCT country.GovernmentForm) FROM country WHERE country.mainland = "Africa"	world_1_4
SELECT count(countrylanguage.Language) FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.Name = "Aruba"	world_1_4
SELECT count(countrylanguage.Language) FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.Name = "Aruba"	world_1_4
SELECT count(*) FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.Name = "Afghanistan" and countrylanguage.IsOfficial = "T"	world_1_4
SELECT count(*) FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.Name = "Afghanistan" and countrylanguage.IsOfficial = "T"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT country.mainland FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher GROUP BY country.mainland ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT country.mainland FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher GROUP BY country.mainland ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "Dutch" )	world_1_4
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "Dutch" )	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "French"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "French"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "French" and countrylanguage.IsOfficial = "T"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "French" and countrylanguage.IsOfficial = "T"	world_1_4
SELECT count(DISTINCT country.mainland) FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "Chinese"	world_1_4
SELECT count(DISTINCT country.mainland) FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "Chinese"	world_1_4
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" or countrylanguage.Language = "Dutch"	world_1_4
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" or countrylanguage.Language = "Dutch"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "english" and countrylanguage.IsOfficial = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "dutch" and countrylanguage.IsOfficial = "t"	world_1_4
SELECT * FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "Dutch" and countrylanguage.IsOfficial = "T"	world_1_4
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.mainland = "Asia" GROUP BY countrylanguage.Language ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.mainland = "Asia" GROUP BY countrylanguage.Language ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.GovernmentForm = "Republic" GROUP BY countrylanguage.Language HAVING count(*) = 1	world_1_4
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.GovernmentForm = "Republic" GROUP BY countrylanguage.Language HAVING count(*) = 1	world_1_4
SELECT city.Name , city.Population FROM city JOIN countrylanguage ON city.country_num = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" ORDER BY city.Population desc LIMIT 1	world_1_4
SELECT city.Name , city.Population FROM city JOIN countrylanguage ON city.country_num = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" ORDER BY city.Population desc LIMIT 1	world_1_4
SELECT country.Name , country.citizens , country.LifeExpectancy FROM country WHERE country.mainland = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_4
SELECT country.Name , country.citizens , country.LifeExpectancy FROM country WHERE country.mainland = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_4
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T")	world_1_4
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English" and countrylanguage.IsOfficial = "T")	world_1_4
SELECT sum(country.citizens) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English")	world_1_4
SELECT sum(country.citizens) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.Language = "English")	world_1_4
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.country_principal = "Beatrix" and countrylanguage.IsOfficial = "T"	world_1_4
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.country_principal = "Beatrix" and countrylanguage.IsOfficial = "T"	world_1_4
SELECT count(DISTINCT countrylanguage.Language) FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.IndepYear < 1930 and countrylanguage.IsOfficial = "T"	world_1_4
SELECT count(DISTINCT countrylanguage.Language) FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE country.IndepYear < 1930 and countrylanguage.IsOfficial = "T"	world_1_4
SELECT country.Name FROM country WHERE country.SurfaceArea > (SELECT min(country.SurfaceArea) FROM country WHERE country.mainland = "Europe")	world_1_4
SELECT country.Name FROM country WHERE country.SurfaceArea > (SELECT min(country.SurfaceArea) FROM country WHERE country.mainland = "Europe")	world_1_4
SELECT country.Name FROM country WHERE country.mainland = "Africa" and country.citizens < (SELECT max(country.citizens) FROM country WHERE country.mainland = "Asia")	world_1_4
SELECT country.Name FROM country WHERE country.mainland = "Africa" and country.citizens < (SELECT min(country.citizens) FROM country WHERE country.mainland = "Asia")	world_1_4
SELECT country.Name FROM country WHERE country.mainland = "Asia" and country.citizens > (SELECT max(country.citizens) FROM country WHERE country.mainland = "Africa")	world_1_4
SELECT country.Name FROM country WHERE country.mainland = "Asia" and country.citizens > (SELECT min(country.citizens) FROM country WHERE country.mainland = "Africa")	world_1_4
SELECT countrylanguage.country_cipher FROM countrylanguage EXCEPT SELECT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language = "English"	world_1_4
SELECT countrylanguage.country_cipher FROM countrylanguage EXCEPT SELECT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language = "English"	world_1_4
SELECT DISTINCT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language != "English"	world_1_4
SELECT DISTINCT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language != "English"	world_1_4
SELECT country.codification FROM country WHERE country.GovernmentForm != "Republic" EXCEPT SELECT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language = "English"	world_1_4
SELECT country.codification FROM country WHERE country.GovernmentForm != "Republic" EXCEPT SELECT countrylanguage.country_cipher FROM countrylanguage WHERE countrylanguage.Language = "English"	world_1_4
SELECT DISTINCT city.Name FROM country JOIN city ON city.country_num = country.codification WHERE country.mainland = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.IsOfficial = "T" and countrylanguage.Language = "English")	world_1_4
SELECT DISTINCT city.Name FROM country JOIN city ON city.country_num = country.codification WHERE country.mainland = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher WHERE countrylanguage.IsOfficial = "T" and countrylanguage.Language = "English")	world_1_4
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher JOIN city ON country.codification = city.country_num WHERE countrylanguage.IsOfficial = "t" and countrylanguage.Language = "chinese" and country.mainland = "asia"	world_1_4
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher JOIN city ON country.codification = city.country_num WHERE countrylanguage.IsOfficial = "T" and countrylanguage.Language = "Chinese" and country.mainland = "Asia"	world_1_4
SELECT country.Name , country.SurfaceArea , country.IndepYear FROM country ORDER BY country.citizens asc LIMIT 1	world_1_4
SELECT country.Name , country.SurfaceArea , country.IndepYear FROM country ORDER BY country.citizens asc LIMIT 1	world_1_4
SELECT country.Name , country.citizens , country.country_principal FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_4
SELECT country.Name , country.citizens , country.country_principal FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_4
SELECT count(countrylanguage.Language) , country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher GROUP BY country.Name HAVING count(*) > 2	world_1_4
SELECT count(countrylanguage.Language) , country.Name FROM country JOIN countrylanguage ON country.codification = countrylanguage.country_cipher GROUP BY country.Name HAVING count(*) > 2	world_1_4
SELECT sum(country.citizens) , country.GovernmentForm FROM country GROUP BY country.GovernmentForm HAVING avg(country.LifeExpectancy) > 72	world_1_4
SELECT sum(country.citizens) , country.GovernmentForm FROM country GROUP BY country.GovernmentForm HAVING avg(country.LifeExpectancy) > 72	world_1_4
SELECT sum(country.citizens) , avg(country.LifeExpectancy) , country.mainland FROM country GROUP BY country.mainland HAVING avg(country.LifeExpectancy) < 72	world_1_4
SELECT sum(country.citizens) , avg(country.LifeExpectancy) , country.mainland FROM country GROUP BY country.mainland HAVING avg(country.LifeExpectancy) < 72	world_1_4
SELECT country.Name FROM country ORDER BY country.citizens desc LIMIT 3	world_1_4
SELECT country.Name FROM country ORDER BY country.citizens desc LIMIT 3	world_1_4
SELECT country.Name FROM country ORDER BY country.citizens asc LIMIT 3	world_1_4
SELECT country.Name FROM country ORDER BY country.citizens asc LIMIT 3	world_1_4
SELECT count(*) FROM country WHERE country.mainland = "Asia"	world_1_4
SELECT count(*) FROM country WHERE country.mainland = "Asia"	world_1_4
SELECT country.Name FROM country WHERE country.mainland = "Europe" and country.citizens = "80000"	world_1_4
SELECT country.Name FROM country WHERE country.mainland = "Europe" and country.citizens = "80000"	world_1_4
SELECT sum(country.citizens) , avg(country.SurfaceArea) FROM country WHERE country.mainland = "north america" and country.SurfaceArea > 3000	world_1_4
SELECT sum(country.citizens) , avg(country.SurfaceArea) FROM country WHERE country.mainland = "north america" and country.SurfaceArea > 3000	world_1_4
SELECT countrylanguage.Language , countrylanguage.country_cipher , max(countrylanguage.Percentage) FROM countrylanguage GROUP BY countrylanguage.country_cipher	world_1_4
SELECT countrylanguage.Language , countrylanguage.country_cipher , max(countrylanguage.Percentage) FROM countrylanguage GROUP BY countrylanguage.country_cipher	world_1_4
SELECT count(*) , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.country_cipher	world_1_4
SELECT count(*) , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.country_cipher	world_1_4
SELECT countrylanguage.country_cipher , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.country_cipher	world_1_4
SELECT countrylanguage.country_cipher , max(countrylanguage.Percentage) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.country_cipher	world_1_4
SELECT conductor.Name FROM conductor WHERE conductor.citizen_of != "USA"	orchestra_0
SELECT conductor.Name FROM conductor WHERE conductor.citizen_of != "USA"	orchestra_0
SELECT orchestra.record_firm FROM orchestra ORDER BY orchestra.year_foundation desc	orchestra_0
SELECT orchestra.record_firm FROM orchestra ORDER BY orchestra.year_foundation desc	orchestra_0
SELECT avg(show.audience_number) FROM show	orchestra_0
SELECT avg(show.audience_number) FROM show	orchestra_0
SELECT max(performance.Share) , min(performance.Share) FROM performance WHERE performance.class != "Live final"	orchestra_0
SELECT max(performance.Share) , min(performance.Share) FROM performance WHERE performance.class != "Live final"	orchestra_0
SELECT count(DISTINCT conductor.citizen_of) FROM conductor	orchestra_0
SELECT count(DISTINCT conductor.citizen_of) FROM conductor	orchestra_0
SELECT conductor.Name FROM conductor ORDER BY conductor.how_long_worked desc	orchestra_0
SELECT conductor.Name FROM conductor ORDER BY conductor.how_long_worked desc	orchestra_0
SELECT conductor.Name FROM conductor ORDER BY conductor.how_long_worked desc LIMIT 1	orchestra_0
SELECT conductor.Name FROM conductor ORDER BY conductor.how_long_worked desc LIMIT 1	orchestra_0
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID WHERE orchestra.year_foundation > 2008	orchestra_0
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID WHERE orchestra.year_foundation > 2008	orchestra_0
SELECT orchestra.record_firm , count(*) FROM orchestra GROUP BY orchestra.record_firm	orchestra_0
SELECT orchestra.record_firm , count(*) FROM orchestra GROUP BY orchestra.record_firm	orchestra_0
SELECT orchestra.main_format FROM orchestra GROUP BY orchestra.main_format ORDER BY count(*) asc	orchestra_0
SELECT orchestra.main_format FROM orchestra GROUP BY orchestra.main_format ORDER BY count(*) asc	orchestra_0
SELECT orchestra.record_firm FROM orchestra GROUP BY orchestra.record_firm ORDER BY count(*) desc LIMIT 1	orchestra_0
SELECT orchestra.record_firm FROM orchestra GROUP BY orchestra.record_firm ORDER BY count(*) desc LIMIT 1	orchestra_0
SELECT orchestra.record_firm FROM orchestra WHERE orchestra.year_foundation < 2003 INTERSECT SELECT orchestra.record_firm FROM orchestra WHERE orchestra.year_foundation > 2003	orchestra_0
SELECT orchestra.record_firm FROM orchestra WHERE orchestra.year_foundation < 2003 INTERSECT SELECT orchestra.record_firm FROM orchestra WHERE orchestra.year_foundation > 2003	orchestra_0
SELECT count(*) FROM orchestra WHERE orchestra.main_format = "CD" or orchestra.main_format = "DVD"	orchestra_0
SELECT count(*) FROM orchestra WHERE orchestra.main_format = "CD" or orchestra.main_format = "DVD"	orchestra_0
SELECT orchestra.year_foundation FROM orchestra JOIN performance ON orchestra.Orchestra_ID = performance.Orchestra_ID GROUP BY performance.Orchestra_ID HAVING count(*) > 1	orchestra_0
SELECT orchestra.year_foundation FROM orchestra JOIN performance ON orchestra.Orchestra_ID = performance.Orchestra_ID GROUP BY performance.Orchestra_ID HAVING count(*) > 1	orchestra_0
SELECT orchestra.Record_Company FROM orchestra ORDER BY orchestra.year_of_created desc	orchestra_1
SELECT orchestra.Record_Company FROM orchestra ORDER BY orchestra.year_of_created desc	orchestra_1
SELECT max(performance.portion) , min(performance.portion) FROM performance WHERE performance.Type != "Live final"	orchestra_1
SELECT max(performance.portion) , min(performance.portion) FROM performance WHERE performance.Type != "Live final"	orchestra_1
SELECT conductor.Name FROM conductor ORDER BY conductor.how_long_worked desc	orchestra_1
SELECT conductor.Name FROM conductor ORDER BY conductor.how_long_worked desc	orchestra_1
SELECT conductor.Name FROM conductor ORDER BY conductor.how_long_worked desc LIMIT 1	orchestra_1
SELECT conductor.Name FROM conductor ORDER BY conductor.how_long_worked desc LIMIT 1	orchestra_1
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID WHERE orchestra.year_of_created > 2008	orchestra_1
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.Conductor_ID WHERE orchestra.year_of_created > 2008	orchestra_1
SELECT orchestra.Record_Company FROM orchestra WHERE orchestra.year_of_created < 2003 INTERSECT SELECT orchestra.Record_Company FROM orchestra WHERE orchestra.year_of_created > 2003	orchestra_1
SELECT orchestra.Record_Company FROM orchestra WHERE orchestra.year_of_created < 2003 INTERSECT SELECT orchestra.Record_Company FROM orchestra WHERE orchestra.year_of_created > 2003	orchestra_1
SELECT orchestra.year_of_created FROM orchestra JOIN performance ON orchestra.Orchestra_ID = performance.Orchestra_ID GROUP BY performance.Orchestra_ID HAVING count(*) > 1	orchestra_1
SELECT orchestra.year_of_created FROM orchestra JOIN performance ON orchestra.Orchestra_ID = performance.Orchestra_ID GROUP BY performance.Orchestra_ID HAVING count(*) > 1	orchestra_1
SELECT max(performance.Share) , min(performance.Share) FROM performance WHERE performance.class_note != "Live final"	orchestra_2
SELECT max(performance.Share) , min(performance.Share) FROM performance WHERE performance.class_note != "Live final"	orchestra_2
SELECT conductor.Name FROM conductor WHERE conductor.ethnic_group != "USA"	orchestra_3
SELECT conductor.Name FROM conductor WHERE conductor.ethnic_group != "USA"	orchestra_3
SELECT orchestra.recorded_by FROM orchestra ORDER BY orchestra.Year_of_Founded desc	orchestra_3
SELECT orchestra.recorded_by FROM orchestra ORDER BY orchestra.Year_of_Founded desc	orchestra_3
SELECT avg(show.audience_number) FROM show	orchestra_3
SELECT avg(show.audience_number) FROM show	orchestra_3
SELECT max(performance.Share) , min(performance.Share) FROM performance WHERE performance.kind != "Live final"	orchestra_3
SELECT max(performance.Share) , min(performance.Share) FROM performance WHERE performance.kind != "Live final"	orchestra_3
SELECT count(DISTINCT conductor.ethnic_group) FROM conductor	orchestra_3
SELECT count(DISTINCT conductor.ethnic_group) FROM conductor	orchestra_3
SELECT orchestra.recorded_by , count(*) FROM orchestra GROUP BY orchestra.recorded_by	orchestra_3
SELECT orchestra.recorded_by , count(*) FROM orchestra GROUP BY orchestra.recorded_by	orchestra_3
SELECT orchestra.recorded_by FROM orchestra GROUP BY orchestra.recorded_by ORDER BY count(*) desc LIMIT 1	orchestra_3
SELECT orchestra.recorded_by FROM orchestra GROUP BY orchestra.recorded_by ORDER BY count(*) desc LIMIT 1	orchestra_3
SELECT orchestra.recorded_by FROM orchestra WHERE orchestra.Year_of_Founded < 2003 INTERSECT SELECT orchestra.recorded_by FROM orchestra WHERE orchestra.Year_of_Founded > 2003	orchestra_3
SELECT orchestra.recorded_by FROM orchestra WHERE orchestra.Year_of_Founded < 2003 INTERSECT SELECT orchestra.recorded_by FROM orchestra WHERE orchestra.Year_of_Founded > 2003	orchestra_3
SELECT max(performance.portion) , min(performance.portion) FROM performance WHERE performance.sort != "Live final"	orchestra_4
SELECT max(performance.portion) , min(performance.portion) FROM performance WHERE performance.sort != "Live final"	orchestra_4
SELECT conductor.Name FROM conductor ORDER BY conductor.practition_length desc	orchestra_4
SELECT conductor.Name FROM conductor ORDER BY conductor.practition_length desc	orchestra_4
SELECT conductor.Name FROM conductor ORDER BY conductor.practition_length desc LIMIT 1	orchestra_4
SELECT conductor.Name FROM conductor ORDER BY conductor.practition_length desc LIMIT 1	orchestra_4
SELECT orchestra.main_format FROM orchestra GROUP BY orchestra.main_format ORDER BY count(*) asc	orchestra_4
SELECT orchestra.main_format FROM orchestra GROUP BY orchestra.main_format ORDER BY count(*) asc	orchestra_4
SELECT count(*) FROM orchestra WHERE orchestra.main_format = "CD" or orchestra.main_format = "DVD"	orchestra_4
SELECT count(*) FROM orchestra WHERE orchestra.main_format = "CD" or orchestra.main_format = "DVD"	orchestra_4
SELECT Highschooler.name , Highschooler.school_level FROM Highschooler	network_1_0
SELECT Highschooler.name , Highschooler.school_level FROM Highschooler	network_1_0
SELECT Highschooler.school_level FROM Highschooler	network_1_0
SELECT Highschooler.school_level FROM Highschooler	network_1_0
SELECT Highschooler.school_level FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_0
SELECT Highschooler.school_level FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_0
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.school_level = 10	network_1_0
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.school_level = 10	network_1_0
SELECT count(*) FROM Highschooler WHERE Highschooler.school_level = 9 or Highschooler.school_level = 10	network_1_0
SELECT count(*) FROM Highschooler WHERE Highschooler.school_level = 9 or Highschooler.school_level = 10	network_1_0
SELECT Highschooler.school_level , count(*) FROM Highschooler GROUP BY Highschooler.school_level	network_1_0
SELECT Highschooler.school_level , count(*) FROM Highschooler GROUP BY Highschooler.school_level	network_1_0
SELECT Highschooler.school_level FROM Highschooler GROUP BY Highschooler.school_level ORDER BY count(*) desc LIMIT 1	network_1_0
SELECT Highschooler.school_level FROM Highschooler GROUP BY Highschooler.school_level ORDER BY count(*) desc LIMIT 1	network_1_0
SELECT Highschooler.school_level FROM Highschooler GROUP BY Highschooler.school_level HAVING count(*) >= 4	network_1_0
SELECT Highschooler.school_level FROM Highschooler GROUP BY Highschooler.school_level HAVING count(*) >= 4	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID WHERE Highschooler.school_level > 5 GROUP BY Friend.student_id HAVING count(*) >= 2	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID WHERE Highschooler.school_level > 5 GROUP BY Friend.student_id HAVING count(*) >= 2	network_1_0
SELECT avg(Highschooler.school_level) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_0
SELECT avg(Highschooler.school_level) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_0
SELECT min(Highschooler.school_level) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_0
SELECT min(Highschooler.school_level) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_0
SELECT Highschooler.name , Highschooler.level FROM Highschooler	network_1_1
SELECT Highschooler.name , Highschooler.level FROM Highschooler	network_1_1
SELECT Highschooler.level FROM Highschooler	network_1_1
SELECT Highschooler.level FROM Highschooler	network_1_1
SELECT Highschooler.level FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_1
SELECT Highschooler.level FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_1
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.level = 10	network_1_1
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.level = 10	network_1_1
SELECT count(*) FROM Highschooler WHERE Highschooler.level = 9 or Highschooler.level = 10	network_1_1
SELECT count(*) FROM Highschooler WHERE Highschooler.level = 9 or Highschooler.level = 10	network_1_1
SELECT Highschooler.level , count(*) FROM Highschooler GROUP BY Highschooler.level	network_1_1
SELECT Highschooler.level , count(*) FROM Highschooler GROUP BY Highschooler.level	network_1_1
SELECT Highschooler.level FROM Highschooler GROUP BY Highschooler.level ORDER BY count(*) desc LIMIT 1	network_1_1
SELECT Highschooler.level FROM Highschooler GROUP BY Highschooler.level ORDER BY count(*) desc LIMIT 1	network_1_1
SELECT Highschooler.level FROM Highschooler GROUP BY Highschooler.level HAVING count(*) >= 4	network_1_1
SELECT Highschooler.level FROM Highschooler GROUP BY Highschooler.level HAVING count(*) >= 4	network_1_1
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID WHERE Highschooler.level > 5 GROUP BY Friend.student_id HAVING count(*) >= 2	network_1_1
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID WHERE Highschooler.level > 5 GROUP BY Friend.student_id HAVING count(*) >= 2	network_1_1
SELECT avg(Highschooler.level) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_1
SELECT avg(Highschooler.level) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_1
SELECT min(Highschooler.level) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_1
SELECT min(Highschooler.level) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_1
SELECT Highschooler.name , Highschooler.class FROM Highschooler	network_1_2
SELECT Highschooler.name , Highschooler.class FROM Highschooler	network_1_2
SELECT Highschooler.class FROM Highschooler	network_1_2
SELECT Highschooler.class FROM Highschooler	network_1_2
SELECT Highschooler.class FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_2
SELECT Highschooler.class FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_2
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.class = 10	network_1_2
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.class = 10	network_1_2
SELECT count(*) FROM Highschooler WHERE Highschooler.class = 9 or Highschooler.class = 10	network_1_2
SELECT count(*) FROM Highschooler WHERE Highschooler.class = 9 or Highschooler.class = 10	network_1_2
SELECT Highschooler.class , count(*) FROM Highschooler GROUP BY Highschooler.class	network_1_2
SELECT Highschooler.class , count(*) FROM Highschooler GROUP BY Highschooler.class	network_1_2
SELECT Highschooler.class FROM Highschooler GROUP BY Highschooler.class ORDER BY count(*) desc LIMIT 1	network_1_2
SELECT Highschooler.class FROM Highschooler GROUP BY Highschooler.class ORDER BY count(*) desc LIMIT 1	network_1_2
SELECT Highschooler.class FROM Highschooler GROUP BY Highschooler.class HAVING count(*) >= 4	network_1_2
SELECT Highschooler.class FROM Highschooler GROUP BY Highschooler.class HAVING count(*) >= 4	network_1_2
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID WHERE Highschooler.class > 5 GROUP BY Friend.student_id HAVING count(*) >= 2	network_1_2
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID WHERE Highschooler.class > 5 GROUP BY Friend.student_id HAVING count(*) >= 2	network_1_2
SELECT avg(Highschooler.class) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_2
SELECT avg(Highschooler.class) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_2
SELECT min(Highschooler.class) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_2
SELECT min(Highschooler.class) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_2
SELECT Owners.province FROM Owners INTERSECT SELECT Professionals.region FROM Professionals	dog_kennels_0
SELECT Owners.province FROM Owners INTERSECT SELECT Professionals.region FROM Professionals	dog_kennels_0
SELECT Professionals.professional_id , Professionals.last_name , Professionals.cell_no FROM Professionals WHERE Professionals.region = "Indiana" UNION SELECT Professionals.professional_id , Professionals.last_name , Professionals.cell_no FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) > 2	dog_kennels_0
SELECT Professionals.professional_id , Professionals.last_name , Professionals.cell_no FROM Professionals WHERE Professionals.region = "Indiana" UNION SELECT Professionals.professional_id , Professionals.last_name , Professionals.cell_no FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) > 2	dog_kennels_0
SELECT Professionals.forename FROM Professionals UNION SELECT Owners.first_name FROM Owners EXCEPT SELECT Dogs.name FROM Dogs	dog_kennels_0
SELECT Professionals.forename FROM Professionals UNION SELECT Owners.first_name FROM Owners EXCEPT SELECT Dogs.name FROM Dogs	dog_kennels_0
SELECT Professionals.professional_id , Professionals.part_code , Professionals.e_mail_address FROM Professionals EXCEPT SELECT Professionals.professional_id , Professionals.part_code , Professionals.e_mail_address FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id	dog_kennels_0
SELECT Professionals.professional_id , Professionals.part_code , Professionals.e_mail_address FROM Professionals EXCEPT SELECT Professionals.professional_id , Professionals.part_code , Professionals.e_mail_address FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id	dog_kennels_0
SELECT Dogs.owner_id , Owners.first_name , Owners.family_name FROM Dogs JOIN Owners ON Dogs.owner_id = Owners.owner_id GROUP BY Dogs.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_0
SELECT Dogs.owner_id , Owners.first_name , Owners.family_name FROM Dogs JOIN Owners ON Dogs.owner_id = Owners.owner_id GROUP BY Dogs.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_0
SELECT Professionals.professional_id , Professionals.part_code , Professionals.forename FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_0
SELECT Professionals.professional_id , Professionals.part_code , Professionals.forename FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_0
SELECT Breeds.breed_name FROM Breeds JOIN Dogs ON Breeds.breed_cipher = Dogs.breed_cipher GROUP BY Breeds.breed_name ORDER BY count(*) desc LIMIT 1	dog_kennels_0
SELECT Breeds.breed_name FROM Breeds JOIN Dogs ON Breeds.breed_cipher = Dogs.breed_cipher GROUP BY Breeds.breed_name ORDER BY count(*) desc LIMIT 1	dog_kennels_0
SELECT Owners.owner_id , Owners.family_name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_0
SELECT Owners.owner_id , Owners.family_name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_0
SELECT Treatment_Types.treatment_category_description FROM Treatment_Types JOIN Treatments ON Treatment_Types.medical_category_code = Treatments.care_type_encipher GROUP BY Treatment_Types.medical_category_code ORDER BY sum(Treatments.cost_of_treatment) asc LIMIT 1	dog_kennels_0
SELECT Treatment_Types.treatment_category_description FROM Treatment_Types JOIN Treatments ON Treatment_Types.medical_category_code = Treatments.care_type_encipher GROUP BY Treatment_Types.medical_category_code ORDER BY sum(Treatments.cost_of_treatment) asc LIMIT 1	dog_kennels_0
SELECT Owners.owner_id , Owners.zip_number FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY sum(Treatments.cost_of_treatment) desc LIMIT 1	dog_kennels_0
SELECT Owners.owner_id , Owners.zip_number FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY sum(Treatments.cost_of_treatment) desc LIMIT 1	dog_kennels_0
SELECT Professionals.professional_id , Professionals.cell_no FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_0
SELECT Professionals.professional_id , Professionals.cell_no FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_0
SELECT DISTINCT Professionals.forename , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.cost_of_treatment < (SELECT avg(Treatments.cost_of_treatment) FROM Treatments)	dog_kennels_0
SELECT DISTINCT Professionals.forename , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.cost_of_treatment < (SELECT avg(Treatments.cost_of_treatment) FROM Treatments)	dog_kennels_0
SELECT Treatments.time_of_therapeutics , Professionals.forename FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_0
SELECT Treatments.time_of_therapeutics , Professionals.forename FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_0
SELECT Treatments.cost_of_treatment , Treatment_Types.treatment_category_description FROM Treatments JOIN Treatment_Types ON Treatments.care_type_encipher = Treatment_Types.medical_category_code	dog_kennels_0
SELECT Treatments.cost_of_treatment , Treatment_Types.treatment_category_description FROM Treatments JOIN Treatment_Types ON Treatments.care_type_encipher = Treatment_Types.medical_category_code	dog_kennels_0
SELECT Owners.first_name , Owners.family_name , Dogs.measurement_number FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_0
SELECT Owners.first_name , Owners.family_name , Dogs.measurement_number FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_0
SELECT Dogs.name , Treatments.time_of_therapeutics FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_cipher = (SELECT Dogs.breed_cipher FROM Dogs GROUP BY Dogs.breed_cipher ORDER BY count(*) asc LIMIT 1)	dog_kennels_0
SELECT Dogs.name , Treatments.time_of_therapeutics FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_cipher = (SELECT Dogs.breed_cipher FROM Dogs GROUP BY Dogs.breed_cipher ORDER BY count(*) asc LIMIT 1)	dog_kennels_0
SELECT Owners.first_name , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.province = "Virginia"	dog_kennels_0
SELECT Owners.first_name , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.province = "Virginia"	dog_kennels_0
SELECT DISTINCT Dogs.time_reached , Dogs.leave_time FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_0
SELECT DISTINCT Dogs.time_reached , Dogs.leave_time FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_0
SELECT Owners.family_name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Dogs.age = (SELECT max(Dogs.age) FROM Dogs)	dog_kennels_0
SELECT Owners.family_name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Dogs.age = (SELECT max(Dogs.age) FROM Dogs)	dog_kennels_0
SELECT Professionals.e_mail_address FROM Professionals WHERE Professionals.region = "Hawaii" or Professionals.region = "Wisconsin"	dog_kennels_0
SELECT Professionals.e_mail_address FROM Professionals WHERE Professionals.region = "Hawaii" or Professionals.region = "Wisconsin"	dog_kennels_0
SELECT Dogs.time_reached , Dogs.leave_time FROM Dogs	dog_kennels_0
SELECT Dogs.time_reached , Dogs.leave_time FROM Dogs	dog_kennels_0
SELECT Professionals.part_code , Professionals.avenue , Professionals.metropolis , Professionals.region FROM Professionals WHERE Professionals.metropolis like "%West%"	dog_kennels_0
SELECT Professionals.part_code , Professionals.avenue , Professionals.metropolis , Professionals.region FROM Professionals WHERE Professionals.metropolis like "%West%"	dog_kennels_0
SELECT Owners.first_name , Owners.family_name , Owners.mail FROM Owners WHERE Owners.province like "%North%"	dog_kennels_0
SELECT Owners.first_name , Owners.family_name , Owners.mail FROM Owners WHERE Owners.province like "%North%"	dog_kennels_0
SELECT Treatments.cost_of_treatment FROM Treatments ORDER BY Treatments.time_of_therapeutics desc LIMIT 1	dog_kennels_0
SELECT Treatments.cost_of_treatment FROM Treatments ORDER BY Treatments.time_of_therapeutics desc LIMIT 1	dog_kennels_0
SELECT Charges.cost_category , Charges.charges FROM Charges	dog_kennels_0
SELECT Charges.cost_category , Charges.charges FROM Charges	dog_kennels_0
SELECT max(Charges.charges) FROM Charges	dog_kennels_0
SELECT max(Charges.charges) FROM Charges	dog_kennels_0
SELECT Professionals.e_mail_address , Professionals.cell_no , Professionals.dwelling_calling FROM Professionals	dog_kennels_0
SELECT Professionals.e_mail_address , Professionals.cell_no , Professionals.dwelling_calling FROM Professionals	dog_kennels_0
SELECT DISTINCT Dogs.breed_cipher , Dogs.measurement_number FROM Dogs	dog_kennels_0
SELECT DISTINCT Dogs.breed_cipher , Dogs.measurement_number FROM Dogs	dog_kennels_0
SELECT DISTINCT Professionals.forename , Treatment_Types.treatment_category_description FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.care_type_encipher = Treatment_Types.medical_category_code	dog_kennels_0
SELECT DISTINCT Professionals.forename , Treatment_Types.treatment_category_description FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.care_type_encipher = Treatment_Types.medical_category_code	dog_kennels_0
SELECT Owners.province FROM Owners INTERSECT SELECT Professionals.state FROM Professionals	dog_kennels_1
SELECT Owners.province FROM Owners INTERSECT SELECT Professionals.state FROM Professionals	dog_kennels_1
SELECT avg(Dogs.age) FROM Dogs WHERE Dogs.dog_id in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_1
SELECT avg(Dogs.age) FROM Dogs WHERE Dogs.dog_id in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_1
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments GROUP BY Treatments.dog_included HAVING sum(Treatments.cost_of_treatment) > 1000.0)	dog_kennels_1
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments GROUP BY Treatments.dog_included HAVING sum(Treatments.cost_of_treatment) > 1000.0)	dog_kennels_1
SELECT Breeds.breed_designation FROM Breeds JOIN Dogs ON Breeds.breed_code = Dogs.breed_code GROUP BY Breeds.breed_designation ORDER BY count(*) desc LIMIT 1	dog_kennels_1
SELECT Breeds.breed_designation FROM Breeds JOIN Dogs ON Breeds.breed_code = Dogs.breed_code GROUP BY Breeds.breed_designation ORDER BY count(*) desc LIMIT 1	dog_kennels_1
SELECT Owners.owner_id , Owners.last_name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_1
SELECT Owners.owner_id , Owners.last_name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_1
SELECT Treatment_Types.therapy_type_fine_grained_info FROM Treatment_Types JOIN Treatments ON Treatment_Types.treatment_type_code = Treatments.treatment_type_code GROUP BY Treatment_Types.treatment_type_code ORDER BY sum(Treatments.cost_of_treatment) asc LIMIT 1	dog_kennels_1
SELECT Treatment_Types.therapy_type_fine_grained_info FROM Treatment_Types JOIN Treatments ON Treatment_Types.treatment_type_code = Treatments.treatment_type_code GROUP BY Treatment_Types.treatment_type_code ORDER BY sum(Treatments.cost_of_treatment) asc LIMIT 1	dog_kennels_1
SELECT Owners.owner_id , Owners.zip_number FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY sum(Treatments.cost_of_treatment) desc LIMIT 1	dog_kennels_1
SELECT Owners.owner_id , Owners.zip_number FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY sum(Treatments.cost_of_treatment) desc LIMIT 1	dog_kennels_1
SELECT Treatments.cost_of_treatment , Treatment_Types.therapy_type_fine_grained_info FROM Treatments JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.treatment_type_code	dog_kennels_1
SELECT Treatments.cost_of_treatment , Treatment_Types.therapy_type_fine_grained_info FROM Treatments JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.treatment_type_code	dog_kennels_1
SELECT Dogs.name , Treatments.date_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_1
SELECT Dogs.name , Treatments.date_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_1
SELECT Owners.first_name , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.province = "Virginia"	dog_kennels_1
SELECT Owners.first_name , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.province = "Virginia"	dog_kennels_1
SELECT DISTINCT Dogs.when_arrived , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included	dog_kennels_1
SELECT DISTINCT Dogs.when_arrived , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included	dog_kennels_1
SELECT Dogs.when_arrived , Dogs.date_departed FROM Dogs	dog_kennels_1
SELECT Dogs.when_arrived , Dogs.date_departed FROM Dogs	dog_kennels_1
SELECT count(DISTINCT Treatments.dog_included) FROM Treatments	dog_kennels_1
SELECT count(DISTINCT Treatments.dog_included) FROM Treatments	dog_kennels_1
SELECT Owners.first_name , Owners.last_name , Owners.email_address FROM Owners WHERE Owners.province like "%North%"	dog_kennels_1
SELECT Owners.first_name , Owners.last_name , Owners.email_address FROM Owners WHERE Owners.province like "%North%"	dog_kennels_1
SELECT count(*) FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_1
SELECT count(*) FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_1
SELECT Professionals.email_address , Professionals.cell_number , Professionals.home_ring_up FROM Professionals	dog_kennels_1
SELECT Professionals.email_address , Professionals.cell_number , Professionals.home_ring_up FROM Professionals	dog_kennels_1
SELECT DISTINCT Professionals.first_name , Treatment_Types.therapy_type_fine_grained_info FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.treatment_type_code	dog_kennels_1
SELECT DISTINCT Professionals.first_name , Treatment_Types.therapy_type_fine_grained_info FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.treatment_type_code	dog_kennels_1
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_id FROM Treatments GROUP BY Treatments.dog_id HAVING sum(Treatments.charge_of_curative) > 1000.0)	dog_kennels_2
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_id FROM Treatments GROUP BY Treatments.dog_id HAVING sum(Treatments.charge_of_curative) > 1000.0)	dog_kennels_2
SELECT Professionals.professional_id , Professionals.role_code , Professionals.mail FROM Professionals EXCEPT SELECT Professionals.professional_id , Professionals.role_code , Professionals.mail FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id	dog_kennels_2
SELECT Professionals.professional_id , Professionals.role_code , Professionals.mail FROM Professionals EXCEPT SELECT Professionals.professional_id , Professionals.role_code , Professionals.mail FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id	dog_kennels_2
SELECT Treatment_Types.treatment_type_description FROM Treatment_Types JOIN Treatments ON Treatment_Types.treatment_type_code = Treatments.treatment_type_code GROUP BY Treatment_Types.treatment_type_code ORDER BY sum(Treatments.charge_of_curative) asc LIMIT 1	dog_kennels_2
SELECT Treatment_Types.treatment_type_description FROM Treatment_Types JOIN Treatments ON Treatment_Types.treatment_type_code = Treatments.treatment_type_code GROUP BY Treatment_Types.treatment_type_code ORDER BY sum(Treatments.charge_of_curative) asc LIMIT 1	dog_kennels_2
SELECT Owners.owner_id , Owners.zip_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY sum(Treatments.charge_of_curative) desc LIMIT 1	dog_kennels_2
SELECT Owners.owner_id , Owners.zip_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY sum(Treatments.charge_of_curative) desc LIMIT 1	dog_kennels_2
SELECT DISTINCT Professionals.first_name , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.charge_of_curative < (SELECT avg(Treatments.charge_of_curative) FROM Treatments)	dog_kennels_2
SELECT DISTINCT Professionals.first_name , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.charge_of_curative < (SELECT avg(Treatments.charge_of_curative) FROM Treatments)	dog_kennels_2
SELECT Treatments.charge_of_curative , Treatment_Types.treatment_type_description FROM Treatments JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.treatment_type_code	dog_kennels_2
SELECT Treatments.charge_of_curative , Treatment_Types.treatment_type_description FROM Treatments JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.treatment_type_code	dog_kennels_2
SELECT DISTINCT Dogs.date_arrived , Dogs.when_left FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_2
SELECT DISTINCT Dogs.date_arrived , Dogs.when_left FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_2
SELECT Professionals.mail FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_2
SELECT Professionals.mail FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_2
SELECT Dogs.date_arrived , Dogs.when_left FROM Dogs	dog_kennels_2
SELECT Dogs.date_arrived , Dogs.when_left FROM Dogs	dog_kennels_2
SELECT Treatments.charge_of_curative FROM Treatments ORDER BY Treatments.date_of_treatment desc LIMIT 1	dog_kennels_2
SELECT Treatments.charge_of_curative FROM Treatments ORDER BY Treatments.date_of_treatment desc LIMIT 1	dog_kennels_2
SELECT Dogs.name , Dogs.age , Dogs.mass FROM Dogs WHERE Dogs.abandoned_yn = 1	dog_kennels_2
SELECT Dogs.name , Dogs.age , Dogs.mass FROM Dogs WHERE Dogs.abandoned_yn = 1	dog_kennels_2
SELECT Professionals.mail , Professionals.cell_number , Professionals.home_phone FROM Professionals	dog_kennels_2
SELECT Professionals.mail , Professionals.cell_number , Professionals.home_phone FROM Professionals	dog_kennels_2
SELECT Owners.province FROM Owners INTERSECT SELECT Professionals.district FROM Professionals	dog_kennels_3
SELECT Owners.province FROM Owners INTERSECT SELECT Professionals.district FROM Professionals	dog_kennels_3
SELECT avg(Dogs.age) FROM Dogs WHERE Dogs.dog_id in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_3
SELECT avg(Dogs.age) FROM Dogs WHERE Dogs.dog_id in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_3
SELECT Professionals.professional_id , Professionals.surname , Professionals.calling FROM Professionals WHERE Professionals.district = "Indiana" UNION SELECT Professionals.professional_id , Professionals.surname , Professionals.calling FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) > 2	dog_kennels_3
SELECT Professionals.professional_id , Professionals.surname , Professionals.calling FROM Professionals WHERE Professionals.district = "Indiana" UNION SELECT Professionals.professional_id , Professionals.surname , Professionals.calling FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) > 2	dog_kennels_3
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments GROUP BY Treatments.dog_included HAVING sum(Treatments.cost_of_treatment) > 1000.0)	dog_kennels_3
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments GROUP BY Treatments.dog_included HAVING sum(Treatments.cost_of_treatment) > 1000.0)	dog_kennels_3
SELECT Dogs.owner_id , Owners.first_name , Owners.surname FROM Dogs JOIN Owners ON Dogs.owner_id = Owners.owner_id GROUP BY Dogs.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_3
SELECT Dogs.owner_id , Owners.first_name , Owners.surname FROM Dogs JOIN Owners ON Dogs.owner_id = Owners.owner_id GROUP BY Dogs.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_3
SELECT Breeds.breed_cognomen FROM Breeds JOIN Dogs ON Breeds.breed_code = Dogs.breed_digits GROUP BY Breeds.breed_cognomen ORDER BY count(*) desc LIMIT 1	dog_kennels_3
SELECT Breeds.breed_cognomen FROM Breeds JOIN Dogs ON Breeds.breed_code = Dogs.breed_digits GROUP BY Breeds.breed_cognomen ORDER BY count(*) desc LIMIT 1	dog_kennels_3
SELECT Owners.owner_id , Owners.surname FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_3
SELECT Owners.owner_id , Owners.surname FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_3
SELECT Treatment_Types.treatment_type_description FROM Treatment_Types JOIN Treatments ON Treatment_Types.medical_category_code = Treatments.treatment_type_code GROUP BY Treatment_Types.medical_category_code ORDER BY sum(Treatments.cost_of_treatment) asc LIMIT 1	dog_kennels_3
SELECT Treatment_Types.treatment_type_description FROM Treatment_Types JOIN Treatments ON Treatment_Types.medical_category_code = Treatments.treatment_type_code GROUP BY Treatment_Types.medical_category_code ORDER BY sum(Treatments.cost_of_treatment) asc LIMIT 1	dog_kennels_3
SELECT Owners.owner_id , Owners.zip_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY sum(Treatments.cost_of_treatment) desc LIMIT 1	dog_kennels_3
SELECT Owners.owner_id , Owners.zip_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY sum(Treatments.cost_of_treatment) desc LIMIT 1	dog_kennels_3
SELECT Professionals.professional_id , Professionals.calling FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_3
SELECT Professionals.professional_id , Professionals.calling FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_3
SELECT DISTINCT Professionals.first_name , Professionals.surname FROM Professionals JOIN Treatments WHERE Treatments.cost_of_treatment < (SELECT avg(Treatments.cost_of_treatment) FROM Treatments)	dog_kennels_3
SELECT DISTINCT Professionals.first_name , Professionals.surname FROM Professionals JOIN Treatments WHERE Treatments.cost_of_treatment < (SELECT avg(Treatments.cost_of_treatment) FROM Treatments)	dog_kennels_3
SELECT Treatments.cost_of_treatment , Treatment_Types.treatment_type_description FROM Treatments JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.medical_category_code	dog_kennels_3
SELECT Treatments.cost_of_treatment , Treatment_Types.treatment_type_description FROM Treatments JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.medical_category_code	dog_kennels_3
SELECT Owners.first_name , Owners.surname , Dogs.size_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_3
SELECT Owners.first_name , Owners.surname , Dogs.size_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_3
SELECT Dogs.name , Treatments.date_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included WHERE Dogs.breed_digits = (SELECT Dogs.breed_digits FROM Dogs GROUP BY Dogs.breed_digits ORDER BY count(*) asc LIMIT 1)	dog_kennels_3
SELECT Dogs.name , Treatments.date_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included WHERE Dogs.breed_digits = (SELECT Dogs.breed_digits FROM Dogs GROUP BY Dogs.breed_digits ORDER BY count(*) asc LIMIT 1)	dog_kennels_3
SELECT Owners.first_name , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.province = "Virginia"	dog_kennels_3
SELECT Owners.first_name , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.province = "Virginia"	dog_kennels_3
SELECT DISTINCT Dogs.date_arrived , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included	dog_kennels_3
SELECT DISTINCT Dogs.date_arrived , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included	dog_kennels_3
SELECT Owners.surname FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Dogs.age = (SELECT max(Dogs.age) FROM Dogs)	dog_kennels_3
SELECT Owners.surname FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Dogs.age = (SELECT max(Dogs.age) FROM Dogs)	dog_kennels_3
SELECT Professionals.email_address FROM Professionals WHERE Professionals.district = "Hawaii" or Professionals.district = "Wisconsin"	dog_kennels_3
SELECT Professionals.email_address FROM Professionals WHERE Professionals.district = "Hawaii" or Professionals.district = "Wisconsin"	dog_kennels_3
SELECT count(DISTINCT Treatments.dog_included) FROM Treatments	dog_kennels_3
SELECT count(DISTINCT Treatments.dog_included) FROM Treatments	dog_kennels_3
SELECT Professionals.role_code , Professionals.avenue , Professionals.location , Professionals.district FROM Professionals WHERE Professionals.location like "%West%"	dog_kennels_3
SELECT Professionals.role_code , Professionals.avenue , Professionals.location , Professionals.district FROM Professionals WHERE Professionals.location like "%West%"	dog_kennels_3
SELECT Owners.first_name , Owners.surname , Owners.mailbox FROM Owners WHERE Owners.province like "%North%"	dog_kennels_3
SELECT Owners.first_name , Owners.surname , Owners.mailbox FROM Owners WHERE Owners.province like "%North%"	dog_kennels_3
SELECT count(*) FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_3
SELECT count(*) FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_3
SELECT Dogs.name , Dogs.age , Dogs.mass FROM Dogs WHERE Dogs.is_forsaken = 1	dog_kennels_3
SELECT Dogs.name , Dogs.age , Dogs.mass FROM Dogs WHERE Dogs.is_forsaken = 1	dog_kennels_3
SELECT Charges.charge_type , Charges.cost FROM Charges	dog_kennels_3
SELECT Charges.charge_type , Charges.cost FROM Charges	dog_kennels_3
SELECT max(Charges.cost) FROM Charges	dog_kennels_3
SELECT max(Charges.cost) FROM Charges	dog_kennels_3
SELECT Professionals.email_address , Professionals.calling , Professionals.home_phone FROM Professionals	dog_kennels_3
SELECT Professionals.email_address , Professionals.calling , Professionals.home_phone FROM Professionals	dog_kennels_3
SELECT DISTINCT Dogs.breed_digits , Dogs.size_code FROM Dogs	dog_kennels_3
SELECT DISTINCT Dogs.breed_digits , Dogs.size_code FROM Dogs	dog_kennels_3
SELECT DISTINCT Professionals.first_name , Treatment_Types.treatment_type_description FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.medical_category_code	dog_kennels_3
SELECT DISTINCT Professionals.first_name , Treatment_Types.treatment_type_description FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.medical_category_code	dog_kennels_3
SELECT Owners.province FROM Owners INTERSECT SELECT Professionals.state FROM Professionals	dog_kennels_4
SELECT Owners.province FROM Owners INTERSECT SELECT Professionals.state FROM Professionals	dog_kennels_4
SELECT avg(Dogs.age) FROM Dogs WHERE Dogs.dog_id in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_4
SELECT avg(Dogs.age) FROM Dogs WHERE Dogs.dog_id in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_4
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments GROUP BY Treatments.dog_included HAVING sum(Treatments.cost_of_treatment) > 1000.0)	dog_kennels_4
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments GROUP BY Treatments.dog_included HAVING sum(Treatments.cost_of_treatment) > 1000.0)	dog_kennels_4
SELECT Professionals.forename FROM Professionals UNION SELECT Owners.forename FROM Owners EXCEPT SELECT Dogs.name FROM Dogs	dog_kennels_4
SELECT Professionals.forename FROM Professionals UNION SELECT Owners.forename FROM Owners EXCEPT SELECT Dogs.name FROM Dogs	dog_kennels_4
SELECT Professionals.professional_id , Professionals.role_cipher , Professionals.e_mail_address FROM Professionals EXCEPT SELECT Professionals.professional_id , Professionals.role_cipher , Professionals.e_mail_address FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id	dog_kennels_4
SELECT Professionals.professional_id , Professionals.role_cipher , Professionals.e_mail_address FROM Professionals EXCEPT SELECT Professionals.professional_id , Professionals.role_cipher , Professionals.e_mail_address FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id	dog_kennels_4
SELECT Dogs.owner_id , Owners.forename , Owners.last_name FROM Dogs JOIN Owners ON Dogs.owner_id = Owners.owner_id GROUP BY Dogs.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_4
SELECT Dogs.owner_id , Owners.forename , Owners.last_name FROM Dogs JOIN Owners ON Dogs.owner_id = Owners.owner_id GROUP BY Dogs.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_4
SELECT Professionals.professional_id , Professionals.role_cipher , Professionals.forename FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_4
SELECT Professionals.professional_id , Professionals.role_cipher , Professionals.forename FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_4
SELECT Breeds.breed_name FROM Breeds JOIN Dogs ON Breeds.breed_code = Dogs.breed_cipher GROUP BY Breeds.breed_name ORDER BY count(*) desc LIMIT 1	dog_kennels_4
SELECT Breeds.breed_name FROM Breeds JOIN Dogs ON Breeds.breed_code = Dogs.breed_cipher GROUP BY Breeds.breed_name ORDER BY count(*) desc LIMIT 1	dog_kennels_4
SELECT Owners.owner_id , Owners.last_name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_4
SELECT Owners.owner_id , Owners.last_name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY count(*) desc LIMIT 1	dog_kennels_4
SELECT Treatment_Types.treatment_type_description FROM Treatment_Types JOIN Treatments ON Treatment_Types.treatment_type_number = Treatments.category GROUP BY Treatment_Types.treatment_type_number ORDER BY sum(Treatments.cost_of_treatment) asc LIMIT 1	dog_kennels_4
SELECT Treatment_Types.treatment_type_description FROM Treatment_Types JOIN Treatments ON Treatment_Types.treatment_type_number = Treatments.category GROUP BY Treatment_Types.treatment_type_number ORDER BY sum(Treatments.cost_of_treatment) asc LIMIT 1	dog_kennels_4
SELECT Owners.owner_id , Owners.zip_number FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY sum(Treatments.cost_of_treatment) desc LIMIT 1	dog_kennels_4
SELECT Owners.owner_id , Owners.zip_number FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_included GROUP BY Owners.owner_id ORDER BY sum(Treatments.cost_of_treatment) desc LIMIT 1	dog_kennels_4
SELECT DISTINCT Professionals.forename , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.cost_of_treatment < (SELECT avg(Treatments.cost_of_treatment) FROM Treatments)	dog_kennels_4
SELECT DISTINCT Professionals.forename , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.cost_of_treatment < (SELECT avg(Treatments.cost_of_treatment) FROM Treatments)	dog_kennels_4
SELECT Treatments.date_of_treatment , Professionals.forename FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_4
SELECT Treatments.date_of_treatment , Professionals.forename FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id	dog_kennels_4
SELECT Treatments.cost_of_treatment , Treatment_Types.treatment_type_description FROM Treatments JOIN Treatment_Types ON Treatments.category = Treatment_Types.treatment_type_number	dog_kennels_4
SELECT Treatments.cost_of_treatment , Treatment_Types.treatment_type_description FROM Treatments JOIN Treatment_Types ON Treatments.category = Treatment_Types.treatment_type_number	dog_kennels_4
SELECT Owners.forename , Owners.last_name , Dogs.size_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_4
SELECT Owners.forename , Owners.last_name , Dogs.size_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_4
SELECT Owners.forename , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_4
SELECT Owners.forename , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_4
SELECT Dogs.name , Treatments.date_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included WHERE Dogs.breed_cipher = (SELECT Dogs.breed_cipher FROM Dogs GROUP BY Dogs.breed_cipher ORDER BY count(*) asc LIMIT 1)	dog_kennels_4
SELECT Dogs.name , Treatments.date_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included WHERE Dogs.breed_cipher = (SELECT Dogs.breed_cipher FROM Dogs GROUP BY Dogs.breed_cipher ORDER BY count(*) asc LIMIT 1)	dog_kennels_4
SELECT Owners.forename , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.province = "Virginia"	dog_kennels_4
SELECT Owners.forename , Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.province = "Virginia"	dog_kennels_4
SELECT DISTINCT Dogs.date_arrived , Dogs.depature_day FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included	dog_kennels_4
SELECT DISTINCT Dogs.date_arrived , Dogs.depature_day FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_included	dog_kennels_4
SELECT Professionals.e_mail_address FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_4
SELECT Professionals.e_mail_address FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_4
SELECT Dogs.date_arrived , Dogs.depature_day FROM Dogs	dog_kennels_4
SELECT Dogs.date_arrived , Dogs.depature_day FROM Dogs	dog_kennels_4
SELECT count(DISTINCT Treatments.dog_included) FROM Treatments	dog_kennels_4
SELECT count(DISTINCT Treatments.dog_included) FROM Treatments	dog_kennels_4
SELECT Professionals.role_cipher , Professionals.avenue , Professionals.capital_area , Professionals.state FROM Professionals WHERE Professionals.capital_area like "%West%"	dog_kennels_4
SELECT Professionals.role_cipher , Professionals.avenue , Professionals.capital_area , Professionals.state FROM Professionals WHERE Professionals.capital_area like "%West%"	dog_kennels_4
SELECT Owners.forename , Owners.last_name , Owners.email_address FROM Owners WHERE Owners.province like "%North%"	dog_kennels_4
SELECT Owners.forename , Owners.last_name , Owners.email_address FROM Owners WHERE Owners.province like "%North%"	dog_kennels_4
SELECT count(*) FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_4
SELECT count(*) FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_included FROM Treatments)	dog_kennels_4
SELECT Dogs.name , Dogs.age , Dogs.weight FROM Dogs WHERE Dogs.deserted = 1	dog_kennels_4
SELECT Dogs.name , Dogs.age , Dogs.weight FROM Dogs WHERE Dogs.deserted = 1	dog_kennels_4
SELECT Professionals.e_mail_address , Professionals.cell_number , Professionals.host_ring_up FROM Professionals	dog_kennels_4
SELECT Professionals.e_mail_address , Professionals.cell_number , Professionals.host_ring_up FROM Professionals	dog_kennels_4
SELECT DISTINCT Dogs.breed_cipher , Dogs.size_code FROM Dogs	dog_kennels_4
SELECT DISTINCT Dogs.breed_cipher , Dogs.size_code FROM Dogs	dog_kennels_4
SELECT DISTINCT Professionals.forename , Treatment_Types.treatment_type_description FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.category = Treatment_Types.treatment_type_number	dog_kennels_4
SELECT DISTINCT Professionals.forename , Treatment_Types.treatment_type_description FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.category = Treatment_Types.treatment_type_number	dog_kennels_4
SELECT singer.Name FROM singer ORDER BY singer.value_estimation asc	singer_0
SELECT singer.Name FROM singer ORDER BY singer.value_estimation asc	singer_0
SELECT singer.born_date , singer.nationality FROM singer	singer_0
SELECT singer.born_date , singer.nationality FROM singer	singer_0
SELECT singer.Name FROM singer WHERE singer.nationality != "France"	singer_0
SELECT singer.Name FROM singer WHERE singer.nationality != "France"	singer_0
SELECT singer.Name FROM singer WHERE singer.born_date = 1948 or singer.born_date = 1949	singer_0
SELECT singer.Name FROM singer WHERE singer.born_date = 1948 or singer.born_date = 1949	singer_0
SELECT singer.Name FROM singer ORDER BY singer.value_estimation desc LIMIT 1	singer_0
SELECT singer.Name FROM singer ORDER BY singer.value_estimation desc LIMIT 1	singer_0
SELECT singer.nationality , count(*) FROM singer GROUP BY singer.nationality	singer_0
SELECT singer.nationality , count(*) FROM singer GROUP BY singer.nationality	singer_0
SELECT singer.nationality FROM singer GROUP BY singer.nationality ORDER BY count(*) desc LIMIT 1	singer_0
SELECT singer.nationality FROM singer GROUP BY singer.nationality ORDER BY count(*) desc LIMIT 1	singer_0
SELECT singer.nationality , max(singer.value_estimation) FROM singer GROUP BY singer.nationality	singer_0
SELECT singer.nationality , max(singer.value_estimation) FROM singer GROUP BY singer.nationality	singer_0
SELECT DISTINCT singer.Name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID WHERE song.selling > 300000	singer_0
SELECT DISTINCT singer.Name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID WHERE song.selling > 300000	singer_0
SELECT singer.Name , sum(song.selling) FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.Name	singer_0
SELECT singer.Name , sum(song.selling) FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.Name	singer_0
SELECT singer.nationality FROM singer WHERE singer.born_date < 1945 INTERSECT SELECT singer.nationality FROM singer WHERE singer.born_date > 1955	singer_0
SELECT singer.nationality FROM singer WHERE singer.born_date < 1945 INTERSECT SELECT singer.nationality FROM singer WHERE singer.born_date > 1955	singer_0
SELECT singer.born_yr , singer.Citizenship FROM singer	singer_1
SELECT singer.born_yr , singer.Citizenship FROM singer	singer_1
SELECT singer.Name FROM singer WHERE singer.born_yr = 1948 or singer.born_yr = 1949	singer_1
SELECT singer.Name FROM singer WHERE singer.born_yr = 1948 or singer.born_yr = 1949	singer_1
SELECT DISTINCT singer.Name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID WHERE song.sold > 300000	singer_1
SELECT DISTINCT singer.Name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID WHERE song.sold > 300000	singer_1
SELECT singer.Name , sum(song.sold) FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.Name	singer_1
SELECT singer.Name , sum(song.sold) FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.Name	singer_1
SELECT singer.Citizenship FROM singer WHERE singer.born_yr < 1945 INTERSECT SELECT singer.Citizenship FROM singer WHERE singer.born_yr > 1955	singer_1
SELECT singer.Citizenship FROM singer WHERE singer.born_yr < 1945 INTERSECT SELECT singer.Citizenship FROM singer WHERE singer.born_yr > 1955	singer_1
SELECT singer.Name FROM singer ORDER BY singer.gross_value asc	singer_2
SELECT singer.Name FROM singer ORDER BY singer.gross_value asc	singer_2
SELECT singer.Name FROM singer ORDER BY singer.gross_value desc LIMIT 1	singer_2
SELECT singer.Name FROM singer ORDER BY singer.gross_value desc LIMIT 1	singer_2
SELECT singer.Citizenship , max(singer.gross_value) FROM singer GROUP BY singer.Citizenship	singer_2
SELECT singer.Citizenship , max(singer.gross_value) FROM singer GROUP BY singer.Citizenship	singer_2
SELECT singer.born_yr , singer.Citizenship FROM singer	singer_3
SELECT singer.born_yr , singer.Citizenship FROM singer	singer_3
SELECT singer.Name FROM singer WHERE singer.born_yr = 1948 or singer.born_yr = 1949	singer_3
SELECT singer.Name FROM singer WHERE singer.born_yr = 1948 or singer.born_yr = 1949	singer_3
SELECT DISTINCT singer.Name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID WHERE song.number_of_trading > 300000	singer_3
SELECT DISTINCT singer.Name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID WHERE song.number_of_trading > 300000	singer_3
SELECT singer.Name , sum(song.number_of_trading) FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.Name	singer_3
SELECT singer.Name , sum(song.number_of_trading) FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.Name	singer_3
SELECT singer.Citizenship FROM singer WHERE singer.born_yr < 1945 INTERSECT SELECT singer.Citizenship FROM singer WHERE singer.born_yr > 1955	singer_3
SELECT singer.Citizenship FROM singer WHERE singer.born_yr < 1945 INTERSECT SELECT singer.Citizenship FROM singer WHERE singer.born_yr > 1955	singer_3
SELECT singer.born_date , singer.home_country FROM singer	singer_4
SELECT singer.born_date , singer.home_country FROM singer	singer_4
SELECT singer.Name FROM singer WHERE singer.home_country != "France"	singer_4
SELECT singer.Name FROM singer WHERE singer.home_country != "France"	singer_4
SELECT singer.Name FROM singer WHERE singer.born_date = 1948 or singer.born_date = 1949	singer_4
SELECT singer.Name FROM singer WHERE singer.born_date = 1948 or singer.born_date = 1949	singer_4
SELECT singer.home_country , count(*) FROM singer GROUP BY singer.home_country	singer_4
SELECT singer.home_country , count(*) FROM singer GROUP BY singer.home_country	singer_4
SELECT singer.home_country FROM singer GROUP BY singer.home_country ORDER BY count(*) desc LIMIT 1	singer_4
SELECT singer.home_country FROM singer GROUP BY singer.home_country ORDER BY count(*) desc LIMIT 1	singer_4
SELECT singer.home_country , max(singer.Net_Worth_Millions) FROM singer GROUP BY singer.home_country	singer_4
SELECT singer.home_country , max(singer.Net_Worth_Millions) FROM singer GROUP BY singer.home_country	singer_4
SELECT singer.home_country FROM singer WHERE singer.born_date < 1945 INTERSECT SELECT singer.home_country FROM singer WHERE singer.born_date > 1955	singer_4
SELECT singer.home_country FROM singer WHERE singer.born_date < 1945 INTERSECT SELECT singer.home_country FROM singer WHERE singer.born_date > 1955	singer_4
SELECT Ref_Feature_Types.characteristics_type_name FROM Other_Available_Features JOIN Ref_Feature_Types ON Other_Available_Features.attribute_type_num = Ref_Feature_Types.attribute_category_number WHERE Other_Available_Features.attribute_appellation = "AirCon"	real_estate_properties_0
SELECT Ref_Property_Types.category_details FROM Properties JOIN Ref_Property_Types ON Properties.type_of_property = Ref_Property_Types.property_type_code GROUP BY Properties.type_of_property	real_estate_properties_0
SELECT Properties.property_name FROM Properties WHERE Properties.type_of_property = "House" UNION SELECT Properties.property_name FROM Properties WHERE Properties.type_of_property = "Apartment" and Properties.total_room > 1	real_estate_properties_0
SELECT Ref_Property_Types.property_type_description FROM Properties JOIN Ref_Property_Types ON Properties.possessions_class_num = Ref_Property_Types.property_type_code GROUP BY Properties.possessions_class_num	real_estate_properties_1
SELECT Properties.estate_name FROM Properties WHERE Properties.possessions_class_num = "House" UNION SELECT Properties.estate_name FROM Properties WHERE Properties.possessions_class_num = "Apartment" and Properties.number_room > 1	real_estate_properties_1
SELECT Ref_Feature_Types.feature_type_name FROM Other_Available_Features JOIN Ref_Feature_Types ON Other_Available_Features.trait_type_cipher = Ref_Feature_Types.feature_type_code WHERE Other_Available_Features.feature_name = "AirCon"	real_estate_properties_2
SELECT Ref_Feature_Types.property_type_name FROM Other_Available_Features JOIN Ref_Feature_Types ON Other_Available_Features.feature_type_code = Ref_Feature_Types.attribute_category_num WHERE Other_Available_Features.feature_name = "AirCon"	real_estate_properties_3
SELECT Ref_Property_Types.property_type_description FROM Properties JOIN Ref_Property_Types ON Properties.possessions_class_num = Ref_Property_Types.property_type_code GROUP BY Properties.possessions_class_num	real_estate_properties_3
SELECT Properties.property_cognomen FROM Properties WHERE Properties.possessions_class_num = "House" UNION SELECT Properties.property_cognomen FROM Properties WHERE Properties.possessions_class_num = "Apartment" and Properties.room_count > 1	real_estate_properties_3
SELECT Ref_Feature_Types.characteristics_type_name FROM Other_Available_Features JOIN Ref_Feature_Types ON Other_Available_Features.feature_type_code = Ref_Feature_Types.feature_type_code WHERE Other_Available_Features.feature_name = "AirCon"	real_estate_properties_4
SELECT Ref_Property_Types.genus_details FROM Properties JOIN Ref_Property_Types ON Properties.property_type_code = Ref_Property_Types.property_type_code GROUP BY Properties.property_type_code	real_estate_properties_4
SELECT Properties.house_designation FROM Properties WHERE Properties.property_type_code = "House" UNION SELECT Properties.house_designation FROM Properties WHERE Properties.property_type_code = "Apartment" and Properties.total_room > 1	real_estate_properties_4
