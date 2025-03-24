CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE,
    password VARCHAR NOT NULL
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR UNIQUE NOT NULL,
    price INT UNIQUE NOT NULL,
    image VARCHAR NOT NULL
);



INSERT INTO users (username, password) VALUES ("admin", "admin"),
                                              ("user", "user"),
                                              ("kouzelnik", "kouzelnik");

INSERT INTO products (name, price, image) VALUES ("Twixx - Dual Choco", "39","/static/img/produkt_1.jpeg");
