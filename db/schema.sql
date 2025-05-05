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

INSERT INTO conversion (mode_id, type_of_conversion) VALUES
('TXTAFF', 'Text to Affine Cipher'),
('AFFTXT', 'Affine Cipher to Text'),
('TXTATB', 'Text to Atbash Cipher'),
('ATBTXT', 'Atbash Cipher to Text'),
('TXTB64', 'Text to Base64'),
('B64TXT', 'Base64 to Text'),
('TXTBI', 'Text to Binary'),
('BITXT', 'Binary to Text'),
('TXTCAE', 'Text to Caesar Cipher'),
('CAETXT', 'Caesar Cipher to Text'),
('TXTHEX', 'Text to HexaDecimal'),
('HEXTXT', 'HexaDecimal to Text'),
('TXTMRS', 'Text to Morse Code'),
('MRSTXT', 'Morse Code to Text'),
('TXTRLF', 'Text to Rail Fence Cipher'),
('RLFTXT', 'Rail Fence Cipher to Text'),
('TXTR13', 'Text to ROT13 Cipher'),
('R13TXT', 'ROT13 Cipher to Text'),
('TXTVIG', 'Text to Vigenère Cipher'),
('VIGTXT', 'Vigenère Cipher to Text');

CREATE TABLE history (
    history_id VARCHAR(10) PRIMARY KEY,  
    user_id VARCHAR(10),                               
    crypt_id VARCHAR(5),                       
    mode_id VARCHAR(10),                       
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,  
    `key` VARCHAR(255) DEFAULT 'n/a',
    a_value INT DEFAULT NULL,                  
    b_value INT DEFAULT NULL,          
    rail INT DEFAULT NULL,                     
    input MEDIUMTEXT NOT NULL,                 
    output MEDIUMTEXT NOT NULL,                               
    FOREIGN KEY (user_id) REFERENCES users(user_id),  
    FOREIGN KEY (crypt_id) REFERENCES ciphers(crypt_id),  
    FOREIGN KEY (mode_id) REFERENCES conversion(mode_id)  
);

ALTER TABLE conversion 
ADD COLUMN crypt_id VARCHAR(5),
ADD CONSTRAINT fk_crypt_id FOREIGN KEY (crypt_id) REFERENCES ciphers(crypt_id);

UPDATE conversion SET crypt_id = 'CC001' WHERE mode_id = 'TXTAFF';
UPDATE conversion SET crypt_id = 'CC001' WHERE mode_id = 'AFFTXT';
UPDATE conversion SET crypt_id = 'CC002' WHERE mode_id = 'TXTATB';
UPDATE conversion SET crypt_id = 'CC002' WHERE mode_id = 'ATBTXT';
UPDATE conversion SET crypt_id = 'CC003' WHERE mode_id = 'TXTB64';
UPDATE conversion SET crypt_id = 'CC003' WHERE mode_id = 'B64TXT';
UPDATE conversion SET crypt_id = 'CC004' WHERE mode_id = 'TXTBI';
UPDATE conversion SET crypt_id = 'CC004' WHERE mode_id = 'BITXT';
UPDATE conversion SET crypt_id = 'CC005' WHERE mode_id = 'TXTCAE';
UPDATE conversion SET crypt_id = 'CC005' WHERE mode_id = 'CAETXT';
UPDATE conversion SET crypt_id = 'CC006' WHERE mode_id = 'TXTHEX';
UPDATE conversion SET crypt_id = 'CC006' WHERE mode_id = 'HEXTXT';
UPDATE conversion SET crypt_id = 'CC007' WHERE mode_id = 'TXTMRS';
UPDATE conversion SET crypt_id = 'CC007' WHERE mode_id = 'MRSTXT';
UPDATE conversion SET crypt_id = 'CC008' WHERE mode_id = 'TXTRLF';
UPDATE conversion SET crypt_id = 'CC008' WHERE mode_id = 'RLFTXT';
UPDATE conversion SET crypt_id = 'CC009' WHERE mode_id = 'TXTR13';
UPDATE conversion SET crypt_id = 'CC009' WHERE mode_id = 'R13TXT';
UPDATE conversion SET crypt_id = 'CC010' WHERE mode_id = 'TXTVIG';
UPDATE conversion SET crypt_id = 'CC010' WHERE mode_id = 'VIGTXT';

ALTER TABLE history
ADD COLUMN shift INT DEFAULT NULL
AFTER date_time;

CREATE TABLE favorites (
    fav_id VARCHAR(7) PRIMARY KEY, 
    user_id VARCHAR(10),
    crypt_id VARCHAR(5),
    description TEXT,
    icon_text VARCHAR(255),
    href VARCHAR(25),
    FOREIGN KEY (crypt_id) REFERENCES ciphers(crypt_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
