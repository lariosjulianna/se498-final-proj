-- Run these in data grip
-- This will populate the DB with dummy data -- make changes if needed to DB structure
-- Create DB
CREATE DATABASE StrikingVipers;

-- Ensure it exists
SHOW DATABASES;

-- Use SV DB
USE StrikingVipers;

-- Create tables
CREATE TABLE Teachers(
    TeacherID INT PRIMARY KEY AUTO_INCREMENT,
    TeacherFirstName VARCHAR(255) NOT NULL,
    TeacherLastName VARCHAR(255) NOT NULL,
    TeacherUserName VARCHAR(255) NOT NULL UNIQUE
);
-- Show table
SELECT *
FROM Teachers;

CREATE TABLE Classes(
    ClassCode VARCHAR(255) PRIMARY KEY,
    ClassGrade INT NOT NULL,
    TeacherID INT NOT NULL,
    FOREIGN KEY Classes(TeacherID) REFERENCES Teachers(TeacherID)
);
-- Show table
SELECT *
FROM Classes;

CREATE TABLE Students(
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    StudentFirstName VARCHAR(255) NOT NULL,
    StudentLastName VARCHAR(255) NOT NULL,
    StudentUserName VARCHAR(255) NOT NULL UNIQUE,
    StudentPassWord VARCHAR(255) NOT NULL,
    ClassCode VARCHAR(255) NOT NULL,
    FOREIGN KEY Students(ClassCode) REFERENCES Classes(ClassCode)
);
-- Show table
SELECT *
FROM Students;


-- Populate Tables

INSERT INTO Teachers (TeacherFirstName, TeacherLastName, TeacherUserName)
VALUES ('Maria', 'Ramirez', 'mariar');

INSERT INTO Teachers (TeacherFirstName, TeacherLastName, TeacherUserName)
VALUES ('Adam', 'Lee', 'adaml');

INSERT INTO Teachers (TeacherFirstName, TeacherLastName, TeacherUserName)
VALUES ('Jennifer', 'Soto', 'jennifers');

INSERT INTO Teachers (TeacherFirstName, TeacherLastName, TeacherUserName)
VALUES ('Nico', 'Jones', 'nicoj');

INSERT INTO Teachers (TeacherFirstName, TeacherLastName, TeacherUserName)
VALUES ('Manvir', 'Kaur', 'manvirk');

-- Show table
SELECT *
FROM Teachers;


INSERT INTO Classes (ClassCode, ClassGrade, TeacherID)
VALUES ('a5h83k', 5, 1);

INSERT INTO Classes (ClassCode, ClassGrade, TeacherID)
VALUES ('p9j61s', 4, 2);

INSERT INTO Classes (ClassCode, ClassGrade, TeacherID)
VALUES ('b4g27e', 5, 5);

INSERT INTO Classes (ClassCode, ClassGrade, TeacherID)
VALUES ('k0z40t', 3, 4);

INSERT INTO Classes (ClassCode, ClassGrade, TeacherID)
VALUES ('i4x22f', 4, 3);

-- Show table
SELECT *
FROM Classes;


INSERT INTO Students (StudentFirstName, StudentLastName, StudentUserName, StudentPassWord, ClassCode)
VALUES ('Mia', 'Lamb', 'mial','mial', 'a5h83k');

INSERT INTO Students (StudentFirstName, StudentLastName, StudentUserName, StudentPassWord, ClassCode)
VALUES ('Tina', 'Hernandez', 'tinah','tinah', 'a5h83k');

INSERT INTO Students (StudentFirstName, StudentLastName, StudentUserName, StudentPassWord, ClassCode)
VALUES ('Joey', 'Garcia', 'joeyg','joeyg', 'b4g27e');

INSERT INTO Students (StudentFirstName, StudentLastName, StudentUserName, StudentPassWord, ClassCode)
VALUES ('Devin', 'Stone', 'devins','devins', 'p9j61s');

INSERT INTO Students (StudentFirstName, StudentLastName, StudentUserName, StudentPassWord, ClassCode)
VALUES ('Leah', 'Manto', 'leahm','leahm', 'i4x22f');

-- Show table
SELECT *
FROM Students;

