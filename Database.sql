-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 04, 2024 at 09:33 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `temp`
--
CREATE DATABASE IF NOT EXISTS `temp` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `temp`;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `email`, `password`) VALUES
(1, 'admin1', 'admin1@example.com', 'password1'),
(2, 'admin2', 'admin2@example.com', 'password2'),
(3, 'admin3', 'admin3@example.com', 'password3');

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `event_id` int(11) NOT NULL,
  `event_name` varchar(100) NOT NULL,
  `event_date` varchar(100) NOT NULL,
  `event_time` varchar(100) NOT NULL,
  `event_venue` varchar(100) NOT NULL,
  `event_description` varchar(100) NOT NULL,
  `event_winner` varchar(100) DEFAULT NULL,
  `event_organizer` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`event_id`, `event_name`, `event_date`, `event_time`, `event_venue`, `event_description`, `event_winner`, `event_organizer`) VALUES
(1, 'Event One', '2023-10-01', '10:00', 'Venue 1', 'Description 1', 'Winner 1', 1),
(2, 'Event Two', '2023-11-01', '11:00', 'Venue 2', 'Description 2', 'Winner 2', 2),
(3, 'Event Three', '2023-12-01', '12:00', 'Venue 3', 'Description 3', 'Winner 3', 3),
(4, 'Spring fest', '2024-03-05', '20:30', 'Kalidas', 'Awesome Event', 'No Winner', 4),
(5, 'Kshitij', '2024-03-05', '21:30', 'Kalidas', 'MOderate Event', 'No Winner', 4);

-- --------------------------------------------------------

--
-- Table structure for table `organizer`
--

CREATE TABLE `organizer` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `organizer`
--

INSERT INTO `organizer` (`id`, `name`, `email`, `password`, `contact`) VALUES
(1, 'Organizer One', 'organizer1@example.com', 'password1', '1234567890'),
(2, 'Organizer Two', 'organizer2@example.com', 'password2', '0987654321'),
(3, 'Organizer Three', 'organizer3@example.com', 'password3', '1122334455'),
(4, 'o1', 'o1@gmail.com', '2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1d', '74328492834'),
(5, 'o2', 'o2@gmail.com', '2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1d', '4392141298');

-- --------------------------------------------------------

--
-- Table structure for table `participant`
--

CREATE TABLE `participant` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `room_no` varchar(100) DEFAULT NULL,
  `is_allocated` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `participant`
--

INSERT INTO `participant` (`id`, `name`, `email`, `password`, `room_no`, `is_allocated`) VALUES
(1, 'Participant One', 'participant1@example.com', 'password1', 'ROOM#101', 0),
(2, 'Participant Two', 'participant2@example.com', 'password2', 'ROOM#102', 0),
(3, 'Participant Three', 'participant3@example.com', 'password3', 'ROOM#103', 0),
(4, 'p1', 'p1@gmail.com', '2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1d', 'ROOM#2', 1);

-- --------------------------------------------------------

--
-- Table structure for table `participants_events`
--

CREATE TABLE `participants_events` (
  `participant_id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `participants_events`
--

INSERT INTO `participants_events` (`participant_id`, `event_id`) VALUES
(4, 1),
(4, 2),
(4, 3),
(4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `email`, `password`) VALUES
(1, 'Student One', 'student1@example.com', 'password1'),
(2, 'Student Two', 'student2@example.com', 'password2'),
(3, 'Student Three', 'student3@example.com', 'password3'),
(4, 's1', 's1@gmail.com', '2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1d'),
(5, 's2', 's2@gmail.com', '2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1d');

-- --------------------------------------------------------

--
-- Table structure for table `volunteer`
--

CREATE TABLE `volunteer` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `volunteer`
--

INSERT INTO `volunteer` (`id`, `name`, `email`, `password`) VALUES
(1, 'Volunteer One', 'volunteer1@example.com', 'password1'),
(2, 'Volunteer Two', 'volunteer2@example.com', 'password2'),
(3, 'Volunteer Three', 'volunteer3@example.com', 'password3'),
(4, 's1', 's1@gmail.com', '2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1d');

-- --------------------------------------------------------

--
-- Table structure for table `volunteer_events`
--

CREATE TABLE `volunteer_events` (
  `volunteer_id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `volunteer_events`
--

INSERT INTO `volunteer_events` (`volunteer_id`, `event_id`) VALUES
(4, 2),
(4, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`event_id`),
  ADD KEY `event_organizer` (`event_organizer`);

--
-- Indexes for table `organizer`
--
ALTER TABLE `organizer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `participant`
--
ALTER TABLE `participant`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `participants_events`
--
ALTER TABLE `participants_events`
  ADD PRIMARY KEY (`participant_id`,`event_id`),
  ADD KEY `event_id` (`event_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `volunteer`
--
ALTER TABLE `volunteer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `volunteer_events`
--
ALTER TABLE `volunteer_events`
  ADD PRIMARY KEY (`volunteer_id`,`event_id`),
  ADD KEY `event_id` (`event_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `event_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `organizer`
--
ALTER TABLE `organizer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `participant`
--
ALTER TABLE `participant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `volunteer`
--
ALTER TABLE `volunteer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `events_ibfk_1` FOREIGN KEY (`event_organizer`) REFERENCES `organizer` (`id`);

--
-- Constraints for table `participants_events`
--
ALTER TABLE `participants_events`
  ADD CONSTRAINT `participants_events_ibfk_1` FOREIGN KEY (`participant_id`) REFERENCES `participant` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `participants_events_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `events` (`event_id`) ON DELETE CASCADE;

--
-- Constraints for table `volunteer_events`
--
ALTER TABLE `volunteer_events`
  ADD CONSTRAINT `volunteer_events_ibfk_1` FOREIGN KEY (`volunteer_id`) REFERENCES `volunteer` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `volunteer_events_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `events` (`event_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
