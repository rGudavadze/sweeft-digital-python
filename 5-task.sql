#1

CREATE TABLE teacher (
  teacher_id INTEGER AUTO_INCREMENT,
	name VARCHAR(20),
	lastname VARCHAR(20),
	sex VARCHAR(20),
	subject VARCHAR(40),
  PRIMARY KEY (teacher_id)
);

CREATE TABLE pupil (
  pupil_id INTEGER AUTO_INCREMENT,
	name VARCHAR(20),
	lastname VARCHAR(20),
	sex VARCHAR(20),
	class VARCHAR(40),
  PRIMARY KEY (pupil_id)
);

CREATE TABLE teacher_pupil (
  teacher_id INTEGER,
  pupil_id INTEGER
);


#2

SELECT DISTINCT teacher.name, teacher.lastname FROM (pupil INNER JOIN teacher_pupil ON pupil.pupil_id = teacher_pupil.pupil_id) AS M
	INNER JOIN teacher ON M.teacher_id = teacher.teacher_id 
  WHERE M.name = "giorgi";