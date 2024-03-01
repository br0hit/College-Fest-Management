-- Bannuru Rohit Kumar Reddy
-- 21CS30011
-- DMBS Assignment 2 
-- Inserting values into the tables which have been created : 

insert into
    student(roll,Name,dept)
values
    (10011, 'Rohit', 'CSE'),
    (10012, 'Chethan', 'CSE'),
    (10013, 'Charan', 'MECH'),
    (10014, 'Varshith', 'CHEM'),
    (10015, 'Ritesh', 'MECH'),
    (10016, 'Rod', 'ECE'),
    (10017, 'Shamitha', 'CSE'),
    (10018, 'Kartik', 'CSE'),
    (10019, 'Chaitanya', 'MECH'),
    (10020, 'Puneeth', 'MECH');


insert into
    Event(EID,Date,Ename,type)
values
    (1,'2024-01-28 16:00:00', 'Megaevent','Pal Night'),
    (2,'2024-01-27 20:20:20', 'Normalevent','Indie concert'),
    (3,'2024-01-26 20:20:20', 'Casualevent','EDM concert'),
    (4,'2024-01-25 20:20:20', 'Trailevent','Prep concert'),
    (5,'2024-01-24 20:20:20', 'Noevent','No concert');



INSERT INTO 
    Student_Manage_Event(Student,Event)
VALUES
    (10011,1),
    (10012,1),
    (10013,1),
    (10013,2),
    (10014,1),
    (10014,2),
    (10015,1),
    (10015,5),
    (10016,1),
    (10017,2),
    (10018,3),
    (10019,4),
    (10020,5);

INSERT INTO 
    Role(RID,RName,Description)
VALUES
    (01,'Secretary','Secretary'),
    (02,'Reception','Reception'),
    (03,'Manager','Manager'),
    (04,'Participant','Participant'),
    (05,'Stage','Stage');


INSERT INTO
    Student_has_role(student,Role)
VALUES
    (10011,01),
    (10012,01),
    (10013,05),
    (10014,01),
    (10015,02),
    (10016,03),
    (10017,04),
    (10018,01),
    (10020,05);

INSERT INTO
    Volunteer(Roll)
VALUES
    (10011),
    (10012),
    (10013),
    (10014),
    (10016),
    (10017),
    (10018),
    (10019),
    (10020),
    (101),
    (102),
    (103),
    (104),
    (105),
    (106),
    (107);

INSERT INTO
    Event_has_Volunteer(event,volunteer)
VALUES
    (1,10011),
    (1,10012),
    (2,10013),
    (1,10014),
    (3,10016),
    (3,10017),
    (4,10018),
    (4,10019),
    (5,10020),
    (1,101),
    (1,102),
    (1,103),
    (3,104),
    (5,105),
    (4,106),
    (4,107);

INSERT INTO
    Participant(Name,PID)
VALUES
    ('Ramesh',1001),
    ('Suresh',1002),
    ('Mukesh',1003),
    ('Adish',1004),
    ('Jagadish',1005),
    ('Pawan',1006),
    ('Kalyan',1007),
    ('Bala',1008),
    ('Krishna',1009),
    ('Rajesh',1010),
    ('Sumanth',1011),
    ('Ravi',1012),
    ('Teja',1013),
    ('Devi',1014),
    ('Chand',1015),
    ('Sai',1016),
    ('Charan',1017),
    ('Hashmitha',1018);

INSERT INTO
    Event_has_Participant(event,participant)
VALUES
    (2,1001),
    (3,1001),
    (4,1001),
    (5,1001),
    (1,1002),
    (3,1002),
    (5,1002),
    (1,1003),
    (2,1003),
    (4,1003),
    (5,1003),
    (1,1004),
    (1,1005),
    (1,1006),
    (2,1007),
    (2,1008),
    (2,1009),
    (3,1010),
    (1,1011),
    (3,1012),
    (3,1013),
    (1,1014),
    (3,1015),
    (3,1016),
    (4,1017),
    (1,1018);

INSERT INTO
    College(Name,Location)
VALUES
    ('IITB','Mumbai'),
    ('IITD','Delhi'),
    ('IITK','Kanpur'),
    ('IITG','Guwahati'),
    ('IITR','Roorkee'),
    ('IITM','Madras');

INSERT INTO
    Participant_from_College(participant,college)
VALUES
    (1001,'IITM'),
    (1002,'IITB'),
    (1003,'IITB'),
    (1004,'IITB'),
    (1005,'IITB'),
    (1006,'IITB'),
    (1007,'IITD'),
    (1008,'IITK'),
    (1009,'IITG'),
    (1010,'IITR'),
    (1011,'IITM'),
    (1012,'IITM'),
    (1013,'IITM'),
    (1014,'IITR'),
    (1015,'IITM'),
    (1016,'IITM'),
    (1017,'IITK'),
    (1018,'IITM');


queries:

-- 1. List the names and roll number of all the students who are managing the event 'Megaevent'.

