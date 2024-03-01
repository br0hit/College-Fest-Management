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


-- 8. Name of the college with the largest number of participants in “Megaevent”.

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


-- 10. Name of the department with the largest number of volunteers in all the events which has
-- at least one participant from “IITB”.


SELECT Dept
FROM (
    SELECT
        s.Dept,
        COUNT(*) AS VolunteerCount
    FROM
        Student s
    JOIN
        Volunteer v ON s.Roll = v.Roll
    JOIN
        Event_has_Volunteer ehv ON v.Roll = ehv.volunteer
    JOIN
        Event_has_Participant ehp ON ehv.event = ehp.event
    JOIN
        Participant_from_College pfc ON ehp.participant = pfc.participant
    WHERE
        pfc.college = 'IITB'
    GROUP BY
        s.Dept
    ORDER BY
        VolunteerCount DESC
    LIMIT 1
) AS subquery;