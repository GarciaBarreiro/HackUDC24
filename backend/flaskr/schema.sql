-- SPDX-FileCopyrightText: 2024 Tomás García Barreiro, Ángel Suárez Torres, Muhammad Imran
--
-- SPDX-License-Identifier: MIT-0

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS consumption;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE consumption (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cups TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    date INTEGER NOT NULL,
    hour INTEGER NOT NULL,
    cons FLOAT NOT NULL,
    obt_met TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
)