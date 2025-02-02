CREATE TABLE Nail_Patterns (
  pattern_id char(4) NOT NULL,
  pattern_Name varchar(45) NOT NULL,
  pattern_Price float,
  PRIMARY KEY (pattern_id)
);

CREATE TABLE Materials (
  spare_id char(4) NOT NULL,
  spare_name varchar(60) NOT NULL,
  spare_Price float,
  PRIMARY KEY (spare_id)
);