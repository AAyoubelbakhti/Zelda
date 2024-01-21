drop DATABASE IF EXISTS ZeldaSQL;

CREATE DATABASE ZeldaSQL;

USE ZeldaSQL;

-- Usuarios
CREATE TABLE Users (
    user_id INT,
    username VARCHAR(50),
    created_at DATETIME,
    modified_at DATETIME
);

-- Partidas
CREATE TABLE Games (
    game_id INT ,
    user_id INT,
    date_started DATETIME,
    hearts_remaining INT,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region VARCHAR(20),
    created_at DATETIME,
    modified_at DATETIME
);

-- Armas
CREATE TABLE Weapons (
    weapon_id INT,
    weapon_name VARCHAR(15)
);

-- Comidas
CREATE TABLE Foods (
    food_id INT,
    food_name VARCHAR(15)
);

-- Enemigos
CREATE TABLE Enemies (
    enemy_id INT,
    game_id INT,
    region VARCHAR(20),
    num INT,
    xpos INT,
    ypos INT,
    lifes_remaining INT
);

-- Santuarios
CREATE TABLE Sanctuaries (
    sanctuary_id INT,
    game_id INT,
    region VARCHAR(20),
    num INT,
    xpos INT,
    ypos INT
);

-- Cofres
CREATE TABLE Chests (
    chest_id INT,
    game_id INT,
    region VARCHAR(20),
    num INT,
    xpos INT,
    ypos INT
);

-- Armas utilizadas por usuarios
CREATE TABLE WeaponsUsed (
    user_id INT,
    weapon_id INT,
    game_id INT,
    lives_remaining INT
);

-- Comidas consumidas por usuarios
CREATE TABLE FoodsConsumed (
    user_id INT,
    food_id INT,
    game_id INT,
    quantity_remaining INT
);




