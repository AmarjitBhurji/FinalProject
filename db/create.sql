CREATE TABLE IF NOT EXISTS Customer (
        id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(30)
        second_name VARCHAR(30)
        email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Product (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(30),
        price DECIMAL (2,2),
        amount INTEGER (2),
        total DECIMAL(3,2),
        fk_customer_id INT, 
        FOREIGN KEY (fk_teamid) REFERENCES teams(id)
);