select 
    s.name,s.roll
from 
    student s,Student_Manage_Event m,event e
where
    s.roll=m.student and m.event=e.eid and e.ename='Megaevent';


-- 2. Roll number and name of all the students who are managing “Megevent” as an “Secretary”

SELECT
    s.Roll,
    s.Name
FROM
    Student s
JOIN
    Student_Manage_Event m ON s.Roll = m.student
JOIN
    Event e ON m.event = e.EID
JOIN
    Student_has_role shr ON s.Roll = shr.student
JOIN
    Role r ON shr.Role = r.RID
WHERE
    e.Ename = 'Megaevent'
    AND r.RName = 'Secretary';


-- 3. Name of all the participants from the college “IITB” in “Megaevent”.

SELECT
    p.Name
FROM
    Participant p
JOIN
    Participant_from_College pfc ON p.PID = pfc.participant
JOIN
    Event_has_Participant ehp ON p.PID = ehp.participant
JOIN
    Event e ON ehp.event = e.EID
WHERE
    pfc.college = 'IITB'
    AND e.Ename = 'Megaevent';


-- 4.Name of all the colleges who have at least one participant in “Megaevent”.

SELECT DISTINCT
    c.Name
FROM
    College c
JOIN
    Participant_from_College pfc ON c.Name = pfc.college
JOIN
    Event_has_Participant ehp ON pfc.participant = ehp.participant
JOIN
    Event e ON ehp.event = e.EID
WHERE
    e.Ename = 'Megaevent';

-- 5. Name of all the events which is managed by a “Secretary”

SELECT DISTINCT
    e.Ename
FROM
    Event e
JOIN
    Student_Manage_Event sme ON e.EID = sme.event
JOIN
    Student_has_role shr ON sme.student = shr.student
JOIN
    Role r ON shr.Role = r.RID
WHERE
    r.RName = 'Secretary';


-- 6.Name of all the “CSE” department student volunteers of “Megaevent”.

SELECT
    s.Name
FROM
    Student s
JOIN
    Volunteer v ON s.Roll = v.Roll
JOIN
    Event_has_Volunteer ehv ON v.Roll = ehv.volunteer
JOIN
    Event e ON ehv.event = e.EID
WHERE
    s.Dept = 'CSE' AND e.Ename = 'Megaevent';

-- 7.Name of all the events which has at least one student volunteer from “CSE” department.

SELECT DISTINCT
    e.Ename
FROM
    Event e
JOIN
    Event_has_Volunteer ehv ON e.EID = ehv.event
JOIN
    Volunteer v ON ehv.volunteer = v.Roll
JOIN
    Student s ON v.Roll = s.Roll
WHERE
    s.Dept = 'CSE';


--  8. Name of the college with the largest number of participants in “Megaevent”.

SELECT
    c.Name,
    COUNT(*) AS ParticipantCount
FROM
    College c
JOIN
    Participant_from_College pfc ON c.Name = pfc.college
JOIN
    Event_has_Participant ehp ON pfc.participant = ehp.participant
JOIN
    Event e ON ehp.event = e.EID
WHERE
    e.Ename = 'Megaevent'
GROUP BY
    c.Name
ORDER BY
    ParticipantCount DESC
LIMIT 1;

-- 9.Name of the college with largest number of participant overall

SELECT
    c.Name,
    COUNT(*) AS TotalParticipants
FROM
    College c
JOIN
    Participant_from_College pfc ON c.Name = pfc.college
GROUP BY
    c.Name
ORDER BY
    TotalParticipants DESC
LIMIT 1;


Chethan Pasupulety
	
3:38 PM (7 minutes ago)
	
to me
create table Student(
 Roll int NOT NULL,
 Name text NOT NULL,
 Dept text NOT NULL,
 primary key (Roll)
);

create table Role(
 RID int NOT NULL,
 RName text NOT NULL,
 Description text NOT NULL,
 primary key (RID)
);

create table Student_has_role(
 student int NOT NULL,
 Role int NOT NULL,
 primary key (student,Role),
 foreign key (student) references Student(roll),
 foreign key (Role) references Role(RID)
);

create table Event(
 EID int NOT NULL,
 Date timestamp NOT NULL,
 Ename text NOT NULL,
 type text NOT NULL,
 primary key (EID)
);

create table Student_Manage_Event(
 student int NOT NULL,
 event int NOT NULL,
 primary key (student,event),
 foreign key (student) references Student(roll),
 foreign key (event) references Event(EID)
);

create table Volunteer(
 Roll int NOT NULL,
 primary key (Roll)
);

create table Participant(
 Name text NOT NULL,
 PID int NOT NULL,
 primary key (PID)
);

create table Event_has_Volunteer(
 event int NOT NULL,
 volunteer int NOT NULL,
 primary key (event,volunteer),
 foreign key (event) references Event(EID),
 foreign key (volunteer) references Volunteer(Roll)
);

