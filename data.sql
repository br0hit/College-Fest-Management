-- Insert into Admin table
INSERT INTO admin (username, email, password) VALUES
('admin1', 'admin1@example.com', 'password1'),
('admin2', 'admin2@example.com', 'password2'),
('admin3', 'admin3@example.com', 'password3');

-- Insert into Student table
INSERT INTO student (name, email, password) VALUES
('Student One', 'student1@example.com', 'password1'),
('Student Two', 'student2@example.com', 'password2'),
('Student Three', 'student3@example.com', 'password3');

-- Insert into Organizer table
INSERT INTO organizer (name, email, password, contact) VALUES
('Organizer One', 'organizer1@example.com', 'password1', '1234567890'),
('Organizer Two', 'organizer2@example.com', 'password2', '0987654321'),
('Organizer Three', 'organizer3@example.com', 'password3', '1122334455');

-- Insert into Volunteer table
INSERT INTO volunteer (name, email, password) VALUES
('Volunteer One', 'volunteer1@example.com', 'password1'),
('Volunteer Two', 'volunteer2@example.com', 'password2'),
('Volunteer Three', 'volunteer3@example.com', 'password3');

-- Insert into Participant table
INSERT INTO participant (name, email, password, room_no, is_allocated) VALUES
('Participant One', 'participant1@example.com', 'password1', 'ROOM#101', FALSE),
('Participant Two', 'participant2@example.com', 'password2', 'ROOM#102', FALSE),
('Participant Three', 'participant3@example.com', 'password3', 'ROOM#103', FALSE);

-- Assuming Organizer IDs are 1, 2, and 3 respectively
-- Insert into Events table
INSERT INTO events (event_name, event_date, event_time, event_venue, event_description, event_winner, event_organizer) VALUES
('Event One', '2023-10-01', '10:00', 'Venue 1', 'Description 1', 'Winner 1', 1),
('Event Two', '2023-11-01', '11:00', 'Venue 2', 'Description 2', 'Winner 2', 2),
('Event Three', '2023-12-01', '12:00', 'Venue 3', 'Description 3', 'Winner 3', 3);

-- You might need to adjust the INSERT statements for the association tables (volunteer_events, participants_events)
-- once you have the specific IDs of volunteers, participants, and events.
-- Example:
-- INSERT INTO volunteer_events (volunteer_id, event_id) VALUES (1, 1), (2, 2), (3, 3);
-- INSERT INTO participants_events (participant_id, event_id) VALUES (1, 1), (2, 2), (3, 3);

-- Insert into room_count table which has a single value
INSERT INTO room_count (room_no) VALUES (5);
