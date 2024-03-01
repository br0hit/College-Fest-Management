
-- Command to crete Student table in the database
create table Student(
    Roll int NOT NULL,
    Name text NOT NULL,
    Dept text NOT NULL,
    primary key (Roll)
);


-- Commantd to create Role table in the database
create table Role(
    RID int NOT NULL,
    RName text NOT NULL,
    Description text NOT NULL,
    primary key (RID)
);

-- Command to create Student_has_role table in the database
create table Student_has_role(
    student int NOT NULL,
    Role int NOT NULL,
    primary key (student,Role),
    foreign key (student) references Student(roll),
    foreign key (Role) references Role(RID)
);

-- Command to create Event table in the database
create table Event(
    EID int NOT NULL,
    Date timestamp NOT NULL,
    Ename text NOT NULL,
    type text NOT NULL,
    primary key (EID)
);

-- Command to create Student_Manage_Event table in the database
create table Student_Manage_Event(
    student int NOT NULL,
    event int NOT NULL,
    primary key (student,event),
    foreign key (student) references Student(roll),
    foreign key (event) references Event(EID)
);


-- Command to create Volunteer table in the database
create table Volunteer(
    Roll int NOT NULL,
    primary key (Roll)
);

-- Command to create Participant table in the database
create table Participant(
    Name text NOT NULL,
    PID int NOT NULL,
    primary key (PID)
);

-- Command to create Event_has_Volunteer table in the database
create table Event_has_Volunteer(
    event int NOT NULL,
    volunteer int NOT NULL,
    primary key (event,volunteer),
    foreign key (event) references Event(EID),
    foreign key (volunteer) references Volunteer(Roll)
);

-- Command to create Event_has_Participant table in the database
create table Event_has_Participant(
    event int NOT NULL,
    participant int NOT NULL,
    primary key (event,participant),
    foreign key (event) references Event(EID),
    foreign key (participant) references Participant(PID)
);

-- Command to create College table in the database
create table College(
    Name text NOT NULL,
    Location text NOT NULL,
    primary key(Name)
);

-- Command to create Participant_from_College table in the database
create table Participant_from_College(
    participant int NOT NULL,
    college text NOT NULL,
    primary key (participant,college),
    foreign key (participant) references Participant(PID),
    foreign key (college) references College(Name)
);

