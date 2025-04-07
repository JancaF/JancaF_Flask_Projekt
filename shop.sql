CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE,
    password VARCHAR NOT NULL,
    role_id INTEGER,
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    price INTEGER NOT NULL,
    image VARCHAR(255) NOT NULL
);

CREATE TABLE roles (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

INSERT INTO roles (name) VALUES ("VISITOR"),
                                ("PRODUCT_MANAGER"),
                                ("ADMINISTRATOR");




INSERT INTO users (username, password, role_id) VALUES ("admin", "admin", 3),
                                              ("user", "user", 1),
                                              ("kouzelnik", "kouzelnik", 2);

INSERT INTO products (name, price, image) VALUES ("Twixx - Dual Choco", "39","/static/img/produkt_1.jpeg");