create table Event_has_Participant(
 event int NOT NULL,
 participant int NOT NULL,
 primary key (event,participant),
 foreign key (event) references Event(EID),
 foreign key (participant) references Participant(PID)
);

create table College(
 Name text NOT NULL,
 Location text NOT NULL,
 primary key(Name)
);

create table Participant_from_College(
 participant int NOT NULL,
 college text NOT NULL,
 primary key (participant,college),
 foreign key (participant) references Participant(PID),
 foreign key (college) references College(Name)
);

insert into
 student(roll,Name,dept)
values
 (10011, 'Rohit', 'CSE'),
 (10012, 'Chethan', 'CSE'),
 (10013, 'Charan', 'MECH'),
 (10014, 'Varshith', 'CHEM'),
 (10015, 'Ritesh', 'MECH'),
 (10016, 'Sreekar', 'ECE'),
 (10017, 'Shamitha', 'CSE'),
 (10018, 'Kartik', 'CSE'),
 (10019, 'Chaitanya', 'MECH'),
 (10020, 'Puneeth', 'MECH');




insert into
 Event(EID,Date,Ename,type)
values
 (1,'2024-01-28 16:00:00', 'Megaevent','Pal Night'),
 (2,'2024-01-27 20:20:20', 'Normalevent','Indie concert'),
 (3,'2024-01-26 20:20:20', 'Casualevent','EDM concert'),
 (4,'2024-01-25 20:20:20', 'Trailevent','Prep concert'),
 (5,'2024-01-24 20:20:20', 'Noevent','No concert');



INSERT INTO 
 Student_Manage_Event(Student,Event)
VALUES
 (10011,1),
 (10012,1),
 (10013,1),
 (10013,2),
 (10018,3),
 (10019,4),
 (10020,5);

INSERT INTO 
 Role(RID,RName,Description)
VALUES
 (01,'Secretary','Secretary'),
 (02,'Reception','Reception'),
 (03,'Manager','Manager'),
 (04,'Participant','Participant'),
 (05,'Stage','Stage');


INSERT INTO
 Student_has_role(student,Role)
VALUES
 (10011,01),
 (10012,01),
 (10013,05),
 (10014,01),
 (10015,02),
 (10016,03),
 (10017,04),
 (10018,01),
(10020,05);

INSERT INTO
 Volunteer(Roll)
VALUES
 (10011),
 (10012),
 (10013),
 (10014),
 (10016),
 (10017),
 (10018),
 (10019),
 (10020),
 (101),
 (102),
 (103),
 (104),
 (105),
 (106),
 (107);

INSERT INTO
 Event_has_Volunteer(event,volunteer)
VALUES
 (1,10011),
 (1,10012),
 (2,10013),
 (1,10014),
 (3,10016),
 (3,10017),
 (4,10018),
 (4,10019),
 (5,10020),
 (1,101),
 (1,102),
 (1,103),
 (3,104),
 (5,105),
 (4,106),
 (4,107);

INSERT INTO
 Participant(Name,PID)
VALUES
 ('Ramesh',1001),
 ('Suresh',1002),
 ('Mukesh',1003),
 ('Adish',1004),
 ('Jagadish',1005),
 ('Pawan',1006),
 ('Kalyan',1007),
 ('Bala',1008),
 ('Krishna',1009),
 ('Rajesh',1010),
 ('Sumanth',1011),
 ('Ravi',1012),
 ('Teja',1013),
 ('Devi',1014),
 ('Chand',1015),
 ('Sai',1016),
 ('Charan',1017),
 ('Hashmitha',1018);

INSERT INTO
 Event_has_Participant(event,participant)
VALUES
 (2,1001),
 (3,1001),
 (4,1001),
 (5,1001),
 (1,1002),
 (3,1002),
 (5,1002),
 (1,1003),
 (2,1003),
 (4,1003),
 (5,1003),
 (1,1004),
 (1,1005),
 (1,1006),
 (2,1007),
 (2,1008),
 (2,1009),
 (3,1010),
 (1,1011),
 (3,1012),
 (3,1013),
 (1,1014),
 (3,1015),
 (3,1016),
 (4,1017),
 (1,1018);

INSERT INTO
 College(Name,Location)
VALUES
 ('IITB','Mumbai'),
 ('IITD','Delhi'),
 ('IITK','Kanpur'),
 ('IITG','Guwahati'),
 ('IITR','Roorkee'),
 ('IITM','Madras');

INSERT INTO
 Participant_from_College(participant,college)
VALUES
 (1001,'IITM'),
 (1002,'IITB'),
 (1003,'IITB'),
 (1004,'IITB'),
 (1005,'IITB'),
 (1006,'IITB'),
 (1007,'IITD'),
 (1008,'IITK'),
 (1009,'IITG'),
 (1010,'IITR'),
 (1011,'IITM'),
 (1012,'IITM'),
 (1013,'IITM'),
 (1014,'IITR'),
 (1015,'IITM'),
 (1016,'IITM'),
 (1017,'IITK'),
 (1018,'IITM');