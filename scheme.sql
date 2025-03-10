CREATE TABLE users(
    id INT PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE,
    password VARCHAR NOT NULL
);


INSERT INTO users (username, password) VALUES ("admin", "admin"),
                                              ("user", "user"),
                                              ("kouzelnik", "kouzelnik")