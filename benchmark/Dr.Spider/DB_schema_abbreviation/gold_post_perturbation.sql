SELECT singer.Name , singer.cntry , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_0
SELECT singer.Name , singer.cntry , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_0
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.cntry = "France"	concert_singer_0
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.cntry = "France"	concert_singer_0
SELECT DISTINCT singer.cntry FROM singer WHERE singer.Age > 20	concert_singer_0
SELECT DISTINCT singer.cntry FROM singer WHERE singer.Age > 20	concert_singer_0
SELECT singer.cntry , count(*) FROM singer GROUP BY singer.cntry	concert_singer_0
SELECT singer.cntry , count(*) FROM singer GROUP BY singer.cntry	concert_singer_0
SELECT stadium.loc , stadium.Name FROM stadium WHERE stadium.cap BETWEEN 5000 AND 10000	concert_singer_0
SELECT stadium.loc , stadium.Name FROM stadium WHERE stadium.cap BETWEEN 5000 AND 10000	concert_singer_0
SELECT max(stadium.cap) , stadium.Average FROM stadium	concert_singer_0
SELECT avg(stadium.cap) , max(stadium.cap) FROM stadium	concert_singer_0
SELECT stadium.Name , stadium.cap FROM stadium ORDER BY stadium.Average desc LIMIT 1	concert_singer_0
SELECT stadium.Name , stadium.cap FROM stadium ORDER BY stadium.Average desc LIMIT 1	concert_singer_0
SELECT stadium.Name , count(*) FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id GROUP BY concert.Stadium_ID	concert_singer_0
SELECT stadium.Name , count(*) FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id GROUP BY concert.Stadium_ID	concert_singer_0
SELECT stadium.Name , stadium.cap FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year >= 2014 GROUP BY stadium.stdm_id ORDER BY count(*) desc LIMIT 1	concert_singer_0
SELECT stadium.Name , stadium.cap FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year > 2013 GROUP BY stadium.stdm_id ORDER BY count(*) desc LIMIT 1	concert_singer_0
SELECT stadium.Name FROM stadium WHERE stadium.stdm_id NOT in (SELECT concert.Stadium_ID FROM concert)	concert_singer_0
SELECT stadium.Name FROM stadium WHERE stadium.stdm_id NOT in (SELECT concert.Stadium_ID FROM concert)	concert_singer_0
SELECT singer.cntry FROM singer WHERE singer.Age > 40 INTERSECT SELECT singer.cntry FROM singer WHERE singer.Age < 30	concert_singer_0
SELECT stadium.Name FROM stadium EXCEPT SELECT stadium.Name FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2014	concert_singer_0
SELECT stadium.Name FROM stadium EXCEPT SELECT stadium.Name FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2014	concert_singer_0
SELECT singer.Name , singer.cntry FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_0
SELECT singer.Name , singer.cntry FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_0
SELECT stadium.Name , stadium.loc FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.loc FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2015	concert_singer_0
SELECT stadium.Name , stadium.loc FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.loc FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2015	concert_singer_0
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.stdm_id FROM stadium ORDER BY stadium.cap desc LIMIT 1)	concert_singer_0
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.stdm_id FROM stadium ORDER BY stadium.cap desc LIMIT 1)	concert_singer_0
SELECT singer.Name , singer.cntry , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_1
SELECT singer.Name , singer.cntry , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_1
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.cntry = "France"	concert_singer_1
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.cntry = "France"	concert_singer_1
SELECT singer.Song_Name , singer.song_rls_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_1
SELECT singer.Song_Name , singer.song_rls_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_1
SELECT DISTINCT singer.cntry FROM singer WHERE singer.Age > 20	concert_singer_1
SELECT DISTINCT singer.cntry FROM singer WHERE singer.Age > 20	concert_singer_1
SELECT singer.cntry , count(*) FROM singer GROUP BY singer.cntry	concert_singer_1
SELECT singer.cntry , count(*) FROM singer GROUP BY singer.cntry	concert_singer_1
SELECT stadium.Location , stadium.Name FROM stadium WHERE stadium.cap BETWEEN 5000 AND 10000	concert_singer_1
SELECT stadium.Location , stadium.Name FROM stadium WHERE stadium.cap BETWEEN 5000 AND 10000	concert_singer_1
SELECT max(stadium.cap) , stadium.avg FROM stadium	concert_singer_1
SELECT avg(stadium.cap) , max(stadium.cap) FROM stadium	concert_singer_1
SELECT stadium.Name , stadium.cap FROM stadium ORDER BY stadium.avg desc LIMIT 1	concert_singer_1
SELECT stadium.Name , stadium.cap FROM stadium ORDER BY stadium.avg desc LIMIT 1	concert_singer_1
SELECT stadium.Name , count(*) FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id GROUP BY concert.stdm_id	concert_singer_1
SELECT stadium.Name , count(*) FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id GROUP BY concert.stdm_id	concert_singer_1
SELECT stadium.Name , stadium.cap FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id WHERE concert.Year >= 2014 GROUP BY stadium.stdm_id ORDER BY count(*) desc LIMIT 1	concert_singer_1
SELECT stadium.Name , stadium.cap FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id WHERE concert.Year > 2013 GROUP BY stadium.stdm_id ORDER BY count(*) desc LIMIT 1	concert_singer_1
SELECT stadium.Name FROM stadium WHERE stadium.stdm_id NOT in (SELECT concert.stdm_id FROM concert)	concert_singer_1
SELECT stadium.Name FROM stadium WHERE stadium.stdm_id NOT in (SELECT concert.stdm_id FROM concert)	concert_singer_1
SELECT singer.cntry FROM singer WHERE singer.Age > 40 INTERSECT SELECT singer.cntry FROM singer WHERE singer.Age < 30	concert_singer_1
SELECT stadium.Name FROM stadium EXCEPT SELECT stadium.Name FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id WHERE concert.Year = 2014	concert_singer_1
SELECT stadium.Name FROM stadium EXCEPT SELECT stadium.Name FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id WHERE concert.Year = 2014	concert_singer_1
SELECT singer.Name , singer.cntry FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_1
SELECT singer.Name , singer.cntry FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_1
SELECT stadium.Name , stadium.Location FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.Location FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id WHERE concert.Year = 2015	concert_singer_1
SELECT stadium.Name , stadium.Location FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.Location FROM concert JOIN stadium ON concert.stdm_id = stadium.stdm_id WHERE concert.Year = 2015	concert_singer_1
SELECT count(*) FROM concert WHERE concert.stdm_id = (SELECT stadium.stdm_id FROM stadium ORDER BY stadium.cap desc LIMIT 1)	concert_singer_1
SELECT count(*) FROM concert WHERE concert.stdm_id = (SELECT stadium.stdm_id FROM stadium ORDER BY stadium.cap desc LIMIT 1)	concert_singer_1
SELECT singer.Name , singer.cntry , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_2
SELECT singer.Name , singer.cntry , singer.Age FROM singer ORDER BY singer.Age desc	concert_singer_2
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.cntry = "France"	concert_singer_2
SELECT avg(singer.Age) , min(singer.Age) , max(singer.Age) FROM singer WHERE singer.cntry = "France"	concert_singer_2
SELECT singer.Song_Name , singer.song_rls_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_2
SELECT singer.Song_Name , singer.song_rls_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_2
SELECT DISTINCT singer.cntry FROM singer WHERE singer.Age > 20	concert_singer_2
SELECT DISTINCT singer.cntry FROM singer WHERE singer.Age > 20	concert_singer_2
SELECT singer.cntry , count(*) FROM singer GROUP BY singer.cntry	concert_singer_2
SELECT singer.cntry , count(*) FROM singer GROUP BY singer.cntry	concert_singer_2
SELECT stadium.loc , stadium.Name FROM stadium WHERE stadium.cap BETWEEN 5000 AND 10000	concert_singer_2
SELECT stadium.loc , stadium.Name FROM stadium WHERE stadium.cap BETWEEN 5000 AND 10000	concert_singer_2
SELECT max(stadium.cap) , stadium.avg FROM stadium	concert_singer_2
SELECT avg(stadium.cap) , max(stadium.cap) FROM stadium	concert_singer_2
SELECT stadium.Name , stadium.cap FROM stadium ORDER BY stadium.avg desc LIMIT 1	concert_singer_2
SELECT stadium.Name , stadium.cap FROM stadium ORDER BY stadium.avg desc LIMIT 1	concert_singer_2
SELECT stadium.Name , stadium.cap FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year >= 2014 GROUP BY stadium.Stadium_ID ORDER BY count(*) desc LIMIT 1	concert_singer_2
SELECT stadium.Name , stadium.cap FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year > 2013 GROUP BY stadium.Stadium_ID ORDER BY count(*) desc LIMIT 1	concert_singer_2
SELECT singer.cntry FROM singer WHERE singer.Age > 40 INTERSECT SELECT singer.cntry FROM singer WHERE singer.Age < 30	concert_singer_2
SELECT singer.Name , singer.cntry FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_2
SELECT singer.Name , singer.cntry FROM singer WHERE singer.Song_Name like "%Hey%"	concert_singer_2
SELECT stadium.Name , stadium.loc FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.loc FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2015	concert_singer_2
SELECT stadium.Name , stadium.loc FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.loc FROM concert JOIN stadium ON concert.Stadium_ID = stadium.Stadium_ID WHERE concert.Year = 2015	concert_singer_2
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.Stadium_ID FROM stadium ORDER BY stadium.cap desc LIMIT 1)	concert_singer_2
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.Stadium_ID FROM stadium ORDER BY stadium.cap desc LIMIT 1)	concert_singer_2
SELECT stadium.Location , stadium.Name FROM stadium WHERE stadium.cap BETWEEN 5000 AND 10000	concert_singer_3
SELECT stadium.Location , stadium.Name FROM stadium WHERE stadium.cap BETWEEN 5000 AND 10000	concert_singer_3
SELECT max(stadium.cap) , stadium.avg FROM stadium	concert_singer_3
SELECT avg(stadium.cap) , max(stadium.cap) FROM stadium	concert_singer_3
SELECT stadium.Name , stadium.cap FROM stadium ORDER BY stadium.avg desc LIMIT 1	concert_singer_3
SELECT stadium.Name , stadium.cap FROM stadium ORDER BY stadium.avg desc LIMIT 1	concert_singer_3
SELECT stadium.Name , count(*) FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id GROUP BY concert.Stadium_ID	concert_singer_3
SELECT stadium.Name , count(*) FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id GROUP BY concert.Stadium_ID	concert_singer_3
SELECT stadium.Name , stadium.cap FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year >= 2014 GROUP BY stadium.stdm_id ORDER BY count(*) desc LIMIT 1	concert_singer_3
SELECT stadium.Name , stadium.cap FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year > 2013 GROUP BY stadium.stdm_id ORDER BY count(*) desc LIMIT 1	concert_singer_3
SELECT stadium.Name FROM stadium WHERE stadium.stdm_id NOT in (SELECT concert.Stadium_ID FROM concert)	concert_singer_3
SELECT stadium.Name FROM stadium WHERE stadium.stdm_id NOT in (SELECT concert.Stadium_ID FROM concert)	concert_singer_3
SELECT stadium.Name FROM stadium EXCEPT SELECT stadium.Name FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2014	concert_singer_3
SELECT stadium.Name FROM stadium EXCEPT SELECT stadium.Name FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2014	concert_singer_3
SELECT stadium.Name , stadium.Location FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.Location FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2015	concert_singer_3
SELECT stadium.Name , stadium.Location FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2014 INTERSECT SELECT stadium.Name , stadium.Location FROM concert JOIN stadium ON concert.Stadium_ID = stadium.stdm_id WHERE concert.Year = 2015	concert_singer_3
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.stdm_id FROM stadium ORDER BY stadium.cap desc LIMIT 1)	concert_singer_3
SELECT count(*) FROM concert WHERE concert.Stadium_ID = (SELECT stadium.stdm_id FROM stadium ORDER BY stadium.cap desc LIMIT 1)	concert_singer_3
SELECT singer.Song_Name , singer.song_rls_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_4
SELECT singer.Song_Name , singer.song_rls_year FROM singer ORDER BY singer.Age asc LIMIT 1	concert_singer_4
SELECT count(*) FROM Pets WHERE Pets.wt > 10	pets_1_1
SELECT count(*) FROM Pets WHERE Pets.wt > 10	pets_1_1
SELECT Pets.wt FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_1
SELECT Pets.wt FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_1
SELECT max(Pets.wt) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_1
SELECT max(Pets.wt) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_1
SELECT Pets.PetType , Pets.wt FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_1
SELECT Pets.PetType , Pets.wt FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_1
SELECT Pets.PetID , Pets.wt FROM Pets WHERE Pets.pet_age > 1	pets_1_1
SELECT Pets.PetID , Pets.wt FROM Pets WHERE Pets.pet_age > 1	pets_1_1
SELECT avg(Pets.wt) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_1
SELECT avg(Pets.wt) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_1
SELECT count(*) FROM Pets WHERE Pets.wt > 10	pets_1_2
SELECT count(*) FROM Pets WHERE Pets.wt > 10	pets_1_2
SELECT Pets.wt FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_2
SELECT Pets.wt FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_2
SELECT max(Pets.wt) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_2
SELECT max(Pets.wt) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_2
SELECT Pets.PetType , Pets.wt FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_2
SELECT Pets.PetType , Pets.wt FROM Pets ORDER BY Pets.pet_age asc LIMIT 1	pets_1_2
SELECT Pets.PetID , Pets.wt FROM Pets WHERE Pets.pet_age > 1	pets_1_2
SELECT Pets.PetID , Pets.wt FROM Pets WHERE Pets.pet_age > 1	pets_1_2
SELECT avg(Pets.wt) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_2
SELECT avg(Pets.wt) , Pets.PetType FROM Pets GROUP BY Pets.PetType	pets_1_2
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.hp asc LIMIT 1	car_1_0
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.hp asc LIMIT 1	car_1_0
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.wt < (SELECT avg(cars_data.wt) FROM cars_data)	car_1_0
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.wt < (SELECT avg(cars_data.wt) FROM cars_data)	car_1_0
SELECT continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.Continent JOIN car_makers ON countries.cntry_id = car_makers.Country GROUP BY continents.Continent	car_1_0
SELECT continents.Continent , count(*) FROM continents JOIN countries ON continents.ContId = countries.Continent JOIN car_makers ON countries.cntry_id = car_makers.Country GROUP BY continents.Continent	car_1_0
SELECT countries.cntry_name FROM car_makers JOIN countries ON car_makers.Country = countries.cntry_id GROUP BY car_makers.Country ORDER BY count(*) desc LIMIT 1	car_1_0
SELECT countries.cntry_name FROM car_makers JOIN countries ON car_makers.Country = countries.cntry_id GROUP BY car_makers.Country ORDER BY count(*) desc LIMIT 1	car_1_0
SELECT count(*) FROM car_makers JOIN countries ON car_makers.Country = countries.cntry_id WHERE countries.cntry_name = "france"	car_1_0
SELECT count(*) FROM car_makers JOIN countries ON car_makers.Country = countries.cntry_id WHERE countries.cntry_name = "france"	car_1_0
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.cntry_id WHERE countries.cntry_name = "usa"	car_1_0
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.cntry_id WHERE countries.cntry_name = "usa"	car_1_0
SELECT min(cars_data.wt) FROM cars_data WHERE cars_data.Cylinders = 8 and cars_data.Year = 1974	car_1_0
SELECT min(cars_data.wt) FROM cars_data WHERE cars_data.Cylinders = 8 and cars_data.Year = 1974	car_1_0
SELECT countries.cntry_name , countries.cntry_id FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country GROUP BY countries.cntry_id HAVING count(*) >= 1	car_1_0
SELECT countries.cntry_name , countries.cntry_id FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country GROUP BY countries.cntry_id HAVING count(*) >= 1	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.hp > 150	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.hp > 150	car_1_0
SELECT avg(cars_data.wt) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_0
SELECT avg(cars_data.wt) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_0
SELECT countries.cntry_name FROM countries JOIN continents ON countries.Continent = continents.ContId JOIN car_makers ON countries.cntry_id = car_makers.Country WHERE continents.Continent = "europe" GROUP BY countries.cntry_name HAVING count(*) >= 3	car_1_0
SELECT countries.cntry_name FROM countries JOIN continents ON countries.Continent = continents.ContId JOIN car_makers ON countries.cntry_id = car_makers.Country WHERE continents.Continent = "europe" GROUP BY countries.cntry_name HAVING count(*) >= 3	car_1_0
SELECT cars_data.hp , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 3 ORDER BY cars_data.hp desc LIMIT 1	car_1_0
SELECT cars_data.hp , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 3 ORDER BY cars_data.hp desc LIMIT 1	car_1_0
SELECT avg(cars_data.hp) FROM cars_data WHERE cars_data.Year < 1980	car_1_0
SELECT avg(cars_data.hp) FROM cars_data WHERE cars_data.Year < 1980	car_1_0
SELECT DISTINCT model_list.Model FROM car_names JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.wt > 3500	car_1_0
SELECT DISTINCT model_list.Model FROM car_names JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.wt > 3500	car_1_0
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.wt BETWEEN 3000 AND 4000	car_1_0
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.wt BETWEEN 3000 AND 4000	car_1_0
SELECT cars_data.hp FROM cars_data ORDER BY cars_data.Accelerate desc LIMIT 1	car_1_0
SELECT cars_data.hp FROM cars_data ORDER BY cars_data.Accelerate desc LIMIT 1	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.Accelerate > (SELECT cars_data.Accelerate FROM cars_data ORDER BY cars_data.hp desc LIMIT 1)	car_1_0
SELECT count(*) FROM cars_data WHERE cars_data.Accelerate > (SELECT cars_data.Accelerate FROM cars_data ORDER BY cars_data.hp desc LIMIT 1)	car_1_0
SELECT count(*) FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country GROUP BY countries.cntry_id HAVING count(*) > 2	car_1_0
SELECT count(*) FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country GROUP BY countries.cntry_id HAVING count(*) > 2	car_1_0
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 4 ORDER BY cars_data.hp desc LIMIT 1	car_1_0
SELECT car_names.Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 4 ORDER BY cars_data.hp desc LIMIT 1	car_1_0
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.hp > (SELECT min(cars_data.hp) FROM cars_data) and cars_data.Cylinders <= 3	car_1_0
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.hp > (SELECT min(cars_data.hp) FROM cars_data) and cars_data.Cylinders < 4	car_1_0
SELECT DISTINCT model_list.Model FROM model_list JOIN car_names ON model_list.Model = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.wt < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_0
SELECT DISTINCT model_list.Model FROM model_list JOIN car_names ON model_list.Model = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.wt < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_0
SELECT countries.cntry_name FROM countries EXCEPT SELECT countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country	car_1_0
SELECT countries.cntry_name FROM countries EXCEPT SELECT countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country	car_1_0
SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country GROUP BY countries.cntry_id HAVING count(*) > 3 UNION SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.Model = "fiat"	car_1_0
SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country GROUP BY countries.cntry_id HAVING count(*) > 3 UNION SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.Model = "fiat"	car_1_0
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_1
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_1
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_1
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_1
SELECT model_list.Maker , model_list.mdl FROM model_list	car_1_1
SELECT model_list.Maker , model_list.mdl FROM model_list	car_1_1
SELECT DISTINCT model_list.mdl FROM car_names JOIN model_list ON car_names.Model = model_list.mdl JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.Weight > 3500	car_1_1
SELECT DISTINCT model_list.mdl FROM car_names JOIN model_list ON car_names.Model = model_list.mdl JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.Weight > 3500	car_1_1
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.Weight < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_1
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.Weight < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_1
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.Model GROUP BY car_makers.Id HAVING count(*) > 3	car_1_1
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.Model GROUP BY car_makers.Id HAVING count(*) > 3	car_1_1
SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.mdl = "fiat"	car_1_1
SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.mdl = "fiat"	car_1_1
SELECT continents.ContId , continents.cont , count(*) FROM continents JOIN countries ON continents.ContId = countries.cont GROUP BY continents.ContId	car_1_2
SELECT continents.ContId , continents.cont , count(*) FROM continents JOIN countries ON continents.ContId = countries.cont GROUP BY continents.ContId	car_1_2
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.hp asc LIMIT 1	car_1_2
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.hp asc LIMIT 1	car_1_2
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.wt < (SELECT avg(cars_data.wt) FROM cars_data)	car_1_2
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.wt < (SELECT avg(cars_data.wt) FROM cars_data)	car_1_2
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_2
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_2
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_2
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_2
SELECT continents.cont , count(*) FROM continents JOIN countries ON continents.ContId = countries.cont JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY continents.cont	car_1_2
SELECT continents.cont , count(*) FROM continents JOIN countries ON continents.ContId = countries.cont JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY continents.cont	car_1_2
SELECT countries.cntry_name FROM car_makers JOIN countries ON car_makers.cntry = countries.cntry_id GROUP BY car_makers.cntry ORDER BY count(*) desc LIMIT 1	car_1_2
SELECT countries.cntry_name FROM car_makers JOIN countries ON car_makers.cntry = countries.cntry_id GROUP BY car_makers.cntry ORDER BY count(*) desc LIMIT 1	car_1_2
SELECT cars_data.aclt FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Make = "amc hornet sportabout (sw)"	car_1_2
SELECT cars_data.aclt FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Make = "amc hornet sportabout (sw)"	car_1_2
SELECT count(*) FROM car_makers JOIN countries ON car_makers.cntry = countries.cntry_id WHERE countries.cntry_name = "france"	car_1_2
SELECT count(*) FROM car_makers JOIN countries ON car_makers.cntry = countries.cntry_id WHERE countries.cntry_name = "france"	car_1_2
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.cntry = countries.cntry_id WHERE countries.cntry_name = "usa"	car_1_2
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.cntry = countries.cntry_id WHERE countries.cntry_name = "usa"	car_1_2
SELECT min(cars_data.wt) FROM cars_data WHERE cars_data.Cylinders = 8 and cars_data.Year = 1974	car_1_2
SELECT min(cars_data.wt) FROM cars_data WHERE cars_data.Cylinders = 8 and cars_data.Year = 1974	car_1_2
SELECT model_list.Maker , model_list.mdl FROM model_list	car_1_2
SELECT model_list.Maker , model_list.mdl FROM model_list	car_1_2
SELECT countries.cntry_name , countries.cntry_id FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) >= 1	car_1_2
SELECT countries.cntry_name , countries.cntry_id FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) >= 1	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.hp > 150	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.hp > 150	car_1_2
SELECT avg(cars_data.wt) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_2
SELECT avg(cars_data.wt) , cars_data.Year FROM cars_data GROUP BY cars_data.Year	car_1_2
SELECT countries.cntry_name FROM countries JOIN continents ON countries.cont = continents.ContId JOIN car_makers ON countries.cntry_id = car_makers.cntry WHERE continents.cont = "europe" GROUP BY countries.cntry_name HAVING count(*) >= 3	car_1_2
SELECT countries.cntry_name FROM countries JOIN continents ON countries.cont = continents.ContId JOIN car_makers ON countries.cntry_id = car_makers.cntry WHERE continents.cont = "europe" GROUP BY countries.cntry_name HAVING count(*) >= 3	car_1_2
SELECT cars_data.hp , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 3 ORDER BY cars_data.hp desc LIMIT 1	car_1_2
SELECT cars_data.hp , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 3 ORDER BY cars_data.hp desc LIMIT 1	car_1_2
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.MPG desc LIMIT 1	car_1_2
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.MPG desc LIMIT 1	car_1_2
SELECT avg(cars_data.hp) FROM cars_data WHERE cars_data.Year < 1980	car_1_2
SELECT avg(cars_data.hp) FROM cars_data WHERE cars_data.Year < 1980	car_1_2
SELECT avg(cars_data.Edispl) FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_names.mdl = "volvo"	car_1_2
SELECT avg(cars_data.Edispl) FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_names.mdl = "volvo"	car_1_2
SELECT max(cars_data.aclt) , cars_data.Cylinders FROM cars_data GROUP BY cars_data.Cylinders	car_1_2
SELECT max(cars_data.aclt) , cars_data.Cylinders FROM cars_data GROUP BY cars_data.Cylinders	car_1_2
SELECT car_names.mdl FROM car_names GROUP BY car_names.mdl ORDER BY count(*) desc LIMIT 1	car_1_2
SELECT car_names.mdl FROM car_names GROUP BY car_names.mdl ORDER BY count(*) desc LIMIT 1	car_1_2
SELECT DISTINCT model_list.mdl FROM car_names JOIN model_list ON car_names.mdl = model_list.mdl JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.wt > 3500	car_1_2
SELECT DISTINCT model_list.mdl FROM car_names JOIN model_list ON car_names.mdl = model_list.mdl JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.wt > 3500	car_1_2
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.wt BETWEEN 3000 AND 4000	car_1_2
SELECT DISTINCT cars_data.Year FROM cars_data WHERE cars_data.wt BETWEEN 3000 AND 4000	car_1_2
SELECT cars_data.hp FROM cars_data ORDER BY cars_data.aclt desc LIMIT 1	car_1_2
SELECT cars_data.hp FROM cars_data ORDER BY cars_data.aclt desc LIMIT 1	car_1_2
SELECT cars_data.Cylinders FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.mdl = "volvo" ORDER BY cars_data.aclt asc LIMIT 1	car_1_2
SELECT cars_data.Cylinders FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.mdl = "volvo" ORDER BY cars_data.aclt asc LIMIT 1	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.aclt > (SELECT cars_data.aclt FROM cars_data ORDER BY cars_data.hp desc LIMIT 1)	car_1_2
SELECT count(*) FROM cars_data WHERE cars_data.aclt > (SELECT cars_data.aclt FROM cars_data ORDER BY cars_data.hp desc LIMIT 1)	car_1_2
SELECT count(*) FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) > 2	car_1_2
SELECT count(*) FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) > 2	car_1_2
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 4 ORDER BY cars_data.hp desc LIMIT 1	car_1_2
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 4 ORDER BY cars_data.hp desc LIMIT 1	car_1_2
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.hp > (SELECT min(cars_data.hp) FROM cars_data) and cars_data.Cylinders <= 3	car_1_2
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.hp > (SELECT min(cars_data.hp) FROM cars_data) and cars_data.Cylinders < 4	car_1_2
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.wt < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_2
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.wt < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_2
SELECT countries.cntry_name FROM countries EXCEPT SELECT countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry	car_1_2
SELECT countries.cntry_name FROM countries EXCEPT SELECT countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry	car_1_2
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.mdl GROUP BY car_makers.Id HAVING count(*) > 3	car_1_2
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.mdl GROUP BY car_makers.Id HAVING count(*) > 3	car_1_2
SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) > 3 UNION SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.mdl = "fiat"	car_1_2
SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) > 3 UNION SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.mdl = "fiat"	car_1_2
SELECT continents.ContId , continents.cont , count(*) FROM continents JOIN countries ON continents.ContId = countries.Continent GROUP BY continents.ContId	car_1_3
SELECT continents.ContId , continents.cont , count(*) FROM continents JOIN countries ON continents.ContId = countries.Continent GROUP BY continents.ContId	car_1_3
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.hp asc LIMIT 1	car_1_3
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.hp asc LIMIT 1	car_1_3
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Weight < (SELECT avg(cars_data.Weight) FROM cars_data)	car_1_3
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Weight < (SELECT avg(cars_data.Weight) FROM cars_data)	car_1_3
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_3
SELECT DISTINCT car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year = "1970"	car_1_3
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_3
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980	car_1_3
SELECT continents.cont , count(*) FROM continents JOIN countries ON continents.ContId = countries.Continent JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY continents.cont	car_1_3
SELECT continents.cont , count(*) FROM continents JOIN countries ON continents.ContId = countries.Continent JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY continents.cont	car_1_3
SELECT countries.cntry_name FROM car_makers JOIN countries ON car_makers.cntry = countries.cntry_id GROUP BY car_makers.cntry ORDER BY count(*) desc LIMIT 1	car_1_3
SELECT countries.cntry_name FROM car_makers JOIN countries ON car_makers.cntry = countries.cntry_id GROUP BY car_makers.cntry ORDER BY count(*) desc LIMIT 1	car_1_3
SELECT cars_data.aclt FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Make = "amc hornet sportabout (sw)"	car_1_3
SELECT cars_data.aclt FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.Make = "amc hornet sportabout (sw)"	car_1_3
SELECT count(*) FROM car_makers JOIN countries ON car_makers.cntry = countries.cntry_id WHERE countries.cntry_name = "france"	car_1_3
SELECT count(*) FROM car_makers JOIN countries ON car_makers.cntry = countries.cntry_id WHERE countries.cntry_name = "france"	car_1_3
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.cntry = countries.cntry_id WHERE countries.cntry_name = "usa"	car_1_3
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.cntry = countries.cntry_id WHERE countries.cntry_name = "usa"	car_1_3
SELECT model_list.Maker , model_list.mdl FROM model_list	car_1_3
SELECT model_list.Maker , model_list.mdl FROM model_list	car_1_3
SELECT countries.cntry_name , countries.cntry_id FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) >= 1	car_1_3
SELECT countries.cntry_name , countries.cntry_id FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) >= 1	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.hp > 150	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.hp > 150	car_1_3
SELECT countries.cntry_name FROM countries JOIN continents ON countries.Continent = continents.ContId JOIN car_makers ON countries.cntry_id = car_makers.cntry WHERE continents.cont = "europe" GROUP BY countries.cntry_name HAVING count(*) >= 3	car_1_3
SELECT countries.cntry_name FROM countries JOIN continents ON countries.Continent = continents.ContId JOIN car_makers ON countries.cntry_id = car_makers.cntry WHERE continents.cont = "europe" GROUP BY countries.cntry_name HAVING count(*) >= 3	car_1_3
SELECT cars_data.hp , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 3 ORDER BY cars_data.hp desc LIMIT 1	car_1_3
SELECT cars_data.hp , car_names.Make FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 3 ORDER BY cars_data.hp desc LIMIT 1	car_1_3
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.MPG desc LIMIT 1	car_1_3
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id ORDER BY cars_data.MPG desc LIMIT 1	car_1_3
SELECT avg(cars_data.hp) FROM cars_data WHERE cars_data.Year < 1980	car_1_3
SELECT avg(cars_data.hp) FROM cars_data WHERE cars_data.Year < 1980	car_1_3
SELECT avg(cars_data.Edispl) FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_names.mdl = "volvo"	car_1_3
SELECT avg(cars_data.Edispl) FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_names.mdl = "volvo"	car_1_3
SELECT max(cars_data.aclt) , cars_data.Cylinders FROM cars_data GROUP BY cars_data.Cylinders	car_1_3
SELECT max(cars_data.aclt) , cars_data.Cylinders FROM cars_data GROUP BY cars_data.Cylinders	car_1_3
SELECT car_names.mdl FROM car_names GROUP BY car_names.mdl ORDER BY count(*) desc LIMIT 1	car_1_3
SELECT car_names.mdl FROM car_names GROUP BY car_names.mdl ORDER BY count(*) desc LIMIT 1	car_1_3
SELECT DISTINCT model_list.mdl FROM car_names JOIN model_list ON car_names.mdl = model_list.mdl JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.Weight > 3500	car_1_3
SELECT DISTINCT model_list.mdl FROM car_names JOIN model_list ON car_names.mdl = model_list.mdl JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.FullName = "General Motors" or cars_data.Weight > 3500	car_1_3
SELECT cars_data.hp FROM cars_data ORDER BY cars_data.aclt desc LIMIT 1	car_1_3
SELECT cars_data.hp FROM cars_data ORDER BY cars_data.aclt desc LIMIT 1	car_1_3
SELECT cars_data.Cylinders FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.mdl = "volvo" ORDER BY cars_data.aclt asc LIMIT 1	car_1_3
SELECT cars_data.Cylinders FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE car_names.mdl = "volvo" ORDER BY cars_data.aclt asc LIMIT 1	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.aclt > (SELECT cars_data.aclt FROM cars_data ORDER BY cars_data.hp desc LIMIT 1)	car_1_3
SELECT count(*) FROM cars_data WHERE cars_data.aclt > (SELECT cars_data.aclt FROM cars_data ORDER BY cars_data.hp desc LIMIT 1)	car_1_3
SELECT count(*) FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) > 2	car_1_3
SELECT count(*) FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) > 2	car_1_3
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 4 ORDER BY cars_data.hp desc LIMIT 1	car_1_3
SELECT car_names.mdl FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Cylinders = 4 ORDER BY cars_data.hp desc LIMIT 1	car_1_3
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.hp > (SELECT min(cars_data.hp) FROM cars_data) and cars_data.Cylinders <= 3	car_1_3
SELECT car_names.MakeId , car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.hp > (SELECT min(cars_data.hp) FROM cars_data) and cars_data.Cylinders < 4	car_1_3
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.Weight < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_3
SELECT DISTINCT model_list.mdl FROM model_list JOIN car_names ON model_list.mdl = car_names.mdl JOIN cars_data ON car_names.MakeId = cars_data.Id JOIN car_makers ON model_list.Maker = car_makers.Id WHERE cars_data.Weight < 3500 and car_makers.FullName != "Ford Motor Company"	car_1_3
SELECT countries.cntry_name FROM countries EXCEPT SELECT countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry	car_1_3
SELECT countries.cntry_name FROM countries EXCEPT SELECT countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry	car_1_3
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.mdl GROUP BY car_makers.Id HAVING count(*) > 3	car_1_3
SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id HAVING count(*) >= 2 INTERSECT SELECT car_makers.Id , car_makers.Maker FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.mdl = car_names.mdl GROUP BY car_makers.Id HAVING count(*) > 3	car_1_3
SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) > 3 UNION SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.mdl = "fiat"	car_1_3
SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry GROUP BY countries.cntry_id HAVING count(*) > 3 UNION SELECT countries.cntry_id , countries.cntry_name FROM countries JOIN car_makers ON countries.cntry_id = car_makers.cntry JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.mdl = "fiat"	car_1_3
SELECT countries.cntry_name FROM car_makers JOIN countries ON car_makers.Country = countries.CountryId GROUP BY car_makers.Country ORDER BY count(*) desc LIMIT 1	car_1_4
SELECT countries.cntry_name FROM car_makers JOIN countries ON car_makers.Country = countries.CountryId GROUP BY car_makers.Country ORDER BY count(*) desc LIMIT 1	car_1_4
SELECT count(*) FROM car_makers JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.cntry_name = "france"	car_1_4
SELECT count(*) FROM car_makers JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.cntry_name = "france"	car_1_4
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.cntry_name = "usa"	car_1_4
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.cntry_name = "usa"	car_1_4
SELECT countries.cntry_name , countries.CountryId FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) >= 1	car_1_4
SELECT countries.cntry_name , countries.CountryId FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) >= 1	car_1_4
SELECT countries.cntry_name FROM countries JOIN continents ON countries.Continent = continents.ContId JOIN car_makers ON countries.CountryId = car_makers.Country WHERE continents.Continent = "europe" GROUP BY countries.cntry_name HAVING count(*) >= 3	car_1_4
SELECT countries.cntry_name FROM countries JOIN continents ON countries.Continent = continents.ContId JOIN car_makers ON countries.CountryId = car_makers.Country WHERE continents.Continent = "europe" GROUP BY countries.cntry_name HAVING count(*) >= 3	car_1_4
SELECT countries.cntry_name FROM countries EXCEPT SELECT countries.cntry_name FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country	car_1_4
SELECT countries.cntry_name FROM countries EXCEPT SELECT countries.cntry_name FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country	car_1_4
SELECT countries.CountryId , countries.cntry_name FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.cntry_name FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.Model = "fiat"	car_1_4
SELECT countries.CountryId , countries.cntry_name FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING count(*) > 3 UNION SELECT countries.CountryId , countries.cntry_name FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country JOIN model_list ON car_makers.Id = model_list.Maker WHERE model_list.Model = "fiat"	car_1_4
SELECT airlines.cntry FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_0
SELECT airlines.cntry FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_0
SELECT airlines.abbr FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_0
SELECT airlines.abbr FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_0
SELECT airlines.air , airlines.abbr FROM airlines WHERE airlines.cntry = "USA"	flight_2_0
SELECT airlines.air , airlines.abbr FROM airlines WHERE airlines.cntry = "USA"	flight_2_0
SELECT airports.apt_code , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_0
SELECT airports.apt_code , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_0
SELECT airlines.air FROM airlines WHERE airlines.abbr = "UAL"	flight_2_0
SELECT airlines.air FROM airlines WHERE airlines.abbr = "UAL"	flight_2_0
SELECT count(*) FROM airlines WHERE airlines.cntry = "USA"	flight_2_0
SELECT count(*) FROM airlines WHERE airlines.cntry = "USA"	flight_2_0
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_0
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_0
SELECT airports.apt_name FROM airports WHERE airports.apt_code = "AKO"	flight_2_0
SELECT airports.apt_name FROM airports WHERE airports.apt_code = "AKO"	flight_2_0
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_0
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights WHERE flights.srcapt = "APG"	flight_2_0
SELECT count(*) FROM flights WHERE flights.srcapt = "APG"	flight_2_0
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_0
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.srcapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.srcapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.apt_code JOIN airports AS T3 ON T1.srcapt = T3.apt_code WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.apt_code JOIN airports AS T3 ON T1.srcapt = T3.apt_code WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.air = "JetBlue Airways"	flight_2_0
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.air = "JetBlue Airways"	flight_2_0
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.destapt = "ASY"	flight_2_0
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.destapt = "ASY"	flight_2_0
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.srcapt = "AHD"	flight_2_0
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.srcapt = "AHD"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.air = "United Airlines"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.air = "United Airlines"	flight_2_0
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.srcapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.srcapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) asc LIMIT 1	flight_2_0
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) asc LIMIT 1	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) desc LIMIT 1	flight_2_0
SELECT airlines.abbr , airlines.cntry FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) asc LIMIT 1	flight_2_0
SELECT airlines.abbr , airlines.cntry FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) asc LIMIT 1	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "AHD"	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "AHD"	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG" INTERSECT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO"	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG" INTERSECT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO"	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO" EXCEPT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG"	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO" EXCEPT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG"	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) > 10	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) > 10	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) < 200	flight_2_0
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) < 200	flight_2_0
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.air = "United Airlines"	flight_2_0
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.air = "United Airlines"	flight_2_0
SELECT flights.FlightNo FROM flights WHERE flights.srcapt = "APG"	flight_2_0
SELECT flights.FlightNo FROM flights WHERE flights.srcapt = "APG"	flight_2_0
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_0
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_0
SELECT flights.FlightNo FROM flights JOIN airports ON flights.srcapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_0
SELECT flights.FlightNo FROM flights JOIN airports ON flights.srcapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_0
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_0
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_0
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_0
SELECT airports.apt_name FROM airports WHERE airports.apt_code NOT in (SELECT flights.srcapt FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_0
SELECT airports.apt_name FROM airports WHERE airports.apt_code NOT in (SELECT flights.srcapt FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_0
SELECT airlines.Country FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_1
SELECT airlines.Country FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_1
SELECT airlines.Abbreviation FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_1
SELECT airlines.Abbreviation FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_1
SELECT airlines.air , airlines.Abbreviation FROM airlines WHERE airlines.Country = "USA"	flight_2_1
SELECT airlines.air , airlines.Abbreviation FROM airlines WHERE airlines.Country = "USA"	flight_2_1
SELECT airports.apt_code , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_1
SELECT airports.apt_code , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_1
SELECT airlines.air FROM airlines WHERE airlines.Abbreviation = "UAL"	flight_2_1
SELECT airlines.air FROM airlines WHERE airlines.Abbreviation = "UAL"	flight_2_1
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_1
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_1
SELECT airports.apt_name FROM airports WHERE airports.apt_code = "AKO"	flight_2_1
SELECT airports.apt_name FROM airports WHERE airports.apt_code = "AKO"	flight_2_1
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_1
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights WHERE flights.srcapt = "APG"	flight_2_1
SELECT count(*) FROM flights WHERE flights.srcapt = "APG"	flight_2_1
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_1
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.srcapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.srcapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.apt_code JOIN airports AS T3 ON T1.srcapt = T3.apt_code WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.apt_code JOIN airports AS T3 ON T1.srcapt = T3.apt_code WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.air = "JetBlue Airways"	flight_2_1
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.air = "JetBlue Airways"	flight_2_1
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.destapt = "ASY"	flight_2_1
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.destapt = "ASY"	flight_2_1
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.srcapt = "AHD"	flight_2_1
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.srcapt = "AHD"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.air = "United Airlines"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.air = "United Airlines"	flight_2_1
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.srcapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.srcapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) asc LIMIT 1	flight_2_1
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) asc LIMIT 1	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) desc LIMIT 1	flight_2_1
SELECT airlines.Abbreviation , airlines.Country FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) asc LIMIT 1	flight_2_1
SELECT airlines.Abbreviation , airlines.Country FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) asc LIMIT 1	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "AHD"	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "AHD"	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG" INTERSECT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO"	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG" INTERSECT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO"	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO" EXCEPT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG"	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO" EXCEPT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG"	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) > 10	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) > 10	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) < 200	flight_2_1
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) < 200	flight_2_1
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.air = "United Airlines"	flight_2_1
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.air = "United Airlines"	flight_2_1
SELECT flights.FlightNo FROM flights WHERE flights.srcapt = "APG"	flight_2_1
SELECT flights.FlightNo FROM flights WHERE flights.srcapt = "APG"	flight_2_1
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_1
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_1
SELECT flights.FlightNo FROM flights JOIN airports ON flights.srcapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_1
SELECT flights.FlightNo FROM flights JOIN airports ON flights.srcapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_1
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_1
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_1
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_1
SELECT airports.apt_name FROM airports WHERE airports.apt_code NOT in (SELECT flights.srcapt FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_1
SELECT airports.apt_name FROM airports WHERE airports.apt_code NOT in (SELECT flights.srcapt FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_1
SELECT airlines.cntry FROM airlines WHERE airlines.Airline = "JetBlue Airways"	flight_2_2
SELECT airlines.cntry FROM airlines WHERE airlines.Airline = "JetBlue Airways"	flight_2_2
SELECT airlines.Airline , airlines.Abbreviation FROM airlines WHERE airlines.cntry = "USA"	flight_2_2
SELECT airlines.Airline , airlines.Abbreviation FROM airlines WHERE airlines.cntry = "USA"	flight_2_2
SELECT airports.apt_code , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_2
SELECT airports.apt_code , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_2
SELECT count(*) FROM airlines WHERE airlines.cntry = "USA"	flight_2_2
SELECT count(*) FROM airlines WHERE airlines.cntry = "USA"	flight_2_2
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_2
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_2
SELECT airports.apt_name FROM airports WHERE airports.apt_code = "AKO"	flight_2_2
SELECT airports.apt_name FROM airports WHERE airports.apt_code = "AKO"	flight_2_2
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_2
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_2
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_2
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.SourceAirport = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.SourceAirport = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_2
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.apt_code JOIN airports AS T3 ON T1.SourceAirport = T3.apt_code WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_2
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.apt_code JOIN airports AS T3 ON T1.SourceAirport = T3.apt_code WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_2
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.Airline = "JetBlue Airways"	flight_2_2
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.Airline = "JetBlue Airways"	flight_2_2
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.destapt = "ASY"	flight_2_2
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.destapt = "ASY"	flight_2_2
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.SourceAirport = "AHD"	flight_2_2
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.Airline = "United Airlines" and flights.SourceAirport = "AHD"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.Airline = "United Airlines"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.Airline = "United Airlines"	flight_2_2
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.SourceAirport GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airports.City FROM airports JOIN flights ON airports.apt_code = flights.SourceAirport GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) asc LIMIT 1	flight_2_2
SELECT airports.apt_code FROM airports JOIN flights ON airports.apt_code = flights.destapt GROUP BY airports.apt_code ORDER BY count(*) asc LIMIT 1	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.Airline ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.Airline ORDER BY count(*) desc LIMIT 1	flight_2_2
SELECT airlines.Abbreviation , airlines.cntry FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.Airline ORDER BY count(*) asc LIMIT 1	flight_2_2
SELECT airlines.Abbreviation , airlines.cntry FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.Airline ORDER BY count(*) asc LIMIT 1	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "AHD"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "AHD"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "APG" INTERSECT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "CVO"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "APG" INTERSECT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "CVO"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "CVO" EXCEPT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "APG"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "CVO" EXCEPT SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "APG"	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.Airline HAVING count(*) > 10	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.Airline HAVING count(*) > 10	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.Airline HAVING count(*) < 200	flight_2_2
SELECT airlines.Airline FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.Airline HAVING count(*) < 200	flight_2_2
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.Airline = "United Airlines"	flight_2_2
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.Airline = "United Airlines"	flight_2_2
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_2
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_2
SELECT flights.FlightNo FROM flights JOIN airports ON flights.SourceAirport = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_2
SELECT flights.FlightNo FROM flights JOIN airports ON flights.SourceAirport = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_2
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_2
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_2
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.apt_code WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_2
SELECT airports.apt_name FROM airports WHERE airports.apt_code NOT in (SELECT flights.SourceAirport FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_2
SELECT airports.apt_name FROM airports WHERE airports.apt_code NOT in (SELECT flights.SourceAirport FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_2
SELECT airlines.cntry FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_3
SELECT airlines.cntry FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_3
SELECT airlines.abbr FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_3
SELECT airlines.abbr FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_3
SELECT airlines.air , airlines.abbr FROM airlines WHERE airlines.cntry = "USA"	flight_2_3
SELECT airlines.air , airlines.abbr FROM airlines WHERE airlines.cntry = "USA"	flight_2_3
SELECT airports.AirportCode , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_3
SELECT airports.AirportCode , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_3
SELECT airlines.air FROM airlines WHERE airlines.abbr = "UAL"	flight_2_3
SELECT airlines.air FROM airlines WHERE airlines.abbr = "UAL"	flight_2_3
SELECT count(*) FROM airlines WHERE airlines.cntry = "USA"	flight_2_3
SELECT count(*) FROM airlines WHERE airlines.cntry = "USA"	flight_2_3
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_3
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_3
SELECT airports.apt_name FROM airports WHERE airports.AirportCode = "AKO"	flight_2_3
SELECT airports.apt_name FROM airports WHERE airports.AirportCode = "AKO"	flight_2_3
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_3
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_3
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_3
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_3
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_3
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_3
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.AirportCode JOIN airports AS T3 ON T1.SourceAirport = T3.AirportCode WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_3
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.AirportCode JOIN airports AS T3 ON T1.SourceAirport = T3.AirportCode WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_3
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.air = "JetBlue Airways"	flight_2_3
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.air = "JetBlue Airways"	flight_2_3
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.destapt = "ASY"	flight_2_3
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.destapt = "ASY"	flight_2_3
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.SourceAirport = "AHD"	flight_2_3
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.SourceAirport = "AHD"	flight_2_3
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.air = "United Airlines"	flight_2_3
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.air = "United Airlines"	flight_2_3
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_3
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_3
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.AirportCode ORDER BY count(*) desc LIMIT 1	flight_2_3
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.AirportCode ORDER BY count(*) desc LIMIT 1	flight_2_3
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.AirportCode ORDER BY count(*) asc LIMIT 1	flight_2_3
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.AirportCode ORDER BY count(*) asc LIMIT 1	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) desc LIMIT 1	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) desc LIMIT 1	flight_2_3
SELECT airlines.abbr , airlines.cntry FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) asc LIMIT 1	flight_2_3
SELECT airlines.abbr , airlines.cntry FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) asc LIMIT 1	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "AHD"	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "AHD"	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "APG" INTERSECT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "CVO"	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "APG" INTERSECT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "CVO"	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "CVO" EXCEPT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "APG"	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "CVO" EXCEPT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.SourceAirport = "APG"	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) > 10	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) > 10	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) < 200	flight_2_3
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) < 200	flight_2_3
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.air = "United Airlines"	flight_2_3
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.air = "United Airlines"	flight_2_3
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_3
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_3
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_3
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_3
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_3
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_3
SELECT airports.apt_name FROM airports WHERE airports.AirportCode NOT in (SELECT flights.SourceAirport FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_3
SELECT airports.apt_name FROM airports WHERE airports.AirportCode NOT in (SELECT flights.SourceAirport FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_3
SELECT airlines.cntry FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_4
SELECT airlines.cntry FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_4
SELECT airlines.abbr FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_4
SELECT airlines.abbr FROM airlines WHERE airlines.air = "JetBlue Airways"	flight_2_4
SELECT airlines.air , airlines.abbr FROM airlines WHERE airlines.cntry = "USA"	flight_2_4
SELECT airlines.air , airlines.abbr FROM airlines WHERE airlines.cntry = "USA"	flight_2_4
SELECT airports.AirportCode , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_4
SELECT airports.AirportCode , airports.apt_name FROM airports WHERE airports.City = "Anthony"	flight_2_4
SELECT airlines.air FROM airlines WHERE airlines.abbr = "UAL"	flight_2_4
SELECT airlines.air FROM airlines WHERE airlines.abbr = "UAL"	flight_2_4
SELECT count(*) FROM airlines WHERE airlines.cntry = "USA"	flight_2_4
SELECT count(*) FROM airlines WHERE airlines.cntry = "USA"	flight_2_4
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_4
SELECT airports.City , airports.cntry FROM airports WHERE airports.apt_name = "Alton"	flight_2_4
SELECT airports.apt_name FROM airports WHERE airports.AirportCode = "AKO"	flight_2_4
SELECT airports.apt_name FROM airports WHERE airports.AirportCode = "AKO"	flight_2_4
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_4
SELECT airports.apt_name FROM airports WHERE airports.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights WHERE flights.srcapt = "APG"	flight_2_4
SELECT count(*) FROM flights WHERE flights.srcapt = "APG"	flight_2_4
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_4
SELECT count(*) FROM flights WHERE flights.destapt = "ATO"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.srcapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.srcapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.AirportCode JOIN airports AS T3 ON T1.srcapt = T3.AirportCode WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.destapt = T2.AirportCode JOIN airports AS T3 ON T1.srcapt = T3.AirportCode WHERE T2.City = "Ashley" and T3.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.air = "JetBlue Airways"	flight_2_4
SELECT count(*) FROM flights JOIN airlines ON flights.air = airlines.uid WHERE airlines.air = "JetBlue Airways"	flight_2_4
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.destapt = "ASY"	flight_2_4
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.destapt = "ASY"	flight_2_4
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.srcapt = "AHD"	flight_2_4
SELECT count(*) FROM airlines JOIN flights ON flights.air = airlines.uid WHERE airlines.air = "United Airlines" and flights.srcapt = "AHD"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.air = "United Airlines"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode JOIN airlines ON airlines.uid = flights.air WHERE airports.City = "Aberdeen" and airlines.air = "United Airlines"	flight_2_4
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.srcapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airports.City FROM airports JOIN flights ON airports.AirportCode = flights.srcapt GROUP BY airports.City ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.AirportCode ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.AirportCode ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.AirportCode ORDER BY count(*) asc LIMIT 1	flight_2_4
SELECT airports.AirportCode FROM airports JOIN flights ON airports.AirportCode = flights.destapt GROUP BY airports.AirportCode ORDER BY count(*) asc LIMIT 1	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) desc LIMIT 1	flight_2_4
SELECT airlines.abbr , airlines.cntry FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) asc LIMIT 1	flight_2_4
SELECT airlines.abbr , airlines.cntry FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air ORDER BY count(*) asc LIMIT 1	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "AHD"	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "AHD"	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.destapt = "AHD"	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG" INTERSECT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO"	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG" INTERSECT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO"	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO" EXCEPT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG"	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "CVO" EXCEPT SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air WHERE flights.srcapt = "APG"	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) > 10	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) > 10	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) < 200	flight_2_4
SELECT airlines.air FROM airlines JOIN flights ON airlines.uid = flights.air GROUP BY airlines.air HAVING count(*) < 200	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.air = "United Airlines"	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airlines ON airlines.uid = flights.air WHERE airlines.air = "United Airlines"	flight_2_4
SELECT flights.FlightNo FROM flights WHERE flights.srcapt = "APG"	flight_2_4
SELECT flights.FlightNo FROM flights WHERE flights.srcapt = "APG"	flight_2_4
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_4
SELECT flights.FlightNo FROM flights WHERE flights.destapt = "APG"	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airports ON flights.srcapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airports ON flights.srcapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT flights.FlightNo FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_4
SELECT count(*) FROM flights JOIN airports ON flights.destapt = airports.AirportCode WHERE airports.City = "Aberdeen" or airports.City = "Abilene"	flight_2_4
SELECT airports.apt_name FROM airports WHERE airports.AirportCode NOT in (SELECT flights.srcapt FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_4
SELECT airports.apt_name FROM airports WHERE airports.AirportCode NOT in (SELECT flights.srcapt FROM flights UNION SELECT flights.destapt FROM flights)	flight_2_4
SELECT count(*) , shop.loc FROM shop GROUP BY shop.loc	employee_hire_evaluation_0
SELECT count(*) , shop.loc FROM shop GROUP BY shop.loc	employee_hire_evaluation_0
SELECT shop.mgr_name , shop.dist FROM shop ORDER BY shop.num_prod desc LIMIT 1	employee_hire_evaluation_0
SELECT shop.mgr_name , shop.dist FROM shop ORDER BY shop.num_prod desc LIMIT 1	employee_hire_evaluation_0
SELECT min(shop.num_prod) , max(shop.num_prod) FROM shop	employee_hire_evaluation_0
SELECT min(shop.num_prod) , max(shop.num_prod) FROM shop	employee_hire_evaluation_0
SELECT shop.Name , shop.loc , shop.dist FROM shop ORDER BY shop.num_prod desc	employee_hire_evaluation_0
SELECT shop.Name , shop.loc , shop.dist FROM shop ORDER BY shop.num_prod desc	employee_hire_evaluation_0
SELECT shop.Name FROM shop WHERE shop.num_prod > (SELECT avg(shop.num_prod) FROM shop)	employee_hire_evaluation_0
SELECT shop.Name FROM shop WHERE shop.num_prod > (SELECT avg(shop.num_prod) FROM shop)	employee_hire_evaluation_0
SELECT employee.Name FROM employee JOIN evaluation ON employee.ee_id = evaluation.Employee_ID GROUP BY evaluation.Employee_ID ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_0
SELECT employee.Name FROM employee JOIN evaluation ON employee.ee_id = evaluation.Employee_ID GROUP BY evaluation.Employee_ID ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_0
SELECT employee.Name FROM employee JOIN evaluation ON employee.ee_id = evaluation.Employee_ID ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_0
SELECT employee.Name FROM employee JOIN evaluation ON employee.ee_id = evaluation.Employee_ID ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_0
SELECT employee.Name FROM employee WHERE employee.ee_id NOT in (SELECT evaluation.Employee_ID FROM evaluation)	employee_hire_evaluation_0
SELECT employee.Name FROM employee WHERE employee.ee_id NOT in (SELECT evaluation.Employee_ID FROM evaluation)	employee_hire_evaluation_0
SELECT shop.dist FROM shop WHERE shop.num_prod < 3000 INTERSECT SELECT shop.dist FROM shop WHERE shop.num_prod > 10000	employee_hire_evaluation_0
SELECT shop.dist FROM shop WHERE shop.num_prod < 3000 INTERSECT SELECT shop.dist FROM shop WHERE shop.num_prod > 10000	employee_hire_evaluation_0
SELECT count(DISTINCT shop.loc) FROM shop	employee_hire_evaluation_0
SELECT count(DISTINCT shop.loc) FROM shop	employee_hire_evaluation_0
SELECT count(*) , shop.loc FROM shop GROUP BY shop.loc	employee_hire_evaluation_1
SELECT count(*) , shop.loc FROM shop GROUP BY shop.loc	employee_hire_evaluation_1
SELECT shop.Manager_name , shop.District FROM shop ORDER BY shop.num_prod desc LIMIT 1	employee_hire_evaluation_1
SELECT shop.Manager_name , shop.District FROM shop ORDER BY shop.num_prod desc LIMIT 1	employee_hire_evaluation_1
SELECT min(shop.num_prod) , max(shop.num_prod) FROM shop	employee_hire_evaluation_1
SELECT min(shop.num_prod) , max(shop.num_prod) FROM shop	employee_hire_evaluation_1
SELECT shop.Name , shop.loc , shop.District FROM shop ORDER BY shop.num_prod desc	employee_hire_evaluation_1
SELECT shop.Name , shop.loc , shop.District FROM shop ORDER BY shop.num_prod desc	employee_hire_evaluation_1
SELECT shop.Name FROM shop WHERE shop.num_prod > (SELECT avg(shop.num_prod) FROM shop)	employee_hire_evaluation_1
SELECT shop.Name FROM shop WHERE shop.num_prod > (SELECT avg(shop.num_prod) FROM shop)	employee_hire_evaluation_1
SELECT employee.Name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.ee_id GROUP BY evaluation.ee_id ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_1
SELECT employee.Name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.ee_id GROUP BY evaluation.ee_id ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_1
SELECT employee.Name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.ee_id ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_1
SELECT employee.Name FROM employee JOIN evaluation ON employee.Employee_ID = evaluation.ee_id ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_1
SELECT employee.Name FROM employee WHERE employee.Employee_ID NOT in (SELECT evaluation.ee_id FROM evaluation)	employee_hire_evaluation_1
SELECT employee.Name FROM employee WHERE employee.Employee_ID NOT in (SELECT evaluation.ee_id FROM evaluation)	employee_hire_evaluation_1
SELECT shop.District FROM shop WHERE shop.num_prod < 3000 INTERSECT SELECT shop.District FROM shop WHERE shop.num_prod > 10000	employee_hire_evaluation_1
SELECT shop.District FROM shop WHERE shop.num_prod < 3000 INTERSECT SELECT shop.District FROM shop WHERE shop.num_prod > 10000	employee_hire_evaluation_1
SELECT count(DISTINCT shop.loc) FROM shop	employee_hire_evaluation_1
SELECT count(DISTINCT shop.loc) FROM shop	employee_hire_evaluation_1
SELECT shop.Manager_name , shop.dist FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_3
SELECT shop.Manager_name , shop.dist FROM shop ORDER BY shop.Number_products desc LIMIT 1	employee_hire_evaluation_3
SELECT shop.Name , shop.Location , shop.dist FROM shop ORDER BY shop.Number_products desc	employee_hire_evaluation_3
SELECT shop.Name , shop.Location , shop.dist FROM shop ORDER BY shop.Number_products desc	employee_hire_evaluation_3
SELECT employee.Name FROM employee JOIN evaluation ON employee.ee_id = evaluation.Employee_ID GROUP BY evaluation.Employee_ID ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_3
SELECT employee.Name FROM employee JOIN evaluation ON employee.ee_id = evaluation.Employee_ID GROUP BY evaluation.Employee_ID ORDER BY count(*) desc LIMIT 1	employee_hire_evaluation_3
SELECT employee.Name FROM employee JOIN evaluation ON employee.ee_id = evaluation.Employee_ID ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_3
SELECT employee.Name FROM employee JOIN evaluation ON employee.ee_id = evaluation.Employee_ID ORDER BY evaluation.Bonus desc LIMIT 1	employee_hire_evaluation_3
SELECT employee.Name FROM employee WHERE employee.ee_id NOT in (SELECT evaluation.Employee_ID FROM evaluation)	employee_hire_evaluation_3
SELECT employee.Name FROM employee WHERE employee.ee_id NOT in (SELECT evaluation.Employee_ID FROM evaluation)	employee_hire_evaluation_3
SELECT shop.dist FROM shop WHERE shop.Number_products < 3000 INTERSECT SELECT shop.dist FROM shop WHERE shop.Number_products > 10000	employee_hire_evaluation_3
SELECT shop.dist FROM shop WHERE shop.Number_products < 3000 INTERSECT SELECT shop.dist FROM shop WHERE shop.Number_products > 10000	employee_hire_evaluation_3
SELECT count(*) , shop.loc FROM shop GROUP BY shop.loc	employee_hire_evaluation_4
SELECT count(*) , shop.loc FROM shop GROUP BY shop.loc	employee_hire_evaluation_4
SELECT shop.Name , shop.loc , shop.District FROM shop ORDER BY shop.Number_products desc	employee_hire_evaluation_4
SELECT shop.Name , shop.loc , shop.District FROM shop ORDER BY shop.Number_products desc	employee_hire_evaluation_4
SELECT count(DISTINCT shop.loc) FROM shop	employee_hire_evaluation_4
SELECT count(DISTINCT shop.loc) FROM shop	employee_hire_evaluation_4
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.tpl_id WHERE Templates.Template_Type_Code = "PPT"	cre_Doc_Template_Mgt_0
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.tpl_id WHERE Templates.Template_Type_Code = "PPT"	cre_Doc_Template_Mgt_0
SELECT Documents.Template_ID , Templates.Template_Type_Code FROM Documents JOIN Templates ON Documents.Template_ID = Templates.tpl_id GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Documents.Template_ID , Templates.Template_Type_Code FROM Documents JOIN Templates ON Documents.Template_ID = Templates.tpl_id GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Templates.tpl_id FROM Templates EXCEPT SELECT Documents.Template_ID FROM Documents	cre_Doc_Template_Mgt_0
SELECT Templates.tpl_id FROM Templates EXCEPT SELECT Documents.Template_ID FROM Documents	cre_Doc_Template_Mgt_0
SELECT Templates.tpl_id , Templates.ver_no , Templates.Template_Type_Code FROM Templates	cre_Doc_Template_Mgt_0
SELECT Templates.tpl_id , Templates.ver_no , Templates.Template_Type_Code FROM Templates	cre_Doc_Template_Mgt_0
SELECT Templates.tpl_id FROM Templates WHERE Templates.Template_Type_Code = "PP" or Templates.Template_Type_Code = "PPT"	cre_Doc_Template_Mgt_0
SELECT Templates.tpl_id FROM Templates WHERE Templates.Template_Type_Code = "PP" or Templates.Template_Type_Code = "PPT"	cre_Doc_Template_Mgt_0
SELECT Templates.ver_no , Templates.Template_Type_Code FROM Templates WHERE Templates.ver_no > 5	cre_Doc_Template_Mgt_0
SELECT Templates.ver_no , Templates.Template_Type_Code FROM Templates WHERE Templates.ver_no > 5	cre_Doc_Template_Mgt_0
SELECT min(Templates.ver_no) , Templates.Template_Type_Code FROM Templates	cre_Doc_Template_Mgt_0
SELECT min(Templates.ver_no) , Templates.Template_Type_Code FROM Templates	cre_Doc_Template_Mgt_0
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID WHERE Documents.Document_Name = "Data base"	cre_Doc_Template_Mgt_0
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID WHERE Documents.Document_Name = "Data base"	cre_Doc_Template_Mgt_0
SELECT Documents.Document_Name FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID WHERE Templates.Template_Type_Code = "BK"	cre_Doc_Template_Mgt_0
SELECT Documents.Document_Name FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID WHERE Templates.Template_Type_Code = "BK"	cre_Doc_Template_Mgt_0
SELECT Templates.Template_Type_Code , count(*) FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID GROUP BY Templates.Template_Type_Code	cre_Doc_Template_Mgt_0
SELECT Templates.Template_Type_Code , count(*) FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID GROUP BY Templates.Template_Type_Code	cre_Doc_Template_Mgt_0
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID GROUP BY Templates.Template_Type_Code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID GROUP BY Templates.Template_Type_Code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Templates.Template_Type_Code FROM Templates EXCEPT SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID	cre_Doc_Template_Mgt_0
SELECT Templates.Template_Type_Code FROM Templates EXCEPT SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.tpl_id = Documents.Template_ID	cre_Doc_Template_Mgt_0
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.Template_Type_Code = Templates.Template_Type_Code JOIN Documents ON Templates.tpl_id = Documents.Template_ID	cre_Doc_Template_Mgt_0
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.Template_Type_Code = Templates.Template_Type_Code JOIN Documents ON Templates.tpl_id = Documents.Template_ID	cre_Doc_Template_Mgt_0
SELECT Templates.tpl_id FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.Template_Type_Code = Templates.Template_Type_Code WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_0
SELECT Templates.tpl_id FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.Template_Type_Code = Templates.Template_Type_Code WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_0
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID WHERE Documents.Document_Name = "Summer Show"	cre_Doc_Template_Mgt_0
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID WHERE Documents.Document_Name = "Summer Show"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.oth_dtl FROM Paragraphs WHERE Paragraphs.Paragraph_Text like "korea"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.oth_dtl FROM Paragraphs WHERE Paragraphs.Paragraph_Text like "korea"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Paragraph_ID , Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID WHERE Documents.Document_Name = "Welcome to NY"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Paragraph_ID , Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID WHERE Documents.Document_Name = "Welcome to NY"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID WHERE Documents.Document_Name = "Customer reviews"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID WHERE Documents.Document_Name = "Customer reviews"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id , count(*) FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY Paragraphs.doc_id asc	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id , count(*) FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY Paragraphs.doc_id asc	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id , Documents.Document_Name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID GROUP BY Paragraphs.doc_id	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id , Documents.Document_Name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID GROUP BY Paragraphs.doc_id	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) >= 2	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) >= 2	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id , Documents.Document_Name FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID GROUP BY Paragraphs.doc_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id , Documents.Document_Name FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.Document_ID GROUP BY Paragraphs.doc_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY count(*) asc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY count(*) asc LIMIT 1	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) BETWEEN 1 AND 2	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) BETWEEN 1 AND 2	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.Paragraph_Text = "Brazil" INTERSECT SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.Paragraph_Text = "Ireland"	cre_Doc_Template_Mgt_0
SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.Paragraph_Text = "Brazil" INTERSECT SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.Paragraph_Text = "Ireland"	cre_Doc_Template_Mgt_0
SELECT Documents.doc_id , Documents.doc_name , Documents.Document_Description FROM Documents	cre_Doc_Template_Mgt_1
SELECT Documents.doc_id , Documents.doc_name , Documents.Document_Description FROM Documents	cre_Doc_Template_Mgt_1
SELECT Documents.doc_name , Documents.tpl_id FROM Documents WHERE Documents.Document_Description like "%w%"	cre_Doc_Template_Mgt_1
SELECT Documents.doc_name , Documents.tpl_id FROM Documents WHERE Documents.Document_Description like "%w%"	cre_Doc_Template_Mgt_1
SELECT Documents.doc_id , Documents.tpl_id , Documents.Document_Description FROM Documents WHERE Documents.doc_name = "Robbin CV"	cre_Doc_Template_Mgt_1
SELECT Documents.doc_id , Documents.tpl_id , Documents.Document_Description FROM Documents WHERE Documents.doc_name = "Robbin CV"	cre_Doc_Template_Mgt_1
SELECT count(DISTINCT Documents.tpl_id) FROM Documents	cre_Doc_Template_Mgt_1
SELECT count(DISTINCT Documents.tpl_id) FROM Documents	cre_Doc_Template_Mgt_1
SELECT count(*) FROM Documents JOIN Templates ON Documents.tpl_id = Templates.Template_ID WHERE Templates.Template_Type_Code = "PPT"	cre_Doc_Template_Mgt_1
SELECT count(*) FROM Documents JOIN Templates ON Documents.tpl_id = Templates.Template_ID WHERE Templates.Template_Type_Code = "PPT"	cre_Doc_Template_Mgt_1
SELECT Documents.tpl_id , count(*) FROM Documents GROUP BY Documents.tpl_id	cre_Doc_Template_Mgt_1
SELECT Documents.tpl_id , count(*) FROM Documents GROUP BY Documents.tpl_id	cre_Doc_Template_Mgt_1
SELECT Documents.tpl_id , Templates.Template_Type_Code FROM Documents JOIN Templates ON Documents.tpl_id = Templates.Template_ID GROUP BY Documents.tpl_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Documents.tpl_id , Templates.Template_Type_Code FROM Documents JOIN Templates ON Documents.tpl_id = Templates.Template_ID GROUP BY Documents.tpl_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Documents.tpl_id FROM Documents GROUP BY Documents.tpl_id HAVING count(*) > 1	cre_Doc_Template_Mgt_1
SELECT Documents.tpl_id FROM Documents GROUP BY Documents.tpl_id HAVING count(*) > 1	cre_Doc_Template_Mgt_1
SELECT Templates.Template_ID FROM Templates EXCEPT SELECT Documents.tpl_id FROM Documents	cre_Doc_Template_Mgt_1
SELECT Templates.Template_ID FROM Templates EXCEPT SELECT Documents.tpl_id FROM Documents	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id WHERE Documents.doc_name = "Data base"	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id WHERE Documents.doc_name = "Data base"	cre_Doc_Template_Mgt_1
SELECT Documents.doc_name FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id WHERE Templates.Template_Type_Code = "BK"	cre_Doc_Template_Mgt_1
SELECT Documents.doc_name FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id WHERE Templates.Template_Type_Code = "BK"	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id GROUP BY Templates.Template_Type_Code	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id GROUP BY Templates.Template_Type_Code	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id GROUP BY Templates.Template_Type_Code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id GROUP BY Templates.Template_Type_Code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code FROM Templates EXCEPT SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id	cre_Doc_Template_Mgt_1
SELECT Templates.Template_Type_Code FROM Templates EXCEPT SELECT Templates.Template_Type_Code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id	cre_Doc_Template_Mgt_1
SELECT Ref_Template_Types.tpl_type_code , Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types	cre_Doc_Template_Mgt_1
SELECT Ref_Template_Types.tpl_type_code , Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types	cre_Doc_Template_Mgt_1
SELECT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types WHERE Ref_Template_Types.tpl_type_code = "AD"	cre_Doc_Template_Mgt_1
SELECT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types WHERE Ref_Template_Types.tpl_type_code = "AD"	cre_Doc_Template_Mgt_1
SELECT Ref_Template_Types.tpl_type_code FROM Ref_Template_Types WHERE Ref_Template_Types.Template_Type_Description = "Book"	cre_Doc_Template_Mgt_1
SELECT Ref_Template_Types.tpl_type_code FROM Ref_Template_Types WHERE Ref_Template_Types.Template_Type_Description = "Book"	cre_Doc_Template_Mgt_1
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.Template_Type_Code JOIN Documents ON Templates.Template_ID = Documents.tpl_id	cre_Doc_Template_Mgt_1
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.Template_Type_Code JOIN Documents ON Templates.Template_ID = Documents.tpl_id	cre_Doc_Template_Mgt_1
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.Template_Type_Code WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_1
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.Template_Type_Code WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_1
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Summer Show"	cre_Doc_Template_Mgt_1
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Summer Show"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Other_Details FROM Paragraphs WHERE Paragraphs.para_txt like "korea"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.Other_Details FROM Paragraphs WHERE Paragraphs.para_txt like "korea"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.para_id , Paragraphs.para_txt FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Welcome to NY"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.para_id , Paragraphs.para_txt FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Welcome to NY"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.para_txt FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Customer reviews"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.para_txt FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Customer reviews"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id , count(*) FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY Paragraphs.doc_id asc	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id , count(*) FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY Paragraphs.doc_id asc	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id , Documents.doc_name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id GROUP BY Paragraphs.doc_id	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id , Documents.doc_name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id GROUP BY Paragraphs.doc_id	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) >= 2	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) >= 2	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id , Documents.doc_name FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id GROUP BY Paragraphs.doc_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id , Documents.doc_name FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id GROUP BY Paragraphs.doc_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY count(*) asc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY count(*) asc LIMIT 1	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) BETWEEN 1 AND 2	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) BETWEEN 1 AND 2	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.para_txt = "Brazil" INTERSECT SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.para_txt = "Ireland"	cre_Doc_Template_Mgt_1
SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.para_txt = "Brazil" INTERSECT SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.para_txt = "Ireland"	cre_Doc_Template_Mgt_1
SELECT Documents.doc_id , Documents.doc_name , Documents.doc_desc FROM Documents	cre_Doc_Template_Mgt_2
SELECT Documents.doc_id , Documents.doc_name , Documents.doc_desc FROM Documents	cre_Doc_Template_Mgt_2
SELECT Documents.doc_name , Documents.tpl_id FROM Documents WHERE Documents.doc_desc like "%w%"	cre_Doc_Template_Mgt_2
SELECT Documents.doc_name , Documents.tpl_id FROM Documents WHERE Documents.doc_desc like "%w%"	cre_Doc_Template_Mgt_2
SELECT Documents.doc_id , Documents.tpl_id , Documents.doc_desc FROM Documents WHERE Documents.doc_name = "Robbin CV"	cre_Doc_Template_Mgt_2
SELECT Documents.doc_id , Documents.tpl_id , Documents.doc_desc FROM Documents WHERE Documents.doc_name = "Robbin CV"	cre_Doc_Template_Mgt_2
SELECT count(DISTINCT Documents.tpl_id) FROM Documents	cre_Doc_Template_Mgt_2
SELECT count(DISTINCT Documents.tpl_id) FROM Documents	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Documents JOIN Templates ON Documents.tpl_id = Templates.Template_ID WHERE Templates.tpl_tpye_code = "PPT"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Documents JOIN Templates ON Documents.tpl_id = Templates.Template_ID WHERE Templates.tpl_tpye_code = "PPT"	cre_Doc_Template_Mgt_2
SELECT Documents.tpl_id , count(*) FROM Documents GROUP BY Documents.tpl_id	cre_Doc_Template_Mgt_2
SELECT Documents.tpl_id , count(*) FROM Documents GROUP BY Documents.tpl_id	cre_Doc_Template_Mgt_2
SELECT Documents.tpl_id , Templates.tpl_tpye_code FROM Documents JOIN Templates ON Documents.tpl_id = Templates.Template_ID GROUP BY Documents.tpl_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Documents.tpl_id , Templates.tpl_tpye_code FROM Documents JOIN Templates ON Documents.tpl_id = Templates.Template_ID GROUP BY Documents.tpl_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Documents.tpl_id FROM Documents GROUP BY Documents.tpl_id HAVING count(*) > 1	cre_Doc_Template_Mgt_2
SELECT Documents.tpl_id FROM Documents GROUP BY Documents.tpl_id HAVING count(*) > 1	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Templates EXCEPT SELECT Documents.tpl_id FROM Documents	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Templates EXCEPT SELECT Documents.tpl_id FROM Documents	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID , Templates.ver_no , Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID , Templates.ver_no , Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_2
SELECT DISTINCT Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_2
SELECT DISTINCT Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Templates WHERE Templates.tpl_tpye_code = "PP" or Templates.tpl_tpye_code = "PPT"	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Templates WHERE Templates.tpl_tpye_code = "PP" or Templates.tpl_tpye_code = "PPT"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Templates WHERE Templates.tpl_tpye_code = "CV"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Templates WHERE Templates.tpl_tpye_code = "CV"	cre_Doc_Template_Mgt_2
SELECT Templates.ver_no , Templates.tpl_tpye_code FROM Templates WHERE Templates.ver_no > 5	cre_Doc_Template_Mgt_2
SELECT Templates.ver_no , Templates.tpl_tpye_code FROM Templates WHERE Templates.ver_no > 5	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code , count(*) FROM Templates GROUP BY Templates.tpl_tpye_code	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code , count(*) FROM Templates GROUP BY Templates.tpl_tpye_code	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates GROUP BY Templates.tpl_tpye_code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates GROUP BY Templates.tpl_tpye_code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates GROUP BY Templates.tpl_tpye_code HAVING count(*) < 3	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates GROUP BY Templates.tpl_tpye_code HAVING count(*) < 3	cre_Doc_Template_Mgt_2
SELECT min(Templates.ver_no) , Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_2
SELECT min(Templates.ver_no) , Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id WHERE Documents.doc_name = "Data base"	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id WHERE Documents.doc_name = "Data base"	cre_Doc_Template_Mgt_2
SELECT Documents.doc_name FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id WHERE Templates.tpl_tpye_code = "BK"	cre_Doc_Template_Mgt_2
SELECT Documents.doc_name FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id WHERE Templates.tpl_tpye_code = "BK"	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id GROUP BY Templates.tpl_tpye_code	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id GROUP BY Templates.tpl_tpye_code	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id GROUP BY Templates.tpl_tpye_code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id GROUP BY Templates.tpl_tpye_code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates EXCEPT SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id	cre_Doc_Template_Mgt_2
SELECT Templates.tpl_tpye_code FROM Templates EXCEPT SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.tpl_id	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.tpl_type_code , Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.tpl_type_code , Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types WHERE Ref_Template_Types.tpl_type_code = "AD"	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types WHERE Ref_Template_Types.tpl_type_code = "AD"	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.tpl_type_code FROM Ref_Template_Types WHERE Ref_Template_Types.Template_Type_Description = "Book"	cre_Doc_Template_Mgt_2
SELECT Ref_Template_Types.tpl_type_code FROM Ref_Template_Types WHERE Ref_Template_Types.Template_Type_Description = "Book"	cre_Doc_Template_Mgt_2
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.tpl_tpye_code JOIN Documents ON Templates.Template_ID = Documents.tpl_id	cre_Doc_Template_Mgt_2
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.tpl_tpye_code JOIN Documents ON Templates.Template_ID = Documents.tpl_id	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.tpl_tpye_code WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_2
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.tpl_tpye_code WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Summer Show"	cre_Doc_Template_Mgt_2
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Summer Show"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.para_id , Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Welcome to NY"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.para_id , Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Welcome to NY"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Customer reviews"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id WHERE Documents.doc_name = "Customer reviews"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id , count(*) FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY Paragraphs.doc_id asc	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id , count(*) FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY Paragraphs.doc_id asc	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id , Documents.doc_name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id GROUP BY Paragraphs.doc_id	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id , Documents.doc_name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id GROUP BY Paragraphs.doc_id	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) >= 2	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) >= 2	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id , Documents.doc_name FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id GROUP BY Paragraphs.doc_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id , Documents.doc_name FROM Paragraphs JOIN Documents ON Paragraphs.doc_id = Documents.doc_id GROUP BY Paragraphs.doc_id ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY count(*) asc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id ORDER BY count(*) asc LIMIT 1	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) BETWEEN 1 AND 2	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id FROM Paragraphs GROUP BY Paragraphs.doc_id HAVING count(*) BETWEEN 1 AND 2	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.Paragraph_Text = "Brazil" INTERSECT SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.Paragraph_Text = "Ireland"	cre_Doc_Template_Mgt_2
SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.Paragraph_Text = "Brazil" INTERSECT SELECT Paragraphs.doc_id FROM Paragraphs WHERE Paragraphs.Paragraph_Text = "Ireland"	cre_Doc_Template_Mgt_2
SELECT Documents.doc_id , Documents.Document_Name , Documents.Document_Description FROM Documents	cre_Doc_Template_Mgt_3
SELECT Documents.doc_id , Documents.Document_Name , Documents.Document_Description FROM Documents	cre_Doc_Template_Mgt_3
SELECT Documents.doc_id , Documents.Template_ID , Documents.Document_Description FROM Documents WHERE Documents.Document_Name = "Robbin CV"	cre_Doc_Template_Mgt_3
SELECT Documents.doc_id , Documents.Template_ID , Documents.Document_Description FROM Documents WHERE Documents.Document_Name = "Robbin CV"	cre_Doc_Template_Mgt_3
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.Document_Name = "Summer Show"	cre_Doc_Template_Mgt_3
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.Document_Name = "Summer Show"	cre_Doc_Template_Mgt_3
SELECT Paragraphs.Paragraph_ID , Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.Document_Name = "Welcome to NY"	cre_Doc_Template_Mgt_3
SELECT Paragraphs.Paragraph_ID , Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.Document_Name = "Welcome to NY"	cre_Doc_Template_Mgt_3
SELECT Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.Document_Name = "Customer reviews"	cre_Doc_Template_Mgt_3
SELECT Paragraphs.Paragraph_Text FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.Document_Name = "Customer reviews"	cre_Doc_Template_Mgt_3
SELECT Paragraphs.Document_ID , Documents.Document_Name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_3
SELECT Paragraphs.Document_ID , Documents.Document_Name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_3
SELECT Paragraphs.Document_ID , Documents.Document_Name FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_3
SELECT Paragraphs.Document_ID , Documents.Document_Name FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_3
SELECT Documents.doc_id , Documents.doc_name , Documents.Document_Description FROM Documents	cre_Doc_Template_Mgt_4
SELECT Documents.doc_id , Documents.doc_name , Documents.Document_Description FROM Documents	cre_Doc_Template_Mgt_4
SELECT Documents.doc_name , Documents.Template_ID FROM Documents WHERE Documents.Document_Description like "%w%"	cre_Doc_Template_Mgt_4
SELECT Documents.doc_name , Documents.Template_ID FROM Documents WHERE Documents.Document_Description like "%w%"	cre_Doc_Template_Mgt_4
SELECT Documents.doc_id , Documents.Template_ID , Documents.Document_Description FROM Documents WHERE Documents.doc_name = "Robbin CV"	cre_Doc_Template_Mgt_4
SELECT Documents.doc_id , Documents.Template_ID , Documents.Document_Description FROM Documents WHERE Documents.doc_name = "Robbin CV"	cre_Doc_Template_Mgt_4
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID WHERE Templates.tpl_tpye_code = "PPT"	cre_Doc_Template_Mgt_4
SELECT count(*) FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID WHERE Templates.tpl_tpye_code = "PPT"	cre_Doc_Template_Mgt_4
SELECT Documents.Template_ID , Templates.tpl_tpye_code FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_4
SELECT Documents.Template_ID , Templates.tpl_tpye_code FROM Documents JOIN Templates ON Documents.Template_ID = Templates.Template_ID GROUP BY Documents.Template_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_4
SELECT Templates.Template_ID , Templates.ver_no , Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_4
SELECT Templates.Template_ID , Templates.ver_no , Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_4
SELECT DISTINCT Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_4
SELECT DISTINCT Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_4
SELECT Templates.Template_ID FROM Templates WHERE Templates.tpl_tpye_code = "PP" or Templates.tpl_tpye_code = "PPT"	cre_Doc_Template_Mgt_4
SELECT Templates.Template_ID FROM Templates WHERE Templates.tpl_tpye_code = "PP" or Templates.tpl_tpye_code = "PPT"	cre_Doc_Template_Mgt_4
SELECT count(*) FROM Templates WHERE Templates.tpl_tpye_code = "CV"	cre_Doc_Template_Mgt_4
SELECT count(*) FROM Templates WHERE Templates.tpl_tpye_code = "CV"	cre_Doc_Template_Mgt_4
SELECT Templates.ver_no , Templates.tpl_tpye_code FROM Templates WHERE Templates.ver_no > 5	cre_Doc_Template_Mgt_4
SELECT Templates.ver_no , Templates.tpl_tpye_code FROM Templates WHERE Templates.ver_no > 5	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code , count(*) FROM Templates GROUP BY Templates.tpl_tpye_code	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code , count(*) FROM Templates GROUP BY Templates.tpl_tpye_code	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates GROUP BY Templates.tpl_tpye_code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates GROUP BY Templates.tpl_tpye_code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates GROUP BY Templates.tpl_tpye_code HAVING count(*) < 3	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates GROUP BY Templates.tpl_tpye_code HAVING count(*) < 3	cre_Doc_Template_Mgt_4
SELECT min(Templates.ver_no) , Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_4
SELECT min(Templates.ver_no) , Templates.tpl_tpye_code FROM Templates	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.doc_name = "Data base"	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Documents.doc_name = "Data base"	cre_Doc_Template_Mgt_4
SELECT Documents.doc_name FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.tpl_tpye_code = "BK"	cre_Doc_Template_Mgt_4
SELECT Documents.doc_name FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID WHERE Templates.tpl_tpye_code = "BK"	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.tpl_tpye_code	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code , count(*) FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.tpl_tpye_code	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.tpl_tpye_code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Templates.tpl_tpye_code ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates EXCEPT SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_4
SELECT Templates.tpl_tpye_code FROM Templates EXCEPT SELECT Templates.tpl_tpye_code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_4
SELECT Ref_Template_Types.tpl_type_code , Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types	cre_Doc_Template_Mgt_4
SELECT Ref_Template_Types.tpl_type_code , Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types	cre_Doc_Template_Mgt_4
SELECT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types WHERE Ref_Template_Types.tpl_type_code = "AD"	cre_Doc_Template_Mgt_4
SELECT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types WHERE Ref_Template_Types.tpl_type_code = "AD"	cre_Doc_Template_Mgt_4
SELECT Ref_Template_Types.tpl_type_code FROM Ref_Template_Types WHERE Ref_Template_Types.Template_Type_Description = "Book"	cre_Doc_Template_Mgt_4
SELECT Ref_Template_Types.tpl_type_code FROM Ref_Template_Types WHERE Ref_Template_Types.Template_Type_Description = "Book"	cre_Doc_Template_Mgt_4
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.tpl_tpye_code JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_4
SELECT DISTINCT Ref_Template_Types.Template_Type_Description FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.tpl_tpye_code JOIN Documents ON Templates.Template_ID = Documents.Template_ID	cre_Doc_Template_Mgt_4
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.tpl_tpye_code WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_4
SELECT Templates.Template_ID FROM Ref_Template_Types JOIN Templates ON Ref_Template_Types.tpl_type_code = Templates.tpl_tpye_code WHERE Ref_Template_Types.Template_Type_Description = "Presentation"	cre_Doc_Template_Mgt_4
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.doc_name = "Summer Show"	cre_Doc_Template_Mgt_4
SELECT count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.doc_name = "Summer Show"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Other_Details FROM Paragraphs WHERE Paragraphs.para_txt like "korea"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Other_Details FROM Paragraphs WHERE Paragraphs.para_txt like "korea"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.para_id , Paragraphs.para_txt FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.doc_name = "Welcome to NY"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.para_id , Paragraphs.para_txt FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.doc_name = "Welcome to NY"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.para_txt FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.doc_name = "Customer reviews"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.para_txt FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id WHERE Documents.doc_name = "Customer reviews"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Document_ID , Documents.doc_name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Document_ID , Documents.doc_name , count(*) FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id GROUP BY Paragraphs.Document_ID	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Document_ID , Documents.doc_name FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Document_ID , Documents.doc_name FROM Paragraphs JOIN Documents ON Paragraphs.Document_ID = Documents.doc_id GROUP BY Paragraphs.Document_ID ORDER BY count(*) desc LIMIT 1	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.para_txt = "Brazil" INTERSECT SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.para_txt = "Ireland"	cre_Doc_Template_Mgt_4
SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.para_txt = "Brazil" INTERSECT SELECT Paragraphs.Document_ID FROM Paragraphs WHERE Paragraphs.para_txt = "Ireland"	cre_Doc_Template_Mgt_4
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID	course_teach_0
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID	course_teach_0
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID ORDER BY teacher.Name asc	course_teach_0
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID ORDER BY teacher.Name asc	course_teach_0
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID WHERE course.crs = "Math"	course_teach_0
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID WHERE course.crs = "Math"	course_teach_0
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id	course_teach_1
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id	course_teach_1
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id ORDER BY teacher.Name asc	course_teach_1
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id ORDER BY teacher.Name asc	course_teach_1
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id WHERE course.crs = "Math"	course_teach_1
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.crs_id = course.crs_id JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id WHERE course.crs = "Math"	course_teach_1
SELECT teacher.Name , count(*) FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id GROUP BY teacher.Name	course_teach_1
SELECT teacher.Name , count(*) FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id GROUP BY teacher.Name	course_teach_1
SELECT teacher.Name FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id GROUP BY teacher.Name HAVING count(*) >= 2	course_teach_1
SELECT teacher.Name FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id GROUP BY teacher.Name HAVING count(*) >= 2	course_teach_1
SELECT teacher.Name FROM teacher WHERE teacher.tchr_id NOT in (SELECT course_arrange.tchr_id FROM course_arrange)	course_teach_1
SELECT teacher.Name FROM teacher WHERE teacher.tchr_id NOT in (SELECT course_arrange.tchr_id FROM course_arrange)	course_teach_1
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id	course_teach_2
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id	course_teach_2
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id ORDER BY teacher.Name asc	course_teach_2
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.crs_id = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id ORDER BY teacher.Name asc	course_teach_2
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.crs_id = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id WHERE course.crs = "Math"	course_teach_2
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.crs_id = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id WHERE course.crs = "Math"	course_teach_2
SELECT teacher.Name , count(*) FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id GROUP BY teacher.Name	course_teach_2
SELECT teacher.Name , count(*) FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id GROUP BY teacher.Name	course_teach_2
SELECT teacher.Name FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id GROUP BY teacher.Name HAVING count(*) >= 2	course_teach_2
SELECT teacher.Name FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.tchr_id GROUP BY teacher.Name HAVING count(*) >= 2	course_teach_2
SELECT teacher.Name FROM teacher WHERE teacher.tchr_id NOT in (SELECT course_arrange.tchr_id FROM course_arrange)	course_teach_2
SELECT teacher.Name FROM teacher WHERE teacher.tchr_id NOT in (SELECT course_arrange.tchr_id FROM course_arrange)	course_teach_2
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.Course_ID = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id	course_teach_3
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.Course_ID = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id	course_teach_3
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.Course_ID = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id ORDER BY teacher.Name asc	course_teach_3
SELECT teacher.Name , course.crs FROM course_arrange JOIN course ON course_arrange.Course_ID = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id ORDER BY teacher.Name asc	course_teach_3
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.Course_ID = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id WHERE course.crs = "Math"	course_teach_3
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.Course_ID = course.crs_id JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id WHERE course.crs = "Math"	course_teach_3
SELECT teacher.Name , count(*) FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id GROUP BY teacher.Name	course_teach_3
SELECT teacher.Name , count(*) FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id GROUP BY teacher.Name	course_teach_3
SELECT teacher.Name FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id GROUP BY teacher.Name HAVING count(*) >= 2	course_teach_3
SELECT teacher.Name FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.tchr_id GROUP BY teacher.Name HAVING count(*) >= 2	course_teach_3
SELECT teacher.Name FROM teacher WHERE teacher.tchr_id NOT in (SELECT course_arrange.Teacher_ID FROM course_arrange)	course_teach_3
SELECT teacher.Name FROM teacher WHERE teacher.tchr_id NOT in (SELECT course_arrange.Teacher_ID FROM course_arrange)	course_teach_3
SELECT teacher.Name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID	course_teach_4
SELECT teacher.Name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID	course_teach_4
SELECT teacher.Name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID ORDER BY teacher.Name asc	course_teach_4
SELECT teacher.Name , course.Course FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID ORDER BY teacher.Name asc	course_teach_4
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID WHERE course.Course = "Math"	course_teach_4
SELECT teacher.Name FROM course_arrange JOIN course ON course_arrange.Course_ID = course.Course_ID JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID WHERE course.Course = "Math"	course_teach_4
SELECT teacher.Name , count(*) FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID GROUP BY teacher.Name	course_teach_4
SELECT teacher.Name , count(*) FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID GROUP BY teacher.Name	course_teach_4
SELECT teacher.Name FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID GROUP BY teacher.Name HAVING count(*) >= 2	course_teach_4
SELECT teacher.Name FROM course_arrange JOIN teacher ON course_arrange.tchr_id = teacher.Teacher_ID GROUP BY teacher.Name HAVING count(*) >= 2	course_teach_4
SELECT teacher.Name FROM teacher WHERE teacher.Teacher_ID NOT in (SELECT course_arrange.tchr_id FROM course_arrange)	course_teach_4
SELECT teacher.Name FROM teacher WHERE teacher.Teacher_ID NOT in (SELECT course_arrange.tchr_id FROM course_arrange)	course_teach_4
SELECT visitor.Name FROM visitor WHERE visitor.lvl_mem > 4 ORDER BY visitor.lvl_mem desc	museum_visit_0
SELECT avg(visitor.Age) FROM visitor WHERE visitor.lvl_mem <= 4	museum_visit_0
SELECT visitor.Name , visitor.lvl_mem FROM visitor WHERE visitor.lvl_mem > 4 ORDER BY visitor.Age desc	museum_visit_0
SELECT museum.Museum_ID , museum.Name FROM museum ORDER BY museum.num_stf desc LIMIT 1	museum_visit_0
SELECT avg(museum.num_stf) FROM museum WHERE museum.Open_Year < 2009	museum_visit_0
SELECT museum.num_stf , museum.Open_Year FROM museum WHERE museum.Name = "Plaza Museum"	museum_visit_0
SELECT museum.Name FROM museum WHERE museum.num_stf > (SELECT min(museum.num_stf) FROM museum WHERE museum.Open_Year > 2010.0)	museum_visit_0
SELECT visit.visitor_ID , visitor.Name , visitor.lvl_mem FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID GROUP BY visit.visitor_ID ORDER BY sum(visit.Total_spent) desc LIMIT 1	museum_visit_0
SELECT visitor.Name , visitor.Age FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID ORDER BY visit.num_tkt desc LIMIT 1	museum_visit_0
SELECT avg(visit.num_tkt) , max(visit.num_tkt) FROM visit	museum_visit_0
SELECT sum(visit.Total_spent) FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID WHERE visitor.lvl_mem = 1	museum_visit_0
SELECT visitor.Name FROM visitor WHERE visitor.lvl_mem > 4 ORDER BY visitor.lvl_mem desc	museum_visit_1
SELECT avg(visitor.Age) FROM visitor WHERE visitor.lvl_mem <= 4	museum_visit_1
SELECT visitor.Name , visitor.lvl_mem FROM visitor WHERE visitor.lvl_mem > 4 ORDER BY visitor.Age desc	museum_visit_1
SELECT museum.mus_id , museum.Name FROM museum ORDER BY museum.Num_of_Staff desc LIMIT 1	museum_visit_1
SELECT visit.visitor_ID , visitor.Name , visitor.lvl_mem FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID GROUP BY visit.visitor_ID ORDER BY sum(visit.tot_spent) desc LIMIT 1	museum_visit_1
SELECT visit.mus_id , museum.Name FROM museum JOIN visit ON museum.mus_id = visit.mus_id GROUP BY visit.mus_id ORDER BY count(*) desc LIMIT 1	museum_visit_1
SELECT museum.Name FROM museum WHERE museum.mus_id NOT in (SELECT visit.mus_id FROM visit)	museum_visit_1
SELECT sum(visit.tot_spent) FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID WHERE visitor.lvl_mem = 1	museum_visit_1
SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.mus_id = visit.mus_id WHERE museum.Open_Year < 2009 INTERSECT SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.mus_id = visit.mus_id WHERE museum.Open_Year > 2011	museum_visit_1
SELECT count(*) FROM visitor WHERE visitor.ID NOT in (SELECT visit.visitor_ID FROM museum JOIN visit ON museum.mus_id = visit.mus_id WHERE museum.Open_Year > 2010.0)	museum_visit_1
SELECT visitor.Name FROM visitor WHERE visitor.lvl_mem > 4 ORDER BY visitor.lvl_mem desc	museum_visit_2
SELECT avg(visitor.Age) FROM visitor WHERE visitor.lvl_mem <= 4	museum_visit_2
SELECT visitor.Name , visitor.lvl_mem FROM visitor WHERE visitor.lvl_mem > 4 ORDER BY visitor.Age desc	museum_visit_2
SELECT museum.Museum_ID , museum.Name FROM museum ORDER BY museum.num_stf desc LIMIT 1	museum_visit_2
SELECT avg(museum.num_stf) FROM museum WHERE museum.Open_Year < 2009	museum_visit_2
SELECT museum.num_stf , museum.Open_Year FROM museum WHERE museum.Name = "Plaza Museum"	museum_visit_2
SELECT museum.Name FROM museum WHERE museum.num_stf > (SELECT min(museum.num_stf) FROM museum WHERE museum.Open_Year > 2010.0)	museum_visit_2
SELECT visit.visitor_ID , visitor.Name , visitor.lvl_mem FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID GROUP BY visit.visitor_ID ORDER BY sum(visit.Total_spent) desc LIMIT 1	museum_visit_2
SELECT visit.mus_id , museum.Name FROM museum JOIN visit ON museum.Museum_ID = visit.mus_id GROUP BY visit.mus_id ORDER BY count(*) desc LIMIT 1	museum_visit_2
SELECT museum.Name FROM museum WHERE museum.Museum_ID NOT in (SELECT visit.mus_id FROM visit)	museum_visit_2
SELECT sum(visit.Total_spent) FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID WHERE visitor.lvl_mem = 1	museum_visit_2
SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.mus_id WHERE museum.Open_Year < 2009 INTERSECT SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.mus_id WHERE museum.Open_Year > 2011	museum_visit_2
SELECT count(*) FROM visitor WHERE visitor.ID NOT in (SELECT visit.visitor_ID FROM museum JOIN visit ON museum.Museum_ID = visit.mus_id WHERE museum.Open_Year > 2010.0)	museum_visit_2
SELECT visit.mus_id , museum.Name FROM museum JOIN visit ON museum.Museum_ID = visit.mus_id GROUP BY visit.mus_id ORDER BY count(*) desc LIMIT 1	museum_visit_4
SELECT museum.Name FROM museum WHERE museum.Museum_ID NOT in (SELECT visit.mus_id FROM visit)	museum_visit_4
SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.mus_id WHERE museum.Open_Year < 2009 INTERSECT SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.Museum_ID = visit.mus_id WHERE museum.Open_Year > 2011	museum_visit_4
SELECT count(*) FROM visitor WHERE visitor.ID NOT in (SELECT visit.visitor_ID FROM museum JOIN visit ON museum.Museum_ID = visit.mus_id WHERE museum.Open_Year > 2010.0)	museum_visit_4
SELECT museum.mus_id , museum.Name FROM museum ORDER BY museum.num_stf desc LIMIT 1	museum_visit_5
SELECT avg(museum.num_stf) FROM museum WHERE museum.Open_Year < 2009	museum_visit_5
SELECT museum.num_stf , museum.Open_Year FROM museum WHERE museum.Name = "Plaza Museum"	museum_visit_5
SELECT museum.Name FROM museum WHERE museum.num_stf > (SELECT min(museum.num_stf) FROM museum WHERE museum.Open_Year > 2010.0)	museum_visit_5
SELECT visit.Museum_ID , museum.Name FROM museum JOIN visit ON museum.mus_id = visit.Museum_ID GROUP BY visit.Museum_ID ORDER BY count(*) desc LIMIT 1	museum_visit_5
SELECT museum.Name FROM museum WHERE museum.mus_id NOT in (SELECT visit.Museum_ID FROM visit)	museum_visit_5
SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.mus_id = visit.Museum_ID WHERE museum.Open_Year < 2009 INTERSECT SELECT visitor.Name FROM visitor JOIN visit ON visitor.ID = visit.visitor_ID JOIN museum ON museum.mus_id = visit.Museum_ID WHERE museum.Open_Year > 2011	museum_visit_5
SELECT count(*) FROM visitor WHERE visitor.ID NOT in (SELECT visit.visitor_ID FROM museum JOIN visit ON museum.mus_id = visit.Museum_ID WHERE museum.Open_Year > 2010.0)	museum_visit_5
SELECT players.first_name , players.dob FROM players WHERE players.cntry_code = "USA"	wta_1_0
SELECT players.first_name , players.dob FROM players WHERE players.cntry_code = "USA"	wta_1_0
SELECT count(DISTINCT players.cntry_code) FROM players	wta_1_0
SELECT count(DISTINCT players.cntry_code) FROM players	wta_1_0
SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_0
SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_0
SELECT players.first_name , players.cntry_code FROM players ORDER BY players.dob asc LIMIT 1	wta_1_0
SELECT players.first_name , players.cntry_code FROM players ORDER BY players.dob asc LIMIT 1	wta_1_0
SELECT players.first_name , players.last_name FROM players ORDER BY players.dob asc	wta_1_0
SELECT players.first_name , players.last_name FROM players ORDER BY players.dob asc	wta_1_0
SELECT players.first_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.dob asc	wta_1_0
SELECT players.first_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.dob asc	wta_1_0
SELECT players.cntry_code , players.first_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_0
SELECT players.cntry_code , players.first_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_0
SELECT count(*) , players.cntry_code FROM players GROUP BY players.cntry_code	wta_1_0
SELECT count(*) , players.cntry_code FROM players GROUP BY players.cntry_code	wta_1_0
SELECT players.cntry_code FROM players GROUP BY players.cntry_code ORDER BY count(*) desc LIMIT 1	wta_1_0
SELECT players.cntry_code FROM players GROUP BY players.cntry_code ORDER BY count(*) desc LIMIT 1	wta_1_0
SELECT players.cntry_code FROM players GROUP BY players.cntry_code HAVING count(*) > 50	wta_1_0
SELECT players.cntry_code FROM players GROUP BY players.cntry_code HAVING count(*) > 50	wta_1_0
SELECT players.first_name , players.cntry_code , players.dob FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_0
SELECT players.first_name , players.cntry_code , players.dob FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_0
SELECT players.first_name , players.birth_date FROM players WHERE players.cntry_code = "USA"	wta_1_1
SELECT players.first_name , players.birth_date FROM players WHERE players.cntry_code = "USA"	wta_1_1
SELECT count(DISTINCT players.cntry_code) FROM players	wta_1_1
SELECT count(DISTINCT players.cntry_code) FROM players	wta_1_1
SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_1
SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_1
SELECT players.first_name , players.cntry_code FROM players ORDER BY players.birth_date asc LIMIT 1	wta_1_1
SELECT players.first_name , players.cntry_code FROM players ORDER BY players.birth_date asc LIMIT 1	wta_1_1
SELECT players.cntry_code , players.first_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_1
SELECT players.cntry_code , players.first_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_1
SELECT matches.winner_name , matches.winner_rank_pts FROM matches GROUP BY matches.winner_name ORDER BY count(*) desc LIMIT 1	wta_1_1
SELECT matches.winner_name , matches.winner_rank_pts FROM matches GROUP BY matches.winner_name ORDER BY count(*) desc LIMIT 1	wta_1_1
SELECT matches.winner_name FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.winner_rank_pts desc LIMIT 1	wta_1_1
SELECT matches.winner_name FROM matches WHERE matches.tourney_name = "Australian Open" ORDER BY matches.winner_rank_pts desc LIMIT 1	wta_1_1
SELECT count(*) , players.cntry_code FROM players GROUP BY players.cntry_code	wta_1_1
SELECT count(*) , players.cntry_code FROM players GROUP BY players.cntry_code	wta_1_1
SELECT players.cntry_code FROM players GROUP BY players.cntry_code ORDER BY count(*) desc LIMIT 1	wta_1_1
SELECT players.cntry_code FROM players GROUP BY players.cntry_code ORDER BY count(*) desc LIMIT 1	wta_1_1
SELECT players.cntry_code FROM players GROUP BY players.cntry_code HAVING count(*) > 50	wta_1_1
SELECT players.cntry_code FROM players GROUP BY players.cntry_code HAVING count(*) > 50	wta_1_1
SELECT players.first_name , players.cntry_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_pts desc LIMIT 1	wta_1_1
SELECT players.first_name , players.cntry_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_pts desc LIMIT 1	wta_1_1
SELECT players.first_name , players.dob FROM players WHERE players.country_code = "USA"	wta_1_3
SELECT players.first_name , players.dob FROM players WHERE players.country_code = "USA"	wta_1_3
SELECT players.first_name , players.country_code FROM players ORDER BY players.dob asc LIMIT 1	wta_1_3
SELECT players.first_name , players.country_code FROM players ORDER BY players.dob asc LIMIT 1	wta_1_3
SELECT players.first_name , players.last_name FROM players ORDER BY players.dob asc	wta_1_3
SELECT players.first_name , players.last_name FROM players ORDER BY players.dob asc	wta_1_3
SELECT players.first_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.dob asc	wta_1_3
SELECT players.first_name , players.last_name FROM players WHERE players.hand = "L" ORDER BY players.dob asc	wta_1_3
SELECT sum(rankings.ranking_pts) , players.first_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.first_name	wta_1_3
SELECT sum(rankings.ranking_pts) , players.first_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.first_name	wta_1_3
SELECT players.first_name , players.country_code , players.dob FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_3
SELECT players.first_name , players.country_code , players.dob FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_3
SELECT players.first_name , players.birth_date FROM players WHERE players.cntry_code = "USA"	wta_1_4
SELECT players.first_name , players.birth_date FROM players WHERE players.cntry_code = "USA"	wta_1_4
SELECT count(DISTINCT players.cntry_code) FROM players	wta_1_4
SELECT count(DISTINCT players.cntry_code) FROM players	wta_1_4
SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_4
SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "WTA Championships" INTERSECT SELECT players.cntry_code , players.first_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = "Australian Open"	wta_1_4
SELECT players.first_name , players.cntry_code FROM players ORDER BY players.birth_date asc LIMIT 1	wta_1_4
SELECT players.first_name , players.cntry_code FROM players ORDER BY players.birth_date asc LIMIT 1	wta_1_4
SELECT players.cntry_code , players.first_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_4
SELECT players.cntry_code , players.first_name FROM players JOIN rankings ON players.player_id = rankings.player_id ORDER BY rankings.tours desc LIMIT 1	wta_1_4
SELECT count(*) , players.cntry_code FROM players GROUP BY players.cntry_code	wta_1_4
SELECT count(*) , players.cntry_code FROM players GROUP BY players.cntry_code	wta_1_4
SELECT players.cntry_code FROM players GROUP BY players.cntry_code ORDER BY count(*) desc LIMIT 1	wta_1_4
SELECT players.cntry_code FROM players GROUP BY players.cntry_code ORDER BY count(*) desc LIMIT 1	wta_1_4
SELECT players.cntry_code FROM players GROUP BY players.cntry_code HAVING count(*) > 50	wta_1_4
SELECT players.cntry_code FROM players GROUP BY players.cntry_code HAVING count(*) > 50	wta_1_4
SELECT players.first_name , players.cntry_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_4
SELECT players.first_name , players.cntry_code , players.birth_date FROM players JOIN matches ON players.player_id = matches.winner_id ORDER BY matches.winner_rank_points desc LIMIT 1	wta_1_4
SELECT battle.name , battle.result FROM battle WHERE battle.bg_cdr != "Boril"	battle_death_0
SELECT DISTINCT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.ship_type = "Brig"	battle_death_0
SELECT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.lib JOIN death ON ship.id = death.caused_by_ship_id GROUP BY battle.id HAVING sum(death.killed) > 10	battle_death_0
SELECT battle.name FROM battle WHERE battle.bg_cdr = "Kaloyan" and battle.latin_cdr = "Baldwin I"	battle_death_0
SELECT count(*) FROM battle WHERE battle.id NOT in (SELECT ship.lib FROM ship WHERE ship.tonnage = "225")	battle_death_0
SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.name = "Lettice" INTERSECT SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.name = "HMS Atalanta"	battle_death_0
SELECT battle.name , battle.result , battle.bg_cdr FROM battle EXCEPT SELECT battle.name , battle.result , battle.bg_cdr FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.loc = "English Channel"	battle_death_0
SELECT count(*) FROM ship WHERE ship.dos = "Captured"	battle_death_1
SELECT death.killed , death.injured FROM death JOIN ship ON death.cbs = ship.id WHERE ship.tonnage = "t"	battle_death_1
SELECT battle.name , battle.result FROM battle WHERE battle.bg_cdr != "Boril"	battle_death_1
SELECT DISTINCT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.st = "Brig"	battle_death_1
SELECT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.lib JOIN death ON ship.id = death.cbs GROUP BY battle.id HAVING sum(death.killed) > 10	battle_death_1
SELECT ship.id , ship.name FROM death JOIN ship ON death.cbs = ship.id GROUP BY ship.id ORDER BY count(*) desc LIMIT 1	battle_death_1
SELECT battle.name FROM battle WHERE battle.bg_cdr = "Kaloyan" and battle.latin_commander = "Baldwin I"	battle_death_1
SELECT count(*) FROM battle WHERE battle.id NOT in (SELECT ship.lib FROM ship WHERE ship.tonnage = "225")	battle_death_1
SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.name = "Lettice" INTERSECT SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.name = "HMS Atalanta"	battle_death_1
SELECT battle.name , battle.result , battle.bg_cdr FROM battle EXCEPT SELECT battle.name , battle.result , battle.bg_cdr FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.loc = "English Channel"	battle_death_1
SELECT count(*) FROM ship WHERE ship.dos = "Captured"	battle_death_2
SELECT DISTINCT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.st = "Brig"	battle_death_2
SELECT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.lib JOIN death ON ship.id = death.caused_by_ship_id GROUP BY battle.id HAVING sum(death.killed) > 10	battle_death_2
SELECT battle.name FROM battle WHERE battle.bulgarian_commander = "Kaloyan" and battle.latin_cdr = "Baldwin I"	battle_death_2
SELECT count(*) FROM battle WHERE battle.id NOT in (SELECT ship.lib FROM ship WHERE ship.tonnage = "225")	battle_death_2
SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.name = "Lettice" INTERSECT SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.name = "HMS Atalanta"	battle_death_2
SELECT battle.name , battle.result , battle.bulgarian_commander FROM battle EXCEPT SELECT battle.name , battle.result , battle.bulgarian_commander FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.loc = "English Channel"	battle_death_2
SELECT battle.name , battle.result FROM battle WHERE battle.bg_cdr != "Boril"	battle_death_3
SELECT DISTINCT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.st = "Brig"	battle_death_3
SELECT battle.id , battle.name FROM battle JOIN ship ON battle.id = ship.lib JOIN death ON ship.id = death.caused_by_ship_id GROUP BY battle.id HAVING sum(death.killed) > 10	battle_death_3
SELECT battle.name FROM battle WHERE battle.bg_cdr = "Kaloyan" and battle.latin_commander = "Baldwin I"	battle_death_3
SELECT count(*) FROM battle WHERE battle.id NOT in (SELECT ship.lib FROM ship WHERE ship.tonnage = "225")	battle_death_3
SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.name = "Lettice" INTERSECT SELECT battle.name , battle.date FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.name = "HMS Atalanta"	battle_death_3
SELECT battle.name , battle.result , battle.bg_cdr FROM battle EXCEPT SELECT battle.name , battle.result , battle.bg_cdr FROM battle JOIN ship ON battle.id = ship.lib WHERE ship.location = "English Channel"	battle_death_3
SELECT count(*) FROM ship WHERE ship.dos = "Captured"	battle_death_4
SELECT Courses.course_description FROM Courses WHERE Courses.crs_name = "math"	student_transcripts_tracking_0
SELECT Courses.course_description FROM Courses WHERE Courses.crs_name = "math"	student_transcripts_tracking_0
SELECT Addresses.zipcode FROM Addresses WHERE Addresses.city = "Port Chelsea"	student_transcripts_tracking_0
SELECT Addresses.zipcode FROM Addresses WHERE Addresses.city = "Port Chelsea"	student_transcripts_tracking_0
SELECT Departments.department_name , Degree_Programs.dept_id FROM Degree_Programs JOIN Departments ON Degree_Programs.dept_id = Departments.department_id GROUP BY Degree_Programs.dept_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Departments.department_name , Degree_Programs.dept_id FROM Degree_Programs JOIN Departments ON Degree_Programs.dept_id = Departments.department_id GROUP BY Degree_Programs.dept_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT count(DISTINCT Degree_Programs.dept_id) FROM Degree_Programs	student_transcripts_tracking_0
SELECT count(DISTINCT Degree_Programs.dept_id) FROM Degree_Programs	student_transcripts_tracking_0
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_0
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_0
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.department_id = Degree_Programs.dept_id WHERE Departments.department_name = "engineer"	student_transcripts_tracking_0
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.department_id = Degree_Programs.dept_id WHERE Departments.department_name = "engineer"	student_transcripts_tracking_0
SELECT Sections.section_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_0
SELECT Sections.section_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_0
SELECT Courses.crs_name , Courses.course_id FROM Courses JOIN Sections ON Courses.course_id = Sections.course_id GROUP BY Courses.course_id HAVING count(*) <= 2	student_transcripts_tracking_0
SELECT Courses.crs_name , Courses.course_id FROM Courses JOIN Sections ON Courses.course_id = Sections.course_id GROUP BY Courses.course_id HAVING count(*) <= 2	student_transcripts_tracking_0
SELECT Departments.dept_desc FROM Departments WHERE Departments.department_name like "%computer%"	student_transcripts_tracking_0
SELECT Departments.dept_desc FROM Departments WHERE Departments.department_name like "%computer%"	student_transcripts_tracking_0
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_0
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_0
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT DISTINCT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.course_id = Student_Enrolment_Courses.course_id	student_transcripts_tracking_0
SELECT DISTINCT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.course_id = Student_Enrolment_Courses.course_id	student_transcripts_tracking_0
SELECT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.course_id = Student_Enrolment_Courses.course_id GROUP BY Courses.crs_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.course_id = Student_Enrolment_Courses.course_id GROUP BY Courses.crs_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id	student_transcripts_tracking_0
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.student_id = Student_Enrolment.student_id	student_transcripts_tracking_0
SELECT Students.cell FROM Students WHERE Students.first_name = "Timmothy" and Students.last_name = "Ward"	student_transcripts_tracking_0
SELECT Students.cell FROM Students WHERE Students.first_name = "timmothy" and Students.last_name = "ward"	student_transcripts_tracking_0
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.permanent_address_id	student_transcripts_tracking_0
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.permanent_address_id	student_transcripts_tracking_0
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_0
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_0
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_0
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_0
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_0
SELECT Sections.sect_desc FROM Sections WHERE Sections.section_name = "h"	student_transcripts_tracking_0
SELECT Sections.sect_desc FROM Sections WHERE Sections.section_name = "h"	student_transcripts_tracking_0
SELECT Students.first_name FROM Students JOIN Addresses ON Students.permanent_address_id = Addresses.adr_id WHERE Addresses.country = "haiti" or Students.cell = "09700166582"	student_transcripts_tracking_0
SELECT Students.first_name FROM Students JOIN Addresses ON Students.permanent_address_id = Addresses.adr_id WHERE Addresses.country = "haiti" or Students.cell = "09700166582"	student_transcripts_tracking_0
SELECT Courses.crs_desc FROM Courses WHERE Courses.crs_name = "math"	student_transcripts_tracking_1
SELECT Courses.crs_desc FROM Courses WHERE Courses.crs_name = "math"	student_transcripts_tracking_1
SELECT Addresses.zipcode FROM Addresses WHERE Addresses.city = "Port Chelsea"	student_transcripts_tracking_1
SELECT Addresses.zipcode FROM Addresses WHERE Addresses.city = "Port Chelsea"	student_transcripts_tracking_1
SELECT Departments.dept_name , Degree_Programs.dept_id FROM Degree_Programs JOIN Departments ON Degree_Programs.dept_id = Departments.dept_id GROUP BY Degree_Programs.dept_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Departments.dept_name , Degree_Programs.dept_id FROM Degree_Programs JOIN Departments ON Degree_Programs.dept_id = Departments.dept_id GROUP BY Degree_Programs.dept_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT count(DISTINCT Degree_Programs.dept_id) FROM Degree_Programs	student_transcripts_tracking_1
SELECT count(DISTINCT Degree_Programs.dept_id) FROM Degree_Programs	student_transcripts_tracking_1
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_1
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_1
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.dept_id = Degree_Programs.dept_id WHERE Departments.dept_name = "engineer"	student_transcripts_tracking_1
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.dept_id = Degree_Programs.dept_id WHERE Departments.dept_name = "engineer"	student_transcripts_tracking_1
SELECT Sections.sect_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_1
SELECT Sections.sect_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_1
SELECT Courses.crs_name , Courses.crs_id FROM Courses JOIN Sections ON Courses.crs_id = Sections.crs_id GROUP BY Courses.crs_id HAVING count(*) <= 2	student_transcripts_tracking_1
SELECT Courses.crs_name , Courses.crs_id FROM Courses JOIN Sections ON Courses.crs_id = Sections.crs_id GROUP BY Courses.crs_id HAVING count(*) <= 2	student_transcripts_tracking_1
SELECT Sections.sect_name FROM Sections ORDER BY Sections.sect_name desc	student_transcripts_tracking_1
SELECT Sections.sect_name FROM Sections ORDER BY Sections.sect_name desc	student_transcripts_tracking_1
SELECT Semesters.sem_name , Semesters.sem_id FROM Semesters JOIN Student_Enrolment ON Semesters.sem_id = Student_Enrolment.sem_id GROUP BY Semesters.sem_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Semesters.sem_name , Semesters.sem_id FROM Semesters JOIN Student_Enrolment ON Semesters.sem_id = Student_Enrolment.sem_id GROUP BY Semesters.sem_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Departments.dept_desc FROM Departments WHERE Departments.dept_name like "%computer%"	student_transcripts_tracking_1
SELECT Departments.dept_desc FROM Departments WHERE Departments.dept_name like "%computer%"	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.last_name , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid HAVING count(*) = 2	student_transcripts_tracking_1
SELECT Students.first_name , Students.middle_name , Students.last_name , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid HAVING count(*) = 2	student_transcripts_tracking_1
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_1
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_1
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Students.stuid , Students.first_name , Students.middle_name , Students.last_name , count(*) , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Students.stuid , Students.first_name , Students.middle_name , Students.last_name , count(*) , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Semesters.sem_name FROM Semesters WHERE Semesters.sem_id NOT in (SELECT Student_Enrolment.sem_id FROM Student_Enrolment)	student_transcripts_tracking_1
SELECT Semesters.sem_name FROM Semesters WHERE Semesters.sem_id NOT in (SELECT Student_Enrolment.sem_id FROM Student_Enrolment)	student_transcripts_tracking_1
SELECT DISTINCT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.crs_id	student_transcripts_tracking_1
SELECT DISTINCT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.crs_id	student_transcripts_tracking_1
SELECT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.crs_id GROUP BY Courses.crs_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.crs_id GROUP BY Courses.crs_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id	student_transcripts_tracking_1
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id	student_transcripts_tracking_1
SELECT Students.cell FROM Students WHERE Students.first_name = "Timmothy" and Students.last_name = "Ward"	student_transcripts_tracking_1
SELECT Students.cell FROM Students WHERE Students.first_name = "timmothy" and Students.last_name = "ward"	student_transcripts_tracking_1
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.pa_id	student_transcripts_tracking_1
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.pa_id	student_transcripts_tracking_1
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT Transcripts.transcript_date , Transcripts.oth_dtl FROM Transcripts ORDER BY Transcripts.transcript_date asc LIMIT 1	student_transcripts_tracking_1
SELECT Transcripts.transcript_date , Transcripts.oth_dtl FROM Transcripts ORDER BY Transcripts.transcript_date asc LIMIT 1	student_transcripts_tracking_1
SELECT count(*) , Transcript_Contents.stu_crs_id FROM Transcript_Contents GROUP BY Transcript_Contents.stu_crs_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT count(*) , Transcript_Contents.stu_crs_id FROM Transcript_Contents GROUP BY Transcript_Contents.stu_crs_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_1
SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_1
SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_1
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_1
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_1
SELECT Students.oth_stu_dtl FROM Students ORDER BY Students.oth_stu_dtl desc	student_transcripts_tracking_1
SELECT Students.oth_stu_dtl FROM Students ORDER BY Students.oth_stu_dtl desc	student_transcripts_tracking_1
SELECT Sections.sect_desc FROM Sections WHERE Sections.sect_name = "h"	student_transcripts_tracking_1
SELECT Sections.sect_desc FROM Sections WHERE Sections.sect_name = "h"	student_transcripts_tracking_1
SELECT Students.first_name FROM Students JOIN Addresses ON Students.pa_id = Addresses.adr_id WHERE Addresses.cntry = "haiti" or Students.cell = "09700166582"	student_transcripts_tracking_1
SELECT Students.first_name FROM Students JOIN Addresses ON Students.pa_id = Addresses.adr_id WHERE Addresses.cntry = "haiti" or Students.cell = "09700166582"	student_transcripts_tracking_1
SELECT Courses.crs_desc FROM Courses WHERE Courses.course_name = "math"	student_transcripts_tracking_2
SELECT Courses.crs_desc FROM Courses WHERE Courses.course_name = "math"	student_transcripts_tracking_2
SELECT Addresses.zipcode FROM Addresses WHERE Addresses.city = "Port Chelsea"	student_transcripts_tracking_2
SELECT Addresses.zipcode FROM Addresses WHERE Addresses.city = "Port Chelsea"	student_transcripts_tracking_2
SELECT Departments.dept_name , Degree_Programs.department_id FROM Degree_Programs JOIN Departments ON Degree_Programs.department_id = Departments.dept_id GROUP BY Degree_Programs.department_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Departments.dept_name , Degree_Programs.department_id FROM Degree_Programs JOIN Departments ON Degree_Programs.department_id = Departments.dept_id GROUP BY Degree_Programs.department_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_2
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_2
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.dept_id = Degree_Programs.department_id WHERE Departments.dept_name = "engineer"	student_transcripts_tracking_2
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.dept_id = Degree_Programs.department_id WHERE Departments.dept_name = "engineer"	student_transcripts_tracking_2
SELECT Sections.section_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_2
SELECT Sections.section_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_2
SELECT Courses.course_name , Courses.crs_id FROM Courses JOIN Sections ON Courses.crs_id = Sections.crs_id GROUP BY Courses.crs_id HAVING count(*) <= 2	student_transcripts_tracking_2
SELECT Courses.course_name , Courses.crs_id FROM Courses JOIN Sections ON Courses.crs_id = Sections.crs_id GROUP BY Courses.crs_id HAVING count(*) <= 2	student_transcripts_tracking_2
SELECT Semesters.semester_name , Semesters.sem_id FROM Semesters JOIN Student_Enrolment ON Semesters.sem_id = Student_Enrolment.semester_id GROUP BY Semesters.sem_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Semesters.semester_name , Semesters.sem_id FROM Semesters JOIN Student_Enrolment ON Semesters.sem_id = Student_Enrolment.semester_id GROUP BY Semesters.sem_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Departments.department_description FROM Departments WHERE Departments.dept_name like "%computer%"	student_transcripts_tracking_2
SELECT Departments.department_description FROM Departments WHERE Departments.dept_name like "%computer%"	student_transcripts_tracking_2
SELECT Students.first_name , Students.middle_name , Students.last_name , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid HAVING count(*) = 2	student_transcripts_tracking_2
SELECT Students.first_name , Students.middle_name , Students.last_name , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid HAVING count(*) = 2	student_transcripts_tracking_2
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_2
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_2
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Students.stuid , Students.first_name , Students.middle_name , Students.last_name , count(*) , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Students.stuid , Students.first_name , Students.middle_name , Students.last_name , count(*) , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Semesters.semester_name FROM Semesters WHERE Semesters.sem_id NOT in (SELECT Student_Enrolment.semester_id FROM Student_Enrolment)	student_transcripts_tracking_2
SELECT Semesters.semester_name FROM Semesters WHERE Semesters.sem_id NOT in (SELECT Student_Enrolment.semester_id FROM Student_Enrolment)	student_transcripts_tracking_2
SELECT DISTINCT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.crs_id	student_transcripts_tracking_2
SELECT DISTINCT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.crs_id	student_transcripts_tracking_2
SELECT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.crs_id GROUP BY Courses.course_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Courses.course_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.crs_id GROUP BY Courses.course_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id	student_transcripts_tracking_2
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id	student_transcripts_tracking_2
SELECT Students.cell FROM Students WHERE Students.first_name = "Timmothy" and Students.last_name = "Ward"	student_transcripts_tracking_2
SELECT Students.cell FROM Students WHERE Students.first_name = "timmothy" and Students.last_name = "ward"	student_transcripts_tracking_2
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.pa_id	student_transcripts_tracking_2
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.pa_id	student_transcripts_tracking_2
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT count(*) , Transcript_Contents.stu_crs_id FROM Transcript_Contents GROUP BY Transcript_Contents.stu_crs_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT count(*) , Transcript_Contents.stu_crs_id FROM Transcript_Contents GROUP BY Transcript_Contents.stu_crs_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_2
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_2
SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.semester_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_2
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_2
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_2
SELECT Students.oth_stu_dtl FROM Students ORDER BY Students.oth_stu_dtl desc	student_transcripts_tracking_2
SELECT Students.oth_stu_dtl FROM Students ORDER BY Students.oth_stu_dtl desc	student_transcripts_tracking_2
SELECT Sections.sect_desc FROM Sections WHERE Sections.section_name = "h"	student_transcripts_tracking_2
SELECT Sections.sect_desc FROM Sections WHERE Sections.section_name = "h"	student_transcripts_tracking_2
SELECT Students.first_name FROM Students JOIN Addresses ON Students.pa_id = Addresses.adr_id WHERE Addresses.country = "haiti" or Students.cell = "09700166582"	student_transcripts_tracking_2
SELECT Students.first_name FROM Students JOIN Addresses ON Students.pa_id = Addresses.adr_id WHERE Addresses.country = "haiti" or Students.cell = "09700166582"	student_transcripts_tracking_2
SELECT Courses.crs_desc FROM Courses WHERE Courses.crs_name = "math"	student_transcripts_tracking_3
SELECT Courses.crs_desc FROM Courses WHERE Courses.crs_name = "math"	student_transcripts_tracking_3
SELECT Addresses.zipcode FROM Addresses WHERE Addresses.city = "Port Chelsea"	student_transcripts_tracking_3
SELECT Addresses.zipcode FROM Addresses WHERE Addresses.city = "Port Chelsea"	student_transcripts_tracking_3
SELECT Departments.dept_name , Degree_Programs.dept_id FROM Degree_Programs JOIN Departments ON Degree_Programs.dept_id = Departments.department_id GROUP BY Degree_Programs.dept_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Departments.dept_name , Degree_Programs.dept_id FROM Degree_Programs JOIN Departments ON Degree_Programs.dept_id = Departments.department_id GROUP BY Degree_Programs.dept_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT count(DISTINCT Degree_Programs.dept_id) FROM Degree_Programs	student_transcripts_tracking_3
SELECT count(DISTINCT Degree_Programs.dept_id) FROM Degree_Programs	student_transcripts_tracking_3
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_3
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_3
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.department_id = Degree_Programs.dept_id WHERE Departments.dept_name = "engineer"	student_transcripts_tracking_3
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.department_id = Degree_Programs.dept_id WHERE Departments.dept_name = "engineer"	student_transcripts_tracking_3
SELECT Sections.sect_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_3
SELECT Sections.sect_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_3
SELECT Courses.crs_name , Courses.crs_id FROM Courses JOIN Sections ON Courses.crs_id = Sections.crs_id GROUP BY Courses.crs_id HAVING count(*) <= 2	student_transcripts_tracking_3
SELECT Courses.crs_name , Courses.crs_id FROM Courses JOIN Sections ON Courses.crs_id = Sections.crs_id GROUP BY Courses.crs_id HAVING count(*) <= 2	student_transcripts_tracking_3
SELECT Sections.sect_name FROM Sections ORDER BY Sections.sect_name desc	student_transcripts_tracking_3
SELECT Sections.sect_name FROM Sections ORDER BY Sections.sect_name desc	student_transcripts_tracking_3
SELECT Semesters.sem_name , Semesters.sem_id FROM Semesters JOIN Student_Enrolment ON Semesters.sem_id = Student_Enrolment.sem_id GROUP BY Semesters.sem_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Semesters.sem_name , Semesters.sem_id FROM Semesters JOIN Student_Enrolment ON Semesters.sem_id = Student_Enrolment.sem_id GROUP BY Semesters.sem_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Departments.dept_desc FROM Departments WHERE Departments.dept_name like "%computer%"	student_transcripts_tracking_3
SELECT Departments.dept_desc FROM Departments WHERE Departments.dept_name like "%computer%"	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.last_name , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.student_id GROUP BY Students.stuid HAVING count(*) = 2	student_transcripts_tracking_3
SELECT Students.first_name , Students.middle_name , Students.last_name , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.student_id GROUP BY Students.stuid HAVING count(*) = 2	student_transcripts_tracking_3
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_3
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.student_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_3
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Students.stuid , Students.first_name , Students.middle_name , Students.last_name , count(*) , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.student_id GROUP BY Students.stuid ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Students.stuid , Students.first_name , Students.middle_name , Students.last_name , count(*) , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.student_id GROUP BY Students.stuid ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Semesters.sem_name FROM Semesters WHERE Semesters.sem_id NOT in (SELECT Student_Enrolment.sem_id FROM Student_Enrolment)	student_transcripts_tracking_3
SELECT Semesters.sem_name FROM Semesters WHERE Semesters.sem_id NOT in (SELECT Student_Enrolment.sem_id FROM Student_Enrolment)	student_transcripts_tracking_3
SELECT DISTINCT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.course_id	student_transcripts_tracking_3
SELECT DISTINCT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.course_id	student_transcripts_tracking_3
SELECT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.course_id GROUP BY Courses.crs_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Courses.crs_name FROM Courses JOIN Student_Enrolment_Courses ON Courses.crs_id = Student_Enrolment_Courses.course_id GROUP BY Courses.crs_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.student_id	student_transcripts_tracking_3
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.student_id	student_transcripts_tracking_3
SELECT Students.cell FROM Students WHERE Students.first_name = "Timmothy" and Students.last_name = "Ward"	student_transcripts_tracking_3
SELECT Students.cell FROM Students WHERE Students.first_name = "timmothy" and Students.last_name = "ward"	student_transcripts_tracking_3
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.pa_id	student_transcripts_tracking_3
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.pa_id	student_transcripts_tracking_3
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT Transcripts.transcript_date , Transcripts.oth_dtl FROM Transcripts ORDER BY Transcripts.transcript_date asc LIMIT 1	student_transcripts_tracking_3
SELECT Transcripts.transcript_date , Transcripts.oth_dtl FROM Transcripts ORDER BY Transcripts.transcript_date asc LIMIT 1	student_transcripts_tracking_3
SELECT count(*) , Transcript_Contents.stu_crs_id FROM Transcript_Contents GROUP BY Transcript_Contents.stu_crs_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT count(*) , Transcript_Contents.stu_crs_id FROM Transcript_Contents GROUP BY Transcript_Contents.stu_crs_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_3
SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_3
SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_3
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_3
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_3
SELECT Students.oth_stu_dtl FROM Students ORDER BY Students.oth_stu_dtl desc	student_transcripts_tracking_3
SELECT Students.oth_stu_dtl FROM Students ORDER BY Students.oth_stu_dtl desc	student_transcripts_tracking_3
SELECT Sections.sect_desc FROM Sections WHERE Sections.sect_name = "h"	student_transcripts_tracking_3
SELECT Sections.sect_desc FROM Sections WHERE Sections.sect_name = "h"	student_transcripts_tracking_3
SELECT Students.first_name FROM Students JOIN Addresses ON Students.pa_id = Addresses.adr_id WHERE Addresses.cntry = "haiti" or Students.cell = "09700166582"	student_transcripts_tracking_3
SELECT Students.first_name FROM Students JOIN Addresses ON Students.pa_id = Addresses.adr_id WHERE Addresses.cntry = "haiti" or Students.cell = "09700166582"	student_transcripts_tracking_3
SELECT Departments.department_name , Degree_Programs.dept_id FROM Degree_Programs JOIN Departments ON Degree_Programs.dept_id = Departments.dept_id GROUP BY Degree_Programs.dept_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Departments.department_name , Degree_Programs.dept_id FROM Degree_Programs JOIN Departments ON Degree_Programs.dept_id = Departments.dept_id GROUP BY Degree_Programs.dept_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT count(DISTINCT Degree_Programs.dept_id) FROM Degree_Programs	student_transcripts_tracking_4
SELECT count(DISTINCT Degree_Programs.dept_id) FROM Degree_Programs	student_transcripts_tracking_4
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_4
SELECT count(DISTINCT Degree_Programs.degree_smry_name) FROM Degree_Programs	student_transcripts_tracking_4
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.dept_id = Degree_Programs.dept_id WHERE Departments.department_name = "engineer"	student_transcripts_tracking_4
SELECT count(*) FROM Departments JOIN Degree_Programs ON Departments.dept_id = Degree_Programs.dept_id WHERE Departments.department_name = "engineer"	student_transcripts_tracking_4
SELECT Sections.section_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_4
SELECT Sections.section_name , Sections.sect_desc FROM Sections	student_transcripts_tracking_4
SELECT Courses.course_name , Courses.course_id FROM Courses JOIN Sections ON Courses.course_id = Sections.crs_id GROUP BY Courses.course_id HAVING count(*) <= 2	student_transcripts_tracking_4
SELECT Courses.course_name , Courses.course_id FROM Courses JOIN Sections ON Courses.course_id = Sections.crs_id GROUP BY Courses.course_id HAVING count(*) <= 2	student_transcripts_tracking_4
SELECT Semesters.sem_name , Semesters.sem_id FROM Semesters JOIN Student_Enrolment ON Semesters.sem_id = Student_Enrolment.sem_id GROUP BY Semesters.sem_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Semesters.sem_name , Semesters.sem_id FROM Semesters JOIN Student_Enrolment ON Semesters.sem_id = Student_Enrolment.sem_id GROUP BY Semesters.sem_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Departments.dept_desc FROM Departments WHERE Departments.department_name like "%computer%"	student_transcripts_tracking_4
SELECT Departments.dept_desc FROM Departments WHERE Departments.department_name like "%computer%"	student_transcripts_tracking_4
SELECT Students.first_name , Students.middle_name , Students.last_name , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid HAVING count(*) = 2	student_transcripts_tracking_4
SELECT Students.first_name , Students.middle_name , Students.last_name , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid HAVING count(*) = 2	student_transcripts_tracking_4
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_4
SELECT DISTINCT Students.first_name , Students.middle_name , Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id JOIN Degree_Programs ON Student_Enrolment.degree_program_id = Degree_Programs.degree_pmg_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_4
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_smry_name ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Degree_Programs.degree_pmg_id , Degree_Programs.degree_smry_name FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id GROUP BY Degree_Programs.degree_pmg_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Students.stuid , Students.first_name , Students.middle_name , Students.last_name , count(*) , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Students.stuid , Students.first_name , Students.middle_name , Students.last_name , count(*) , Students.stuid FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id GROUP BY Students.stuid ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Semesters.sem_name FROM Semesters WHERE Semesters.sem_id NOT in (SELECT Student_Enrolment.sem_id FROM Student_Enrolment)	student_transcripts_tracking_4
SELECT Semesters.sem_name FROM Semesters WHERE Semesters.sem_id NOT in (SELECT Student_Enrolment.sem_id FROM Student_Enrolment)	student_transcripts_tracking_4
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id	student_transcripts_tracking_4
SELECT Students.last_name FROM Students JOIN Addresses ON Students.ca_id = Addresses.adr_id WHERE Addresses.state_province_county = "NorthCarolina" EXCEPT SELECT DISTINCT Students.last_name FROM Students JOIN Student_Enrolment ON Students.stuid = Student_Enrolment.stu_id	student_transcripts_tracking_4
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.pa_id	student_transcripts_tracking_4
SELECT Students.first_name FROM Students WHERE Students.ca_id != Students.pa_id	student_transcripts_tracking_4
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Addresses.adr_id , Addresses.line_1 , Addresses.line_2 FROM Addresses JOIN Students ON Addresses.adr_id = Students.ca_id GROUP BY Addresses.adr_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.transcript_date , Transcripts.oth_dtl FROM Transcripts ORDER BY Transcripts.transcript_date asc LIMIT 1	student_transcripts_tracking_4
SELECT Transcripts.transcript_date , Transcripts.oth_dtl FROM Transcripts ORDER BY Transcripts.transcript_date asc LIMIT 1	student_transcripts_tracking_4
SELECT count(*) , Transcript_Contents.stu_crs_id FROM Transcript_Contents GROUP BY Transcript_Contents.stu_crs_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT count(*) , Transcript_Contents.stu_crs_id FROM Transcript_Contents GROUP BY Transcript_Contents.stu_crs_id ORDER BY count(*) desc LIMIT 1	student_transcripts_tracking_4
SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_4
SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Master" INTERSECT SELECT DISTINCT Student_Enrolment.sem_id FROM Degree_Programs JOIN Student_Enrolment ON Degree_Programs.degree_pmg_id = Student_Enrolment.degree_program_id WHERE Degree_Programs.degree_smry_name = "Bachelor"	student_transcripts_tracking_4
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_4
SELECT count(DISTINCT Students.ca_id) FROM Students	student_transcripts_tracking_4
SELECT Sections.sect_desc FROM Sections WHERE Sections.section_name = "h"	student_transcripts_tracking_4
SELECT Sections.sect_desc FROM Sections WHERE Sections.section_name = "h"	student_transcripts_tracking_4
SELECT Students.first_name FROM Students JOIN Addresses ON Students.pa_id = Addresses.adr_id WHERE Addresses.cntry = "haiti" or Students.cell_mobile_number = "09700166582"	student_transcripts_tracking_4
SELECT Students.first_name FROM Students JOIN Addresses ON Students.pa_id = Addresses.adr_id WHERE Addresses.cntry = "haiti" or Students.cell_mobile_number = "09700166582"	student_transcripts_tracking_4
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_0
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_0
SELECT count(*) FROM Cartoon WHERE Cartoon.wr = "Joseph Kuhr"	tvshow_0
SELECT count(*) FROM Cartoon WHERE Cartoon.wr = "Joseph Kuhr"	tvshow_0
SELECT Cartoon.Title , Cartoon.dir FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_0
SELECT Cartoon.Title , Cartoon.dir FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_0
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones" or Cartoon.dir = "Brandon Vietti"	tvshow_0
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones" or Cartoon.dir = "Brandon Vietti"	tvshow_0
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_0
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_0
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.cont) FROM TV_Channel	tvshow_0
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.cont) FROM TV_Channel	tvshow_0
SELECT TV_Channel.cont FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_0
SELECT TV_Channel.cont FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_0
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_0
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_0
SELECT count(*) FROM TV_Channel WHERE TV_Channel.lang = "English"	tvshow_0
SELECT count(*) FROM TV_Channel WHERE TV_Channel.lang = "English"	tvshow_0
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang ORDER BY count(*) asc LIMIT 1	tvshow_0
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang ORDER BY count(*) asc LIMIT 1	tvshow_0
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang	tvshow_0
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang	tvshow_0
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_0
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_0
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_0
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_0
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.rtg asc	tvshow_0
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.rtg asc	tvshow_0
SELECT TV_series.ep , TV_series.rtg FROM TV_series ORDER BY TV_series.rtg desc LIMIT 3	tvshow_0
SELECT TV_series.ep , TV_series.rtg FROM TV_series ORDER BY TV_series.rtg desc LIMIT 3	tvshow_0
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_0
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_0
SELECT TV_series.wkly_rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_0
SELECT TV_series.wkly_rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_0
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_0
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_0
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_0
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_0
SELECT count(*) , Cartoon.dir FROM Cartoon GROUP BY Cartoon.dir	tvshow_0
SELECT count(*) , Cartoon.dir FROM Cartoon GROUP BY Cartoon.dir	tvshow_0
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_0
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_0
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_0
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_0
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_0
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_0
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_0
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_0
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Ben Jones"	tvshow_0
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Ben Jones"	tvshow_0
SELECT TV_Channel.par , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.lang != "English"	tvshow_0
SELECT TV_Channel.par , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.lang != "English"	tvshow_0
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_0
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_0
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_0
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_0
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones")	tvshow_0
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones")	tvshow_0
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_1
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_1
SELECT Cartoon.Title , Cartoon.dir FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_1
SELECT Cartoon.Title , Cartoon.dir FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_1
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones" or Cartoon.dir = "Brandon Vietti"	tvshow_1
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones" or Cartoon.dir = "Brandon Vietti"	tvshow_1
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_1
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_1
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.cont) FROM TV_Channel	tvshow_1
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.cont) FROM TV_Channel	tvshow_1
SELECT TV_Channel.cont FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_1
SELECT TV_Channel.cont FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_1
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_1
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_1
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_1
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_1
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_1
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_1
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.rtg asc	tvshow_1
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.rtg asc	tvshow_1
SELECT TV_series.ep , TV_series.rtg FROM TV_series ORDER BY TV_series.rtg desc LIMIT 3	tvshow_1
SELECT TV_series.ep , TV_series.rtg FROM TV_series ORDER BY TV_series.rtg desc LIMIT 3	tvshow_1
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_1
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_1
SELECT TV_series.Weekly_Rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_1
SELECT TV_series.Weekly_Rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_1
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_1
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_1
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_1
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_1
SELECT count(*) , Cartoon.dir FROM Cartoon GROUP BY Cartoon.dir	tvshow_1
SELECT count(*) , Cartoon.dir FROM Cartoon GROUP BY Cartoon.dir	tvshow_1
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_1
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_1
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_1
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_1
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Written_by = "Todd Casey"	tvshow_1
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Written_by = "Todd Casey"	tvshow_1
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Written_by = "Todd Casey"	tvshow_1
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Written_by = "Todd Casey"	tvshow_1
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Ben Jones"	tvshow_1
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Ben Jones"	tvshow_1
SELECT TV_Channel.par , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.Language != "English"	tvshow_1
SELECT TV_Channel.par , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.Language != "English"	tvshow_1
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_1
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_1
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_1
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_1
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones")	tvshow_1
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones")	tvshow_1
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_3
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_3
SELECT count(*) FROM Cartoon WHERE Cartoon.wr = "Joseph Kuhr"	tvshow_3
SELECT count(*) FROM Cartoon WHERE Cartoon.wr = "Joseph Kuhr"	tvshow_3
SELECT Cartoon.Title , Cartoon.dir FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_3
SELECT Cartoon.Title , Cartoon.dir FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_3
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones" or Cartoon.dir = "Brandon Vietti"	tvshow_3
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones" or Cartoon.dir = "Brandon Vietti"	tvshow_3
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_3
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_3
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.Content) FROM TV_Channel	tvshow_3
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.Content) FROM TV_Channel	tvshow_3
SELECT TV_Channel.Content FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_3
SELECT TV_Channel.Content FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_3
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_3
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_3
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_3
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_3
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_3
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_3
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.Rating asc	tvshow_3
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.Rating asc	tvshow_3
SELECT TV_series.ep , TV_series.Rating FROM TV_series ORDER BY TV_series.Rating desc LIMIT 3	tvshow_3
SELECT TV_series.ep , TV_series.Rating FROM TV_series ORDER BY TV_series.Rating desc LIMIT 3	tvshow_3
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_3
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_3
SELECT TV_series.Weekly_Rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_3
SELECT TV_series.Weekly_Rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_3
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_3
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_3
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_3
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_3
SELECT count(*) , Cartoon.dir FROM Cartoon GROUP BY Cartoon.dir	tvshow_3
SELECT count(*) , Cartoon.dir FROM Cartoon GROUP BY Cartoon.dir	tvshow_3
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_3
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_3
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_3
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_3
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_3
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_3
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_3
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_3
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Ben Jones"	tvshow_3
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Ben Jones"	tvshow_3
SELECT TV_Channel.par , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.Language != "English"	tvshow_3
SELECT TV_Channel.par , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.Language != "English"	tvshow_3
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_3
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_3
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_3
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_3
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones")	tvshow_3
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones")	tvshow_3
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_4
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_4
SELECT count(*) FROM Cartoon WHERE Cartoon.wr = "Joseph Kuhr"	tvshow_4
SELECT count(*) FROM Cartoon WHERE Cartoon.wr = "Joseph Kuhr"	tvshow_4
SELECT Cartoon.Title , Cartoon.dir FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_4
SELECT Cartoon.Title , Cartoon.dir FROM Cartoon ORDER BY Cartoon.Original_air_date asc	tvshow_4
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones" or Cartoon.dir = "Brandon Vietti"	tvshow_4
SELECT Cartoon.Title FROM Cartoon WHERE Cartoon.dir = "Ben Jones" or Cartoon.dir = "Brandon Vietti"	tvshow_4
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_4
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_4
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.Content) FROM TV_Channel	tvshow_4
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.Content) FROM TV_Channel	tvshow_4
SELECT TV_Channel.Content FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_4
SELECT TV_Channel.Content FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_4
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_4
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_4
SELECT count(*) FROM TV_Channel WHERE TV_Channel.lang = "English"	tvshow_4
SELECT count(*) FROM TV_Channel WHERE TV_Channel.lang = "English"	tvshow_4
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang ORDER BY count(*) asc LIMIT 1	tvshow_4
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang ORDER BY count(*) asc LIMIT 1	tvshow_4
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang	tvshow_4
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang	tvshow_4
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_4
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_4
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_4
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_4
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.rtg asc	tvshow_4
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.rtg asc	tvshow_4
SELECT TV_series.ep , TV_series.rtg FROM TV_series ORDER BY TV_series.rtg desc LIMIT 3	tvshow_4
SELECT TV_series.ep , TV_series.rtg FROM TV_series ORDER BY TV_series.rtg desc LIMIT 3	tvshow_4
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_4
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_4
SELECT TV_series.wkly_rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_4
SELECT TV_series.wkly_rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_4
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_4
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_4
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_4
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_4
SELECT count(*) , Cartoon.dir FROM Cartoon GROUP BY Cartoon.dir	tvshow_4
SELECT count(*) , Cartoon.dir FROM Cartoon GROUP BY Cartoon.dir	tvshow_4
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_4
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_4
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_4
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_4
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_4
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_4
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_4
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_4
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Ben Jones"	tvshow_4
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.dir = "Ben Jones"	tvshow_4
SELECT TV_Channel.Pixel_aspect_ratio_PAR , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.lang != "English"	tvshow_4
SELECT TV_Channel.Pixel_aspect_ratio_PAR , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.lang != "English"	tvshow_4
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_4
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_4
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_4
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones"	tvshow_4
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones")	tvshow_4
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.dir = "Ben Jones")	tvshow_4
SELECT count(*) FROM Cartoon WHERE Cartoon.wr = "Joseph Kuhr"	tvshow_5
SELECT count(*) FROM Cartoon WHERE Cartoon.wr = "Joseph Kuhr"	tvshow_5
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_5
SELECT TV_Channel.cntry , count(*) FROM TV_Channel GROUP BY TV_Channel.cntry ORDER BY count(*) desc LIMIT 1	tvshow_5
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.cont) FROM TV_Channel	tvshow_5
SELECT count(DISTINCT TV_Channel.ser_name) , count(DISTINCT TV_Channel.cont) FROM TV_Channel	tvshow_5
SELECT TV_Channel.cont FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_5
SELECT TV_Channel.cont FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_5
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_5
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_5
SELECT count(*) FROM TV_Channel WHERE TV_Channel.lang = "English"	tvshow_5
SELECT count(*) FROM TV_Channel WHERE TV_Channel.lang = "English"	tvshow_5
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang ORDER BY count(*) asc LIMIT 1	tvshow_5
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang ORDER BY count(*) asc LIMIT 1	tvshow_5
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang	tvshow_5
SELECT TV_Channel.lang , count(*) FROM TV_Channel GROUP BY TV_Channel.lang	tvshow_5
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_5
SELECT TV_Channel.ser_name FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Title = "The Rise of the Blue Beetle!"	tvshow_5
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_5
SELECT Cartoon.Title FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_5
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.rtg asc	tvshow_5
SELECT TV_series.ep FROM TV_series ORDER BY TV_series.rtg asc	tvshow_5
SELECT TV_series.ep , TV_series.rtg FROM TV_series ORDER BY TV_series.rtg desc LIMIT 3	tvshow_5
SELECT TV_series.ep , TV_series.rtg FROM TV_series ORDER BY TV_series.rtg desc LIMIT 3	tvshow_5
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_5
SELECT TV_series.Air_Date FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_5
SELECT TV_series.Weekly_Rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_5
SELECT TV_series.Weekly_Rank FROM TV_series WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_5
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_5
SELECT TV_Channel.ser_name FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_series.ep = "A Love of a Lifetime"	tvshow_5
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_5
SELECT TV_series.ep FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.chnl WHERE TV_Channel.ser_name = "Sky Radio"	tvshow_5
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_5
SELECT Cartoon.prod_code , Cartoon.chnl FROM Cartoon ORDER BY Cartoon.Original_air_date desc LIMIT 1	tvshow_5
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_5
SELECT TV_Channel.Package_Option , TV_Channel.ser_name FROM TV_Channel WHERE TV_Channel.hd = "yes"	tvshow_5
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_5
SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_5
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_5
SELECT TV_Channel.cntry FROM TV_Channel EXCEPT SELECT TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.wr = "Todd Casey"	tvshow_5
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Directed_by = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_5
SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Directed_by = "Michael Chang" INTERSECT SELECT TV_Channel.ser_name , TV_Channel.cntry FROM TV_Channel JOIN Cartoon ON TV_Channel.id = Cartoon.chnl WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_5
SELECT TV_Channel.Pixel_aspect_ratio_PAR , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.lang != "English"	tvshow_5
SELECT TV_Channel.Pixel_aspect_ratio_PAR , TV_Channel.cntry FROM TV_Channel WHERE TV_Channel.lang != "English"	tvshow_5
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_5
SELECT TV_Channel.id FROM TV_Channel GROUP BY TV_Channel.cntry HAVING count(*) > 2	tvshow_5
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_5
SELECT TV_Channel.id FROM TV_Channel EXCEPT SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones"	tvshow_5
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones")	tvshow_5
SELECT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT in (SELECT Cartoon.chnl FROM Cartoon WHERE Cartoon.Directed_by = "Ben Jones")	tvshow_5
SELECT poker_player.Final_Table_Made , poker_player.best_fin FROM poker_player	poker_player_0
SELECT poker_player.Final_Table_Made , poker_player.best_fin FROM poker_player	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE poker_player.Earnings > 300000	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE poker_player.Earnings > 300000	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Final_Table_Made asc	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Final_Table_Made asc	poker_player_0
SELECT people.dob FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_0
SELECT people.dob FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_0
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY people.Height desc LIMIT 1	poker_player_0
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY people.Height desc LIMIT 1	poker_player_0
SELECT avg(poker_player.Earnings) FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE people.Height > 200	poker_player_0
SELECT avg(poker_player.Earnings) FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE people.Height > 200	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings desc	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings desc	poker_player_0
SELECT people.Name , people.dob FROM people ORDER BY people.Name asc	poker_player_0
SELECT people.Name , people.dob FROM people ORDER BY people.Name asc	poker_player_0
SELECT people.Name FROM people WHERE people.ppl_id NOT in (SELECT poker_player.ppl_id FROM poker_player)	poker_player_0
SELECT people.Name FROM people WHERE people.ppl_id NOT in (SELECT poker_player.ppl_id FROM poker_player)	poker_player_0
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID WHERE poker_player.Earnings > 300000	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID WHERE poker_player.Earnings > 300000	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID ORDER BY poker_player.Final_Table_Made asc	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID ORDER BY poker_player.Final_Table_Made asc	poker_player_1
SELECT people.Birth_Date FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_1
SELECT people.Birth_Date FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_1
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_1
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID ORDER BY people.Height desc LIMIT 1	poker_player_1
SELECT avg(poker_player.Earnings) FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID WHERE people.Height > 200	poker_player_1
SELECT avg(poker_player.Earnings) FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID WHERE people.Height > 200	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID ORDER BY poker_player.Earnings desc	poker_player_1
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.People_ID ORDER BY poker_player.Earnings desc	poker_player_1
SELECT people.nal , count(*) FROM people GROUP BY people.nal	poker_player_1
SELECT people.nal , count(*) FROM people GROUP BY people.nal	poker_player_1
SELECT people.nal FROM people GROUP BY people.nal ORDER BY count(*) desc LIMIT 1	poker_player_1
SELECT people.nal FROM people GROUP BY people.nal ORDER BY count(*) desc LIMIT 1	poker_player_1
SELECT people.nal FROM people GROUP BY people.nal HAVING count(*) >= 2	poker_player_1
SELECT people.nal FROM people GROUP BY people.nal HAVING count(*) >= 2	poker_player_1
SELECT people.Name FROM people WHERE people.nal != "Russia"	poker_player_1
SELECT people.Name FROM people WHERE people.nal != "Russia"	poker_player_1
SELECT people.Name FROM people WHERE people.ppl_id NOT in (SELECT poker_player.People_ID FROM poker_player)	poker_player_1
SELECT people.Name FROM people WHERE people.ppl_id NOT in (SELECT poker_player.People_ID FROM poker_player)	poker_player_1
SELECT count(DISTINCT people.nal) FROM people	poker_player_1
SELECT count(DISTINCT people.nal) FROM people	poker_player_1
SELECT poker_player.earn FROM poker_player ORDER BY poker_player.earn desc	poker_player_2
SELECT poker_player.earn FROM poker_player ORDER BY poker_player.earn desc	poker_player_2
SELECT poker_player.Final_Table_Made , poker_player.best_fin FROM poker_player	poker_player_2
SELECT poker_player.Final_Table_Made , poker_player.best_fin FROM poker_player	poker_player_2
SELECT avg(poker_player.earn) FROM poker_player	poker_player_2
SELECT avg(poker_player.earn) FROM poker_player	poker_player_2
SELECT poker_player.Money_Rank FROM poker_player ORDER BY poker_player.earn desc LIMIT 1	poker_player_2
SELECT poker_player.Money_Rank FROM poker_player ORDER BY poker_player.earn desc LIMIT 1	poker_player_2
SELECT max(poker_player.Final_Table_Made) FROM poker_player WHERE poker_player.earn < 200000	poker_player_2
SELECT max(poker_player.Final_Table_Made) FROM poker_player WHERE poker_player.earn < 200000	poker_player_2
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE poker_player.earn > 300000	poker_player_2
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE poker_player.earn > 300000	poker_player_2
SELECT people.Birth_Date FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.earn asc LIMIT 1	poker_player_2
SELECT people.Birth_Date FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.earn asc LIMIT 1	poker_player_2
SELECT avg(poker_player.earn) FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE people.Height > 200	poker_player_2
SELECT avg(poker_player.earn) FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID WHERE people.Height > 200	poker_player_2
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.earn desc	poker_player_2
SELECT people.Name FROM people JOIN poker_player ON people.People_ID = poker_player.People_ID ORDER BY poker_player.earn desc	poker_player_2
SELECT people.nal , count(*) FROM people GROUP BY people.nal	poker_player_2
SELECT people.nal , count(*) FROM people GROUP BY people.nal	poker_player_2
SELECT people.nal FROM people GROUP BY people.nal ORDER BY count(*) desc LIMIT 1	poker_player_2
SELECT people.nal FROM people GROUP BY people.nal ORDER BY count(*) desc LIMIT 1	poker_player_2
SELECT people.nal FROM people GROUP BY people.nal HAVING count(*) >= 2	poker_player_2
SELECT people.nal FROM people GROUP BY people.nal HAVING count(*) >= 2	poker_player_2
SELECT people.Name FROM people WHERE people.nal != "Russia"	poker_player_2
SELECT people.Name FROM people WHERE people.nal != "Russia"	poker_player_2
SELECT count(DISTINCT people.nal) FROM people	poker_player_2
SELECT count(DISTINCT people.nal) FROM people	poker_player_2
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id	poker_player_3
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id	poker_player_3
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE poker_player.Earnings > 300000	poker_player_3
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE poker_player.Earnings > 300000	poker_player_3
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Final_Table_Made asc	poker_player_3
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Final_Table_Made asc	poker_player_3
SELECT people.Birth_Date FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_3
SELECT people.Birth_Date FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_3
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY people.Height desc LIMIT 1	poker_player_3
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY people.Height desc LIMIT 1	poker_player_3
SELECT avg(poker_player.Earnings) FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE people.Height > 200	poker_player_3
SELECT avg(poker_player.Earnings) FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE people.Height > 200	poker_player_3
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings desc	poker_player_3
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings desc	poker_player_3
SELECT people.nal , count(*) FROM people GROUP BY people.nal	poker_player_3
SELECT people.nal , count(*) FROM people GROUP BY people.nal	poker_player_3
SELECT people.nal FROM people GROUP BY people.nal ORDER BY count(*) desc LIMIT 1	poker_player_3
SELECT people.nal FROM people GROUP BY people.nal ORDER BY count(*) desc LIMIT 1	poker_player_3
SELECT people.nal FROM people GROUP BY people.nal HAVING count(*) >= 2	poker_player_3
SELECT people.nal FROM people GROUP BY people.nal HAVING count(*) >= 2	poker_player_3
SELECT people.Name FROM people WHERE people.nal != "Russia"	poker_player_3
SELECT people.Name FROM people WHERE people.nal != "Russia"	poker_player_3
SELECT people.Name FROM people WHERE people.ppl_id NOT in (SELECT poker_player.ppl_id FROM poker_player)	poker_player_3
SELECT people.Name FROM people WHERE people.ppl_id NOT in (SELECT poker_player.ppl_id FROM poker_player)	poker_player_3
SELECT count(DISTINCT people.nal) FROM people	poker_player_3
SELECT count(DISTINCT people.nal) FROM people	poker_player_3
SELECT poker_player.ftm , poker_player.Best_Finish FROM poker_player	poker_player_4
SELECT poker_player.ftm , poker_player.Best_Finish FROM poker_player	poker_player_4
SELECT max(poker_player.ftm) FROM poker_player WHERE poker_player.Earnings < 200000	poker_player_4
SELECT max(poker_player.ftm) FROM poker_player WHERE poker_player.Earnings < 200000	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE poker_player.Earnings > 300000	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE poker_player.Earnings > 300000	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.ftm asc	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.ftm asc	poker_player_4
SELECT people.dob FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_4
SELECT people.dob FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings asc LIMIT 1	poker_player_4
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY people.ht desc LIMIT 1	poker_player_4
SELECT poker_player.Money_Rank FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY people.ht desc LIMIT 1	poker_player_4
SELECT avg(poker_player.Earnings) FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE people.ht > 200	poker_player_4
SELECT avg(poker_player.Earnings) FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id WHERE people.ht > 200	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings desc	poker_player_4
SELECT people.Name FROM people JOIN poker_player ON people.ppl_id = poker_player.ppl_id ORDER BY poker_player.Earnings desc	poker_player_4
SELECT people.nal , count(*) FROM people GROUP BY people.nal	poker_player_4
SELECT people.nal , count(*) FROM people GROUP BY people.nal	poker_player_4
SELECT people.nal FROM people GROUP BY people.nal ORDER BY count(*) desc LIMIT 1	poker_player_4
SELECT people.nal FROM people GROUP BY people.nal ORDER BY count(*) desc LIMIT 1	poker_player_4
SELECT people.nal FROM people GROUP BY people.nal HAVING count(*) >= 2	poker_player_4
SELECT people.nal FROM people GROUP BY people.nal HAVING count(*) >= 2	poker_player_4
SELECT people.Name , people.dob FROM people ORDER BY people.Name asc	poker_player_4
SELECT people.Name , people.dob FROM people ORDER BY people.Name asc	poker_player_4
SELECT people.Name FROM people WHERE people.nal != "Russia"	poker_player_4
SELECT people.Name FROM people WHERE people.nal != "Russia"	poker_player_4
SELECT people.Name FROM people WHERE people.ppl_id NOT in (SELECT poker_player.ppl_id FROM poker_player)	poker_player_4
SELECT people.Name FROM people WHERE people.ppl_id NOT in (SELECT poker_player.ppl_id FROM poker_player)	poker_player_4
SELECT count(DISTINCT people.nal) FROM people	poker_player_4
SELECT count(DISTINCT people.nal) FROM people	poker_player_4
SELECT CONTESTANTS.contestant_no , CONTESTANTS.name FROM CONTESTANTS ORDER BY CONTESTANTS.name desc	voter_1_0
SELECT VOTES.vote_id , VOTES.ph , VOTES.state FROM VOTES	voter_1_0
SELECT CONTESTANTS.name FROM CONTESTANTS WHERE CONTESTANTS.name != "Jessie Alloway"	voter_1_0
SELECT CONTESTANTS.contestant_no , CONTESTANTS.name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no GROUP BY CONTESTANTS.contestant_no HAVING count(*) >= 2	voter_1_0
SELECT CONTESTANTS.contestant_no , CONTESTANTS.name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no GROUP BY CONTESTANTS.contestant_no ORDER BY count(*) asc LIMIT 1	voter_1_0
SELECT count(*) FROM CONTESTANTS WHERE CONTESTANTS.contestant_no NOT in (SELECT VOTES.contestant_no FROM VOTES)	voter_1_0
SELECT VOTES.created , VOTES.state , VOTES.ph FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no WHERE CONTESTANTS.name = "Tabatha Gehling"	voter_1_0
SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.name = "Tabatha Gehling" INTERSECT SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no JOIN AREA_CODE_STATE ON VOTES.state = AREA_CODE_STATE.state WHERE CONTESTANTS.name = "Kelly Clauss"	voter_1_0
SELECT CONTESTANTS.name FROM CONTESTANTS WHERE CONTESTANTS.name like "%al%"	voter_1_0
SELECT CONTESTANTS.contestant_no , CONTESTANTS.contestant_name FROM CONTESTANTS ORDER BY CONTESTANTS.contestant_name desc	voter_1_1
SELECT VOTES.vote_id , VOTES.ph , VOTES.st FROM VOTES	voter_1_1
SELECT max(VOTES.created) FROM VOTES WHERE VOTES.st = "CA"	voter_1_1
SELECT DISTINCT VOTES.st , VOTES.created FROM VOTES	voter_1_1
SELECT CONTESTANTS.contestant_no , CONTESTANTS.contestant_name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no GROUP BY CONTESTANTS.contestant_no HAVING count(*) >= 2	voter_1_1
SELECT CONTESTANTS.contestant_no , CONTESTANTS.contestant_name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no GROUP BY CONTESTANTS.contestant_no ORDER BY count(*) asc LIMIT 1	voter_1_1
SELECT count(*) FROM VOTES WHERE VOTES.st = "NY" or VOTES.st = "CA"	voter_1_1
SELECT count(*) FROM CONTESTANTS WHERE CONTESTANTS.contestant_no NOT in (SELECT VOTES.contestant_no FROM VOTES)	voter_1_1
SELECT AREA_CODE_STATE.area_code FROM AREA_CODE_STATE JOIN VOTES ON AREA_CODE_STATE.state = VOTES.st GROUP BY AREA_CODE_STATE.area_code ORDER BY count(*) desc LIMIT 1	voter_1_1
SELECT VOTES.created , VOTES.st , VOTES.ph FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no WHERE CONTESTANTS.contestant_name = "Tabatha Gehling"	voter_1_1
SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no JOIN AREA_CODE_STATE ON VOTES.st = AREA_CODE_STATE.state WHERE CONTESTANTS.contestant_name = "Tabatha Gehling" INTERSECT SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no JOIN AREA_CODE_STATE ON VOTES.st = AREA_CODE_STATE.state WHERE CONTESTANTS.contestant_name = "Kelly Clauss"	voter_1_1
SELECT CONTESTANTS.contestant_number , CONTESTANTS.name FROM CONTESTANTS ORDER BY CONTESTANTS.name desc	voter_1_2
SELECT VOTES.vote_id , VOTES.ph , VOTES.st FROM VOTES	voter_1_2
SELECT max(VOTES.created) FROM VOTES WHERE VOTES.st = "CA"	voter_1_2
SELECT CONTESTANTS.name FROM CONTESTANTS WHERE CONTESTANTS.name != "Jessie Alloway"	voter_1_2
SELECT DISTINCT VOTES.st , VOTES.created FROM VOTES	voter_1_2
SELECT CONTESTANTS.contestant_number , CONTESTANTS.name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number HAVING count(*) >= 2	voter_1_2
SELECT CONTESTANTS.contestant_number , CONTESTANTS.name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number GROUP BY CONTESTANTS.contestant_number ORDER BY count(*) asc LIMIT 1	voter_1_2
SELECT count(*) FROM VOTES WHERE VOTES.st = "NY" or VOTES.st = "CA"	voter_1_2
SELECT AREA_CODE_STATE.area_code FROM AREA_CODE_STATE JOIN VOTES ON AREA_CODE_STATE.state = VOTES.st GROUP BY AREA_CODE_STATE.area_code ORDER BY count(*) desc LIMIT 1	voter_1_2
SELECT VOTES.created , VOTES.st , VOTES.ph FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number WHERE CONTESTANTS.name = "Tabatha Gehling"	voter_1_2
SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.st = AREA_CODE_STATE.state WHERE CONTESTANTS.name = "Tabatha Gehling" INTERSECT SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_number JOIN AREA_CODE_STATE ON VOTES.st = AREA_CODE_STATE.state WHERE CONTESTANTS.name = "Kelly Clauss"	voter_1_2
SELECT CONTESTANTS.name FROM CONTESTANTS WHERE CONTESTANTS.name like "%al%"	voter_1_2
SELECT CONTESTANTS.contestant_no , CONTESTANTS.name FROM CONTESTANTS ORDER BY CONTESTANTS.name desc	voter_1_3
SELECT VOTES.vote_id , VOTES.ph , VOTES.st FROM VOTES	voter_1_3
SELECT max(VOTES.created) FROM VOTES WHERE VOTES.st = "CA"	voter_1_3
SELECT CONTESTANTS.name FROM CONTESTANTS WHERE CONTESTANTS.name != "Jessie Alloway"	voter_1_3
SELECT DISTINCT VOTES.st , VOTES.created FROM VOTES	voter_1_3
SELECT CONTESTANTS.contestant_no , CONTESTANTS.name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no GROUP BY CONTESTANTS.contestant_no HAVING count(*) >= 2	voter_1_3
SELECT CONTESTANTS.contestant_no , CONTESTANTS.name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no GROUP BY CONTESTANTS.contestant_no ORDER BY count(*) asc LIMIT 1	voter_1_3
SELECT count(*) FROM VOTES WHERE VOTES.st = "NY" or VOTES.st = "CA"	voter_1_3
SELECT count(*) FROM CONTESTANTS WHERE CONTESTANTS.contestant_no NOT in (SELECT VOTES.contestant_no FROM VOTES)	voter_1_3
SELECT AREA_CODE_STATE.area_code FROM AREA_CODE_STATE JOIN VOTES ON AREA_CODE_STATE.state = VOTES.st GROUP BY AREA_CODE_STATE.area_code ORDER BY count(*) desc LIMIT 1	voter_1_3
SELECT VOTES.created , VOTES.st , VOTES.ph FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no WHERE CONTESTANTS.name = "Tabatha Gehling"	voter_1_3
SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no JOIN AREA_CODE_STATE ON VOTES.st = AREA_CODE_STATE.state WHERE CONTESTANTS.name = "Tabatha Gehling" INTERSECT SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_no = VOTES.contestant_no JOIN AREA_CODE_STATE ON VOTES.st = AREA_CODE_STATE.state WHERE CONTESTANTS.name = "Kelly Clauss"	voter_1_3
SELECT CONTESTANTS.name FROM CONTESTANTS WHERE CONTESTANTS.name like "%al%"	voter_1_3
SELECT VOTES.vote_id , VOTES.phone_number , VOTES.st FROM VOTES	voter_1_4
SELECT max(VOTES.created) FROM VOTES WHERE VOTES.st = "CA"	voter_1_4
SELECT DISTINCT VOTES.st , VOTES.created FROM VOTES	voter_1_4
SELECT CONTESTANTS.contestant_number , CONTESTANTS.contestant_name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_no GROUP BY CONTESTANTS.contestant_number HAVING count(*) >= 2	voter_1_4
SELECT CONTESTANTS.contestant_number , CONTESTANTS.contestant_name FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_no GROUP BY CONTESTANTS.contestant_number ORDER BY count(*) asc LIMIT 1	voter_1_4
SELECT count(*) FROM VOTES WHERE VOTES.st = "NY" or VOTES.st = "CA"	voter_1_4
SELECT count(*) FROM CONTESTANTS WHERE CONTESTANTS.contestant_number NOT in (SELECT VOTES.contestant_no FROM VOTES)	voter_1_4
SELECT AREA_CODE_STATE.area_code FROM AREA_CODE_STATE JOIN VOTES ON AREA_CODE_STATE.state = VOTES.st GROUP BY AREA_CODE_STATE.area_code ORDER BY count(*) desc LIMIT 1	voter_1_4
SELECT VOTES.created , VOTES.st , VOTES.phone_number FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_no WHERE CONTESTANTS.contestant_name = "Tabatha Gehling"	voter_1_4
SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_no JOIN AREA_CODE_STATE ON VOTES.st = AREA_CODE_STATE.state WHERE CONTESTANTS.contestant_name = "Tabatha Gehling" INTERSECT SELECT AREA_CODE_STATE.area_code FROM CONTESTANTS JOIN VOTES ON CONTESTANTS.contestant_number = VOTES.contestant_no JOIN AREA_CODE_STATE ON VOTES.st = AREA_CODE_STATE.state WHERE CONTESTANTS.contestant_name = "Kelly Clauss"	voter_1_4
SELECT count(*) FROM country WHERE country.gf = "Republic"	world_1_0
SELECT count(*) FROM country WHERE country.gf = "Republic"	world_1_0
SELECT sum(country.sa) FROM country WHERE country.Region = "Caribbean"	world_1_0
SELECT sum(country.sa) FROM country WHERE country.Region = "Caribbean"	world_1_0
SELECT country.cont FROM country WHERE country.Name = "Anguilla"	world_1_0
SELECT country.cont FROM country WHERE country.Name = "Anguilla"	world_1_0
SELECT country.Region FROM country JOIN city ON country.Code = city.cntry_code WHERE city.Name = "Kabul"	world_1_0
SELECT country.Region FROM country JOIN city ON country.Code = city.cntry_code WHERE city.Name = "Kabul"	world_1_0
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_0
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_0
SELECT country.popn , country.le FROM country WHERE country.Name = "Brazil"	world_1_0
SELECT country.popn , country.le FROM country WHERE country.Name = "Brazil"	world_1_0
SELECT country.popn , country.Region FROM country WHERE country.Name = "Angola"	world_1_0
SELECT country.popn , country.Region FROM country WHERE country.Name = "Angola"	world_1_0
SELECT avg(country.le) FROM country WHERE country.Region = "Central Africa"	world_1_0
SELECT avg(country.le) FROM country WHERE country.Region = "Central Africa"	world_1_0
SELECT country.Name FROM country WHERE country.cont = "Asia" ORDER BY country.le asc LIMIT 1	world_1_0
SELECT country.Name FROM country WHERE country.cont = "Asia" ORDER BY country.le asc LIMIT 1	world_1_0
SELECT sum(country.popn) , max(country.GNP) FROM country WHERE country.cont = "Asia"	world_1_0
SELECT sum(country.popn) , max(country.GNP) FROM country WHERE country.cont = "Asia"	world_1_0
SELECT avg(country.le) FROM country WHERE country.cont = "Africa" and country.gf = "Republic"	world_1_0
SELECT avg(country.le) FROM country WHERE country.cont = "Africa" and country.gf = "Republic"	world_1_0
SELECT sum(country.sa) FROM country WHERE country.cont = "Asia" or country.cont = "Europe"	world_1_0
SELECT sum(country.sa) FROM country WHERE country.cont = "Asia" or country.cont = "Europe"	world_1_0
SELECT sum(city.popn) FROM city WHERE city.dist = "Gelderland"	world_1_0
SELECT sum(city.popn) FROM city WHERE city.dist = "Gelderland"	world_1_0
SELECT avg(country.GNP) , sum(country.popn) FROM country WHERE country.gf = "US Territory"	world_1_0
SELECT avg(country.GNP) , sum(country.popn) FROM country WHERE country.gf = "US Territory"	world_1_0
SELECT count(DISTINCT countrylanguage.lang) FROM countrylanguage	world_1_0
SELECT count(DISTINCT countrylanguage.lang) FROM countrylanguage	world_1_0
SELECT count(DISTINCT country.gf) FROM country WHERE country.cont = "Africa"	world_1_0
SELECT count(DISTINCT country.gf) FROM country WHERE country.cont = "Africa"	world_1_0
SELECT count(countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba"	world_1_0
SELECT count(countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba"	world_1_0
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Afghanistan" and countrylanguage.ofcl = "T"	world_1_0
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Afghanistan" and countrylanguage.ofcl = "T"	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT country.cont FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.cont ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT country.cont FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.cont ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Dutch" )	world_1_0
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Dutch" )	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French"	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French"	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French" and countrylanguage.ofcl = "T"	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French" and countrylanguage.ofcl = "T"	world_1_0
SELECT count(DISTINCT country.cont) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Chinese"	world_1_0
SELECT count(DISTINCT country.cont) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Chinese"	world_1_0
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" or countrylanguage.lang = "Dutch"	world_1_0
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" or countrylanguage.lang = "Dutch"	world_1_0
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "english" and countrylanguage.ofcl = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "dutch" and countrylanguage.ofcl = "t"	world_1_0
SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Dutch" and countrylanguage.ofcl = "T"	world_1_0
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.cont = "Asia" GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.cont = "Asia" GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.gf = "Republic" GROUP BY countrylanguage.lang HAVING count(*) = 1	world_1_0
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.gf = "Republic" GROUP BY countrylanguage.lang HAVING count(*) = 1	world_1_0
SELECT city.Name , city.popn FROM city JOIN countrylanguage ON city.cntry_code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" ORDER BY city.popn desc LIMIT 1	world_1_0
SELECT city.Name , city.popn FROM city JOIN countrylanguage ON city.cntry_code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" ORDER BY city.popn desc LIMIT 1	world_1_0
SELECT country.Name , country.popn , country.le FROM country WHERE country.cont = "Asia" ORDER BY country.sa desc LIMIT 1	world_1_0
SELECT country.Name , country.popn , country.le FROM country WHERE country.cont = "Asia" ORDER BY country.sa desc LIMIT 1	world_1_0
SELECT avg(country.le) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T")	world_1_0
SELECT avg(country.le) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T")	world_1_0
SELECT sum(country.popn) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English")	world_1_0
SELECT sum(country.popn) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English")	world_1_0
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.hos = "Beatrix" and countrylanguage.ofcl = "T"	world_1_0
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.hos = "Beatrix" and countrylanguage.ofcl = "T"	world_1_0
SELECT count(DISTINCT countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.IndepYear < 1930 and countrylanguage.ofcl = "T"	world_1_0
SELECT count(DISTINCT countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.IndepYear < 1930 and countrylanguage.ofcl = "T"	world_1_0
SELECT country.Name FROM country WHERE country.sa > (SELECT min(country.sa) FROM country WHERE country.cont = "Europe")	world_1_0
SELECT country.Name FROM country WHERE country.sa > (SELECT min(country.sa) FROM country WHERE country.cont = "Europe")	world_1_0
SELECT country.Name FROM country WHERE country.cont = "Africa" and country.popn < (SELECT max(country.popn) FROM country WHERE country.cont = "Asia")	world_1_0
SELECT country.Name FROM country WHERE country.cont = "Africa" and country.popn < (SELECT min(country.popn) FROM country WHERE country.cont = "Asia")	world_1_0
SELECT country.Name FROM country WHERE country.cont = "Asia" and country.popn > (SELECT max(country.popn) FROM country WHERE country.cont = "Africa")	world_1_0
SELECT country.Name FROM country WHERE country.cont = "Asia" and country.popn > (SELECT min(country.popn) FROM country WHERE country.cont = "Africa")	world_1_0
SELECT countrylanguage.cntry_code FROM countrylanguage EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_0
SELECT countrylanguage.cntry_code FROM countrylanguage EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_0
SELECT DISTINCT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang != "English"	world_1_0
SELECT DISTINCT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang != "English"	world_1_0
SELECT country.Code FROM country WHERE country.gf != "Republic" EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_0
SELECT country.Code FROM country WHERE country.gf != "Republic" EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_0
SELECT DISTINCT city.Name FROM country JOIN city ON city.cntry_code = country.Code WHERE country.cont = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.ofcl = "T" and countrylanguage.lang = "English")	world_1_0
SELECT DISTINCT city.Name FROM country JOIN city ON city.cntry_code = country.Code WHERE country.cont = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.ofcl = "T" and countrylanguage.lang = "English")	world_1_0
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code JOIN city ON country.Code = city.cntry_code WHERE countrylanguage.ofcl = "t" and countrylanguage.lang = "chinese" and country.cont = "asia"	world_1_0
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code JOIN city ON country.Code = city.cntry_code WHERE countrylanguage.ofcl = "T" and countrylanguage.lang = "Chinese" and country.cont = "Asia"	world_1_0
SELECT country.Name , country.sa , country.IndepYear FROM country ORDER BY country.popn asc LIMIT 1	world_1_0
SELECT country.Name , country.sa , country.IndepYear FROM country ORDER BY country.popn asc LIMIT 1	world_1_0
SELECT country.Name , country.popn , country.hos FROM country ORDER BY country.sa desc LIMIT 1	world_1_0
SELECT country.Name , country.popn , country.hos FROM country ORDER BY country.sa desc LIMIT 1	world_1_0
SELECT count(countrylanguage.lang) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name HAVING count(*) > 2	world_1_0
SELECT count(countrylanguage.lang) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name HAVING count(*) > 2	world_1_0
SELECT count(*) , city.dist FROM city WHERE city.popn > (SELECT avg(city.popn) FROM city) GROUP BY city.dist	world_1_0
SELECT count(*) , city.dist FROM city WHERE city.popn > (SELECT avg(city.popn) FROM city) GROUP BY city.dist	world_1_0
SELECT sum(country.popn) , country.gf FROM country GROUP BY country.gf HAVING avg(country.le) > 72	world_1_0
SELECT sum(country.popn) , country.gf FROM country GROUP BY country.gf HAVING avg(country.le) > 72	world_1_0
SELECT sum(country.popn) , avg(country.le) , country.cont FROM country GROUP BY country.cont HAVING avg(country.le) < 72	world_1_0
SELECT sum(country.popn) , avg(country.le) , country.cont FROM country GROUP BY country.cont HAVING avg(country.le) < 72	world_1_0
SELECT country.Name , country.sa FROM country ORDER BY country.sa desc LIMIT 5	world_1_0
SELECT country.Name , country.sa FROM country ORDER BY country.sa desc LIMIT 5	world_1_0
SELECT country.Name FROM country ORDER BY country.popn desc LIMIT 3	world_1_0
SELECT country.Name FROM country ORDER BY country.popn desc LIMIT 3	world_1_0
SELECT country.Name FROM country ORDER BY country.popn asc LIMIT 3	world_1_0
SELECT country.Name FROM country ORDER BY country.popn asc LIMIT 3	world_1_0
SELECT count(*) FROM country WHERE country.cont = "Asia"	world_1_0
SELECT count(*) FROM country WHERE country.cont = "Asia"	world_1_0
SELECT country.Name FROM country WHERE country.cont = "Europe" and country.popn = "80000"	world_1_0
SELECT country.Name FROM country WHERE country.cont = "Europe" and country.popn = "80000"	world_1_0
SELECT sum(country.popn) , avg(country.sa) FROM country WHERE country.cont = "north america" and country.sa > 3000	world_1_0
SELECT sum(country.popn) , avg(country.sa) FROM country WHERE country.cont = "north america" and country.sa > 3000	world_1_0
SELECT city.Name FROM city WHERE city.popn BETWEEN 160000 AND 900000	world_1_0
SELECT city.Name FROM city WHERE city.popn BETWEEN 160000 AND 900000	world_1_0
SELECT countrylanguage.lang FROM countrylanguage GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT countrylanguage.lang FROM countrylanguage GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_0
SELECT countrylanguage.lang , countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.cntry_code	world_1_0
SELECT countrylanguage.lang , countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.cntry_code	world_1_0
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_0
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_0
SELECT countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_0
SELECT countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_0
SELECT country.cont FROM country WHERE country.Name = "Anguilla"	world_1_1
SELECT country.cont FROM country WHERE country.Name = "Anguilla"	world_1_1
SELECT country.Region FROM country JOIN city ON country.Code = city.cntry_code WHERE city.Name = "Kabul"	world_1_1
SELECT country.Region FROM country JOIN city ON country.Code = city.cntry_code WHERE city.Name = "Kabul"	world_1_1
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_1
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_1
SELECT country.popn , country.le FROM country WHERE country.Name = "Brazil"	world_1_1
SELECT country.popn , country.le FROM country WHERE country.Name = "Brazil"	world_1_1
SELECT country.popn , country.Region FROM country WHERE country.Name = "Angola"	world_1_1
SELECT country.popn , country.Region FROM country WHERE country.Name = "Angola"	world_1_1
SELECT avg(country.le) FROM country WHERE country.Region = "Central Africa"	world_1_1
SELECT avg(country.le) FROM country WHERE country.Region = "Central Africa"	world_1_1
SELECT country.Name FROM country WHERE country.cont = "Asia" ORDER BY country.le asc LIMIT 1	world_1_1
SELECT country.Name FROM country WHERE country.cont = "Asia" ORDER BY country.le asc LIMIT 1	world_1_1
SELECT sum(country.popn) , max(country.GNP) FROM country WHERE country.cont = "Asia"	world_1_1
SELECT sum(country.popn) , max(country.GNP) FROM country WHERE country.cont = "Asia"	world_1_1
SELECT avg(country.le) FROM country WHERE country.cont = "Africa" and country.GovernmentForm = "Republic"	world_1_1
SELECT avg(country.le) FROM country WHERE country.cont = "Africa" and country.GovernmentForm = "Republic"	world_1_1
SELECT sum(country.SurfaceArea) FROM country WHERE country.cont = "Asia" or country.cont = "Europe"	world_1_1
SELECT sum(country.SurfaceArea) FROM country WHERE country.cont = "Asia" or country.cont = "Europe"	world_1_1
SELECT avg(country.GNP) , sum(country.popn) FROM country WHERE country.GovernmentForm = "US Territory"	world_1_1
SELECT avg(country.GNP) , sum(country.popn) FROM country WHERE country.GovernmentForm = "US Territory"	world_1_1
SELECT count(DISTINCT country.GovernmentForm) FROM country WHERE country.cont = "Africa"	world_1_1
SELECT count(DISTINCT country.GovernmentForm) FROM country WHERE country.cont = "Africa"	world_1_1
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.ofcl = "T"	world_1_1
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.ofcl = "T"	world_1_1
SELECT country.cont FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.cont ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT country.cont FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.cont ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "English" and countrylanguage.ofcl = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "French" and countrylanguage.ofcl = "T"	world_1_1
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "English" and countrylanguage.ofcl = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "French" and countrylanguage.ofcl = "T"	world_1_1
SELECT count(DISTINCT country.cont) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "Chinese"	world_1_1
SELECT count(DISTINCT country.cont) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "Chinese"	world_1_1
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "english" and countrylanguage.ofcl = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "dutch" and countrylanguage.ofcl = "t"	world_1_1
SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "English" and countrylanguage.ofcl = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "Dutch" and countrylanguage.ofcl = "T"	world_1_1
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.cont = "Asia" GROUP BY countrylanguage.Language ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.cont = "Asia" GROUP BY countrylanguage.Language ORDER BY count(*) desc LIMIT 1	world_1_1
SELECT city.Name , city.Population FROM city JOIN countrylanguage ON city.cntry_code = countrylanguage.CountryCode WHERE countrylanguage.Language = "English" ORDER BY city.Population desc LIMIT 1	world_1_1
SELECT city.Name , city.Population FROM city JOIN countrylanguage ON city.cntry_code = countrylanguage.CountryCode WHERE countrylanguage.Language = "English" ORDER BY city.Population desc LIMIT 1	world_1_1
SELECT country.Name , country.popn , country.le FROM country WHERE country.cont = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_1
SELECT country.Name , country.popn , country.le FROM country WHERE country.cont = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_1
SELECT avg(country.le) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "English" and countrylanguage.ofcl = "T")	world_1_1
SELECT avg(country.le) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "English" and countrylanguage.ofcl = "T")	world_1_1
SELECT sum(country.popn) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "English")	world_1_1
SELECT sum(country.popn) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = "English")	world_1_1
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.hos = "Beatrix" and countrylanguage.ofcl = "T"	world_1_1
SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.hos = "Beatrix" and countrylanguage.ofcl = "T"	world_1_1
SELECT count(DISTINCT countrylanguage.Language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.ofcl = "T"	world_1_1
SELECT count(DISTINCT countrylanguage.Language) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.ofcl = "T"	world_1_1
SELECT country.Name FROM country WHERE country.SurfaceArea > (SELECT min(country.SurfaceArea) FROM country WHERE country.cont = "Europe")	world_1_1
SELECT country.Name FROM country WHERE country.SurfaceArea > (SELECT min(country.SurfaceArea) FROM country WHERE country.cont = "Europe")	world_1_1
SELECT country.Name FROM country WHERE country.cont = "Africa" and country.popn < (SELECT max(country.popn) FROM country WHERE country.cont = "Asia")	world_1_1
SELECT country.Name FROM country WHERE country.cont = "Africa" and country.popn < (SELECT min(country.popn) FROM country WHERE country.cont = "Asia")	world_1_1
SELECT country.Name FROM country WHERE country.cont = "Asia" and country.popn > (SELECT max(country.popn) FROM country WHERE country.cont = "Africa")	world_1_1
SELECT country.Name FROM country WHERE country.cont = "Asia" and country.popn > (SELECT min(country.popn) FROM country WHERE country.cont = "Africa")	world_1_1
SELECT DISTINCT city.Name FROM country JOIN city ON city.cntry_code = country.Code WHERE country.cont = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.ofcl = "T" and countrylanguage.Language = "English")	world_1_1
SELECT DISTINCT city.Name FROM country JOIN city ON city.cntry_code = country.Code WHERE country.cont = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.ofcl = "T" and countrylanguage.Language = "English")	world_1_1
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.cntry_code WHERE countrylanguage.ofcl = "t" and countrylanguage.Language = "chinese" and country.cont = "asia"	world_1_1
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.cntry_code WHERE countrylanguage.ofcl = "T" and countrylanguage.Language = "Chinese" and country.cont = "Asia"	world_1_1
SELECT country.Name , country.SurfaceArea , country.IndepYear FROM country ORDER BY country.popn asc LIMIT 1	world_1_1
SELECT country.Name , country.SurfaceArea , country.IndepYear FROM country ORDER BY country.popn asc LIMIT 1	world_1_1
SELECT country.Name , country.popn , country.hos FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_1
SELECT country.Name , country.popn , country.hos FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_1
SELECT sum(country.popn) , country.GovernmentForm FROM country GROUP BY country.GovernmentForm HAVING avg(country.le) > 72	world_1_1
SELECT sum(country.popn) , country.GovernmentForm FROM country GROUP BY country.GovernmentForm HAVING avg(country.le) > 72	world_1_1
SELECT sum(country.popn) , avg(country.le) , country.cont FROM country GROUP BY country.cont HAVING avg(country.le) < 72	world_1_1
SELECT sum(country.popn) , avg(country.le) , country.cont FROM country GROUP BY country.cont HAVING avg(country.le) < 72	world_1_1
SELECT country.Name FROM country ORDER BY country.popn desc LIMIT 3	world_1_1
SELECT country.Name FROM country ORDER BY country.popn desc LIMIT 3	world_1_1
SELECT country.Name FROM country ORDER BY country.popn asc LIMIT 3	world_1_1
SELECT country.Name FROM country ORDER BY country.popn asc LIMIT 3	world_1_1
SELECT count(*) FROM country WHERE country.cont = "Asia"	world_1_1
SELECT count(*) FROM country WHERE country.cont = "Asia"	world_1_1
SELECT country.Name FROM country WHERE country.cont = "Europe" and country.popn = "80000"	world_1_1
SELECT country.Name FROM country WHERE country.cont = "Europe" and country.popn = "80000"	world_1_1
SELECT sum(country.popn) , avg(country.SurfaceArea) FROM country WHERE country.cont = "north america" and country.SurfaceArea > 3000	world_1_1
SELECT sum(country.popn) , avg(country.SurfaceArea) FROM country WHERE country.cont = "north america" and country.SurfaceArea > 3000	world_1_1
SELECT countrylanguage.Language , countrylanguage.CountryCode , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_1
SELECT countrylanguage.Language , countrylanguage.CountryCode , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_1
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_1
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_1
SELECT countrylanguage.CountryCode , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_1
SELECT countrylanguage.CountryCode , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.Language = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_1
SELECT count(*) FROM country WHERE country.gf = "Republic"	world_1_2
SELECT count(*) FROM country WHERE country.gf = "Republic"	world_1_2
SELECT sum(country.sa) FROM country WHERE country.Region = "Caribbean"	world_1_2
SELECT sum(country.sa) FROM country WHERE country.Region = "Caribbean"	world_1_2
SELECT country.cont FROM country WHERE country.Name = "Anguilla"	world_1_2
SELECT country.cont FROM country WHERE country.Name = "Anguilla"	world_1_2
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_2
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_2
SELECT country.Population , country.le FROM country WHERE country.Name = "Brazil"	world_1_2
SELECT country.Population , country.le FROM country WHERE country.Name = "Brazil"	world_1_2
SELECT avg(country.le) FROM country WHERE country.Region = "Central Africa"	world_1_2
SELECT avg(country.le) FROM country WHERE country.Region = "Central Africa"	world_1_2
SELECT country.Name FROM country WHERE country.cont = "Asia" ORDER BY country.le asc LIMIT 1	world_1_2
SELECT country.Name FROM country WHERE country.cont = "Asia" ORDER BY country.le asc LIMIT 1	world_1_2
SELECT sum(country.Population) , max(country.GNP) FROM country WHERE country.cont = "Asia"	world_1_2
SELECT sum(country.Population) , max(country.GNP) FROM country WHERE country.cont = "Asia"	world_1_2
SELECT avg(country.le) FROM country WHERE country.cont = "Africa" and country.gf = "Republic"	world_1_2
SELECT avg(country.le) FROM country WHERE country.cont = "Africa" and country.gf = "Republic"	world_1_2
SELECT sum(country.sa) FROM country WHERE country.cont = "Asia" or country.cont = "Europe"	world_1_2
SELECT sum(country.sa) FROM country WHERE country.cont = "Asia" or country.cont = "Europe"	world_1_2
SELECT sum(city.popn) FROM city WHERE city.District = "Gelderland"	world_1_2
SELECT sum(city.popn) FROM city WHERE city.District = "Gelderland"	world_1_2
SELECT avg(country.GNP) , sum(country.Population) FROM country WHERE country.gf = "US Territory"	world_1_2
SELECT avg(country.GNP) , sum(country.Population) FROM country WHERE country.gf = "US Territory"	world_1_2
SELECT count(DISTINCT countrylanguage.lang) FROM countrylanguage	world_1_2
SELECT count(DISTINCT countrylanguage.lang) FROM countrylanguage	world_1_2
SELECT count(DISTINCT country.gf) FROM country WHERE country.cont = "Africa"	world_1_2
SELECT count(DISTINCT country.gf) FROM country WHERE country.cont = "Africa"	world_1_2
SELECT count(countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba"	world_1_2
SELECT count(countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba"	world_1_2
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Afghanistan" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Afghanistan" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT country.cont FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.cont ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT country.cont FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.cont ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Dutch" )	world_1_2
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Dutch" )	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.IsOfficial = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.IsOfficial = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT count(DISTINCT country.cont) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Chinese"	world_1_2
SELECT count(DISTINCT country.cont) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Chinese"	world_1_2
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" or countrylanguage.lang = "Dutch"	world_1_2
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" or countrylanguage.lang = "Dutch"	world_1_2
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "english" and countrylanguage.IsOfficial = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "dutch" and countrylanguage.IsOfficial = "t"	world_1_2
SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.IsOfficial = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Dutch" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.cont = "Asia" GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.cont = "Asia" GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.gf = "Republic" GROUP BY countrylanguage.lang HAVING count(*) = 1	world_1_2
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.gf = "Republic" GROUP BY countrylanguage.lang HAVING count(*) = 1	world_1_2
SELECT city.Name , city.popn FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" ORDER BY city.popn desc LIMIT 1	world_1_2
SELECT city.Name , city.popn FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" ORDER BY city.popn desc LIMIT 1	world_1_2
SELECT country.Name , country.Population , country.le FROM country WHERE country.cont = "Asia" ORDER BY country.sa desc LIMIT 1	world_1_2
SELECT country.Name , country.Population , country.le FROM country WHERE country.cont = "Asia" ORDER BY country.sa desc LIMIT 1	world_1_2
SELECT avg(country.le) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.IsOfficial = "T")	world_1_2
SELECT avg(country.le) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.IsOfficial = "T")	world_1_2
SELECT sum(country.Population) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English")	world_1_2
SELECT sum(country.Population) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English")	world_1_2
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.hos = "Beatrix" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.hos = "Beatrix" and countrylanguage.IsOfficial = "T"	world_1_2
SELECT count(DISTINCT countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.IndepYear < 1930 and countrylanguage.IsOfficial = "T"	world_1_2
SELECT count(DISTINCT countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.IndepYear < 1930 and countrylanguage.IsOfficial = "T"	world_1_2
SELECT country.Name FROM country WHERE country.sa > (SELECT min(country.sa) FROM country WHERE country.cont = "Europe")	world_1_2
SELECT country.Name FROM country WHERE country.sa > (SELECT min(country.sa) FROM country WHERE country.cont = "Europe")	world_1_2
SELECT country.Name FROM country WHERE country.cont = "Africa" and country.Population < (SELECT max(country.Population) FROM country WHERE country.cont = "Asia")	world_1_2
SELECT country.Name FROM country WHERE country.cont = "Africa" and country.Population < (SELECT min(country.Population) FROM country WHERE country.cont = "Asia")	world_1_2
SELECT country.Name FROM country WHERE country.cont = "Asia" and country.Population > (SELECT max(country.Population) FROM country WHERE country.cont = "Africa")	world_1_2
SELECT country.Name FROM country WHERE country.cont = "Asia" and country.Population > (SELECT min(country.Population) FROM country WHERE country.cont = "Africa")	world_1_2
SELECT countrylanguage.cntry_code FROM countrylanguage EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_2
SELECT countrylanguage.cntry_code FROM countrylanguage EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_2
SELECT DISTINCT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang != "English"	world_1_2
SELECT DISTINCT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang != "English"	world_1_2
SELECT country.Code FROM country WHERE country.gf != "Republic" EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_2
SELECT country.Code FROM country WHERE country.gf != "Republic" EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_2
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.cont = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.IsOfficial = "T" and countrylanguage.lang = "English")	world_1_2
SELECT DISTINCT city.Name FROM country JOIN city ON city.CountryCode = country.Code WHERE country.cont = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.IsOfficial = "T" and countrylanguage.lang = "English")	world_1_2
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.IsOfficial = "t" and countrylanguage.lang = "chinese" and country.cont = "asia"	world_1_2
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code JOIN city ON country.Code = city.CountryCode WHERE countrylanguage.IsOfficial = "T" and countrylanguage.lang = "Chinese" and country.cont = "Asia"	world_1_2
SELECT country.Name , country.sa , country.IndepYear FROM country ORDER BY country.Population asc LIMIT 1	world_1_2
SELECT country.Name , country.sa , country.IndepYear FROM country ORDER BY country.Population asc LIMIT 1	world_1_2
SELECT country.Name , country.Population , country.hos FROM country ORDER BY country.sa desc LIMIT 1	world_1_2
SELECT country.Name , country.Population , country.hos FROM country ORDER BY country.sa desc LIMIT 1	world_1_2
SELECT count(countrylanguage.lang) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name HAVING count(*) > 2	world_1_2
SELECT count(countrylanguage.lang) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name HAVING count(*) > 2	world_1_2
SELECT count(*) , city.District FROM city WHERE city.popn > (SELECT avg(city.popn) FROM city) GROUP BY city.District	world_1_2
SELECT count(*) , city.District FROM city WHERE city.popn > (SELECT avg(city.popn) FROM city) GROUP BY city.District	world_1_2
SELECT sum(country.Population) , country.gf FROM country GROUP BY country.gf HAVING avg(country.le) > 72	world_1_2
SELECT sum(country.Population) , country.gf FROM country GROUP BY country.gf HAVING avg(country.le) > 72	world_1_2
SELECT sum(country.Population) , avg(country.le) , country.cont FROM country GROUP BY country.cont HAVING avg(country.le) < 72	world_1_2
SELECT sum(country.Population) , avg(country.le) , country.cont FROM country GROUP BY country.cont HAVING avg(country.le) < 72	world_1_2
SELECT country.Name , country.sa FROM country ORDER BY country.sa desc LIMIT 5	world_1_2
SELECT country.Name , country.sa FROM country ORDER BY country.sa desc LIMIT 5	world_1_2
SELECT count(*) FROM country WHERE country.cont = "Asia"	world_1_2
SELECT count(*) FROM country WHERE country.cont = "Asia"	world_1_2
SELECT country.Name FROM country WHERE country.cont = "Europe" and country.Population = "80000"	world_1_2
SELECT country.Name FROM country WHERE country.cont = "Europe" and country.Population = "80000"	world_1_2
SELECT sum(country.Population) , avg(country.sa) FROM country WHERE country.cont = "north america" and country.sa > 3000	world_1_2
SELECT sum(country.Population) , avg(country.sa) FROM country WHERE country.cont = "north america" and country.sa > 3000	world_1_2
SELECT city.Name FROM city WHERE city.popn BETWEEN 160000 AND 900000	world_1_2
SELECT city.Name FROM city WHERE city.popn BETWEEN 160000 AND 900000	world_1_2
SELECT countrylanguage.lang FROM countrylanguage GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT countrylanguage.lang FROM countrylanguage GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_2
SELECT countrylanguage.lang , countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.cntry_code	world_1_2
SELECT countrylanguage.lang , countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.cntry_code	world_1_2
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_2
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_2
SELECT countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_2
SELECT countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_2
SELECT count(*) FROM country WHERE country.gf = "Republic"	world_1_3
SELECT count(*) FROM country WHERE country.gf = "Republic"	world_1_3
SELECT sum(country.sa) FROM country WHERE country.Region = "Caribbean"	world_1_3
SELECT sum(country.sa) FROM country WHERE country.Region = "Caribbean"	world_1_3
SELECT country.Region FROM country JOIN city ON country.Code = city.cntry_code WHERE city.Name = "Kabul"	world_1_3
SELECT country.Region FROM country JOIN city ON country.Code = city.cntry_code WHERE city.Name = "Kabul"	world_1_3
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_3
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_3
SELECT country.popn , country.le FROM country WHERE country.Name = "Brazil"	world_1_3
SELECT country.popn , country.le FROM country WHERE country.Name = "Brazil"	world_1_3
SELECT country.popn , country.Region FROM country WHERE country.Name = "Angola"	world_1_3
SELECT country.popn , country.Region FROM country WHERE country.Name = "Angola"	world_1_3
SELECT avg(country.le) FROM country WHERE country.Region = "Central Africa"	world_1_3
SELECT avg(country.le) FROM country WHERE country.Region = "Central Africa"	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Asia" ORDER BY country.le asc LIMIT 1	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Asia" ORDER BY country.le asc LIMIT 1	world_1_3
SELECT sum(country.popn) , max(country.GNP) FROM country WHERE country.Continent = "Asia"	world_1_3
SELECT sum(country.popn) , max(country.GNP) FROM country WHERE country.Continent = "Asia"	world_1_3
SELECT avg(country.le) FROM country WHERE country.Continent = "Africa" and country.gf = "Republic"	world_1_3
SELECT avg(country.le) FROM country WHERE country.Continent = "Africa" and country.gf = "Republic"	world_1_3
SELECT sum(country.sa) FROM country WHERE country.Continent = "Asia" or country.Continent = "Europe"	world_1_3
SELECT sum(country.sa) FROM country WHERE country.Continent = "Asia" or country.Continent = "Europe"	world_1_3
SELECT sum(city.popn) FROM city WHERE city.dist = "Gelderland"	world_1_3
SELECT sum(city.popn) FROM city WHERE city.dist = "Gelderland"	world_1_3
SELECT avg(country.GNP) , sum(country.popn) FROM country WHERE country.gf = "US Territory"	world_1_3
SELECT avg(country.GNP) , sum(country.popn) FROM country WHERE country.gf = "US Territory"	world_1_3
SELECT count(DISTINCT countrylanguage.lang) FROM countrylanguage	world_1_3
SELECT count(DISTINCT countrylanguage.lang) FROM countrylanguage	world_1_3
SELECT count(DISTINCT country.gf) FROM country WHERE country.Continent = "Africa"	world_1_3
SELECT count(DISTINCT country.gf) FROM country WHERE country.Continent = "Africa"	world_1_3
SELECT count(countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba"	world_1_3
SELECT count(countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Aruba"	world_1_3
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.ofcl = "T"	world_1_3
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Name = "Afghanistan" and countrylanguage.ofcl = "T"	world_1_3
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "Dutch" )	world_1_3
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "Dutch" )	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "French"	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "French"	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "French" and countrylanguage.ofcl = "T"	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "French" and countrylanguage.ofcl = "T"	world_1_3
SELECT count(DISTINCT country.Continent) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "Chinese"	world_1_3
SELECT count(DISTINCT country.Continent) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "Chinese"	world_1_3
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" or countrylanguage.lang = "Dutch"	world_1_3
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" or countrylanguage.lang = "Dutch"	world_1_3
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "english" and countrylanguage.ofcl = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "dutch" and countrylanguage.ofcl = "t"	world_1_3
SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "Dutch" and countrylanguage.ofcl = "T"	world_1_3
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = "Asia" GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_3
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = "Asia" GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_3
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.gf = "Republic" GROUP BY countrylanguage.lang HAVING count(*) = 1	world_1_3
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.gf = "Republic" GROUP BY countrylanguage.lang HAVING count(*) = 1	world_1_3
SELECT city.Name , city.popn FROM city JOIN countrylanguage ON city.cntry_code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" ORDER BY city.popn desc LIMIT 1	world_1_3
SELECT city.Name , city.popn FROM city JOIN countrylanguage ON city.cntry_code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" ORDER BY city.popn desc LIMIT 1	world_1_3
SELECT country.Name , country.popn , country.le FROM country WHERE country.Continent = "Asia" ORDER BY country.sa desc LIMIT 1	world_1_3
SELECT country.Name , country.popn , country.le FROM country WHERE country.Continent = "Asia" ORDER BY country.sa desc LIMIT 1	world_1_3
SELECT avg(country.le) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T")	world_1_3
SELECT avg(country.le) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T")	world_1_3
SELECT sum(country.popn) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English")	world_1_3
SELECT sum(country.popn) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.lang = "English")	world_1_3
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.hos = "Beatrix" and countrylanguage.ofcl = "T"	world_1_3
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.hos = "Beatrix" and countrylanguage.ofcl = "T"	world_1_3
SELECT count(DISTINCT countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.ofcl = "T"	world_1_3
SELECT count(DISTINCT countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.IndepYear < 1930 and countrylanguage.ofcl = "T"	world_1_3
SELECT country.Name FROM country WHERE country.sa > (SELECT min(country.sa) FROM country WHERE country.Continent = "Europe")	world_1_3
SELECT country.Name FROM country WHERE country.sa > (SELECT min(country.sa) FROM country WHERE country.Continent = "Europe")	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Africa" and country.popn < (SELECT max(country.popn) FROM country WHERE country.Continent = "Asia")	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Africa" and country.popn < (SELECT min(country.popn) FROM country WHERE country.Continent = "Asia")	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Asia" and country.popn > (SELECT max(country.popn) FROM country WHERE country.Continent = "Africa")	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Asia" and country.popn > (SELECT min(country.popn) FROM country WHERE country.Continent = "Africa")	world_1_3
SELECT countrylanguage.CountryCode FROM countrylanguage EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_3
SELECT countrylanguage.CountryCode FROM countrylanguage EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_3
SELECT DISTINCT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.lang != "English"	world_1_3
SELECT DISTINCT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.lang != "English"	world_1_3
SELECT country.Code FROM country WHERE country.gf != "Republic" EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_3
SELECT country.Code FROM country WHERE country.gf != "Republic" EXCEPT SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_3
SELECT DISTINCT city.Name FROM country JOIN city ON city.cntry_code = country.Code WHERE country.Continent = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.ofcl = "T" and countrylanguage.lang = "English")	world_1_3
SELECT DISTINCT city.Name FROM country JOIN city ON city.cntry_code = country.Code WHERE country.Continent = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.ofcl = "T" and countrylanguage.lang = "English")	world_1_3
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.cntry_code WHERE countrylanguage.ofcl = "t" and countrylanguage.lang = "chinese" and country.Continent = "asia"	world_1_3
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode JOIN city ON country.Code = city.cntry_code WHERE countrylanguage.ofcl = "T" and countrylanguage.lang = "Chinese" and country.Continent = "Asia"	world_1_3
SELECT country.Name , country.sa , country.IndepYear FROM country ORDER BY country.popn asc LIMIT 1	world_1_3
SELECT country.Name , country.sa , country.IndepYear FROM country ORDER BY country.popn asc LIMIT 1	world_1_3
SELECT country.Name , country.popn , country.hos FROM country ORDER BY country.sa desc LIMIT 1	world_1_3
SELECT country.Name , country.popn , country.hos FROM country ORDER BY country.sa desc LIMIT 1	world_1_3
SELECT count(countrylanguage.lang) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Name HAVING count(*) > 2	world_1_3
SELECT count(countrylanguage.lang) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Name HAVING count(*) > 2	world_1_3
SELECT count(*) , city.dist FROM city WHERE city.popn > (SELECT avg(city.popn) FROM city) GROUP BY city.dist	world_1_3
SELECT count(*) , city.dist FROM city WHERE city.popn > (SELECT avg(city.popn) FROM city) GROUP BY city.dist	world_1_3
SELECT sum(country.popn) , country.gf FROM country GROUP BY country.gf HAVING avg(country.le) > 72	world_1_3
SELECT sum(country.popn) , country.gf FROM country GROUP BY country.gf HAVING avg(country.le) > 72	world_1_3
SELECT sum(country.popn) , avg(country.le) , country.Continent FROM country GROUP BY country.Continent HAVING avg(country.le) < 72	world_1_3
SELECT sum(country.popn) , avg(country.le) , country.Continent FROM country GROUP BY country.Continent HAVING avg(country.le) < 72	world_1_3
SELECT country.Name , country.sa FROM country ORDER BY country.sa desc LIMIT 5	world_1_3
SELECT country.Name , country.sa FROM country ORDER BY country.sa desc LIMIT 5	world_1_3
SELECT country.Name FROM country ORDER BY country.popn desc LIMIT 3	world_1_3
SELECT country.Name FROM country ORDER BY country.popn desc LIMIT 3	world_1_3
SELECT country.Name FROM country ORDER BY country.popn asc LIMIT 3	world_1_3
SELECT country.Name FROM country ORDER BY country.popn asc LIMIT 3	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Europe" and country.popn = "80000"	world_1_3
SELECT country.Name FROM country WHERE country.Continent = "Europe" and country.popn = "80000"	world_1_3
SELECT sum(country.popn) , avg(country.sa) FROM country WHERE country.Continent = "north america" and country.sa > 3000	world_1_3
SELECT sum(country.popn) , avg(country.sa) FROM country WHERE country.Continent = "north america" and country.sa > 3000	world_1_3
SELECT city.Name FROM city WHERE city.popn BETWEEN 160000 AND 900000	world_1_3
SELECT city.Name FROM city WHERE city.popn BETWEEN 160000 AND 900000	world_1_3
SELECT countrylanguage.lang FROM countrylanguage GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_3
SELECT countrylanguage.lang FROM countrylanguage GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_3
SELECT countrylanguage.lang , countrylanguage.CountryCode , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_3
SELECT countrylanguage.lang , countrylanguage.CountryCode , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.CountryCode	world_1_3
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_3
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_3
SELECT countrylanguage.CountryCode , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_3
SELECT countrylanguage.CountryCode , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.CountryCode	world_1_3
SELECT count(*) FROM country WHERE country.gf = "Republic"	world_1_4
SELECT count(*) FROM country WHERE country.gf = "Republic"	world_1_4
SELECT country.Region FROM country JOIN city ON country.Code = city.cntry_code WHERE city.Name = "Kabul"	world_1_4
SELECT country.Region FROM country JOIN city ON country.Code = city.cntry_code WHERE city.Name = "Kabul"	world_1_4
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_4
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba" ORDER BY countrylanguage.pct desc LIMIT 1	world_1_4
SELECT country.popn , country.LifeExpectancy FROM country WHERE country.Name = "Brazil"	world_1_4
SELECT country.popn , country.LifeExpectancy FROM country WHERE country.Name = "Brazil"	world_1_4
SELECT country.popn , country.Region FROM country WHERE country.Name = "Angola"	world_1_4
SELECT country.popn , country.Region FROM country WHERE country.Name = "Angola"	world_1_4
SELECT sum(country.popn) , max(country.GNP) FROM country WHERE country.Continent = "Asia"	world_1_4
SELECT sum(country.popn) , max(country.GNP) FROM country WHERE country.Continent = "Asia"	world_1_4
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Continent = "Africa" and country.gf = "Republic"	world_1_4
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Continent = "Africa" and country.gf = "Republic"	world_1_4
SELECT sum(city.popn) FROM city WHERE city.District = "Gelderland"	world_1_4
SELECT sum(city.popn) FROM city WHERE city.District = "Gelderland"	world_1_4
SELECT avg(country.GNP) , sum(country.popn) FROM country WHERE country.gf = "US Territory"	world_1_4
SELECT avg(country.GNP) , sum(country.popn) FROM country WHERE country.gf = "US Territory"	world_1_4
SELECT count(DISTINCT countrylanguage.lang) FROM countrylanguage	world_1_4
SELECT count(DISTINCT countrylanguage.lang) FROM countrylanguage	world_1_4
SELECT count(DISTINCT country.gf) FROM country WHERE country.Continent = "Africa"	world_1_4
SELECT count(DISTINCT country.gf) FROM country WHERE country.Continent = "Africa"	world_1_4
SELECT count(countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba"	world_1_4
SELECT count(countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Aruba"	world_1_4
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Afghanistan" and countrylanguage.ofcl = "T"	world_1_4
SELECT count(*) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Name = "Afghanistan" and countrylanguage.ofcl = "T"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT country.Continent FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Continent ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT country.Continent FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Continent ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Dutch" )	world_1_4
SELECT count(*) FROM ( SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Dutch" )	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French" and countrylanguage.ofcl = "T"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T" INTERSECT SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "French" and countrylanguage.ofcl = "T"	world_1_4
SELECT count(DISTINCT country.Continent) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Chinese"	world_1_4
SELECT count(DISTINCT country.Continent) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Chinese"	world_1_4
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" or countrylanguage.lang = "Dutch"	world_1_4
SELECT DISTINCT country.Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" or countrylanguage.lang = "Dutch"	world_1_4
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "english" and countrylanguage.ofcl = "t" UNION SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "dutch" and countrylanguage.ofcl = "t"	world_1_4
SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T" UNION SELECT * FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "Dutch" and countrylanguage.ofcl = "T"	world_1_4
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Continent = "Asia" GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.Continent = "Asia" GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.gf = "Republic" GROUP BY countrylanguage.lang HAVING count(*) = 1	world_1_4
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.gf = "Republic" GROUP BY countrylanguage.lang HAVING count(*) = 1	world_1_4
SELECT city.Name , city.popn FROM city JOIN countrylanguage ON city.cntry_code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" ORDER BY city.popn desc LIMIT 1	world_1_4
SELECT city.Name , city.popn FROM city JOIN countrylanguage ON city.cntry_code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" ORDER BY city.popn desc LIMIT 1	world_1_4
SELECT country.Name , country.popn , country.LifeExpectancy FROM country WHERE country.Continent = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_4
SELECT country.Name , country.popn , country.LifeExpectancy FROM country WHERE country.Continent = "Asia" ORDER BY country.SurfaceArea desc LIMIT 1	world_1_4
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T")	world_1_4
SELECT avg(country.LifeExpectancy) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English" and countrylanguage.ofcl = "T")	world_1_4
SELECT sum(country.popn) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English")	world_1_4
SELECT sum(country.popn) FROM country WHERE country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.lang = "English")	world_1_4
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.hos = "Beatrix" and countrylanguage.ofcl = "T"	world_1_4
SELECT countrylanguage.lang FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.hos = "Beatrix" and countrylanguage.ofcl = "T"	world_1_4
SELECT count(DISTINCT countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.IndepYear < 1930 and countrylanguage.ofcl = "T"	world_1_4
SELECT count(DISTINCT countrylanguage.lang) FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE country.IndepYear < 1930 and countrylanguage.ofcl = "T"	world_1_4
SELECT country.Name FROM country WHERE country.Continent = "Africa" and country.popn < (SELECT max(country.popn) FROM country WHERE country.Continent = "Asia")	world_1_4
SELECT country.Name FROM country WHERE country.Continent = "Africa" and country.popn < (SELECT min(country.popn) FROM country WHERE country.Continent = "Asia")	world_1_4
SELECT country.Name FROM country WHERE country.Continent = "Asia" and country.popn > (SELECT max(country.popn) FROM country WHERE country.Continent = "Africa")	world_1_4
SELECT country.Name FROM country WHERE country.Continent = "Asia" and country.popn > (SELECT min(country.popn) FROM country WHERE country.Continent = "Africa")	world_1_4
SELECT countrylanguage.cntry_code FROM countrylanguage EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_4
SELECT countrylanguage.cntry_code FROM countrylanguage EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_4
SELECT DISTINCT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang != "English"	world_1_4
SELECT DISTINCT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang != "English"	world_1_4
SELECT country.Code FROM country WHERE country.gf != "Republic" EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_4
SELECT country.Code FROM country WHERE country.gf != "Republic" EXCEPT SELECT countrylanguage.cntry_code FROM countrylanguage WHERE countrylanguage.lang = "English"	world_1_4
SELECT DISTINCT city.Name FROM country JOIN city ON city.cntry_code = country.Code WHERE country.Continent = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.ofcl = "T" and countrylanguage.lang = "English")	world_1_4
SELECT DISTINCT city.Name FROM country JOIN city ON city.cntry_code = country.Code WHERE country.Continent = "Europe" and country.Name NOT in (SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code WHERE countrylanguage.ofcl = "T" and countrylanguage.lang = "English")	world_1_4
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code JOIN city ON country.Code = city.cntry_code WHERE countrylanguage.ofcl = "t" and countrylanguage.lang = "chinese" and country.Continent = "asia"	world_1_4
SELECT DISTINCT city.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code JOIN city ON country.Code = city.cntry_code WHERE countrylanguage.ofcl = "T" and countrylanguage.lang = "Chinese" and country.Continent = "Asia"	world_1_4
SELECT country.Name , country.SurfaceArea , country.IndepYear FROM country ORDER BY country.popn asc LIMIT 1	world_1_4
SELECT country.Name , country.SurfaceArea , country.IndepYear FROM country ORDER BY country.popn asc LIMIT 1	world_1_4
SELECT country.Name , country.popn , country.hos FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_4
SELECT country.Name , country.popn , country.hos FROM country ORDER BY country.SurfaceArea desc LIMIT 1	world_1_4
SELECT count(countrylanguage.lang) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name HAVING count(*) > 2	world_1_4
SELECT count(countrylanguage.lang) , country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.cntry_code GROUP BY country.Name HAVING count(*) > 2	world_1_4
SELECT count(*) , city.District FROM city WHERE city.popn > (SELECT avg(city.popn) FROM city) GROUP BY city.District	world_1_4
SELECT count(*) , city.District FROM city WHERE city.popn > (SELECT avg(city.popn) FROM city) GROUP BY city.District	world_1_4
SELECT sum(country.popn) , country.gf FROM country GROUP BY country.gf HAVING avg(country.LifeExpectancy) > 72	world_1_4
SELECT sum(country.popn) , country.gf FROM country GROUP BY country.gf HAVING avg(country.LifeExpectancy) > 72	world_1_4
SELECT sum(country.popn) , avg(country.LifeExpectancy) , country.Continent FROM country GROUP BY country.Continent HAVING avg(country.LifeExpectancy) < 72	world_1_4
SELECT sum(country.popn) , avg(country.LifeExpectancy) , country.Continent FROM country GROUP BY country.Continent HAVING avg(country.LifeExpectancy) < 72	world_1_4
SELECT country.Name FROM country ORDER BY country.popn desc LIMIT 3	world_1_4
SELECT country.Name FROM country ORDER BY country.popn desc LIMIT 3	world_1_4
SELECT country.Name FROM country ORDER BY country.popn asc LIMIT 3	world_1_4
SELECT country.Name FROM country ORDER BY country.popn asc LIMIT 3	world_1_4
SELECT country.Name FROM country WHERE country.Continent = "Europe" and country.popn = "80000"	world_1_4
SELECT country.Name FROM country WHERE country.Continent = "Europe" and country.popn = "80000"	world_1_4
SELECT sum(country.popn) , avg(country.SurfaceArea) FROM country WHERE country.Continent = "north america" and country.SurfaceArea > 3000	world_1_4
SELECT sum(country.popn) , avg(country.SurfaceArea) FROM country WHERE country.Continent = "north america" and country.SurfaceArea > 3000	world_1_4
SELECT city.Name FROM city WHERE city.popn BETWEEN 160000 AND 900000	world_1_4
SELECT city.Name FROM city WHERE city.popn BETWEEN 160000 AND 900000	world_1_4
SELECT countrylanguage.lang FROM countrylanguage GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT countrylanguage.lang FROM countrylanguage GROUP BY countrylanguage.lang ORDER BY count(*) desc LIMIT 1	world_1_4
SELECT countrylanguage.lang , countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.cntry_code	world_1_4
SELECT countrylanguage.lang , countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage GROUP BY countrylanguage.cntry_code	world_1_4
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_4
SELECT count(*) , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_4
SELECT countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_4
SELECT countrylanguage.cntry_code , max(countrylanguage.pct) FROM countrylanguage WHERE countrylanguage.lang = "Spanish" GROUP BY countrylanguage.cntry_code	world_1_4
SELECT orchestra.record_co FROM orchestra ORDER BY orchestra.Year_of_Founded desc	orchestra_0
SELECT orchestra.record_co FROM orchestra ORDER BY orchestra.Year_of_Founded desc	orchestra_0
SELECT avg(show.attend) FROM show	orchestra_0
SELECT avg(show.attend) FROM show	orchestra_0
SELECT conductor.Name , orchestra.orch FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id	orchestra_0
SELECT conductor.Name , orchestra.orch FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id	orchestra_0
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id GROUP BY orchestra.cond_id HAVING count(*) > 1	orchestra_0
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id GROUP BY orchestra.cond_id HAVING count(*) > 1	orchestra_0
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id GROUP BY orchestra.cond_id ORDER BY count(*) desc LIMIT 1	orchestra_0
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id GROUP BY orchestra.cond_id ORDER BY count(*) desc LIMIT 1	orchestra_0
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id WHERE orchestra.Year_of_Founded > 2008	orchestra_0
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id WHERE orchestra.Year_of_Founded > 2008	orchestra_0
SELECT orchestra.record_co , count(*) FROM orchestra GROUP BY orchestra.record_co	orchestra_0
SELECT orchestra.record_co , count(*) FROM orchestra GROUP BY orchestra.record_co	orchestra_0
SELECT orchestra.maj_fmt FROM orchestra GROUP BY orchestra.maj_fmt ORDER BY count(*) asc	orchestra_0
SELECT orchestra.maj_fmt FROM orchestra GROUP BY orchestra.maj_fmt ORDER BY count(*) asc	orchestra_0
SELECT orchestra.record_co FROM orchestra GROUP BY orchestra.record_co ORDER BY count(*) desc LIMIT 1	orchestra_0
SELECT orchestra.record_co FROM orchestra GROUP BY orchestra.record_co ORDER BY count(*) desc LIMIT 1	orchestra_0
SELECT orchestra.orch FROM orchestra WHERE orchestra.orch_id NOT in (SELECT performance.orch_id FROM performance)	orchestra_0
SELECT orchestra.orch FROM orchestra WHERE orchestra.orch_id NOT in (SELECT performance.orch_id FROM performance)	orchestra_0
SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded < 2003 INTERSECT SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded > 2003	orchestra_0
SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded < 2003 INTERSECT SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded > 2003	orchestra_0
SELECT count(*) FROM orchestra WHERE orchestra.maj_fmt = "CD" or orchestra.maj_fmt = "DVD"	orchestra_0
SELECT count(*) FROM orchestra WHERE orchestra.maj_fmt = "CD" or orchestra.maj_fmt = "DVD"	orchestra_0
SELECT orchestra.Year_of_Founded FROM orchestra JOIN performance ON orchestra.orch_id = performance.orch_id GROUP BY performance.orch_id HAVING count(*) > 1	orchestra_0
SELECT orchestra.Year_of_Founded FROM orchestra JOIN performance ON orchestra.orch_id = performance.orch_id GROUP BY performance.orch_id HAVING count(*) > 1	orchestra_0
SELECT avg(show.attend) FROM show	orchestra_1
SELECT avg(show.attend) FROM show	orchestra_1
SELECT conductor.Name , orchestra.Orchestra FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id	orchestra_1
SELECT conductor.Name , orchestra.Orchestra FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id	orchestra_1
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id GROUP BY orchestra.cond_id HAVING count(*) > 1	orchestra_1
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id GROUP BY orchestra.cond_id HAVING count(*) > 1	orchestra_1
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id GROUP BY orchestra.cond_id ORDER BY count(*) desc LIMIT 1	orchestra_1
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id GROUP BY orchestra.cond_id ORDER BY count(*) desc LIMIT 1	orchestra_1
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id WHERE orchestra.Year_of_Founded > 2008	orchestra_1
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.cond_id WHERE orchestra.Year_of_Founded > 2008	orchestra_1
SELECT orchestra.maj_fmt FROM orchestra GROUP BY orchestra.maj_fmt ORDER BY count(*) asc	orchestra_1
SELECT orchestra.maj_fmt FROM orchestra GROUP BY orchestra.maj_fmt ORDER BY count(*) asc	orchestra_1
SELECT count(*) FROM orchestra WHERE orchestra.maj_fmt = "CD" or orchestra.maj_fmt = "DVD"	orchestra_1
SELECT count(*) FROM orchestra WHERE orchestra.maj_fmt = "CD" or orchestra.maj_fmt = "DVD"	orchestra_1
SELECT orchestra.record_co FROM orchestra ORDER BY orchestra.Year_of_Founded desc	orchestra_2
SELECT orchestra.record_co FROM orchestra ORDER BY orchestra.Year_of_Founded desc	orchestra_2
SELECT avg(show.attend) FROM show	orchestra_2
SELECT avg(show.attend) FROM show	orchestra_2
SELECT conductor.Name , orchestra.orch FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.cond_id	orchestra_2
SELECT conductor.Name , orchestra.orch FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.cond_id	orchestra_2
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.cond_id GROUP BY orchestra.cond_id HAVING count(*) > 1	orchestra_2
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.cond_id GROUP BY orchestra.cond_id HAVING count(*) > 1	orchestra_2
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.cond_id GROUP BY orchestra.cond_id ORDER BY count(*) desc LIMIT 1	orchestra_2
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.cond_id GROUP BY orchestra.cond_id ORDER BY count(*) desc LIMIT 1	orchestra_2
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.cond_id WHERE orchestra.Year_of_Founded > 2008	orchestra_2
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.Conductor_ID = orchestra.cond_id WHERE orchestra.Year_of_Founded > 2008	orchestra_2
SELECT orchestra.record_co , count(*) FROM orchestra GROUP BY orchestra.record_co	orchestra_2
SELECT orchestra.record_co , count(*) FROM orchestra GROUP BY orchestra.record_co	orchestra_2
SELECT orchestra.record_co FROM orchestra GROUP BY orchestra.record_co ORDER BY count(*) desc LIMIT 1	orchestra_2
SELECT orchestra.record_co FROM orchestra GROUP BY orchestra.record_co ORDER BY count(*) desc LIMIT 1	orchestra_2
SELECT orchestra.orch FROM orchestra WHERE orchestra.Orchestra_ID NOT in (SELECT performance.orch_id FROM performance)	orchestra_2
SELECT orchestra.orch FROM orchestra WHERE orchestra.Orchestra_ID NOT in (SELECT performance.orch_id FROM performance)	orchestra_2
SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded < 2003 INTERSECT SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded > 2003	orchestra_2
SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded < 2003 INTERSECT SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded > 2003	orchestra_2
SELECT orchestra.Year_of_Founded FROM orchestra JOIN performance ON orchestra.Orchestra_ID = performance.orch_id GROUP BY performance.orch_id HAVING count(*) > 1	orchestra_2
SELECT orchestra.Year_of_Founded FROM orchestra JOIN performance ON orchestra.Orchestra_ID = performance.orch_id GROUP BY performance.orch_id HAVING count(*) > 1	orchestra_2
SELECT orchestra.record_co FROM orchestra ORDER BY orchestra.Year_of_Founded desc	orchestra_3
SELECT orchestra.record_co FROM orchestra ORDER BY orchestra.Year_of_Founded desc	orchestra_3
SELECT avg(show.attend) FROM show	orchestra_3
SELECT avg(show.attend) FROM show	orchestra_3
SELECT conductor.Name , orchestra.orch FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID	orchestra_3
SELECT conductor.Name , orchestra.orch FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID	orchestra_3
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID HAVING count(*) > 1	orchestra_3
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID HAVING count(*) > 1	orchestra_3
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID ORDER BY count(*) desc LIMIT 1	orchestra_3
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID ORDER BY count(*) desc LIMIT 1	orchestra_3
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID WHERE orchestra.Year_of_Founded > 2008	orchestra_3
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID WHERE orchestra.Year_of_Founded > 2008	orchestra_3
SELECT orchestra.record_co , count(*) FROM orchestra GROUP BY orchestra.record_co	orchestra_3
SELECT orchestra.record_co , count(*) FROM orchestra GROUP BY orchestra.record_co	orchestra_3
SELECT orchestra.maj_fmt FROM orchestra GROUP BY orchestra.maj_fmt ORDER BY count(*) asc	orchestra_3
SELECT orchestra.maj_fmt FROM orchestra GROUP BY orchestra.maj_fmt ORDER BY count(*) asc	orchestra_3
SELECT orchestra.record_co FROM orchestra GROUP BY orchestra.record_co ORDER BY count(*) desc LIMIT 1	orchestra_3
SELECT orchestra.record_co FROM orchestra GROUP BY orchestra.record_co ORDER BY count(*) desc LIMIT 1	orchestra_3
SELECT orchestra.orch FROM orchestra WHERE orchestra.orch_id NOT in (SELECT performance.orch_id FROM performance)	orchestra_3
SELECT orchestra.orch FROM orchestra WHERE orchestra.orch_id NOT in (SELECT performance.orch_id FROM performance)	orchestra_3
SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded < 2003 INTERSECT SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded > 2003	orchestra_3
SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded < 2003 INTERSECT SELECT orchestra.record_co FROM orchestra WHERE orchestra.Year_of_Founded > 2003	orchestra_3
SELECT count(*) FROM orchestra WHERE orchestra.maj_fmt = "CD" or orchestra.maj_fmt = "DVD"	orchestra_3
SELECT count(*) FROM orchestra WHERE orchestra.maj_fmt = "CD" or orchestra.maj_fmt = "DVD"	orchestra_3
SELECT orchestra.Year_of_Founded FROM orchestra JOIN performance ON orchestra.orch_id = performance.orch_id GROUP BY performance.orch_id HAVING count(*) > 1	orchestra_3
SELECT orchestra.Year_of_Founded FROM orchestra JOIN performance ON orchestra.orch_id = performance.orch_id GROUP BY performance.orch_id HAVING count(*) > 1	orchestra_3
SELECT avg(show.attend) FROM show	orchestra_4
SELECT avg(show.attend) FROM show	orchestra_4
SELECT conductor.Name , orchestra.orch FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID	orchestra_4
SELECT conductor.Name , orchestra.orch FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID	orchestra_4
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID HAVING count(*) > 1	orchestra_4
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID HAVING count(*) > 1	orchestra_4
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID ORDER BY count(*) desc LIMIT 1	orchestra_4
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID GROUP BY orchestra.Conductor_ID ORDER BY count(*) desc LIMIT 1	orchestra_4
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID WHERE orchestra.Year_of_Founded > 2008	orchestra_4
SELECT conductor.Name FROM conductor JOIN orchestra ON conductor.cond_id = orchestra.Conductor_ID WHERE orchestra.Year_of_Founded > 2008	orchestra_4
SELECT orchestra.maj_fmt FROM orchestra GROUP BY orchestra.maj_fmt ORDER BY count(*) asc	orchestra_4
SELECT orchestra.maj_fmt FROM orchestra GROUP BY orchestra.maj_fmt ORDER BY count(*) asc	orchestra_4
SELECT orchestra.orch FROM orchestra WHERE orchestra.Orchestra_ID NOT in (SELECT performance.orch_id FROM performance)	orchestra_4
SELECT orchestra.orch FROM orchestra WHERE orchestra.Orchestra_ID NOT in (SELECT performance.orch_id FROM performance)	orchestra_4
SELECT count(*) FROM orchestra WHERE orchestra.maj_fmt = "CD" or orchestra.maj_fmt = "DVD"	orchestra_4
SELECT count(*) FROM orchestra WHERE orchestra.maj_fmt = "CD" or orchestra.maj_fmt = "DVD"	orchestra_4
SELECT orchestra.Year_of_Founded FROM orchestra JOIN performance ON orchestra.Orchestra_ID = performance.orch_id GROUP BY performance.orch_id HAVING count(*) > 1	orchestra_4
SELECT orchestra.Year_of_Founded FROM orchestra JOIN performance ON orchestra.Orchestra_ID = performance.orch_id GROUP BY performance.orch_id HAVING count(*) > 1	orchestra_4
SELECT Highschooler.name , Highschooler.gr FROM Highschooler	network_1_0
SELECT Highschooler.name , Highschooler.gr FROM Highschooler	network_1_0
SELECT Highschooler.gr FROM Highschooler	network_1_0
SELECT Highschooler.gr FROM Highschooler	network_1_0
SELECT Highschooler.gr FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_0
SELECT Highschooler.gr FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_0
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.gr = 10	network_1_0
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.gr = 10	network_1_0
SELECT count(*) FROM Highschooler WHERE Highschooler.gr = 9 or Highschooler.gr = 10	network_1_0
SELECT count(*) FROM Highschooler WHERE Highschooler.gr = 9 or Highschooler.gr = 10	network_1_0
SELECT Highschooler.gr , count(*) FROM Highschooler GROUP BY Highschooler.gr	network_1_0
SELECT Highschooler.gr , count(*) FROM Highschooler GROUP BY Highschooler.gr	network_1_0
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr ORDER BY count(*) desc LIMIT 1	network_1_0
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr ORDER BY count(*) desc LIMIT 1	network_1_0
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr HAVING count(*) >= 4	network_1_0
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr HAVING count(*) >= 4	network_1_0
SELECT Friend.stu_id , count(*) FROM Friend GROUP BY Friend.stu_id	network_1_0
SELECT Friend.stu_id , count(*) FROM Friend GROUP BY Friend.stu_id	network_1_0
SELECT Highschooler.name , count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id	network_1_0
SELECT Highschooler.name , count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id ORDER BY count(*) desc LIMIT 1	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id ORDER BY count(*) desc LIMIT 1	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id HAVING count(*) >= 3	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id HAVING count(*) >= 3	network_1_0
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.stu_id = T2.ID JOIN Highschooler AS T3 ON T1.frnd_id = T3.ID WHERE T2.name = "Kyle"	network_1_0
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.stu_id = T2.ID JOIN Highschooler AS T3 ON T1.frnd_id = T3.ID WHERE T2.name = "Kyle"	network_1_0
SELECT count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_0
SELECT count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_0
SELECT Highschooler.ID FROM Highschooler EXCEPT SELECT Friend.stu_id FROM Friend	network_1_0
SELECT Highschooler.ID FROM Highschooler EXCEPT SELECT Friend.stu_id FROM Friend	network_1_0
SELECT Highschooler.name FROM Highschooler EXCEPT SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID	network_1_0
SELECT Highschooler.name FROM Highschooler EXCEPT SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID	network_1_0
SELECT Friend.stu_id FROM Friend INTERSECT SELECT Likes.liked_id FROM Likes	network_1_0
SELECT Friend.stu_id FROM Friend INTERSECT SELECT Likes.liked_id FROM Likes	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID INTERSECT SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.liked_id = Highschooler.ID	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID INTERSECT SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.liked_id = Highschooler.ID	network_1_0
SELECT Likes.stu_id , count(*) FROM Likes GROUP BY Likes.stu_id	network_1_0
SELECT Likes.stu_id , count(*) FROM Likes GROUP BY Likes.stu_id	network_1_0
SELECT Highschooler.name , count(*) FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id	network_1_0
SELECT Highschooler.name , count(*) FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id	network_1_0
SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id ORDER BY count(*) desc LIMIT 1	network_1_0
SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id ORDER BY count(*) desc LIMIT 1	network_1_0
SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id HAVING count(*) >= 2	network_1_0
SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id HAVING count(*) >= 2	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.gr > 5 GROUP BY Friend.stu_id HAVING count(*) >= 2	network_1_0
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.gr > 5 GROUP BY Friend.stu_id HAVING count(*) >= 2	network_1_0
SELECT count(*) FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_0
SELECT count(*) FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_0
SELECT avg(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_0
SELECT avg(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_0
SELECT min(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_0
SELECT min(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_0
SELECT Friend.stu_id , count(*) FROM Friend GROUP BY Friend.stu_id	network_1_2
SELECT Friend.stu_id , count(*) FROM Friend GROUP BY Friend.stu_id	network_1_2
SELECT Highschooler.name , count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id	network_1_2
SELECT Highschooler.name , count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id	network_1_2
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id ORDER BY count(*) desc LIMIT 1	network_1_2
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id ORDER BY count(*) desc LIMIT 1	network_1_2
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id HAVING count(*) >= 3	network_1_2
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id HAVING count(*) >= 3	network_1_2
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.stu_id = T2.ID JOIN Highschooler AS T3 ON T1.frnd_id = T3.ID WHERE T2.name = "Kyle"	network_1_2
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.stu_id = T2.ID JOIN Highschooler AS T3 ON T1.frnd_id = T3.ID WHERE T2.name = "Kyle"	network_1_2
SELECT count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_2
SELECT count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_2
SELECT Highschooler.ID FROM Highschooler EXCEPT SELECT Friend.stu_id FROM Friend	network_1_2
SELECT Highschooler.ID FROM Highschooler EXCEPT SELECT Friend.stu_id FROM Friend	network_1_2
SELECT Highschooler.name FROM Highschooler EXCEPT SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID	network_1_2
SELECT Highschooler.name FROM Highschooler EXCEPT SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID	network_1_2
SELECT Friend.stu_id FROM Friend INTERSECT SELECT Likes.liked_id FROM Likes	network_1_2
SELECT Friend.stu_id FROM Friend INTERSECT SELECT Likes.liked_id FROM Likes	network_1_2
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.grade > 5 GROUP BY Friend.stu_id HAVING count(*) >= 2	network_1_2
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.grade > 5 GROUP BY Friend.stu_id HAVING count(*) >= 2	network_1_2
SELECT avg(Highschooler.grade) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_2
SELECT avg(Highschooler.grade) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_2
SELECT min(Highschooler.grade) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_2
SELECT min(Highschooler.grade) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_2
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID INTERSECT SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.liked_id = Highschooler.ID	network_1_3
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID INTERSECT SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.liked_id = Highschooler.ID	network_1_3
SELECT Likes.stu_id , count(*) FROM Likes GROUP BY Likes.stu_id	network_1_3
SELECT Likes.stu_id , count(*) FROM Likes GROUP BY Likes.stu_id	network_1_3
SELECT Highschooler.name , count(*) FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id	network_1_3
SELECT Highschooler.name , count(*) FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id	network_1_3
SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id ORDER BY count(*) desc LIMIT 1	network_1_3
SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id ORDER BY count(*) desc LIMIT 1	network_1_3
SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id HAVING count(*) >= 2	network_1_3
SELECT Highschooler.name FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID GROUP BY Likes.stu_id HAVING count(*) >= 2	network_1_3
SELECT count(*) FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_3
SELECT count(*) FROM Likes JOIN Highschooler ON Likes.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_3
SELECT Highschooler.name , Highschooler.gr FROM Highschooler	network_1_5
SELECT Highschooler.name , Highschooler.gr FROM Highschooler	network_1_5
SELECT Highschooler.gr FROM Highschooler	network_1_5
SELECT Highschooler.gr FROM Highschooler	network_1_5
SELECT Highschooler.gr FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_5
SELECT Highschooler.gr FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_5
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.gr = 10	network_1_5
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.gr = 10	network_1_5
SELECT count(*) FROM Highschooler WHERE Highschooler.gr = 9 or Highschooler.gr = 10	network_1_5
SELECT count(*) FROM Highschooler WHERE Highschooler.gr = 9 or Highschooler.gr = 10	network_1_5
SELECT Highschooler.gr , count(*) FROM Highschooler GROUP BY Highschooler.gr	network_1_5
SELECT Highschooler.gr , count(*) FROM Highschooler GROUP BY Highschooler.gr	network_1_5
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr ORDER BY count(*) desc LIMIT 1	network_1_5
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr ORDER BY count(*) desc LIMIT 1	network_1_5
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr HAVING count(*) >= 4	network_1_5
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr HAVING count(*) >= 4	network_1_5
SELECT Friend.stu_id , count(*) FROM Friend GROUP BY Friend.stu_id	network_1_5
SELECT Friend.stu_id , count(*) FROM Friend GROUP BY Friend.stu_id	network_1_5
SELECT Highschooler.name , count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id	network_1_5
SELECT Highschooler.name , count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id	network_1_5
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id ORDER BY count(*) desc LIMIT 1	network_1_5
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id ORDER BY count(*) desc LIMIT 1	network_1_5
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id HAVING count(*) >= 3	network_1_5
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID GROUP BY Friend.stu_id HAVING count(*) >= 3	network_1_5
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.stu_id = T2.ID JOIN Highschooler AS T3 ON T1.friend_id = T3.ID WHERE T2.name = "Kyle"	network_1_5
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.stu_id = T2.ID JOIN Highschooler AS T3 ON T1.friend_id = T3.ID WHERE T2.name = "Kyle"	network_1_5
SELECT count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_5
SELECT count(*) FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.name = "Kyle"	network_1_5
SELECT Highschooler.ID FROM Highschooler EXCEPT SELECT Friend.stu_id FROM Friend	network_1_5
SELECT Highschooler.ID FROM Highschooler EXCEPT SELECT Friend.stu_id FROM Friend	network_1_5
SELECT Highschooler.name FROM Highschooler EXCEPT SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID	network_1_5
SELECT Highschooler.name FROM Highschooler EXCEPT SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID	network_1_5
SELECT Friend.stu_id FROM Friend INTERSECT SELECT Likes.liked_id FROM Likes	network_1_5
SELECT Friend.stu_id FROM Friend INTERSECT SELECT Likes.liked_id FROM Likes	network_1_5
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.gr > 5 GROUP BY Friend.stu_id HAVING count(*) >= 2	network_1_5
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID WHERE Highschooler.gr > 5 GROUP BY Friend.stu_id HAVING count(*) >= 2	network_1_5
SELECT avg(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_5
SELECT avg(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_5
SELECT min(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_5
SELECT min(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.stu_id FROM Friend JOIN Highschooler ON Friend.stu_id = Highschooler.ID)	network_1_5
SELECT Highschooler.name , Highschooler.gr FROM Highschooler	network_1_8
SELECT Highschooler.name , Highschooler.gr FROM Highschooler	network_1_8
SELECT Highschooler.gr FROM Highschooler	network_1_8
SELECT Highschooler.gr FROM Highschooler	network_1_8
SELECT Highschooler.gr FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_8
SELECT Highschooler.gr FROM Highschooler WHERE Highschooler.name = "Kyle"	network_1_8
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.gr = 10	network_1_8
SELECT Highschooler.name FROM Highschooler WHERE Highschooler.gr = 10	network_1_8
SELECT count(*) FROM Highschooler WHERE Highschooler.gr = 9 or Highschooler.gr = 10	network_1_8
SELECT count(*) FROM Highschooler WHERE Highschooler.gr = 9 or Highschooler.gr = 10	network_1_8
SELECT Highschooler.gr , count(*) FROM Highschooler GROUP BY Highschooler.gr	network_1_8
SELECT Highschooler.gr , count(*) FROM Highschooler GROUP BY Highschooler.gr	network_1_8
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr ORDER BY count(*) desc LIMIT 1	network_1_8
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr ORDER BY count(*) desc LIMIT 1	network_1_8
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr HAVING count(*) >= 4	network_1_8
SELECT Highschooler.gr FROM Highschooler GROUP BY Highschooler.gr HAVING count(*) >= 4	network_1_8
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.ID JOIN Highschooler AS T3 ON T1.frnd_id = T3.ID WHERE T2.name = "Kyle"	network_1_8
SELECT T3.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.ID JOIN Highschooler AS T3 ON T1.frnd_id = T3.ID WHERE T2.name = "Kyle"	network_1_8
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID WHERE Highschooler.gr > 5 GROUP BY Friend.student_id HAVING count(*) >= 2	network_1_8
SELECT Highschooler.name FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID WHERE Highschooler.gr > 5 GROUP BY Friend.student_id HAVING count(*) >= 2	network_1_8
SELECT avg(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_8
SELECT avg(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_8
SELECT min(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_8
SELECT min(Highschooler.gr) FROM Highschooler WHERE Highschooler.ID NOT in (SELECT Friend.student_id FROM Friend JOIN Highschooler ON Friend.student_id = Highschooler.ID)	network_1_8
SELECT Professionals.pro_id , Professionals.last_name , Professionals.cell FROM Professionals WHERE Professionals.state = "Indiana" UNION SELECT Professionals.pro_id , Professionals.last_name , Professionals.cell FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id GROUP BY Professionals.pro_id HAVING count(*) > 2	dog_kennels_1
SELECT Professionals.pro_id , Professionals.last_name , Professionals.cell FROM Professionals WHERE Professionals.state = "Indiana" UNION SELECT Professionals.pro_id , Professionals.last_name , Professionals.cell FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id GROUP BY Professionals.pro_id HAVING count(*) > 2	dog_kennels_1
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_id FROM Treatments GROUP BY Treatments.dog_id HAVING sum(Treatments.cot) > 1000.0)	dog_kennels_1
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_id FROM Treatments GROUP BY Treatments.dog_id HAVING sum(Treatments.cot) > 1000.0)	dog_kennels_1
SELECT Professionals.pro_id , Professionals.role_code , Professionals.email_adr FROM Professionals EXCEPT SELECT Professionals.pro_id , Professionals.role_code , Professionals.email_adr FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id	dog_kennels_1
SELECT Professionals.pro_id , Professionals.role_code , Professionals.email_adr FROM Professionals EXCEPT SELECT Professionals.pro_id , Professionals.role_code , Professionals.email_adr FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id	dog_kennels_1
SELECT Professionals.pro_id , Professionals.role_code , Professionals.first_name FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id GROUP BY Professionals.pro_id HAVING count(*) >= 2	dog_kennels_1
SELECT Professionals.pro_id , Professionals.role_code , Professionals.first_name FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id GROUP BY Professionals.pro_id HAVING count(*) >= 2	dog_kennels_1
SELECT Treatment_Types.tx_type_desc FROM Treatment_Types JOIN Treatments ON Treatment_Types.tx_type_code = Treatments.tx_type_code GROUP BY Treatment_Types.tx_type_code ORDER BY sum(Treatments.cot) asc LIMIT 1	dog_kennels_1
SELECT Treatment_Types.tx_type_desc FROM Treatment_Types JOIN Treatments ON Treatment_Types.tx_type_code = Treatments.tx_type_code GROUP BY Treatment_Types.tx_type_code ORDER BY sum(Treatments.cot) asc LIMIT 1	dog_kennels_1
SELECT Owners.owner_id , Owners.zip_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY sum(Treatments.cot) desc LIMIT 1	dog_kennels_1
SELECT Owners.owner_id , Owners.zip_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY sum(Treatments.cot) desc LIMIT 1	dog_kennels_1
SELECT Professionals.pro_id , Professionals.cell FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id GROUP BY Professionals.pro_id HAVING count(*) >= 2	dog_kennels_1
SELECT Professionals.pro_id , Professionals.cell FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id GROUP BY Professionals.pro_id HAVING count(*) >= 2	dog_kennels_1
SELECT DISTINCT Professionals.first_name , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.cot < (SELECT avg(Treatments.cot) FROM Treatments)	dog_kennels_1
SELECT DISTINCT Professionals.first_name , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.cot < (SELECT avg(Treatments.cot) FROM Treatments)	dog_kennels_1
SELECT Treatments.dot , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.pro_id	dog_kennels_1
SELECT Treatments.dot , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.pro_id	dog_kennels_1
SELECT Treatments.cot , Treatment_Types.tx_type_desc FROM Treatments JOIN Treatment_Types ON Treatments.tx_type_code = Treatment_Types.tx_type_code	dog_kennels_1
SELECT Treatments.cot , Treatment_Types.tx_type_desc FROM Treatments JOIN Treatment_Types ON Treatments.tx_type_code = Treatment_Types.tx_type_code	dog_kennels_1
SELECT Owners.first_name , Owners.last_name , Dogs.sz_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_1
SELECT Owners.first_name , Owners.last_name , Dogs.sz_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id	dog_kennels_1
SELECT Dogs.name , Treatments.dot FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_1
SELECT Dogs.name , Treatments.dot FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_1
SELECT DISTINCT Dogs.date_arr , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_1
SELECT DISTINCT Dogs.date_arr , Dogs.date_departed FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_1
SELECT Professionals.email_adr FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_1
SELECT Professionals.email_adr FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_1
SELECT Dogs.date_arr , Dogs.date_departed FROM Dogs	dog_kennels_1
SELECT Dogs.date_arr , Dogs.date_departed FROM Dogs	dog_kennels_1
SELECT Professionals.role_code , Professionals.st , Professionals.city , Professionals.state FROM Professionals WHERE Professionals.city like "%West%"	dog_kennels_1
SELECT Professionals.role_code , Professionals.st , Professionals.city , Professionals.state FROM Professionals WHERE Professionals.city like "%West%"	dog_kennels_1
SELECT Owners.first_name , Owners.last_name , Owners.em_adr FROM Owners WHERE Owners.state like "%North%"	dog_kennels_1
SELECT Owners.first_name , Owners.last_name , Owners.em_adr FROM Owners WHERE Owners.state like "%North%"	dog_kennels_1
SELECT Treatments.cot FROM Treatments ORDER BY Treatments.dot desc LIMIT 1	dog_kennels_1
SELECT Treatments.cot FROM Treatments ORDER BY Treatments.dot desc LIMIT 1	dog_kennels_1
SELECT count(*) FROM Professionals WHERE Professionals.pro_id NOT in (SELECT Treatments.professional_id FROM Treatments)	dog_kennels_1
SELECT count(*) FROM Professionals WHERE Professionals.pro_id NOT in (SELECT Treatments.professional_id FROM Treatments)	dog_kennels_1
SELECT Dogs.name , Dogs.age , Dogs.wt FROM Dogs WHERE Dogs.aband_yn = 1	dog_kennels_1
SELECT Dogs.name , Dogs.age , Dogs.wt FROM Dogs WHERE Dogs.aband_yn = 1	dog_kennels_1
SELECT Charges.chrg_type , Charges.chrg_amt FROM Charges	dog_kennels_1
SELECT Charges.chrg_type , Charges.chrg_amt FROM Charges	dog_kennels_1
SELECT max(Charges.chrg_amt) FROM Charges	dog_kennels_1
SELECT max(Charges.chrg_amt) FROM Charges	dog_kennels_1
SELECT Professionals.email_adr , Professionals.cell , Professionals.hp FROM Professionals	dog_kennels_1
SELECT Professionals.email_adr , Professionals.cell , Professionals.hp FROM Professionals	dog_kennels_1
SELECT DISTINCT Dogs.breed_code , Dogs.sz_code FROM Dogs	dog_kennels_1
SELECT DISTINCT Dogs.breed_code , Dogs.sz_code FROM Dogs	dog_kennels_1
SELECT DISTINCT Professionals.first_name , Treatment_Types.tx_type_desc FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.tx_type_code = Treatment_Types.tx_type_code	dog_kennels_1
SELECT DISTINCT Professionals.first_name , Treatment_Types.tx_type_desc FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.professional_id JOIN Treatment_Types ON Treatments.tx_type_code = Treatment_Types.tx_type_code	dog_kennels_1
SELECT Professionals.role_code , Professionals.st , Professionals.city , Professionals.state FROM Professionals WHERE Professionals.city like "%West%"	dog_kennels_2
SELECT Professionals.role_code , Professionals.st , Professionals.city , Professionals.state FROM Professionals WHERE Professionals.city like "%West%"	dog_kennels_2
SELECT Dogs.name , Dogs.age , Dogs.wt FROM Dogs WHERE Dogs.abandoned_yn = 1	dog_kennels_2
SELECT Dogs.name , Dogs.age , Dogs.wt FROM Dogs WHERE Dogs.abandoned_yn = 1	dog_kennels_2
SELECT Professionals.professional_id , Professionals.last_name , Professionals.cell_number FROM Professionals WHERE Professionals.state = "Indiana" UNION SELECT Professionals.professional_id , Professionals.last_name , Professionals.cell_number FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id GROUP BY Professionals.professional_id HAVING count(*) > 2	dog_kennels_3
SELECT Professionals.professional_id , Professionals.last_name , Professionals.cell_number FROM Professionals WHERE Professionals.state = "Indiana" UNION SELECT Professionals.professional_id , Professionals.last_name , Professionals.cell_number FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id GROUP BY Professionals.professional_id HAVING count(*) > 2	dog_kennels_3
SELECT Professionals.professional_id , Professionals.role_code , Professionals.email_adr FROM Professionals EXCEPT SELECT Professionals.professional_id , Professionals.role_code , Professionals.email_adr FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id	dog_kennels_3
SELECT Professionals.professional_id , Professionals.role_code , Professionals.email_adr FROM Professionals EXCEPT SELECT Professionals.professional_id , Professionals.role_code , Professionals.email_adr FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id	dog_kennels_3
SELECT Professionals.professional_id , Professionals.role_code , Professionals.first_name FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_3
SELECT Professionals.professional_id , Professionals.role_code , Professionals.first_name FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_3
SELECT Professionals.professional_id , Professionals.cell_number FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_3
SELECT Professionals.professional_id , Professionals.cell_number FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id GROUP BY Professionals.professional_id HAVING count(*) >= 2	dog_kennels_3
SELECT Treatments.date_of_treatment , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.pro_id = Professionals.professional_id	dog_kennels_3
SELECT Treatments.date_of_treatment , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.pro_id = Professionals.professional_id	dog_kennels_3
SELECT Professionals.email_adr FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_3
SELECT Professionals.email_adr FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_3
SELECT count(DISTINCT Treatments.pro_id) FROM Treatments	dog_kennels_3
SELECT count(DISTINCT Treatments.pro_id) FROM Treatments	dog_kennels_3
SELECT count(*) FROM Professionals WHERE Professionals.professional_id NOT in (SELECT Treatments.pro_id FROM Treatments)	dog_kennels_3
SELECT count(*) FROM Professionals WHERE Professionals.professional_id NOT in (SELECT Treatments.pro_id FROM Treatments)	dog_kennels_3
SELECT Professionals.email_adr , Professionals.cell_number , Professionals.home_phone FROM Professionals	dog_kennels_3
SELECT Professionals.email_adr , Professionals.cell_number , Professionals.home_phone FROM Professionals	dog_kennels_3
SELECT DISTINCT Professionals.first_name , Treatment_Types.treatment_type_description FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.treatment_type_code	dog_kennels_3
SELECT DISTINCT Professionals.first_name , Treatment_Types.treatment_type_description FROM Professionals JOIN Treatments ON Professionals.professional_id = Treatments.pro_id JOIN Treatment_Types ON Treatments.treatment_type_code = Treatment_Types.treatment_type_code	dog_kennels_3
SELECT Professionals.pro_id , Professionals.last_name , Professionals.cell_number FROM Professionals WHERE Professionals.state = "Indiana" UNION SELECT Professionals.pro_id , Professionals.last_name , Professionals.cell_number FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id GROUP BY Professionals.pro_id HAVING count(*) > 2	dog_kennels_4
SELECT Professionals.pro_id , Professionals.last_name , Professionals.cell_number FROM Professionals WHERE Professionals.state = "Indiana" UNION SELECT Professionals.pro_id , Professionals.last_name , Professionals.cell_number FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id GROUP BY Professionals.pro_id HAVING count(*) > 2	dog_kennels_4
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_id FROM Treatments GROUP BY Treatments.dog_id HAVING sum(Treatments.cot) > 1000.0)	dog_kennels_4
SELECT Dogs.name FROM Dogs WHERE Dogs.dog_id NOT in (SELECT Treatments.dog_id FROM Treatments GROUP BY Treatments.dog_id HAVING sum(Treatments.cot) > 1000.0)	dog_kennels_4
SELECT Professionals.pro_id , Professionals.role_code , Professionals.email_adr FROM Professionals EXCEPT SELECT Professionals.pro_id , Professionals.role_code , Professionals.email_adr FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id	dog_kennels_4
SELECT Professionals.pro_id , Professionals.role_code , Professionals.email_adr FROM Professionals EXCEPT SELECT Professionals.pro_id , Professionals.role_code , Professionals.email_adr FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id	dog_kennels_4
SELECT Professionals.pro_id , Professionals.role_code , Professionals.first_name FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id GROUP BY Professionals.pro_id HAVING count(*) >= 2	dog_kennels_4
SELECT Professionals.pro_id , Professionals.role_code , Professionals.first_name FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id GROUP BY Professionals.pro_id HAVING count(*) >= 2	dog_kennels_4
SELECT Treatment_Types.tx_type_desc FROM Treatment_Types JOIN Treatments ON Treatment_Types.tx_type_code = Treatments.tx_type_code GROUP BY Treatment_Types.tx_type_code ORDER BY sum(Treatments.cot) asc LIMIT 1	dog_kennels_4
SELECT Treatment_Types.tx_type_desc FROM Treatment_Types JOIN Treatments ON Treatment_Types.tx_type_code = Treatments.tx_type_code GROUP BY Treatment_Types.tx_type_code ORDER BY sum(Treatments.cot) asc LIMIT 1	dog_kennels_4
SELECT Owners.owner_id , Owners.zip_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY sum(Treatments.cot) desc LIMIT 1	dog_kennels_4
SELECT Owners.owner_id , Owners.zip_code FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id JOIN Treatments ON Dogs.dog_id = Treatments.dog_id GROUP BY Owners.owner_id ORDER BY sum(Treatments.cot) desc LIMIT 1	dog_kennels_4
SELECT Professionals.pro_id , Professionals.cell_number FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id GROUP BY Professionals.pro_id HAVING count(*) >= 2	dog_kennels_4
SELECT Professionals.pro_id , Professionals.cell_number FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id GROUP BY Professionals.pro_id HAVING count(*) >= 2	dog_kennels_4
SELECT DISTINCT Professionals.first_name , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.cot < (SELECT avg(Treatments.cot) FROM Treatments)	dog_kennels_4
SELECT DISTINCT Professionals.first_name , Professionals.last_name FROM Professionals JOIN Treatments WHERE Treatments.cot < (SELECT avg(Treatments.cot) FROM Treatments)	dog_kennels_4
SELECT Treatments.dot , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.pro_id = Professionals.pro_id	dog_kennels_4
SELECT Treatments.dot , Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.pro_id = Professionals.pro_id	dog_kennels_4
SELECT Treatments.cot , Treatment_Types.tx_type_desc FROM Treatments JOIN Treatment_Types ON Treatments.tx_type_code = Treatment_Types.tx_type_code	dog_kennels_4
SELECT Treatments.cot , Treatment_Types.tx_type_desc FROM Treatments JOIN Treatment_Types ON Treatments.tx_type_code = Treatment_Types.tx_type_code	dog_kennels_4
SELECT Dogs.name , Treatments.dot FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_4
SELECT Dogs.name , Treatments.dot FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT Dogs.breed_code FROM Dogs GROUP BY Dogs.breed_code ORDER BY count(*) asc LIMIT 1)	dog_kennels_4
SELECT DISTINCT Dogs.date_arr , Dogs.date_dpt FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_4
SELECT DISTINCT Dogs.date_arr , Dogs.date_dpt FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id	dog_kennels_4
SELECT Professionals.email_adr FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_4
SELECT Professionals.email_adr FROM Professionals WHERE Professionals.state = "Hawaii" or Professionals.state = "Wisconsin"	dog_kennels_4
SELECT Dogs.date_arr , Dogs.date_dpt FROM Dogs	dog_kennels_4
SELECT Dogs.date_arr , Dogs.date_dpt FROM Dogs	dog_kennels_4
SELECT count(DISTINCT Treatments.pro_id) FROM Treatments	dog_kennels_4
SELECT count(DISTINCT Treatments.pro_id) FROM Treatments	dog_kennels_4
SELECT Professionals.role_code , Professionals.st , Professionals.city , Professionals.state FROM Professionals WHERE Professionals.city like "%West%"	dog_kennels_4
SELECT Professionals.role_code , Professionals.st , Professionals.city , Professionals.state FROM Professionals WHERE Professionals.city like "%West%"	dog_kennels_4
SELECT Owners.first_name , Owners.last_name , Owners.em_adr FROM Owners WHERE Owners.state like "%North%"	dog_kennels_4
SELECT Owners.first_name , Owners.last_name , Owners.em_adr FROM Owners WHERE Owners.state like "%North%"	dog_kennels_4
SELECT Treatments.cot FROM Treatments ORDER BY Treatments.dot desc LIMIT 1	dog_kennels_4
SELECT Treatments.cot FROM Treatments ORDER BY Treatments.dot desc LIMIT 1	dog_kennels_4
SELECT count(*) FROM Professionals WHERE Professionals.pro_id NOT in (SELECT Treatments.pro_id FROM Treatments)	dog_kennels_4
SELECT count(*) FROM Professionals WHERE Professionals.pro_id NOT in (SELECT Treatments.pro_id FROM Treatments)	dog_kennels_4
SELECT Dogs.name , Dogs.age , Dogs.weight FROM Dogs WHERE Dogs.aband_yn = 1	dog_kennels_4
SELECT Dogs.name , Dogs.age , Dogs.weight FROM Dogs WHERE Dogs.aband_yn = 1	dog_kennels_4
SELECT Charges.chrg_type , Charges.chrg_amt FROM Charges	dog_kennels_4
SELECT Charges.chrg_type , Charges.chrg_amt FROM Charges	dog_kennels_4
SELECT max(Charges.chrg_amt) FROM Charges	dog_kennels_4
SELECT max(Charges.chrg_amt) FROM Charges	dog_kennels_4
SELECT Professionals.email_adr , Professionals.cell_number , Professionals.hp FROM Professionals	dog_kennels_4
SELECT Professionals.email_adr , Professionals.cell_number , Professionals.hp FROM Professionals	dog_kennels_4
SELECT DISTINCT Professionals.first_name , Treatment_Types.tx_type_desc FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id JOIN Treatment_Types ON Treatments.tx_type_code = Treatment_Types.tx_type_code	dog_kennels_4
SELECT DISTINCT Professionals.first_name , Treatment_Types.tx_type_desc FROM Professionals JOIN Treatments ON Professionals.pro_id = Treatments.pro_id JOIN Treatment_Types ON Treatments.tx_type_code = Treatment_Types.tx_type_code	dog_kennels_4
SELECT singer.Name FROM singer ORDER BY singer.net_worth_m asc	singer_0
SELECT singer.Name FROM singer ORDER BY singer.net_worth_m asc	singer_0
SELECT singer.Name FROM singer ORDER BY singer.net_worth_m desc LIMIT 1	singer_0
SELECT singer.Name FROM singer ORDER BY singer.net_worth_m desc LIMIT 1	singer_0
SELECT singer.Citizenship , max(singer.net_worth_m) FROM singer GROUP BY singer.Citizenship	singer_0
SELECT singer.Citizenship , max(singer.net_worth_m) FROM singer GROUP BY singer.Citizenship	singer_0
SELECT singer.Name FROM singer ORDER BY singer.net_worth_m asc	singer_1
SELECT singer.Name FROM singer ORDER BY singer.net_worth_m asc	singer_1
SELECT singer.Name FROM singer ORDER BY singer.net_worth_m desc LIMIT 1	singer_1
SELECT singer.Name FROM singer ORDER BY singer.net_worth_m desc LIMIT 1	singer_1
SELECT singer.Citizenship , max(singer.net_worth_m) FROM singer GROUP BY singer.Citizenship	singer_1
SELECT singer.Citizenship , max(singer.net_worth_m) FROM singer GROUP BY singer.Citizenship	singer_1
SELECT Ref_Feature_Types.feature_type_name FROM Other_Available_Features JOIN Ref_Feature_Types ON Other_Available_Features.feat_type_code = Ref_Feature_Types.feat_type_code WHERE Other_Available_Features.feat_name = "AirCon"	real_estate_properties_0
SELECT Ref_Property_Types.prop_type_desc FROM Properties JOIN Ref_Property_Types ON Properties.prop_type_code = Ref_Property_Types.prop_type_code GROUP BY Properties.prop_type_code	real_estate_properties_0
SELECT Properties.prop_name FROM Properties WHERE Properties.prop_type_code = "House" UNION SELECT Properties.prop_name FROM Properties WHERE Properties.prop_type_code = "Apartment" and Properties.room_count > 1	real_estate_properties_0
SELECT Ref_Feature_Types.feature_type_name FROM Other_Available_Features JOIN Ref_Feature_Types ON Other_Available_Features.feature_type_code = Ref_Feature_Types.feat_type_code WHERE Other_Available_Features.feat_name = "AirCon"	real_estate_properties_2
SELECT Ref_Property_Types.prop_type_desc FROM Properties JOIN Ref_Property_Types ON Properties.prop_type_code = Ref_Property_Types.property_type_code GROUP BY Properties.prop_type_code	real_estate_properties_2
SELECT Properties.prop_name FROM Properties WHERE Properties.prop_type_code = "House" UNION SELECT Properties.prop_name FROM Properties WHERE Properties.prop_type_code = "Apartment" and Properties.room_count > 1	real_estate_properties_2
SELECT Ref_Feature_Types.feat_type_name FROM Other_Available_Features JOIN Ref_Feature_Types ON Other_Available_Features.feat_type_code = Ref_Feature_Types.feat_type_code WHERE Other_Available_Features.feat_name = "AirCon"	real_estate_properties_3
SELECT Ref_Property_Types.prop_type_desc FROM Properties JOIN Ref_Property_Types ON Properties.prop_type_code = Ref_Property_Types.prop_type_code GROUP BY Properties.prop_type_code	real_estate_properties_3
SELECT Properties.prop_name FROM Properties WHERE Properties.prop_type_code = "House" UNION SELECT Properties.prop_name FROM Properties WHERE Properties.prop_type_code = "Apartment" and Properties.room_cnt > 1	real_estate_properties_3
SELECT Ref_Feature_Types.feature_type_name FROM Other_Available_Features JOIN Ref_Feature_Types ON Other_Available_Features.feat_type_code = Ref_Feature_Types.feature_type_code WHERE Other_Available_Features.feature_name = "AirCon"	real_estate_properties_4
SELECT Properties.prop_name FROM Properties WHERE Properties.property_type_code = "House" UNION SELECT Properties.prop_name FROM Properties WHERE Properties.property_type_code = "Apartment" and Properties.room_count > 1	real_estate_properties_4
