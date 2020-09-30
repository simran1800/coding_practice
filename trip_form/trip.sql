CREATE DATABASE trip

CREATE TABLE form (
    sr_no int(3) NOT NULL,
    name text(30) NOT NULL,
    age int(3) NOT NULL,
    gender text(10) NOT NULL,
    email varchar(30) NOT NULL,
    phone varchar(10) NOT NULL,
    other text(230),
    dd datetime DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY (sr_no)
)ENGINE=INNODB DEFAULT CHARSET=utf8;