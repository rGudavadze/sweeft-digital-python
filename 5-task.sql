CREATE TABLE teacher (
  id PRIMARY KEY,
	name TEXT,
	lastname TEXT,
	sex TEXT,
	subject TEXT
  pupil_id INTEGER
)

CREATE TABLE pupil (
  id PRIMARY KEY,
	name TEXT,
	lastname TEXT,
	sex TEXT,
	class INTEGER,
  teacher_id INTEGER
)



SELECT teacher_name FROM pupil INNER JOIN teacher ON pupil.id=teacher.pupil_id WHERE pupil_name = "giorgi"