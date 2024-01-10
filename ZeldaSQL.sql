CREATE DATABASE IF NOT EXISTS ZeldaSQL;
use ZeldaSQL;

-- Usuarios
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME,
    UNIQUE (username)
);

-- Partidas
CREATE TABLE Games (
    game_id INT PRIMARY KEY,
    user_id INT,
    date_started DATETIME NOT NULL,
    hearts_remaining INT,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region VARCHAR(20) CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Armas
CREATE TABLE Weapons (
    weapon_id INT PRIMARY KEY,
    weapon_name VARCHAR(15) CHECK (weapon_name IN ('Wood Sword', 'Sword', 'Wood Shield', 'Shield')) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME
);

-- Comidas
CREATE TABLE Foods (
    food_id INT PRIMARY KEY,
    food_name VARCHAR(15) CHECK (food_name IN ('Vegetables', 'Fish', 'Meat', 'Salads', 'Pescatarian', 'Roasted')) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME
);

-- Enemigos
CREATE TABLE Enemies (
    enemy_id INT PRIMARY KEY,
    game_id INT,
    region VARCHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    lifes_remaining INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME,
    FOREIGN KEY (game_id) REFERENCES Games(game_id)
);

-- Santuarios
CREATE TABLE Sanctuaries (
    sanctuary_id INT PRIMARY KEY,
    game_id INT,
    region VARCHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME,
    FOREIGN KEY (game_id) REFERENCES Games(game_id)
);

-- Cofres
CREATE TABLE Chests (
    chest_id INT PRIMARY KEY,
    game_id INT,
    region VARCHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME,
    FOREIGN KEY (game_id) REFERENCES Games(game_id)
);

-- Armas utilizadas por usuarios
CREATE TABLE WeaponsUsed (
    user_id INT,
    weapon_id INT,
    game_id INT,
    lives_remaining INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME,
    PRIMARY KEY (user_id, weapon_id, game_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (weapon_id) REFERENCES Weapons(weapon_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id)
);

-- Comidas consumidas por usuarios
CREATE TABLE FoodsConsumed (
    user_id INT,
    food_id INT,
    game_id INT,
    quantity_remaining INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME,
    PRIMARY KEY (user_id, food_id, game_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (food_id) REFERENCES Foods(food_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id)
);



-- Users
ALTER TABLE Users
MODIFY COLUMN modified_at DATETIME;

-- Games
ALTER TABLE Games
ADD CONSTRAINT fk_user_games
FOREIGN KEY (user_id) REFERENCES Users(user_id);

-- Enemies
ALTER TABLE Enemies
ADD CONSTRAINT fk_game_enemies
FOREIGN KEY (game_id) REFERENCES Games(game_id);

-- Sanctuaries
ALTER TABLE Sanctuaries
ADD CONSTRAINT fk_game_sanctuaries
FOREIGN KEY (game_id) REFERENCES Games(game_id);

-- Chests
ALTER TABLE Chests
ADD CONSTRAINT fk_game_chests
FOREIGN KEY (game_id) REFERENCES Games(game_id);

-- WeaponsUsed
ALTER TABLE WeaponsUsed
ADD CONSTRAINT fk_user_weapons
FOREIGN KEY (user_id) REFERENCES Users(user_id),
ADD CONSTRAINT fk_weapon_weaponsused
FOREIGN KEY (weapon_id) REFERENCES Weapons(weapon_id),
ADD CONSTRAINT fk_game_weaponsused
FOREIGN KEY (game_id) REFERENCES Games(game_id);

-- FoodsConsumed
ALTER TABLE FoodsConsumed
ADD CONSTRAINT fk_user_foods
FOREIGN KEY (user_id) REFERENCES Users(user_id),
ADD CONSTRAINT fk_food_foodsconsumed
FOREIGN KEY (food_id) REFERENCES Foods(food_id),
ADD CONSTRAINT fk_game_foodsconsumed
FOREIGN KEY (game_id) REFERENCES Games(game_id);



