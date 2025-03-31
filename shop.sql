CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE,
    password VARCHAR NOT NULL
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR UNIQUE NOT NULL,
    price INT UNIQUE NOT NULL
);



INSERT INTO users (username, password) VALUES ("admin", "admin"),
                                              ("user", "user"),
                                              ("kouzelnik", "kouzelnik");

INSERT INTO products (name, price) VALUES ("Twixx - Dual Choco", "39"),
                                          ("Desert Stuff", "44"),
                                          ("SnickerBar","47");
