-- Create the database
CREATE DATABASE Customers;

-- Connect to the Customers database
\c Customers;

-- Create the client_details table
CREATE TABLE IF NOT EXISTS client_details (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    surname VARCHAR(50),
    number VARCHAR(15),
    email VARCHAR(100),
    birthday DATE,
    last_check_up DATE
);

-- Populate the table with 10 rows of data
INSERT INTO client_details (name, surname, number, email, birthday, last_check_up)
VALUES 
('John', 'Doe', '123-456-7890', 'john.doe@example.com', '1985-06-15', '2023-02-15'),
('Jane', 'Smith', '987-654-3210', 'jane.smith@example.com', '1990-09-23', '2023-03-10'),
('Michael', 'Johnson', '555-123-4567', 'michael.johnson@example.com', '1987-12-02', '2023-01-20'),
('Emily', 'Davis', '444-987-6543', 'emily.davis@example.com', '1992-04-10', '2023-04-05'),
('Chris', 'Brown', '333-789-0123', 'chris.brown@example.com', '1983-11-25', '2023-05-18'),
('Jessica', 'Wilson', '222-456-7890', 'jessica.wilson@example.com', '1989-07-30', '2023-02-28'),
('David', 'Lee', '111-123-4567', 'david.lee@example.com', '1984-01-15', '2023-06-10'),
('Sophia', 'Martinez', '999-987-6543', 'sophia.martinez@example.com', '1991-08-19', '2023-07-22'),
('James', 'Anderson', '888-789-0123', 'james.anderson@example.com', '1986-03-11', '2023-03-30'),
('Olivia', 'Thomas', '777-456-7890', 'olivia.thomas@example.com', '1993-10-25', '2023-08-01');
