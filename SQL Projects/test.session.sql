-- @block
-- creates the table for the 'Users' tab
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);

-- @block
-- inserts data into the newly created table
INSERT INTO Users (email, bio, country)
VALUES 
    ('for@world.com', 'i hate strangers!', 'US'), 
    ('dylan@bunda.com', 'bar', 'MX'), 
    ('papa@crazy.com', 'poop', 'FR');

-- @block
-- this will display the table we have made and includes arguments to narrow down the results
SELECT id, email FROM Users

WHERE country = 'US'
OR id > 1

ORDER BY id DESC
LIMIT 2;

-- @block
-- creates an index for more precise searching
CREATE INDEX email_index ON Users(email);

-- @block
-- deletes table and allows for a new one to be created
DROP TABLE Users;
