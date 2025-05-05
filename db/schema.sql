CREATE DATABASE seekreto;

USE seekreto;

CREATE TABLE users (
    user_id VARCHAR(10) PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(1000) NOT NULL
);

CREATE TABLE ciphers (
    crypt_id VARCHAR(5) PRIMARY KEY,
    type_of_tool VARCHAR(50)
);

INSERT INTO ciphers (crypt_id, type_of_tool)
VALUES
    ('CC001', 'Affine Cipher'),
    ('CC002', 'Atbash Cipher'),
    ('CC003', 'Base64 Encoding'),
    ('CC004', 'Binary Encoding'),
    ('CC005', 'Caesar Cipher'),
    ('CC006', 'Hexadecimal Encoding'),
    ('CC007', 'Morse Code'),
    ('CC008', 'Rail Fence Cipher'),
    ('CC009', 'ROT13 Cipher'),
    ('CC010', 'Vigenère Cipher');

CREATE TABLE conversion (
    mode_id VARCHAR(10) PRIMARY KEY,
    type_of_conversion VARCHAR(100) NOT NULL
);