DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS trajets;

CREATE TABLE users (
    id int auto_increment,
    username VARCHAR(20) UNIQUE,
    password VARCHAR(200),
    CONSTRAINT pk_users PRIMARY KEY (id)
);

INSERT INTO users VALUES (null, 'admin', '1793AD626C7747BA244201048E700EC6BFF5595842E70CD0D32DC3ABCAEB35D5EBC6C78C99504E53E6F8F7BFE530893B622C7C31338C0CA4EB88BE2060886099');

CREATE TABLE trajets (
    id int auto_increment,
    distance FLOAT,
    temps INT,
    obstacles INT,
    vitesseMoyenne FLOAT,
    vitesseMax FLOAT,
    angleMaxY INT,
    angleMaxX INT,
    dateTrajet DATETIME,
    CONSTRAINT pk_trajets PRIMARY KEY (id)
);