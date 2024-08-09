CREATE DATABASE IF NOT EXISTS python;

USE python;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Age INT NOT NULL,
    City VARCHAR(255) NOT NULL
);