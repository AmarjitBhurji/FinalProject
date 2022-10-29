CREATE TABLE IF NOT EXISTS Customer (
        customer_id INT PRIMARY KEY AUTO_INCREMENT,
        customer_name VARCHAR(50)
        email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Products (
        product_id INT PRIMARY KEY AUTO_INCREMENT,
        product_name VARCHAR(30),
        price DECIMAL (2,2),
        FOREIGN KEY (fk_customer_id) REFERENCES Customer(customer_id)
);
