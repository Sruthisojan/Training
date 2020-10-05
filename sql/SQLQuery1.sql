CREATE DATABASE Students;
USE Students;
CREATE TABLE StudentsInfo
(
StudentsID int,
StudentsName varchar(8000),
ParentsName varchar(8000),
PhoneNo bigint,
City varchar(8000),
Country varchar(8000)
);
DROP TABLE StudentsInfo;
CREATE TABLE StudentsInfo
(
StudentsID int,
StudentsName varchar(8000),
ParentsName varchar(8000),
PhoneNo bigint,
City varchar(8000),
Country varchar(8000) CHECK (COUNTRY='INDIA')
);
DROP TABLE StudentsInfo;


CREATE TABLE StudentsInfo
(
StudentsID int,
StudentsName varchar(8000),
ParentsName varchar(8000),
PhoneNo bigint,
City varchar(8000),
Country varchar(8000) CHECK (COUNTRY='INDIA')
);
INSERT INTO StudentsInfo(StudentsID, StudentsName, ParentsName, PhoneNo, City, Country)
VALUES('1','Harry','Potter','1234','London','India');
INSERT INTO StudentsInfo VALUES('2','Ron','Weasley','2345','London','India');
INSERT INTO StudentsInfo VALUES('3','Hermoine','Granger','3456','London','India');
SELECT * FROM StudentsInfo
UPDATE StudentsInfo SET City='NewYork'
WHERE StudentsID =2;
DROP TABLE StudentsInfo;

CREATE TABLE Samplesourcetable (StudentID int, Studentname varchar(8000), Marks int);
CREATE TABLE Sampletargettable (StudentID int, Studentname varchar(8000), Marks int);

INSERT INTO Samplesourcetable VALUES ('1','Moony','90');
INSERT INTO Samplesourcetable VALUES ('2','Prongs','75');
INSERT INTO Samplesourcetable VALUES ('3','Padfoot','73');

INSERT INTO Sampletargettable VALUES ('1','Moony','90');
INSERT INTO Sampletargettable VALUES ('2','Prongs','80');
INSERT INTO Sampletargettable VALUES ('3','Wormtail','60');

SELECT * FROM Samplesourcetable;
SELECT * FROM Sampletargettable;

MERGE Sampletargettable TARGET USING Samplesourcetable SOURCE ON (TARGET.StudentID = SOURCE.StudentID) 
WHEN MATCHED AND TARGET.Studentname <> SOURCE.Studentname OR TARGET.Marks <> SOURCE.Marks
THEN 
UPDATE SET TARGET.Studentname = SOURCE.Studentname, TARGET.Marks = SOURCE.Marks
WHEN NOT MATCHED BY TARGET THEN
INSERT (StudentID, Studentname, Marks) VALUES (SOURCE.StudentID, SOURCE.Studentname,SOURCE. Marks)
WHEN NOT MATCHED BY SOURCE THEN
DELETE;
SELECT StudentID, Studentname FROM Sampletargettable;
SELECT TOP 2 * FROM Sampletargettable;
SELECT DISTINCT Marks FROM Sampletargettable;
SELECT * FROM Sampletargettable ORDER BY Marks DESC;

CREATE TABLE Offsetmarks (Marks int)
INSERT INTO Offsetmarks VALUES ('65');
INSERT INTO Offsetmarks VALUES ('64');
INSERT INTO Offsetmarks VALUES ('62');
INSERT INTO Offsetmarks VALUES ('65');
INSERT INTO Offsetmarks VALUES ('61');
SELECT * FROM Offsetmarks ORDER BY Marks OFFSET 1 ROWS;
SELECT * FROM Offsetmarks ORDER BY Marks OFFSET 3 ROWS FETCH NEXT 2 ROWS ONLY;

CREATE TABLE Suppliertable
(
SupplierID int NOT NULL,
DOM int,
Cost int, 
CustomerID int,
PurchaseID varchar(4000)
);
SELECT * FROM Suppliertable;
INSERT INTO Suppliertable VALUES ('1','12','1230','11','P1');
INSERT INTO Suppliertable VALUES ('2','21','1543','22','P2');
INSERT INTO Suppliertable VALUES ('3','32','2345','11','P3');
INSERT INTO Suppliertable VALUES ('4','14','8765','22','P1');
INSERT INTO Suppliertable VALUES ('5','42','3452','33','P3');
INSERT INTO Suppliertable VALUES ('6','31','5431','33','P1');
INSERT INTO Suppliertable VALUES ('7','41','2342','11','P2');
INSERT INTO Suppliertable VALUES ('8','54','3654','22','P2');
INSERT INTO Suppliertable VALUES ('9','33','1234','11','P3');
INSERT INTO Suppliertable VALUES ('10','36','6832','33','P2');
INSERT INTO Suppliertable VALUES ('1','12','1230','11','P1');
SELECT CustomerID, AVG(Cost) as Avgcost FROM Suppliertable  GROUP BY CustomerID;
DROP TABLE Suppliertable;

DECLARE @var1 int=30;
SET @var1%=3;
SELECT @var1 AS Example;

CREATE TABLE Subjects(SubjectID int, StudentID int, Subjectname varchar(8000) )
INSERT INTO Subjects VALUES ('10','10','Maths');
INSERT INTO Subjects VALUES ('2','11','Physics');
INSERT INTO Subjects VALUES ('3','12','Chemistry');

SELECT * FROM Subjects;
SELECT Subjects.SubjectID, InfoStudents.StudentsName
FROM Subjects
INNER JOIN
InfoStudents ON
Subjects.StudentID = InfoStudents.StudentsID